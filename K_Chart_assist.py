# -*- coding: utf-8 -*-

from datetime import datetime
import pyqtgraph as pg
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import Qt, QCursor
from PySide6.QtWidgets import *
from UI.LineStyle_dark import Ui_Form as UI_dark
from UI.LineStyle_light import Ui_Form as UI_light

from main import THEME

if THEME == "dark":
    UI = UI_dark
else:
    UI = UI_light



# 绘制时，线条属性设置弹出框
class LineStyleWidget(QWidget, UI):        # 设置直线样式窗口类
    sinout_signal = QtCore.Signal(object)
    def __init__(self):
        super(LineStyleWidget, self).__init__()
        self.setupUi(self)
        # 不显示标题栏, 窗口总在最前
        flags = QtCore.Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        # 不显示空白边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 设置透明度
        self.setWindowOpacity(0.95)
        # 设置窗口左上角初始位置和宽高
        self.setGeometry(300, 100, 320, 260)

        self.default_color: str = '#ff007f'
        self.init_ui()

    def init_ui(self):

        self.Btn_change_color.clicked.connect(self.Btn_change_color_clicked)
        self.Btn_previous_step.clicked.connect(self.Btn_previous_step_clicked)
        self.Btn_linewidth_check.clicked.connect(self.Btn_linewidth_check_clicked)

        self.Btn_change_color.setStyleSheet(u"QPushButton{	\n"
                                            "	background-color:" + self.default_color + ";\n"
                                            "	font: 700 18pt \"\u7b49\u7ebf\";\n"
                                            "	border-radius: 20px;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "	border: 3px solid rgb(255, 200, 0);  \n"
                                            "}\n"
                                            "QPushButton:pressed{\n"
                                            "	color: green;\n"
                                            "	border-color: rgb(255, 0, 0);\n"
                                            "    background-color: rgb(255, 255, 0);\n"
                                            "}\n"
                                            "QPushButton:disabled{\n"
                                            "	color: rgb(31, 31, 31);\n"
                                            "    background-color: rgb(152, 152, 152);\n"
                                            "}")
        self.spinBox_linewidth.setValue(3)


    def Btn_change_color_clicked(self):
        col = QtWidgets.QColorDialog.getColor()
        if col.isValid():
            pal = self.Btn_change_color.palette()
            pal.setColor(QtGui.QPalette.WindowText,col)
            # self.label_current_color.setPalette(pal)
            pre_map = {
                'change_type':'color',
                'data':col.name()
            }
            self.sinout_signal.emit(pre_map)
        pass

    def Btn_previous_step_clicked(self):
        pre_map = {
            'change_type': 'pre_step',
            'data': None
        }
        self.sinout_signal.emit(pre_map)
        pass

    def Btn_linewidth_check_clicked(self):
        line_width = self.spinBox_linewidth.value()
        if int(line_width)<=0:
            QtWidgets.QMessageBox.information(
                self,
                '提示',
                '线条粗细必须大于0',
                QtWidgets.QMessageBox.Yes
            )
            return
        # linewidth
        pre_map = {
            'change_type':'linewidth',
            'data':int(line_width)
        }
        self.sinout_signal.emit(pre_map)
        pass


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

    def mouseMoveEvent(self, e):  # 鼠标拖动事件
        if Qt.LeftButton and self.m_drag:
            self.move(e.globalPosition().toPoint() - self.m_DragPosition)
            e.accept()



########################################################################
# 键盘鼠标功能
########################################################################
class KeyWraper(QWidget):
    """键盘鼠标功能支持的元类"""


    def __init__(self, parent=None):  # 初始化
        QWidget.__init__(self, parent)
        self.setMouseTracking(True)  # 设置鼠标跟踪
        self.autoFillBackground()


    def keyPressEvent(self, event):  # 重载方法keyPressEvent(self,event),即按键按下事件方法
        if event.key() == QtCore.Qt.Key_Up:
            self.onUp()
        elif event.key() == QtCore.Qt.Key_Down:
            self.onDown()
        elif event.key() == QtCore.Qt.Key_Left:
            self.onLeft()
        elif event.key() == QtCore.Qt.Key_Right:
            self.onRight()
        elif event.key() == QtCore.Qt.Key_PageUp:
            self.onPre()
        elif event.key() == QtCore.Qt.Key_PageDown:
            self.onNxt()


    def mousePressEvent(self, event):  # 重载方法mousePressEvent(self,event),即鼠标点击事件方法
        if event.button() == QtCore.Qt.RightButton:
            self.onRClick(event.pos())
        elif event.button() == QtCore.Qt.LeftButton:
            self.onLClick(event.pos())


    def mouseRelease(self, event):  # 重载方法mouseReleaseEvent(self,event),即鼠标点击事件方法
        if event.button() == QtCore.Qt.RightButton:
            self.onRRelease(event.pos())
        elif event.button() == QtCore.Qt.LeftButton:
            self.onLRelease(event.pos())
        self.releaseMouse()


    def wheelEvent(self, event):  # 重载方法wheelEvent(self,event),即滚轮事件方法
        return


    def paintEvent(self, event):  # 重载方法paintEvent(self,event),即拖动事件方法
        self.onPaint()


    def onNxt(self):  # PgDown键
        pass


    def onPre(self):  # PgUp键
        pass


    def onUp(self):  # 向上键和滚轮向上
        pass


    def onDown(self):  # 向下键和滚轮向下
        pass


    def onLeft(self):  # 向左键
        pass


    def onRight(self):  # 向右键
        pass


    def onLClick(self, pos):  # 鼠标左单击
        pass


    def onRClick(self, pos):  # 鼠标右单击
        pass


    def onLRelease(self, pos):  # 鼠标左释放
        pass


    def onRRelease(self, pos):  # 鼠标右释放
        pass


    def onPaint(self):  # 画图
        pass


########################################################################
# 时间序列，横坐标支持
########################################################################
class DatetimeAxis(pg.AxisItem):

    def __init__(self, datas, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data = datas  # 传入k线数据
        self.setPen(pg.mkPen(QtGui.QColor(255, 0, 0), width=1))  # 设置时间轴边框颜色
        self.tickFont = QtGui.QFont("Arial", 6)  # 时间轴刻度字体


    def tickStrings(self, values: list[int], scale: float, spacing: int):
        """
        Convert original index to datetime string.
        values自动传入x坐标
        """
        # 行索引和时间组合字典，行索引和x轴对应
        datetime_index_map = dict(zip(self.data.index, self.data.datetime))
        strings = []
        for ix in values:
            dt = datetime_index_map.get(ix, None)  # x轴对应的时间
            if not dt:
                s = ""
            else:
                dt = datetime.fromtimestamp(dt / 1e9)  # 转换成datetime格式
                if dt.hour:  # 日内周期
                    s = dt.strftime("%m-%d %H:%M")
                else:
                    s = dt.strftime("%Y-%m-%d")
            strings.append(s)
        return strings


