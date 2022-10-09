# -*- coding: utf-8 -*-
import os
import numpy

from PySide6.QtCore import QEvent
from PySide6.QtGui import QCursor, Qt
from PySide6.QtWidgets import QMenu
from ExitDialog_Inheritance import DeleteWarning
from ExitDialog_Inheritance import ModifyParameters

class RightButtonMenu:      # 主界面用到的各种右键菜单
    def __init__(self, parent):
        self.parent = parent

        # 菜单样式 所有菜单共用一个样式
        self.my_menu_style = '''QMenu{
                                        background:transparent;\n   
                                        font: 700 14pt \"\u7b49\u7ebf\";\n   
                                        border-radius: 0px;\n  
                                        border-color: none;\n    
                                        border:none;\n
                                    }\n
                                QMenu::item{
                                        padding:2px 15px 2px 15px;\n 
                                        height:30px;\n  color:blue;\n   
                                        margin:1px 1px 1px 1px;\n
                                        background-color: rgb(200,200,200);\n  
                                        border: none;\n  border-radius: none;\n
                                    }\n
                                QMenu::item:selected:enabled{                                    
                                        background:lightgray;\n   
                                        color:red;\n    
                                        background:rgb(255,255,255);\n
                                    }\n'''

# ---------------------------------------------------------------------
#  以下是右键点击后各个部件的弹出菜单
# ---------------------------------------------------------------------

    def clients_listview_menu(self, pos):
        cell = self.parent.clients_listview.indexAt(pos)
        rowIndex = cell.row()
        if rowIndex >= 0:
            menu = QMenu()
            menu.setStyleSheet(self.my_menu_style)
            meun1 = menu.addAction('删除此用户')
            # screenPos = self.parent.clients_listview.mapToGlobal(pos)  # 获得相对屏幕的位置
            # action = menu.exec(screenPos)  # 被阻塞, 执行菜单
            action = menu.exec(QCursor.pos())  # 被阻塞, 在鼠标点击位置执行菜单

            if action == meun1:
                Warning_Dialog = DeleteWarning()
                Warning_Dialog.show()
                Warning_Dialog.Btn_determine_delete.clicked.connect(lambda: self.delete_clients(rowIndex))
                Warning_Dialog.exec()
        else:
            return


    def clients_listview2_menu(self, pos):
        cell = self.parent.clients_listview2.indexAt(pos)
        rowIndex = cell.row()
        if rowIndex >= 0:
            menu = QMenu()
            menu.setStyleSheet(self.my_menu_style )
            meun1 = menu.addAction('删除此用户')
            # screenPos = self.parent.clients_listview2.mapToGlobal(pos)  # 获得相对屏幕的位置
            # action = menu.exec(screenPos)  # 被阻塞, 执行菜单
            action = menu.exec(QCursor.pos())  # 被阻塞, 在鼠标点击位置执行菜单

            if action == meun1:
                Warning_Dialog = DeleteWarning()
                Warning_Dialog.show()
                Warning_Dialog.Btn_determine_delete.clicked.connect(lambda: self.delete_clients(rowIndex))
                Warning_Dialog.exec()
        else:
            return

    def tq_account_listview_menu(self, pos):
        cell = self.parent.tq_account_listview.indexAt(pos)
        rowIndex = cell.row()
        if rowIndex >= 0:
            menu = QMenu()
            menu.setStyleSheet(self.my_menu_style)
            meun1 = menu.addAction('删除此天勤账户')
            # screenPos = self.parent.tq_account_listview.mapToGlobal(pos)  # 获得相对屏幕的位置
            # action = menu.exec(screenPos)  # 被阻塞, 执行菜单
            action = menu.exec(QCursor.pos())  # 被阻塞, 在鼠标点击位置执行菜单

            if action == meun1:
                Warning_Dialog = DeleteWarning()
                Warning_Dialog.show()
                Warning_Dialog.Btn_determine_delete.clicked.connect(lambda: self.delete_TQ_account(rowIndex))
                Warning_Dialog.exec()
        else:
            return

    def tq_account_listview2_menu(self, pos):
        cell = self.parent.tq_account_listview2.indexAt(pos)
        rowIndex = cell.row()
        if rowIndex >= 0:
            menu = QMenu()
            menu.setStyleSheet(self.my_menu_style)
            meun1 = menu.addAction('删除此天勤账户')
            # screenPos = self.parent.tq_account_listview2.mapToGlobal(pos)  # 获得相对屏幕的位置
            # action = menu.exec(screenPos)  # 被阻塞, 执行菜单
            action = menu.exec(QCursor.pos())  # 被阻塞, 在鼠标点击位置执行菜单

            if action == meun1:
                Warning_Dialog = DeleteWarning()
                Warning_Dialog.show()
                Warning_Dialog.Btn_determine_delete.clicked.connect(lambda: self.delete_TQ_account(rowIndex))
                Warning_Dialog.exec()
        else:
            return

    def self_selection_listview_menu(self, pos):
        cell = self.parent.self_selection_listview.indexAt(pos)
        rowIndex = cell.row()
        if rowIndex >= 0:
            menu = QMenu()
            menu.setStyleSheet(self.my_menu_style)
            meun1 = menu.addAction('删除这个自选')
            # screenPos = self.parent.self_selection_listview.mapToGlobal(pos)  # 获得相对屏幕的位置
            # action = menu.exec(screenPos)  # 被阻塞, 执行菜单
            action = menu.exec(QCursor.pos())  # 被阻塞, 在鼠标点击位置执行菜单

            if action == meun1:
                self.delete_self_seletion(rowIndex)
        else:
            return


    def process_listview_menu(self, pos):
        cell = self.parent.process_listview.indexAt(pos)
        rowIndex = cell.row()           # 在listview中鼠标右键点击位置的行号
        if rowIndex >= 0:

            list = self.parent.process_list_row
            name = list[rowIndex]
            if name.split('-', 3)[0] == '回测':       # 如果是回测进程,只需要一个结束菜单即可
                menu = QMenu()
                menu.setStyleSheet(self.my_menu_style)
                meun1 = menu.addAction('关掉此回测进程')
                # screenPos = self.parent.tableWidget_process.mapToGlobal(pos)  # 获得相对屏幕的位置
                action = menu.exec(QCursor.pos())  # 被阻塞, 在鼠标点击位置执行菜单

                if action == meun1:
                    pid = self.parent.Process_dict[name]
                    self.parent.kill_process(pid)
                    print('刚刚关掉的是回测进程:  ', name)

            else:
                self.parent.process_listview_selected_row = rowIndex
                data = self.parent.ioModal.read_csv_file('./data/config.csv')
                true_index = None               # 这个是策略在config文件中真正的行号,因为文件中有不自启或当前挂掉未运行的策略实例,所以两个行号不一定相同
                for index, item in data.iterrows():     # 通过遍历config.csv文件中,根据进程名,寻找到该进程在config中真正的行号
                    if name == item['process_name']:
                        true_index = index

                menu = QMenu()
                menu.setStyleSheet(self.my_menu_style)
                meun1 = menu.addAction('临时停止此策略实例')
                meun2 = menu.addAction('永久停止此策略实例')
                meun3 = menu.addAction('重启此策略实例')
                meun4 = menu.addAction('修改此策略实例参数')
                meun5 = menu.addAction('停止并删除此策略实例')

                # screenPos = self.parent.tableWidget_process.mapToGlobal(pos)  # 获得相对屏幕的位置
                action = menu.exec(QCursor.pos())  # 被阻塞, 在鼠标点击位置执行菜单

                if action == meun1:             # 临时停止此策略实例
                    self.stop_process_strategy_for_Temporary(true_index)
                elif action == meun2:           # 永久停止此策略实例
                    self.stop_process_strategy_for_Permanent(true_index)
                elif action == meun3:           # 重启此策略实例
                    self.reboot_process_strategy(true_index)
                elif action == meun4:           # 修改此策略实例参数
                    ModifyParameters_window = ModifyParameters(self.parent, true_index)
                    ModifyParameters_window.show()
                    ModifyParameters_window.exec()
                elif action == meun5:           # 停止并删除此策略实例
                    Warning_Dialog = DeleteWarning()
                    Warning_Dialog.show()
                    Warning_Dialog.Btn_determine_delete.clicked.connect(lambda: self.stop_and_delete_process(true_index))
                    Warning_Dialog.exec()

        else:
            return

    def precess_table_menu(self, pos):
        cell = self.parent.tableWidget_process.itemAt(pos)
        self.parent.label_process_right_btn_info.clear()
        if cell is not None:
            # rowIndex = cell.row()
            columnIndex = cell.column()
            menu = QMenu()  # 构造菜单
            menu.setStyleSheet(self.my_menu_style)
            # 添加菜单的选项
            menu1 = menu.addAction("临时停止此策略实例")
            menu2 = menu.addAction("永久停止此策略实例")
            menu3 = menu.addAction("重启此策略实例")
            menu4 = menu.addAction("修改此策略实例参数")
            menu5 = menu.addAction("停止并删除此策略实例")

            # screenPos = self.parent.tableWidget_process.mapToGlobal(pos)  # 获得相对屏幕的位置
            # action = menu.exec(screenPos)  # 被阻塞, 执行菜单

            action = menu.exec(QCursor.pos())  # 被阻塞, 在鼠标点击位置执行菜单
            # print('单元格的值为:' + str(self.parent.tableWidget_process.item(rowIndex, columnIndex).text()))      # 获取单元格的值

            if action == menu1:             # 临时停止此策略实例
                    self.stop_process_strategy_for_Temporary(columnIndex)
            elif action == menu2:           # 永久停止此策略实例
                    self.stop_process_strategy_for_Permanent(columnIndex)
            elif action == menu3:           # 重启此策略实例
                    self.reboot_process_strategy(columnIndex)
            elif action == menu4:           # 修改此策略实例参数
                    ModifyParameters_window = ModifyParameters(self.parent, columnIndex)
                    ModifyParameters_window.show()
                    ModifyParameters_window.exec()
            elif action == menu5:           # 停止并删除此策略实例
                    Warning_Dialog = DeleteWarning()
                    Warning_Dialog.show()
                    Warning_Dialog.Btn_determine_delete.clicked.connect(lambda: self.stop_and_delete_process(columnIndex))
                    Warning_Dialog.exec()
        else:
            self.parent.label_process_right_btn_info.setText('点击的单元格没有数据')
            return


