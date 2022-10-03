# -*- coding: utf-8 -*-
# import imp
import os
import re
import time
from datetime import datetime
from pathlib import Path

import pandas as pd
import psutil
import win32com.client as win32
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QEventLoop, QPropertyAnimation, QStringListModel, QThread, QTimer, Signal
from PySide6.QtGui import QImage, QPixmap, Qt
from PySide6.QtWidgets import QApplication, QFileDialog, QFileSystemModel, QHeaderView, QTableWidgetItem

from dtview import DonutWidget


class EmittingStr(QtCore.QObject):  # 发射信号类
    textWritten = QtCore.Signal(str)  # 发射信号


    def write(self, text):
        self.textWritten.emit(str(text))  # 发射信号
        loop = QEventLoop()  # 创建事件循环
        QTimer.singleShot(1, loop.quit)  # 延时1ms后退出事件循环
        loop.exec()  # 开始事件循环
        QApplication.processEvents()  # 处理事件


    def flush(self):  # 不加这个函数会报错，不要问为什么，我也不知道
        pass


class UpdateTqsdkDate(QThread):  # 更新tqsdk数据类
    TQ_signal = Signal()


    def __init__(self, api):
        super().__init__()
        self.api = api


    def run(self):  # 更新发送信号
        while True:
            self.api.wait_update()
            self.TQ_signal.emit()


