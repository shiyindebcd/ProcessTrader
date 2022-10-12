# -*- coding: utf-8 -*-

from PySide6 import QtCore
from PySide6.QtGui import QCursor, Qt
from PySide6.QtWidgets import (QDialog)

from read_write_file import ReadWriteCsv
from UI.Exit_dialog_dark import Ui_Dialog as UI_dark
from UI.Exit_dialog_light import Ui_Dialog as UI_light


from main import THEME

if THEME == "dark":
    UI = UI_dark
else:
    UI = UI_light


class Exit_Dialog(QDialog, UI):                # 退出程序对话框类
    def __init__(self):
        super(Exit_Dialog, self).__init__()
        self.setupUi(self)

        # 不显示标题栏        
        self.setWindowFlags(QtCore.Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint))
        # 不显示空白边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 设置透明度
        self.setWindowOpacity(0.95)        
        

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





if THEME == 'dark':
    from UI.Delete_Warning_dark import Ui_Dialog
else:
    from UI.Delete_Warning_light import Ui_Dialog
class DeleteWarning(QDialog, Ui_Dialog):  # 删除时警告对话框类

    def __init__(self):
        super(DeleteWarning, self).__init__()
        self.setupUi(self)

        # 不显示标题栏
        self.setWindowFlags(QtCore.Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint))
        # 不显示空白边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 设置透明度
        self.setWindowOpacity(0.95)

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




if THEME == 'dark':
    from UI.ModifyParameters_dark import Ui_Form
else:
    from UI.ModifyParameters_light import Ui_Form
