# -*- coding: utf-8 -*-

import os
import re
from datetime import datetime
import importlib
import webbrowser
from PySide6 import QtCore
from PySide6.QtGui import QCursor, Qt
from PySide6.QtWidgets import (QWidget)

from read_write_file import ReadWriteCsv
from UI.CreateBackTestProcess_dark import Ui_Form as UI_dark
from UI.CreateBackTestProcess_light import Ui_Form as UI_light

from main import THEME

if THEME == "dark":
    UI = UI_dark
else:
    UI = UI_light

class BackTestWindow(QWidget, UI):  # 创建回测窗口类
    def __init__(self, parent):
        super(BackTestWindow, self).__init__()
        self.setupUi(self)
        self.parent = parent

        # 不显示标题栏
        flags = QtCore.Qt.WindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        # 不显示空白边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)        
        # 设置透明度
        self.setWindowOpacity(0.95)

        # self.parent.ioModule = self.parent.ioModule   # 创建读写csv文件对象
        self.pid = None
        self.backtest_name = None
        self.add_paramer_to_combobox()
        self.label_info.setText("回测进程名的定义为：回测+当前时间+策略模板名+合约名+周期（分钟）\n创建回测进程时,策略模板名,合约名,周期三者不可缺少")

        self.Btn_start_backtest.clicked.connect(self.get_backtest_parameters)                       # 开始回测按钮点击事件槽函数
        self.Btn_stop_backtest.clicked.connect(self.stop_backtest_process)
        self.Btn_clear_backtest_parameters.clicked.connect(self.process_parameters_input_clear)     # 清空回测参数按钮点击事件槽函数
        self.Btn_open_with_chrome.clicked.connect(self.open_backtest_web_with_sys_browser)          # 打开回测网页按钮点击事件槽函数
        self.calendar_backtest_startdate.selectionChanged.connect(self.get_backtest_date)           # 回测开始日期日历点击事件槽函数
        self.calendar_backtest_enddate.selectionChanged.connect(self.get_backtest_date)             # 回测结束日期日历点击事件槽函数

        self.comboBox_exchange.activated.connect(self.add_contracts_to_comboBox_symbol)  # comboBox 信号槽函数
        self.comboBox_contract_type.activated.connect(self.add_contracts_to_comboBox_symbol)

    def mousePressEvent(self, e):  # 鼠标点击事件
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPosition().toPoint() - self.pos()
            e.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseReleaseEvent(self, e):  # 鼠标释放事件
        if e.button() == Qt.LeftButton:
            self.m_drag = False
            self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseMoveEvent(self, e):    # 鼠标拖动事件
        if Qt.LeftButton and self.m_drag:  
            self.move(e.globalPosition().toPoint() - self.m_DragPosition)
            e.accept()        

    def add_paramer_to_combobox(self):  # 将参数添加到combobox中
        
        self.comboBox_select_tq_account.clear()
        self.comboBox_select_strategy.clear()
        self.add_tq_account_list_to_combobox()
        self.add_strategy_list_to_combobox()

    def add_tq_account_list_to_combobox(self):  # 将天勤账号列表添加到combobox中
        tq_account_list = self.get_tq_account_list()
        for item in tq_account_list:
            self.comboBox_select_tq_account.addItem(item)

    def get_tq_account_list(self):  # 获取天勤账号列表
        tq_account_list = []
        data = self.parent.ioModule.read_csv_file(path='./data/tq_account.csv')
        if data.empty:
            pass
        else:
            for index, item in data.iterrows():
                tq_account_list.append(str(item['tq_account']))

        return tq_account_list            

    def add_strategy_list_to_combobox(self):    # 将策略列表添加到combobox中
        strategy_list = self.get_strategy_list(path='./strategys')
        for item in strategy_list:
            self.comboBox_select_strategy.addItem(item)
            pass

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
                                cls_match = re.match(r'class\s(.*?)[\(:]', line)        # 用正则表达式寻找class关键字之后的类名
                                if cls_match:
                                    cls_name = cls_match.group(1)    

                                    #判断cls_name是否是和文件名相同的类
                                    if cls_name == file.split('\\')[-1].split('.')[0]:
                                        class_name_list.append(cls_name)                                        
                                    else:
                                        pass                                    
        return class_name_list

    def add_contracts_to_comboBox_symbol(self):
        if self.comboBox_contract_type.currentText():
            exchange = self.comboBox_exchange.currentText().split()[-1]
            type = self.comboBox_contract_type.currentText().split()[-1]
            pth = './available_contracts/' + exchange + '_' + type + '.csv'
            if os.path.exists(pth):
                data = self.parent.ioModule.read_csv_file(path=pth)
                list = data['0'].tolist()
                self.comboBox_symbol.clear()
                self.comboBox_symbol.addItems(list)

    def get_backtest_parameters(self):  # 获取创建一个策略回测进程所需参数
        df = self.parent.ioModule.read_csv_file(path='./data/tq_account.csv')
        my_dict = {}
        now = datetime.now()
        now_str = now.strftime('%Y.%m.%d-%H时%M分')                      # 获取当前时间,用于生成回测进程名

        if self.comboBox_select_tq_account.currentText():               # 检查是否有天勤账户
            if self.comboBox_select_strategy.currentText():             # 检查是否有策略模板
                if self.comboBox_contract_type.currentText():           # 检查合约类型栏是否为空
                    if self.comboBox_symbol.currentText():              # 检查合约栏是否有内容
                        path_contract = ('./available_contracts/' + self.comboBox_exchange.currentText().split()[-1] + '_' + self.comboBox_contract_type.currentText().split()[-1] + '.csv')

                        if os.path.exists(path_contract):  # 检查是否有合约表文件
                            data = self.parent.ioModule.read_csv_file(path=path_contract)
                            list = data['0'].tolist()

                            if self.comboBox_symbol.currentText() in list:  # 检查输入的合约在不在合约表文件里面
                                if self.symbol_period.text():  # 检查是否有合约周期

                                    # 回测进程名的定义为：回测+当前时间+策略名+合约名+周期（分钟），
                                    # 与正式运行的策略名区分开来，
                                    # 因为保存日志的时候是按进程名新建文件夹保存的，区分开来便于查找
                                    process_name = (
                                        '回测' + '-{' + now_str +'}-' + self.comboBox_select_strategy.currentText() + '-'
                                        + self.comboBox_symbol.currentText() + '-' + self.symbol_period.text() + 'min'
                                    )

                                    my_dict['process_name'] = process_name  # 进程名称或策略实例名称
                                    my_dict['client_name'] = ' '  # 回测时不需要客户名称
                                    my_dict['tq_account'] = self.comboBox_select_tq_account.currentText()  # 天勤账号

                                    current_tq_account = self.comboBox_select_tq_account.currentText()
                                    index = df.index[df['tq_account'] == current_tq_account]  # 获取当前所选项目对应的pd行index
                                    for idx, row in df.iterrows():
                                        if idx == index:
                                            my_dict['tq_psd'] = str(row['tq_psd'])  # 天勤密码
                                            my_dict['futures_company'] = row['futures_company']  # 期货公司
                                            my_dict['futures_account'] = row['futures_account']  # 期货账号
                                            my_dict['futures_psd'] = row['futures_psd']          # 期货密码
                                            break
                                    my_dict['symbol'] = self.comboBox_symbol.currentText()  # 合约代码
                                    my_dict['symbol_period'] = self.symbol_period.text()                # 合约周期
                                    my_dict['strategy'] = self.comboBox_select_strategy.currentText()   # 策略名称
                                    my_dict['whether_self_start'] = True                              # 是否自启动，回测时此项默认为True
                                    my_dict['whether_live_trading'] = False                           # 是否实盘交易，回测时此项默认为False
                                    my_dict['whether_backtest'] = True                                # 是否回测
                                    my_dict['whether_open_web_services'] = True                       # 是否启动web服务，回测时此项默认为True
                                    my_dict['web_port'] = self.web_port.text()                          # 网页端口

                                    my_dict['trading_status'] = True                                    # 停止交易标志位，0为正常交易，1为停止交易
                                    my_dict['orientation'] = self.orientation.text()                    # 交易方向,用于半自动化策略,0为无方向,1或正整数为做多,-1或负整数为做空
                                    my_dict['initial_capital'] = self.initial_capital.text()            # 初始资金
                                    my_dict['final_capital'] = self.initial_capital.text()              # 最终资金
                                    my_dict['contract_multiples'] = self.contract_multiples.text()      # 合约倍数
                                    my_dict['margin_rate'] = self.margin_rate.text()                    # 保证金率
                                    my_dict['stop_loss'] = self.stop_loss.text()                        # 止损点
                                    my_dict['stop_profit'] = self.stop_profit.text()                    # 止盈点

                                    my_dict['long_add_times'] = 0  # 做多累积次数
                                    my_dict['long_current_position'] = 0  # 当前多单持仓
                                    my_dict['first_long_price'] = 0  # 第一次做多价格
                                    my_dict['first_long_deal'] = 0  # 第一次做多成交量
                                    my_dict['short_add_times'] = 0  # 做空累积次数
                                    my_dict['short_current_position'] = 0  # 当前空单持仓
                                    my_dict['first_short_price'] = 0  # 第一次做空价格
                                    my_dict['first_short_deal'] = 0  # 第一次做空成交量

                                    my_dict['whether_open_line'] = self.checkBox_whether_open_line.isChecked()  # 是否定义了开仓直线
                                    my_dict['open_line_Coordinates'] = self.open_line_Coordinates.text()  # 开仓线坐标
                                    my_dict['whether_close_line'] = self.checkBox_whether_close_line.isChecked()  # 是否定义了平仓直线
                                    my_dict['close_line_Coordinates'] = self.close_line_Coordinates.text()  # 平仓线坐标

                                    my_dict['CP1'] = self.Customized_parameters1.text()         # 自定义参数1  Customized_parameters 为了方便使用,缩写为CP
                                    my_dict['CP2'] = self.Customized_parameters2.text()         # 自定义参数2
                                    my_dict['CP3'] = self.Customized_parameters3.text()         # 自定义参数3
                                    my_dict['CP4'] = self.Customized_parameters4.text()         # 自定义参数4
                                    my_dict['CP5'] = self.Customized_parameters5.text()         # 自定义参数5
                                    my_dict['CP6'] = self.Customized_parameters6.text()         # 自定义参数6
                                    my_dict['CP7'] = self.Customized_parameters7.text()         # 自定义参数7
                                    my_dict['CP8'] = self.Customized_parameters8.text()         # 自定义参数8
                                    my_dict['CP9'] = self.Customized_parameters9.text()         # 自定义参数9

                                    index = 0

                                    if (self.label_backtest_startdate.text() == '') or (self.label_backtest_enddate.text() == ''):
                                        self.label_info.setText('请先选择回测开始日期和结束日期')
                                    else:
                                        backtest_start_date = self.label_backtest_startdate.text()
                                        backtest_end_date = self.label_backtest_enddate.text()
                                        #定义一个元组，用于存储日期和字典
                                        backtest_tuple = (index, my_dict, backtest_start_date, backtest_end_date)
                                        print('传入回测的元组为：' + str(backtest_tuple))
                                        self.start_backtest_process(backtest_tuple)


                                else:
                                    self.label_info.setText('请先输入回测周期,该项参数不可缺少')
                            else:
                                self.label_info.setText('输入的合约名不在天勤的可用合约列表里,请仔细检查')
                        else:
                            self.label_info.setText('没有可用的合约表,请先运行一次天勤行情服务,下载可用合约表')
                    else:
                        self.label_info.setText('请先输入或选择合适的合约名再点添加')
                else:
                    self.label_info.setText('请先选择合约类型')
            else:
                self.label_info.setText('没有可有用策略模板')
        else:
            self.label_info.setText('请先添加至少一个可用的天勤帐户')



    def start_backtest_process(self, tuple):    # 启动回测进程
        
        module = 'strategys' + '.' + tuple[1]['strategy']
        strategy_class_name = tuple[1]['strategy']

        m = importlib.import_module(module)  # 导入模块
        my_class = getattr(m, strategy_class_name)  # 获取类

        t = my_class(args=tuple)  # 实例化类
        t.name = tuple[1]['process_name']  # 设置进程名称
        t.start()  # 启动进程
        self.parent.Process_dict[tuple[1]['process_name']] = t.pid
        self.pid = t.pid
        self.backtest_name = tuple[1]['process_name']
        self.label_info.setText('已成功添加回测进程： ' + tuple[1]['process_name'] + '     进程pid为:  ' + str(t.pid))

    def stop_backtest_process(self):
        if self.pid:
            list = self.parent.get_alive_process_pid_list()
            if self.pid in list:
                self.parent.kill_process(self.pid)
                self.label_info.setText('pid为:  ' + str(self.pid) + '  的回测进程： ' + self.backtest_name + '     已关闭')
                self.pid = None
            else:
                self.label_info.setText('  没有运行的 回测进程  ')
        else:
            self.label_info.setText('  没有运行的 回测进程  ' )

    def get_backtest_date(self):    # 获取回测日期
        start_date = self.calendar_backtest_startdate.selectedDate()
        self.label_backtest_startdate.setText(str(start_date.toPython()))
        end_date = self.calendar_backtest_enddate.selectedDate()
        self.label_backtest_enddate.setText(str(end_date.toPython()))
        

    def process_parameters_input_clear(self):  # 清空回测进程参数输入框
        self.add_paramer_to_combobox()

        self.comboBox_exchange.setCurrentIndex(0)  # 默认交易所
        self.comboBox_contract_type.setCurrentIndex(-1)
        self.comboBox_symbol.clear()
        self.symbol_period.clear()
        self.initial_capital.clear()
        self.web_port.clear()
        self.orientation.clear()
        self.contract_multiples.clear()
        self.margin_rate.clear()
        self.stop_loss.clear()
        self.stop_profit.clear()
        self.Customized_parameters1.clear()
        self.Customized_parameters2.clear()
        self.Customized_parameters3.clear()
        self.Customized_parameters4.clear()
        self.Customized_parameters5.clear()
        self.Customized_parameters6.clear()
        self.Customized_parameters7.clear()
        self.Customized_parameters8.clear()
        self.Customized_parameters9.clear()
        self.label_backtest_startdate.clear()
        self.label_backtest_enddate.clear()

        self.checkBox_whether_open_line.setChecked(False)
        self.checkBox_whether_close_line.setChecked(False)
        self.open_line_Coordinates.clear()
        self.close_line_Coordinates.clear()

        self.label_info.setText('所有参数已清空，请重新输入')


    def open_backtest_web_with_sys_browser(self): # 用系统浏览器打开回测网页
        if self.web_port.text() == '':
            self.label_info.setText('请先设置网页端口')
        else:
            url = 'http://127.0.0.1' + ':' + self.web_port.text()
            print('打开了:  ', url, '\n')
            try:
                webbrowser.get('chrome').open_new_tab(url)
            except Exception as e:
                webbrowser.open_new_tab(url)