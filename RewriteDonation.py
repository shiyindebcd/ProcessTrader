# -*- coding: utf-8 -*-

import PySide6
from PySide6 import QtCore, QtGui
from PySide6.QtCharts import QChart
from PySide6.QtCore import QEventLoop, QStringListModel, QTimer
from PySide6.QtGui import QCursor, QStandardItem, QStandardItemModel, Qt, QPixmap
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QTableWidgetItem, QWidget, QDialog)
from PySide6.QtWidgets import QMessageBox

from Donation import Ui_Form

class Donation(QWidget, Ui_Form):                # 捐赠窗口类
    def __init__(self):
        super(Donation, self).__init__()
        self.setupUi(self)

        # 不显示标题栏
        flags = QtCore.Qt.WindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        # 不显示空白边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 设置透明度
        self.setWindowOpacity(0.95)

        self.label_5.setText('本项目github地址：  https://github.com/shiyindebcd/ProcessTrader   <a href="https://github.com/shiyindebcd/ProcessTrader">  点击跳转</a>')
        self.label_5.setOpenExternalLinks(True)  # 使其成为超链接
        self.label_5.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.label_6.setText('本项目gitee地址：  https://gitee.com/shiyindebcd/ProcessTrader   <a href="https://gitee.com/shiyindebcd/ProcessTrader">  点击跳转</a>')
        self.label_6.setOpenExternalLinks(True)  
        self.label_6.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.label_7.setText('B站软件用法详细解说地址：  https://www.bilibili.com   <a href="https://www.bilibili.com/video/BV1tY4y177sv?share_source=copy_web&vd_source=0f0ae5e8365c85cd112830a14d80cef6">  点击跳转</a>')
        self.label_7.setOpenExternalLinks(True)  
        self.label_7.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.label_8.setText('YouTube软件详细解说地址：  https://www.youtube.com   <a href="https://www.youtube.com">  点击跳转</a>')
        self.label_8.setOpenExternalLinks(True)  
        self.label_8.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.label_9.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_10.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_11.setTextInteractionFlags(Qt.TextBrowserInteraction)

    
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


