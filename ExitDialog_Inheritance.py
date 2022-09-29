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

    def __init__(self, rowIndex):
        super(ModifyParameters, self).__init__()

        self.rowIndex = rowIndex
        self.path = './data/config.csv'
        self.dict = {}
        self.ioModal = ReadWriteCsv()  # 实例化 csv 读写类
        self.setupUi(self)

        # print('rowIndex: ', self.rowIndex)

        # 不显示标题栏
        self.setWindowFlags(QtCore.Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint))
        # 不显示空白边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 设置透明度
        self.setWindowOpacity(0.95)
        self.add_paramters_to_cell()

        self.Btn_submit_changes.clicked.connect(self.modify_config_parameters)

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
            data = self.ioModal.read_csv_file(self.path)
            self.dict = data.loc[self.rowIndex]
            self.label_info.setText(str(self.dict['process_name']))
            self.checkBox_whether_self_start.setChecked(self.dict['whether_self_start'])
            self.checkBox_whether_live_futures_trading.setChecked(self.dict['whether_live_trading'])
            self.checkBox_stop_trading.setChecked(self.dict['stop_trading'])
            self.checkBox_whether_open_web_services.setChecked(self.dict['whether_open_web_services'])
            self.checkBox_whether_open_line.setChecked(self.dict['whether_open_line'])
            self.checkBox_whether_close_line.setChecked(self.dict['whether_close_line'])

            self.web_port.setText(str(self.dict['web_port']))
            self.symbol_period.setText(str(self.dict['symbol_period']))
            self.initial_capital.setText(str(self.dict['initial_capital']))
            self.orientation.setText(str(self.dict['orientation']))
            self.contract_multiples.setText(str(self.dict['contract_multiples']))
            self.margin_rate.setText(str(self.dict['margin_rate']))
            self.stop_loss.setText(str(self.dict['stop_loss']))
            self.stop_profit.setText(str(self.dict['stop_profit']))
            self.open_line_Coordinates.setText(str(self.dict['open_line_Coordinates']))
            self.close_line_Coordinates.setText(str(self.dict['close_line_Coordinates']))
            self.Customized_parameters1.setText(str(self.dict['Customized_parameters_1']))
            self.Customized_parameters2.setText(str(self.dict['Customized_parameters_2']))
            self.Customized_parameters3.setText(str(self.dict['Customized_parameters_3']))
            self.Customized_parameters4.setText(str(self.dict['Customized_parameters_4']))
            self.Customized_parameters5.setText(str(self.dict['Customized_parameters_5']))
            self.Customized_parameters6.setText(str(self.dict['Customized_parameters_6']))
            self.Customized_parameters7.setText(str(self.dict['Customized_parameters_7']))
            self.Customized_parameters8.setText(str(self.dict['Customized_parameters_8']))


        except Exception as e:
            print(e)
            pass
    def modify_config_parameters(self):
        pass
