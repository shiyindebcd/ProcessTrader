# -*- coding: utf-8 -*-

import os
import re
import pandas as pd
from PySide6 import QtCore
from PySide6.QtGui import QCursor, Qt
from PySide6.QtWidgets import QWidget

from read_write_file import ReadWriteCsv
from UI.CreateNewProcess_dark import Ui_Form as UI_dark
from UI.CreateNewProcess_light import Ui_Form as UI_light

from main import THEME

if THEME == "dark":
    UI = UI_dark
else:
    UI = UI_light


class NewProcessWindow(QWidget, UI):   # 添加新的策略进程窗口类
    def __init__(self, parent):
        super(NewProcessWindow, self).__init__()
        self.parent = parent
        print(parent)
        self.setupUi(self)

        # 不显示标题栏
        flags = QtCore.Qt.WindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        # 不显示空白边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 设置透明度
        self.setWindowOpacity(0.95)

        self.ioModal = ReadWriteCsv()   # 创建读写文件对象

        self.add_paramer_to_combobox()
        self.label_info.setText('命名规则:  进程名（或策略实例名）= 客户名 + 天勤帐户 + 交易所.合约 + 合约周期 + min, '
                                '\n该名称将作为策略实例的名称，不能和已有的策略实例名重复.  添加时五个元素都不可或缺')
        
        self.Btn_add_process_param.clicked.connect(self.get_process_parameters)
        self.Btn_clear_input_process_param.clicked.connect(self.process_parameters_input_clear)
    

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
        self.comboBox_select_clients_name.clear()
        self.comboBox_select_tq_account.clear()
        self.comboBox_select_strategy.clear()        
        self.add_clients_list_to_combobox()
        self.add_tq_account_list_to_combobox()
        self.add_strategy_list_to_combobox()

    def add_clients_list_to_combobox(self): # 将用户列表添加到combobox中
        clients_list = self.get_clients_list()
        for item in clients_list:            
            self.comboBox_select_clients_name.addItem(item)

    def get_clients_list(self):   # 获取用户列表
        clients_list = []
        data = self.ioModal.read_csv_file(path='./data/clients.csv')
        if data.empty:
            clients_list = []
        else:
            for account in data['clients_name']:
                clients_list.append(str(account))

        return clients_list            

    def add_tq_account_list_to_combobox(self):  # 将天勤账号列表添加到combobox中
        tq_account_list = self.get_tq_account_list()
        for item in tq_account_list:
            self.comboBox_select_tq_account.addItem(item)

    def get_tq_account_list(self):  # 获取天勤账号列表
        tq_account_list = []
        data = self.ioModal.read_csv_file(path='./data/tq_account.csv')
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


    def get_process_parameters(self):   # 获取创建一个策略进程所需参数
        if self.comboBox_select_clients_name.currentText():     #检查是否有用户名
            if self.comboBox_select_tq_account.currentText():   # 检查是否有天勤账户
                if self.comboBox_select_strategy.currentText(): # 检查是否有策略模板
                    if self.symbol.text():                      # 检查是否有合约名
                        if self.symbol_period.text():           # 检查是否有合约周期

                            process_df = self.ioModal.read_csv_file(path='./data/config.csv')
                            if len(process_df) > 0:
                                name_list = process_df['process_name'].tolist()
                            else:
                                name_list = []
                            my_dict = {}
                            exchange = self.comboBox_exchange.currentText().split()[-1]  # 获取列表框选择的字符串分割后的最后一部分
                            symbol = exchange + '.' + self.symbol.text()
                            # 进程名（或策略实例名）= 客户名 + 天勤帐户 + 交易所.合约 + 合约周期,  该名称将作为策略实例的名称，不能重复
                            process_name = (
                                            self.comboBox_select_clients_name.currentText() + '-'
                                            + self.comboBox_select_tq_account.currentText() + '-'
                                            + self.comboBox_select_strategy.currentText() + '-'
                                            + symbol + '-' + self.symbol_period.text() + 'min'
                                            )
                            if process_name not in name_list:            # 判断进程名是否已在策略列表中
                                my_dict['process_name'] = process_name  # 进程名称或策略实例名称
                                my_dict['whether_self_start'] = self.checkBox_whether_self_start.isChecked()  # 是否自启动
                                my_dict['client_name'] = self.comboBox_select_clients_name.currentText()  # 客户名称
                                my_dict['tq_account'] = self.comboBox_select_tq_account.currentText()  # 天勤账号
                                current_tq_account = self.comboBox_select_tq_account.currentText()

                                TQ_qccount_df = self.ioModal.read_csv_file(path='./data/tq_account.csv')
                                index = TQ_qccount_df.index[TQ_qccount_df['tq_account'] == current_tq_account]  # 获取当前所选项目对应的pd行index
                                for idx, row in TQ_qccount_df.iterrows():
                                    if idx == index:
                                        my_dict['tq_psd'] = str(row['tq_psd'])  # 天勤密码
                                        my_dict['futures_company'] = row['futures_company']  # 期货公司
                                        my_dict['futures_account'] = row['futures_account']  # 期货账号
                                        my_dict['futures_psd'] = row['futures_psd']  # 期货密码
                                        break
                                my_dict['symbol'] = symbol  # 合约代码
                                my_dict['symbol_period'] = self.symbol_period.text()  # 合约周期
                                my_dict['strategy'] = self.comboBox_select_strategy.currentText()  # 策略名称
                                my_dict['whether_live_trading'] = self.checkBox_whether_live_futures_trading.isChecked()  # 是否实盘交易
                                my_dict['whether_backtest'] = False  # 是否回测
                                my_dict['whether_open_web_services'] = self.checkBox_whether_open_web_services.isChecked()
                                my_dict['web_port'] = self.web_port.text()  # 网页端口

                                my_dict['trading_status'] = True  # 交易状态标志位，默认True为正常交易，Flase为停止交易,可在策略中通过开关此位来停止或开启交易
                                my_dict['orientation'] = self.orientation.text()  # 交易方向,用于半自动化策略,0为无方向,1或正整数为做多,-1或负整数为做空
                                my_dict['initial_capital'] = self.initial_capital.text()  # 初始资金
                                my_dict['final_capital'] = self.initial_capital.text()  # 最终资金
                                my_dict['contract_multiples'] = self.contract_multiples.text()  # 合约倍数
                                my_dict['margin_rate'] = self.margin_rate.text()  # 保证金率
                                my_dict['stop_loss'] = self.stop_loss.text()  # 止损位
                                my_dict['stop_profit'] = self.stop_profit.text()  # 止盈位

                                my_dict['long_add_times'] = 0                               # 做多累积次数
                                my_dict['long_current_position'] = 0                        # 当前多单持仓
                                my_dict['first_long_price'] = 0                             # 第一次做多价格
                                my_dict['first_long_deal'] = 0                              # 第一次做多成交量
                                my_dict['short_add_times'] = 0                              # 做空累积次数
                                my_dict['short_current_position'] = 0                       # 当前空单持仓
                                my_dict['first_short_price'] = 0                            # 第一次做空价格
                                my_dict['first_short_deal'] = 0                             # 第一次做空成交量

                                my_dict['whether_open_line'] = False                      # 是否定义了开仓直线
                                my_dict['open_line_Coordinates'] = '0,0'                  # 开仓线坐标
                                my_dict['whether_close_line'] = False                     # 是否定义了平仓直线
                                my_dict['close_line_Coordinates'] = '0,0'                 # 平仓线坐标

                                my_dict['CP1'] = self.Customized_parameters1.text()         # 自定义参数1    Customized_parameters 为了方便使用,缩写为CP
                                my_dict['CP2'] = self.Customized_parameters2.text()         # 自定义参数2
                                my_dict['CP3'] = self.Customized_parameters3.text()         # 自定义参数3
                                my_dict['CP4'] = self.Customized_parameters4.text()         # 自定义参数4
                                my_dict['CP5'] = self.Customized_parameters5.text()         # 自定义参数5
                                my_dict['CP6'] = self.Customized_parameters6.text()         # 自定义参数6
                                my_dict['CP7'] = self.Customized_parameters7.text()         # 自定义参数7
                                my_dict['CP8'] = self.Customized_parameters8.text()         # 自定义参数8

                                print('已新添加策略，策略参数为： \n' + str(my_dict))
                                df = pd.DataFrame(my_dict, index=[0])
                                self.ioModal.add_dict_to_csv(df, path='./data/config.csv')
                                self.label_info.setText('新策略实例添加成功：  ' + str(my_dict['process_name']))
                                self.parent.load_process_config()
                            else:
                                self.label_info.setText('该进程名(策略实例名) 已在策略列表中,请勿添加相同的策略实例名')
                        else:
                            self.label_info.setText('添加一个策略实例时,合约周期不可缺少')
                    else:
                        self.label_info.setText('添加一个策略实例时,合约名不可缺少')
                else:
                    self.label_info.setText('没有可有用策略')
            else:
                self.label_info.setText('请先添加至少一个可用的天勤帐户')
        else:
            self.label_info.setText('请先添加至少一个用户')


    def process_parameters_input_clear(self):  # 清空进程参数输入框
        self.add_paramer_to_combobox()

        self.checkBox_whether_self_start.setChecked(True)  # 默认自启动
        self.checkBox_whether_live_futures_trading.setChecked(False)    # 默认不实盘交易
        self.checkBox_whether_open_web_services.setChecked(False)    # 默认不需要web服务 
        self.comboBox_exchange.setCurrentIndex(0)  # 默认交易所      
        self.symbol.clear()
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


        
        
       
        