class ModifyParameters(QDialog, Ui_Form):  # 修改策略参数窗口类

    def __init__(self, parent, rowIndex):
        super(ModifyParameters, self).__init__()
        self.parent = parent
        self.rowIndex = rowIndex
        self.setupUi(self)

        self.path = './data/config.csv'
        self.data = self.parent.ioModule.read_csv_file(self.path)
        self.init_dict = self.data.loc[self.rowIndex]
        self.finally_dict = {}

        # 不显示标题栏
        self.setWindowFlags(QtCore.Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint))
        # 不显示空白边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 设置透明度
        self.setWindowOpacity(0.95)
        self.Btn_submit_changes.clicked.connect(self.modify_config_parameters)
        self.add_paramters_to_cell()


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

    def add_paramters_to_cell(self):
        try:
            self.label_info.setText(str(self.init_dict['process_name']))
            self.checkBox_whether_self_start.setChecked(self.init_dict['whether_self_start'])
            self.checkBox_whether_live_futures_trading.setChecked(self.init_dict['whether_live_trading'])
            self.checkBox_trading_status.setChecked(self.init_dict['trading_status'])
            self.checkBox_whether_open_web_services.setChecked(self.init_dict['whether_open_web_services'])
            self.checkBox_whether_open_line.setChecked(self.init_dict['whether_open_line'])
            self.checkBox_whether_close_line.setChecked(self.init_dict['whether_close_line'])

            self.web_port.setText(str(self.init_dict['web_port']))
            self.symbol_period.setText(str(self.init_dict['symbol_period']))
            self.initial_capital.setText(str(self.init_dict['initial_capital']))
            self.orientation.setText(str(self.init_dict['orientation']))
            self.contract_multiples.setText(str(self.init_dict['contract_multiples']))
            self.margin_rate.setText(str(self.init_dict['margin_rate']))
            self.stop_loss.setText(str(self.init_dict['stop_loss']))
            self.stop_profit.setText(str(self.init_dict['stop_profit']))
            self.open_line_Coordinates.setText(str(self.init_dict['open_line_Coordinates']))
            self.close_line_Coordinates.setText(str(self.init_dict['close_line_Coordinates']))
            self.long_add_times.setText(str(self.init_dict['long_add_times']))
            self.short_add_times.setText(str(self.init_dict['short_add_times']))

            self.Customized_parameters1.setText(str(self.init_dict['CP1']))     # Customized_parameters 为了方便使用,缩写为CP
            self.Customized_parameters2.setText(str(self.init_dict['CP2']))
            self.Customized_parameters3.setText(str(self.init_dict['CP3']))
            self.Customized_parameters4.setText(str(self.init_dict['CP4']))
            self.Customized_parameters5.setText(str(self.init_dict['CP5']))
            self.Customized_parameters6.setText(str(self.init_dict['CP6']))
            self.Customized_parameters7.setText(str(self.init_dict['CP7']))
            self.Customized_parameters8.setText(str(self.init_dict['CP8']))
            self.Customized_parameters9.setText(str(self.init_dict['CP9']))

        except Exception as e:
            print(e)
            pass
    def modify_config_parameters(self):

        self.finally_dict['process_name'] = (str(self.init_dict['process_name']).split('-',4)[0] + '-' + str(self.init_dict['process_name']).split('-',4)[1] +
                                             '-' + str(self.init_dict['process_name']).split('-',4)[2] + '-' + str(self.init_dict['process_name']).split('-',4)[3] +
                                             '-' + str(self.symbol_period.text()) + 'min')

        self.finally_dict['whether_self_start'] = self.checkBox_whether_self_start.isChecked()  # 是否自启动
        self.finally_dict['whether_live_trading'] = self.checkBox_whether_live_futures_trading.isChecked()  # 是否实盘交易
        self.finally_dict['trading_status'] = self.checkBox_trading_status.isChecked()   # 交易状态标志位，默认True为正常交易，Flase为停止交易,可在策略中通过开关此位来停止或开启交易
        self.finally_dict['whether_open_web_services'] = self.checkBox_whether_open_web_services.isChecked()
        self.finally_dict['whether_open_line'] = self.checkBox_whether_open_line.isChecked()  # 是否定义了开仓直线
        self.finally_dict['whether_close_line'] = self.checkBox_whether_close_line.isChecked()  # 是否定义了平仓直线

        self.finally_dict['web_port'] = self.web_port.text()                                    # 网页端口
        self.finally_dict['symbol_period'] = self.symbol_period.text()                          # 合约周期
        self.finally_dict['initial_capital'] = self.initial_capital.text()                      # 初始资金
        self.finally_dict['orientation'] = self.orientation.text()                  # 交易方向,用于半自动化策略,0为无方向,1或正整数为做多,-1或负整数为做空
        self.finally_dict['contract_multiples'] = self.contract_multiples.text()    # 合约倍数
        self.finally_dict['margin_rate'] = self.margin_rate.text()                  # 保证金率
        self.finally_dict['stop_loss'] = self.stop_loss.text()                      # 止损位
        self.finally_dict['stop_profit'] = self.stop_profit.text()                  # 止盈位
        self.finally_dict['open_line_Coordinates'] = self.open_line_Coordinates.text()  # 开仓线坐标
        self.finally_dict['close_line_Coordinates'] = self.close_line_Coordinates.text()  # 平仓线坐标

        self.finally_dict['client_name'] = self.init_dict['client_name']
        self.finally_dict['tq_account'] = self.init_dict['tq_account']
        self.finally_dict['tq_psd'] = self.init_dict['tq_psd']
        self.finally_dict['futures_company'] = self.init_dict['futures_company']
        self.finally_dict['futures_account'] = self.init_dict['futures_account']
        self.finally_dict['futures_psd'] = self.init_dict['futures_psd']
        self.finally_dict['symbol'] = self.init_dict['symbol']
        self.finally_dict['strategy'] = self.init_dict['strategy']
        self.finally_dict['whether_backtest'] = self.init_dict['whether_backtest']
        self.finally_dict['final_capital'] = self.init_dict['final_capital']

        self.finally_dict['long_add_times'] = self.long_add_times.text()
        self.finally_dict['long_current_position'] = self.init_dict['long_current_position']
        self.finally_dict['first_long_price'] = self.init_dict['first_long_price']
        self.finally_dict['first_long_deal'] = self.init_dict['first_long_deal']
        self.finally_dict['short_add_times'] = self.short_add_times.text()
        self.finally_dict['short_current_position'] = self.init_dict['short_current_position']
        self.finally_dict['first_short_price'] = self.init_dict['first_short_price']
        self.finally_dict['first_short_deal'] = self.init_dict['first_short_deal']

        self.finally_dict['CP1'] = self.Customized_parameters1.text()  # 自定义参数1     Customized_parameters 为了方便使用,缩写为CP
        self.finally_dict['CP2'] = self.Customized_parameters2.text()  # 自定义参数2
        self.finally_dict['CP3'] = self.Customized_parameters3.text()  # 自定义参数3
        self.finally_dict['CP4'] = self.Customized_parameters4.text()  # 自定义参数4
        self.finally_dict['CP5'] = self.Customized_parameters5.text()  # 自定义参数5
        self.finally_dict['CP6'] = self.Customized_parameters6.text()  # 自定义参数6
        self.finally_dict['CP7'] = self.Customized_parameters7.text()  # 自定义参数7
        self.finally_dict['CP8'] = self.Customized_parameters8.text()  # 自定义参数8
        self.finally_dict['CP9'] = self.Customized_parameters9.text()  # 自定义参数9
        # print('最后的字典', self.finally_dict)

        self.data.loc[self.rowIndex] = self.finally_dict
        self.parent.ioModule.write_datas_to_csv_file(self.data, self.path)
        self.parent.load_process_config()