class Main_Process_Function:  # 主进程函数类，该类由主进程窗口类继承并调用

    def outputWritten(self, text):  # 发射信号
        cursor = self.textBrowser_terminal.textCursor()  # 获取光标
        cursor.movePosition(QtGui.QTextCursor.End)  # 光标移动到最后
        cursor.insertText(text)  # 插入文本
        self.textBrowser_terminal.setTextCursor(cursor)  # 设置光标
        self.textBrowser_terminal.ensureCursorVisible()  # 光标可见

    def count_process_reboot_times(self):
        times = 0
        if self.Process_start_time_dict is not None:
            for key, value in self.Process_start_time_dict.items():
                if value > 1:
                    times = times + value - 1
        return times


    def add_paramer_to_container_by_timer(self):  # 将参数添加到面板各容器中,定时器驱动部分

        self.label_runing_process_quantity.setText(str(len(self.get_alive_process_pid_list())))  # 获取当前活着的策略进程数, (只有子进程，没有父进程和协程)
        self.label_current_time.setText(time.strftime('%Y-%m-%d    %H:%M:%S', time.localtime()))
        self.label_frame_runing_time.setText(self.get_frame_runing_time())
        self.label_tq_account_quantity.setText(str(self.get_tq_account_quantity()))
        self.label_cpu_occupancy.setText(str(psutil.cpu_percent()) + ' %')
        self.label_total_profit.setText(str(self.get_total_profit()))
        self.process_dict_update()
        self.add_process_list_to_process_listview()

    def add_process_list_to_process_listview(self):
        process_model = QStringListModel()
        self.process_list, self.process_list_row = self.get_process_list()
        process_model.setStringList(self.process_list)
        self.process_listview.setModel(process_model)


    def add_paramer_to_container_by_hand(self):         # 将参数添加到面板各容器中, 人工动作驱动部分

        account_model = QStringListModel()
        self.clients_list = self.get_clients_list()
        account_model.setStringList(self.clients_list)
        self.clients_listview.setModel(account_model)
        self.clients_listview2.setModel(account_model)

        tq_account_model = QStringListModel()
        self.tq_account_list = self.get_tq_account_list()
        tq_account_model.setStringList(self.tq_account_list)
        self.tq_account_listview.setModel(tq_account_model)
        self.tq_account_listview2.setModel(tq_account_model)

        quote_model = QStringListModel()
        self.quote_list = self.get_quote_list()
        quote_model.setStringList(self.quote_list)
        self.quote_listview.setModel(quote_model)

        strategy_model = QStringListModel()
        self.strategy_list = self.get_strategy_list(path='./strategys')
        strategy_model.setStringList(self.strategy_list)
        self.strategy_listview.setModel(strategy_model)

        self_selection_model = QStringListModel()
        self.self_selection_list = self.get_self_selection_quote_list()
        self_selection_model.setStringList(self.self_selection_list)
        self.self_selection_listview.setModel(self_selection_model)

        self.add_process_list_to_process_listview()

    def show_clients_info(self, qModelIndex):  # 显示客户信息
        row = qModelIndex.row()
        data = self.ioModal.read_csv_file(path='./data/clients.csv')
        self.textBrowser_clients_details.clear()
        self.textBrowser_clients_details.append('\n' + '客户姓名：   ' + str(data.iloc[row]['clients_name']))
        self.textBrowser_clients_details.append('\n' + '身份证号：   ' + str(data.iloc[row]['clients_id']))
        self.textBrowser_clients_details.append('\n' + '电话号码：   ' + str(data.iloc[row]['clients_tel']))
        self.textBrowser_clients_details.append('\n' + '联系地址：   ' + str(data.iloc[row]['clients_address']))
        self.textBrowser_clients_details.append('\n' + '照片位置：   ' + str(data.iloc[row]['clients_photo_address']))
        if data.iloc[row]['clients_photo_address']:
            photo_path = './clients_photo/' + str(data.iloc[row, 0]) + '.jpg'
            if os.path.exists(photo_path):
                self.show_client_photo(photo_path)
            else:
                self.show_client_photo('./logo/Default_photo.png')


    def show_tq_account_info(self, qModelIndex):  # 显示天勤账户信息
        row = qModelIndex.row()
        data = self.ioModal.read_csv_file(path='./data/tq_account.csv')
        self.textBrowser_tq_account_details.clear()
        self.textBrowser_tq_account_details.append('\n\n' + 22*' ' + '天勤帐户 :     ' + str(data.iloc[row]['tq_account']))
        self.textBrowser_tq_account_details.append('\n\n' + 11*' ' + '该帐户所属客户 :     ' + str(data.iloc[row]['clients_name']))
        self.textBrowser_tq_account_details.append('\n\n' + 22*' ' + '天勤密码 :     ' + str(data.iloc[row]['tq_psd']))
        self.textBrowser_tq_account_details.append('\n\n' + '该帐户绑定的期货公司 :     ' + str(data.iloc[row]['futures_company']))
        self.textBrowser_tq_account_details.append('\n\n' + 7*' ' + '期货实盘资金帐户 :     ' + str(data.iloc[row]['futures_account']))
        self.textBrowser_tq_account_details.append('\n\n' + 7*' ' + '期货实盘资金密码 :     ' + str(data.iloc[row]['futures_psd']))


    def show_file_in_treeview(self):  # 以树状结构显示 log 文件夹和文件
        # 在self.treeView_log中显示./log/ 下的文件和文件夹
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath('./log')
        self.treeview_log.setModel(self.file_system_model)
        self.treeview_log.setRootIndex(self.file_system_model.index('./log'))
        self.treeview_log.setColumnHidden(1, True)
        self.treeview_log.setColumnHidden(2, True)
        self.treeview_log.setColumnHidden(3, True)


    def on_tree_licked(self, qmodelindex):  # 当点击树状结构时，显示文件内容
        # 当点击treeview_log中的文件时，在textBrowser_log显示文件的内容
        if qmodelindex.column() == 0:
            file_name = self.file_system_model.fileName(qmodelindex)  # 获取当前选中的文件名
            file_path = self.file_system_model.filePath(qmodelindex)  # 获取当前选中的文件路径

            if os.path.isfile(file_path):  # 如果是文件
                self.textBrowser_log.clear()
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.textBrowser_log.setText(f.read())  # 将文件内容显示在textBrowser_log中
                    # 显示文本的最底部
                    cursor = self.textBrowser_log.textCursor()  # 获取光标
                    cursor.movePosition(QtGui.QTextCursor.End)  # 光标移动到最后
                    self.textBrowser_log.setTextCursor(cursor)  # 设置光标
                    self.textBrowser_log.ensureCursorVisible()  # 光标可见

                    f.close()  # 关闭文件

            self.label_log_file_name.setText(file_name)  # 显示文件名

            self.label_log_file_address.setText(file_path)  # 显示文件地址
        else:
            pass


    def kill_process(self, pid):  # 杀死单个进程
        try:
            parent_proc = psutil.Process(pid)
            for child_proc in parent_proc.children(recursive=True):
                child_proc.kill()
            parent_proc.kill()
            for key, value in self.Process_dict.items():
                if value == pid:
                    key = None
                break
            print('\npid为 ' + str(pid) + ' 的子进程 关闭成功 ！！！\n')
        except Exception as e:
            print('\npid为 ' + str(pid) + ' 的子进程 关闭失败 ！！！\n')
            print(e, '\n')



    def kill_all_process(self):  # 杀死所有进程 # 关闭所有进程

        for pid in self.get_alive_process_pid_list():
            self.kill_process(pid)
        # self.Process_dict.clear()
        print('所有子进程都已关闭!\n')


    def process_dict_update(self):  # 更新进程字典
        path = './data/config.csv'
        data = self.ioModal.read_csv_file(path)

        for index, item in data.iterrows():
            if item['whether_self_start']:
                # 判断self.Process_dict中是否有该进程，如果有，则不再添加
                if item['process_name'] in self.Process_dict.keys():
                    pass
                else:
                    self.Process_dict[item['process_name']] = None


    def get_clients_list(self):  # 获取用户列表
        clients_list = []
        data = self.ioModal.read_csv_file(path='./data/clients.csv')
        if data.empty:
            clients_list = []
        else:
            for account in data['clients_name']:
                clients_list.append(str(account))

        return clients_list


    def get_tq_account_list(self):  # 获取天勤账号列表
        tq_account_list = []
        data = self.ioModal.read_csv_file(path='./data/tq_account.csv')
        if data.empty:
            pass
        else:
            for index, item in data.iterrows():
                tq_account_list.append(str(item['tq_account']))

        return tq_account_list


    def get_alive_process_pid_list(self):  # 获取运行着的子进程 pid列表
        p = psutil.Process(os.getpid())
        children = p.children()             # 获取p.children()中的所有子进程pid，并生成一个列表
        living_pid_list = []
        for child in children:
            if child.name() == 'python.exe':        # 这里只需要自己策略创建的名为python.exe的子进程,主进程创建的名为conhost.exe的不要
                pid = child.pid
                if pid not in living_pid_list:
                    living_pid_list.append(pid)
            else:
                pass
        return living_pid_list
        # living_pid_list = [x.pid for x in p.children()]        return living_pid_list


    def get_process_list(self):  # 获取活着的进程名列表
        process_list = []       # 这个list中间加了个 \n,用于在listview中显示进程名时从中间拆成两行
        process_list_raw = []    # 这个list是原生的,中间不加 \n
        pid_list = self.get_alive_process_pid_list()
        # 判断self.Process_dict中每一项的值是否在pid_list中，如果在，则添加到process_list中
        for key, value in self.Process_dict.items():
            if value in pid_list:
                if key.split('-',3)[0] == '回测':     # 判断字典键的第一个小块是不是回测
                    tmp = (key.split('-',5)[0] + '-' + key.split('-',5)[1] + '-' + key.split('-',5)[2] + '\n-' +
                            key.split('-',5)[3] + '-' + key.split('-',5)[4] + '-' + key.split('-',5)[5])
                else:
                    tmp = (key.split('-', 3)[0] + '-' + key.split('-', 3)[1] + '-' + key.split('-', 3)[2] +
                           '\n-' + key.split('-', 3)[3])
                process_list.append(tmp)
                process_list_raw.append(key)
        return process_list, process_list_raw


    def get_quote_list(self):  # 获取行情引用列表
        quote_list = []
        data = self.ioModal.read_csv_file(path='./data/config.csv')
        if data.empty:
            quote_list = []
        else:
            for index, item in data.iterrows():
                quote_list.append(str(item['symbol']) + '-->' + str(item['symbol_period']) + ' min')

        return quote_list


    def get_self_selection_quote_list(self):  # 获取自选行情列表
        quote_list = []
        data = self.ioModal.read_csv_file(path='./data/self_selection.csv')
        if data.empty:
            quote_list = []
        else:
            for index, item in data.iterrows():
                quote_list.append(str(item['quote']))
        #         self.self_selection_dict[str(item['quote'] + '_1_min')] = str(item['quote'] + '_1_min')
        #         self.self_selection_dict[str(item['quote'] + '_15_min')] = str(item['quote'] + '_15_min')
        #         self.self_selection_dict[str(item['quote'] + '_30_min')] = str(item['quote'] + '_30_min')
        #         self.self_selection_dict[str(item['quote'] + '_60_min')] = str(item['quote'] + '_60_min')
        #         self.self_selection_dict[str(item['quote'] + '_120_min')] = str(item['quote'] + '_120_min')
        #         self.self_selection_dict[str(item['quote'] + '_240_min')] = str(item['quote'] + '_240_min')
        #         self.self_selection_dict[str(item['quote'] + '_1440_min')] = str(item['quote'] + '_1440_min')

        # print(self.self_selection_dict)
        return quote_list


    def get_strategy_list(self, path):  # 从策略文件中自动搜索并获取策略类名 列表
        class_name_list = []
        try:
            file_list = os.listdir(path)
        except:
            file_list = []
            print('the path is not dir')
        if file_list:
            for file in file_list:
                file = os.path.join(path, file)
                if os.path.isdir(file):
                    self.get_strategy_list(file)
                else:
                    if file.endswith('.py'):
                        with open(file, encoding='utf-8') as f:
                            for line in f.readlines():
                                cls_match = re.match(r'class\s(.*?)[\(:]', line)  # 用正则表达式寻找class关键字之后的类名
                                if cls_match:
                                    cls_name = cls_match.group(1)

                                    # 判断cls_name是否是和文件名相同的类
                                    if cls_name == file.split('\\')[-1].split('.')[0]:
                                        class_name_list.append(cls_name)
                                    else:
                                        pass
        return class_name_list


    def switch_left_panel(self, enable):  # 左侧面板大小切换
        if enable:
            width = self.left_panel.width()
            max_with = 250
            min_with = 0
            if width > 100:
                widthExtended = min_with
            else:
                widthExtended = max_with
            # 动画效果
            self.animation = QPropertyAnimation(self.left_panel, b"maximumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)  # 设置动画的缓动效果
            self.animation.start()


    def maxmize_normalmize(self):  # 窗口最大化和还原
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
            self.left_panel.setMaximumWidth(280)


    def previous_page(self):  # 向前翻页
        t = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(t - 1)

    def next_page(self):  # 向后翻页
        t = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(t + 1)


    def choose_client_photo_File(self):  # 选择客户头像
        fileName_choose, filetype = QFileDialog.getOpenFileName(self, '选取文件', self.cwd,  # 起始路径
                                                                'All Files (*);;Text Files (*.txt)')  # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == '':
            print('\n没有选择任何文件')
            return

        self.clients_photo_address.setText(fileName_choose)
        self.show_client_photo(fileName_choose)


    def show_client_photo(self, file):  # 显示客户头像
        img = QImage()

        if img.load(file):

            width = img.width()
            height = img.height()

            if width >= height:
                ratio = width / 500
            else:
                ratio = height / 500
            new_width = width / ratio
            new_height = height / ratio

            self.label_client_photo_show.setFixedSize(new_width, new_height)
            self.label_client_photo_show.setPixmap(QPixmap(file).scaled(new_width, new_height))


    def get_clients(self):  # 获取并保存输入的用户信息

        if self.clients_name.text():  # 必须输入用户名
            clients_dict = {}
            clients_dict['clients_name'] = self.clients_name.text()
            clients_dict['clients_id'] = self.clients_id.text()
            clients_dict['clients_tel'] = self.clients_tel.text()
            clients_dict['clients_address'] = self.clients_address.text()
            clients_dict['clients_photo_address'] = self.clients_photo_address.text()

            # 判断是否存在clients_photo文件夹，如果不存在，则创建
            if not os.path.exists('./clients_photo'):
                os.makedirs('./clients_photo')
            try:

                if self.clients_photo_address.text():
                    print(clients_dict['clients_address'])
                    # 将clients_photo_address.text()的图片复制到clients_photo文件夹中
                    # 打开源图片
                    f_src = open(self.clients_photo_address.text(), 'rb')
                    # self.clients_photo_address.text()表示图片路径，为字符串。

                    # 读取图片内容并存储到content临时变量
                    content = f_src.read()

                    # 以二进制格式打开复制后的图片（只写）
                    # wb一般用于非文本文件如图片等。
                    # 如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
                    # 如果该文件不存在，创建新文件。
                    photo_name = './clients_photo/' + self.clients_name.text() + '.jpg'
                    f_copy = open(photo_name, 'wb')

                    # 源图片的内容以二进制形式写入新图片
                    f_copy.write(content)
                    # 关闭文件（原则：先打开的后关闭）
                    f_copy.close()
                    f_src.close()

                    clients_dict['clients_photo_address'] = photo_name

                df = pd.DataFrame(clients_dict, index=[0])
                path = './data/clients.csv'
                self.ioModal.judge_config_exist(path)
                self.ioModal.add_dict_to_csv(df, path)
                self.clients_input_clear()
                self.add_paramer_to_container_by_hand()
                self.add_paramer_to_combobox()
            except Exception as e:
                print(e)
        else:
            # self.textBrowser_clients_details.clear()
            self.textBrowser_clients_details.append('添加用户信息时用户名不能为空')

    def clients_input_clear(self):  # 清空客户信息输入框
        self.add_paramer_to_combobox()
        self.clients_name.clear()
        self.clients_id.clear()
        self.clients_tel.clear()
        self.clients_address.clear()
        self.clients_photo_address.clear()


    def get_tq_account(self):  # 获取天勤账号信息
        if self.comboBox_select_clients_name.currentText():
            if self.tq_account.text() and self.tq_psd.text():
                tq_account_dict = {}
                tq_account_dict['clients_name'] = self.comboBox_select_clients_name.currentText()
                tq_account_dict['tq_account'] = self.tq_account.text()
                tq_account_dict['tq_psd'] = self.tq_psd.text()
                tq_account_dict['futures_company'] = self.futures_company.text()
                tq_account_dict['futures_account'] = self.futures_account.text()
                tq_account_dict['futures_psd'] = self.futures_psd.text()

                df = pd.DataFrame(tq_account_dict, index=[0])
                path = './data/tq_account.csv'
                self.ioModal.judge_config_exist(path)
                self.ioModal.add_dict_to_csv(df, path)
                self.tq_account_input_clear()
                self.add_paramer_to_container_by_hand()
                self.add_paramer_to_combobox()
            else:
                # self.textBrowser_tq_account_details.clear()
                self.textBrowser_tq_account_details.append('添加天勤账户时，天勤账户名和密码不能为空')
        else:
            # self.textBrowser_tq_account_details.clear()
            self.textBrowser_tq_account_details.append('请先添加用户，然后才能添加天勤账户')

    def tq_account_input_clear(self):  # 清空天勤账号信息输入框
        self.add_paramer_to_combobox()
        self.tq_account.clear()
        self.tq_psd.clear()
        self.futures_company.clear()
        self.futures_account.clear()
        self.futures_psd.clear()


    def add_paramer_to_combobox(self):  # 将参数添加到combobox中
        self.comboBox_select_clients_name.clear()
        self.add_clients_list_to_combobox()


    def add_clients_list_to_combobox(self):  # 将用户列表添加到combobox中
        clients_list = self.get_clients_list()
        for item in clients_list:
            self.comboBox_select_clients_name.addItem(item)


    def get_inactivated_process_quantity(self):  # 获取可自启动但还未启动的策略进程数量
        path = './data/config.csv'
        data = self.ioModal.read_csv_file(path)
        quantity = 0
        if data.empty:
            pass
        else:
            for index, item in data.iterrows():
                if item['whether_self_start']:
                    quantity += 1
        return quantity


    def get_tq_account_quantity(self):  # 获取天勤账户数量
        path = './data/tq_account.csv'
        data = self.ioModal.read_csv_file(path)
        quantity = 0
        if data.empty:
            pass
        else:
            for index, item in data.iterrows():
                if item['tq_account']:
                    quantity += 1
        return quantity


    def get_total_profit(self):  # 计算总盈亏
        path = './data/config.csv'
        data = self.ioModal.read_csv_file(path)
        total_profit = 0
        if data.empty:
            pass
        else:
            for index, item in data.iterrows():
                try:
                    # 如果item['initial_capital']和item['final_capital']都存在且不为NaN
                    if item['initial_capital'] and item['final_capital']:
                        if item['initial_capital'] != 'NaN' and item['final_capital'] != 'NaN':
                            # 判断item['initial_capital']和item['final_capital']是否为字符型
                            if isinstance(item['initial_capital'], str) and isinstance(item['final_capital'], str):
                                pass
                            else:

                                profit = float(item['final_capital']) - float(item['initial_capital'])
                                total_profit += profit
                        else:
                            pass

                    else:
                        pass
                except:
                    pass
        return total_profit


    def get_frame_runing_time(self):  # 计算框架运行时间
        start_time = self.start_time
        current_time = datetime.now()

        gap = current_time - start_time
        days = gap.days
        hours = gap.seconds // 3600
        minutes = (gap.seconds % 3600) // 60
        seconds = (gap.seconds % 3600) % 60

        time_interval = str(days) + ' 天   ' + str(hours) + ' 小时 \n' + str(minutes) + ' 分   ' + str(seconds) + ' 秒 '
        return time_interval


    def open_file_with_excel(self, path):  # 用 excel 打开文件

        out_file = Path.cwd() / path
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = True
        excel.Workbooks.Open(out_file)


    def draw_dount_chart(self):  # 画饼图
        # chart = QChart()
        pi = self.pieCard
        cd = DonutWidget(pi)
        cd.add_donut()


    def load_deal_detials_data(self):  # 加载交易明细数据
        dirs = './data/'
        deal_detials_header_list = ['日期', '时间', '合约', '开平', '方向', '手数', '价格', '手续费', ]
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        if os.path.exists('./data/deal_detials.csv'):
            df = pd.read_csv('./data/deal_detials.csv')
            if df.empty:
                self.tableWidget_deal_detials.setHorizontalHeaderLabels(deal_detials_header_list)
            else:
                table = self.tableWidget_deal_detials
                table.setColumnCount(len(df.columns))
                table.setHorizontalHeaderLabels(df.columns)
                table.setRowCount(len(df.index))

                for rn, row in enumerate(df.index):
                    for cn, col in enumerate(df.columns):
                        item = QTableWidgetItem(str(df.loc[row, col]))
                        table.setItem(rn, cn, item)
                        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 文字具中显示
        else:
            path = './data/deal_detials.csv'
            self.ioModal.judge_config_exist(path)
            print('文件不存在，已创建空文件')


    def load_process_config(self):  # 加载策略进程配置表
        dirs = './data/'
        process_header_list = ['序号', '进程名（策略实例名）', '是否自行启动', '客户名', '天勤帐户', '天勤密码', '期货公司', '期货帐户', '期货资金密码', '合约名称',
                               '合约周期', '策略名称', '是否实盘', '是否回测', '是否开启web', 'web端口', '交易状态', '交易方向', '初始资金', '当前资金', '合约倍数',
                               '保证金率', '止损位%', '止盈位%', '多单加仓次数', '多单当前持仓', '多单首次成交价', '多单首次成交量', '空单加仓次数', '空单首次成交价',
                               '空单首次成交量', '空单当前持仓', '是否定义了开仓直线', '开仓直线坐标', '是否定义了平仓直线', '平仓直线坐标', '自定义参数1',
                               '自定义参数2', '自定义参数3', '自定义参数4', '自定义参数5', '自定义参数6', '自定义参数7', '自定义参数8', ]
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        if os.path.exists('./data/config.csv'):
            df = pd.read_csv('./data/config.csv')
            self.tableWidget_process.setVerticalHeaderLabels(process_header_list)
            self.tableWidget_process.setColumnCount(10)  # 设置列数量
            if df.empty:
                pass
            else:
                if len(df) == 0:
                    pass
                else:
                    table = self.tableWidget_process
                    if len(df.index) >= 10:
                        table.setColumnCount(len(df.index))  # 设置列数量
                    table.setRowCount(len(df.columns))  # 设置行数量
                    list = df['process_name'].tolist()
                    header_name_list = []
                    for name in list:
                        tmp = name.split('-', 3)[0] + '-' + name.split('-', 3)[1] + '-' + name.split('-', 3)[2] + '\n-' + name.split('-', 3)[3]
                        header_name_list.append(tmp)
                    table.setHorizontalHeaderLabels(header_name_list)
                    table.setVerticalHeaderLabels(df.columns)

                    for cn, col in enumerate(df.columns):
                        table.setColumnWidth(cn, 180)
                        for rn, row in enumerate(df.index):
                            item = QTableWidgetItem(str(df.loc[row, col]))
                            table.setItem(cn, rn, item)
                            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 文字具中显示

                    table.setVerticalHeaderLabels(process_header_list)
                    # table.setRowHeight(1, 40)
                    table.verticalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        else:
            path = './data/config.csv'
            self.ioModal.judge_config_exist(path)
            print('文件不存在，已创建空文件')


    def add_self_selection_list(self):  # 将天勤自选行情引用数据添加到 csv 文件中
        my_dict = {}
        exchange = self.comboBox_add_quote_exchange.currentText().split()[-1]  # 获取列表框选择的字符串分割后的最后一部分
        quote = exchange + '.' + self.add_quote_symbol.text()
        if self.add_quote_symbol.text():
            my_dict['quote'] = quote
            df = pd.DataFrame(my_dict, index=[0])
            # self.ceate_TQ_klines_and_quote(quote)
            self.ioModal.add_dict_to_csv(df, path='./data/self_selection.csv')
            text = '新的自选合约： ' + str(quote) + '  已添加'
            self.label_kline_info.setText(text)
            self.add_quote_symbol.clear()
            self.add_paramer_to_container_by_hand()
        else:
            self.label_kline_info.setText('请输入正确的合约名再点添加')


    def set_current_dissplayed_Kline(self, qModelIndex):  # 显示订阅的k线
        row = qModelIndex.row()
        data = self.ioModal.read_csv_file(path='./data/self_selection.csv')
        self.current_dissplayed_Kline = str(data.loc[row]['quote'])
        print('当前显示的合约为:', self.current_dissplayed_Kline)


    def init_Klines_chart(self):
        self_selection_quote_list = self.get_self_selection_quote_list()  # 获取自选合约列表
        if self_selection_quote_list:  # 如果列表不为空
            for kl in self_selection_quote_list:
                if (kl + '_quote') not in self.Quote_klines_dict:
                    self.current_dissplayed_Kline = kl
                    break
                else:
                    pass
            klines = kl + '_15_min'
            quote = kl + '_quote'
            # datas=self.Quote_klines_dict['%s'%klines]
            # quote=self.Quote_klines_dict['%s'%quote]
            self.Set_Klines_Chart(datas=self.Quote_klines_dict['%s' % klines], quote=self.Quote_klines_dict['%s' % quote])
            self.label_kline_info.setText(klines)


    def Set_Klines_Chart(self, datas, quote):  # 设置K线图表

        self.Update_quotes(quote)

        # pg.setConfigOption