#---------------------------------------------------------------------
#  以下是菜单点击后的执行函数部分
#---------------------------------------------------------------------


    def delete_clients(self, index):        # 删除用户
        path = './data/clients.csv'
        data = self.parent.ioModal.read_csv_file(path)
        photo_path = data.loc[index]['clients_photo_address']
        try:
            if type(photo_path) == numpy.float64:            # 判断照片地址是否为nan,只需要判断他的类型是否为numpy.64
                pass
            else:
                os.remove(photo_path)
        except Exception as e:
            print(e)
        tmp = data.drop(index=index)
        tmp = tmp.reset_index(drop=True)      # 重建索引
        self.parent.ioModal.write_datas_to_csv_file(df_tmp=tmp, path=path)
        self.parent.label_client_photo_show.clear()
        self.parent.textBrowser_clients_details.clear()
        self.parent.add_paramer_to_container_by_hand()

    def delete_TQ_account(self, index):     # 删除天勤账户

        path = './data/tq_account.csv'
        data = self.parent.ioModal.read_csv_file(path)
        tmp = data.drop(index=index)
        tmp = tmp.reset_index(drop=True)      # 重建索引
        self.parent.ioModal.write_datas_to_csv_file(df_tmp=tmp, path=path)
        self.parent.textBrowser_tq_account_details.clear()
        self.parent.add_paramer_to_container_by_hand()

    def stop_and_delete_process(self,  index):      # 停止并删除策略实例
        self.stop_process_strategy_for_Temporary(index)
        self.delete_process_config(index)

    def delete_process_config(self, index):      # 删除策略参数
        path = './data/config.csv'
        try:
            data = self.parent.ioModal.read_csv_file(path)
            tmp = data.drop(index=index)
            tmp1 = tmp.reset_index(drop=True)      # 重建索引
            self.parent.ioModal.write_datas_to_csv_file(df_tmp=tmp1, path=path)
            self.parent.tableWidget_process.clear()
            self.parent.load_process_config()
        except Exception as e:
            print(e)

    def delete_self_seletion(self, index):      # 删除自选
        path = './data/self_selection.csv'
        try:
            data = self.parent.ioModal.read_csv_file(path)
            contract = data.loc[index, 'quote']
            tmp = data.drop(index=index)
            tmp1 = tmp.reset_index(drop=True)      # 重建索引
            self.parent.ioModal.write_datas_to_csv_file(df_tmp=tmp1, path=path)
            self.parent.add_paramer_to_container_by_hand()

            # 删除自选时删除对应的kline数据文件
            path_1min = './Klines_Data/' + contract + '_1min.csv'
            self.parent.ioModal.delete_file(path_1min)
            path_15min = './Klines_Data/' + contract + '_15min.csv'
            self.parent.ioModal.delete_file(path_15min)
            path_30min = './Klines_Data/' + contract + '_30min.csv'
            self.parent.ioModal.delete_file(path_30min)
            path_1hour = './Klines_Data/' + contract + '_1hour.csv'
            self.parent.ioModal.delete_file(path_1hour)
            path_2hour = './Klines_Data/' + contract + '_2hour.csv'
            self.parent.ioModal.delete_file(path_2hour)
            path_4hour = './Klines_Data/' + contract + '_4hour.csv'
            self.parent.ioModal.delete_file(path_4hour)
            path_1day = './Klines_Data/' + contract + '_1day.csv'
            self.parent.ioModal.delete_file(path_1day)

        except Exception as ex:
            print(ex)

    def stop_process_strategy_for_Temporary(self, index):       # 临时停止策略实例
        path = './data/config.csv'
        dict = self.parent.Process_dict
        # print('进程pid字典:', dict)     # 输出为:进程pid字典: {'夺 夺-444444-pingTest-SHFE.rb2210-30min': 14872}
        data = self.parent.ioModal.read_csv_file(path)
        process_name = data.loc[index]['process_name']
        if process_name in dict:
            pid = dict[process_name]
            if pid:
                self.parent.kill_process(pid)
                self.parent.label_process_right_btn_info.setText('策略实例:  ' + str(process_name) + '  已被关闭,但会在一分钟后被框架尝试再次启动')
                print('策略:  ' + str(process_name) + '  已被关闭,但会在一分钟后被框架再次启动')
            else:
                self.parent.label_process_right_btn_info.setText('策略实例:  ' + str(process_name) + '  并未运行,但会在一分钟后被框架尝试启动')
                print('策略实例:  ' + str(process_name) + '  并未运行,但会在一分钟后被框架尝试启动')
        else:
            self.parent.label_process_right_btn_info.setText('策略实例:  ' + str(process_name) + '  从未被启动过')
            print('策略实例:  ' + str(process_name) + '  从未被启动过')

    def stop_process_strategy_for_Permanent(self, index):       # 永久停止策略实例
        path = './data/config.csv'
        dict = self.parent.Process_dict
        data = self.parent.ioModal.read_csv_file(path)
        process_name = data.loc[index, 'process_name']
        data.loc[index, 'whether_self_start'] = False           # 策略实例的 whether_self_start 设为False 就不会自动启动
        if process_name in dict:
            pid = dict[process_name]
            if pid:
                self.parent.kill_process(pid)
                self.parent.label_process_right_btn_info.setText('策略实例:  ' + str(process_name) + '  已被关闭,且已设置为不自动启动')
                print('策略实例:  ' + str(process_name) + '  已被关闭,且已设置为不自动启动')
            else:
                self.parent.label_process_right_btn_info.setText('策略实例:  ' + str(process_name) + '  并未运行,但已设置为不自动启动')
                print('策略实例:  ' + str(process_name) + '  并未运行,但已设置为不自动启动')
        else:
            self.parent.label_process_right_btn_info.setText('策略实例:  ' + str(process_name) + '  从未被启动过, 但已设置为不自动启动')
            print('策略实例:  ' + str(process_name) + '  从未被启动过, 但已设置为不自动启动')

        self.parent.ioModal.write_datas_to_csv_file(data, path)
        self.parent.load_process_config()




    def reboot_process_strategy(self, index):       # 重启此策略
        path = './data/config.csv'
        process_dict = self.parent.Process_dict
        data = self.parent.ioModal.read_csv_file(path)
        process_name = data.loc[index, 'process_name']
        row_dict = data.loc[index].to_dict()
        if row_dict['whether_self_start']:
            pid = process_dict[process_name]
            if pid:
                self.parent.kill_process(pid)
                self.parent.start_single_process(index, row_dict)
                self.parent.label_process_right_btn_info.setText('策略实例:  ' + str(process_name) + '  已重启')
                print('策略实例:  ' + str(process_name) + '  已重启')
            else:
                self.parent.start_single_process(index, row_dict)
                self.parent.label_process_right_btn_info.setText('策略实例:  ' + str(process_name) + '  之前并未运行,现已启动')
                ('策略实例:  ' + str(process_name) + '  之前并未运行,现已启动')
        else:
            self.parent.label_process_right_btn_info.setText('策略实例:  ' + str(process_name) + '  的参数为不自行启动,请先修改为允许自启动再点重启 ')
            print('策略实例:  ' + str(process_name) + '  的参数为不自行启动,请先修改为允许自启动再点重启 ')
