# -*- coding: utf-8 -*-

from PySide6 import QtCore
from PySide6.QtGui import QCursor, Qt
from PySide6.QtWidgets import (QDialog)

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

