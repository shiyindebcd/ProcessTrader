# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Donation_light.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 850)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"	border-radius: 20px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"border:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 10, 20, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.Btn_close_window_2 = QPushButton(self.frame_2)
        self.Btn_close_window_2.setObjectName(u"Btn_close_window_2")
        self.Btn_close_window_2.setMinimumSize(QSize(35, 35))
        self.Btn_close_window_2.setMaximumSize(QSize(35, 35))
        self.Btn_close_window_2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(200, 200, 200);\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(121, 121, 121)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/\u56fe\u6807/icons/\u5173\u95ed (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_close_window_2.setIcon(icon)
        self.Btn_close_window_2.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.Btn_close_window_2)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 255, 240);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 9, -1, -1)
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 16pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 16pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 16pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_3.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 240, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"border: none;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.label_0 = QLabel(self.frame_6)
        self.label_0.setObjectName(u"label_0")
        self.label_0.setMinimumSize(QSize(250, 250))
        self.label_0.setMaximumSize(QSize(250, 250))
        self.label_0.setPixmap(QPixmap(u"D:/OneDrive/\u5929\u52e4\u7a0b\u5e8f\u5316\u4ea4\u6613\u6846\u67b6/logo/weixin.png"))
        self.label_0.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_0, 0, Qt.AlignHCenter)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"font: 700 16pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_6.addWidget(self.label_12, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"border: none;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.label_1 = QLabel(self.frame_7)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(250, 250))
        self.label_1.setMaximumSize(QSize(250, 250))
        self.label_1.setPixmap(QPixmap(u"D:/OneDrive/\u5929\u52e4\u7a0b\u5e8f\u5316\u4ea4\u6613\u6846\u67b6/logo/zhifubao.png"))
        self.label_1.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.label_1, 0, Qt.AlignHCenter)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"font: 700 16pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_7.addWidget(self.label_13, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 150))
        self.frame_4.setStyleSheet(u"background-color: rgb(240, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, -1, -1, -1)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 85, 0);\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.label_8)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color:rgb(227, 252, 228);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(20, -1, -1, -1)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 0, 127);\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_5.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(255, 0, 127);\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_5.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(255, 0, 127);\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_5.addWidget(self.label_11)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)
        self.Btn_close_window_2.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Btn_close_window_2.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u672c\u5f00\u6e90\u6846\u67b6\u53ef\u968f\u610f\u4f7f\u7528", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4e8c\u6b21\u5f00\u53d1\u8bf7\u6ce8\u660e\u51fa\u5904", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u521b\u4f5c\u4e0d\u6613\uff0c\u5982\u679c\u672c\u8f6f\u4ef6\u8ba9\u4f60\u8d5a\u94b1\u4e86\uff0c\u6216\u89c9\u5f97\u597d\u7528\uff0c\u6b22\u8fce\u6350\u52a9\u539f\u4f5c\u8005", None))
        self.label_0.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"\u5fae\u4fe1", None))
        self.label_1.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"\u652f\u4ed8\u5b9d", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u9879\u76eegithub\u5730\u5740\uff1ahttps://github.com/shiyindebcd/ProcessTrader", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u9879\u76eegitee\u5730\u5740\uff1ahttps://gitee.com/shiyindebcd/ProcessTrader", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"B\u7ad9\u8f6f\u4ef6\u7528\u6cd5\u8be6\u7ec6\u89e3\u8bf4\u5730\u5740", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"YouTube\u8f6f\u4ef6\u8be6\u7ec6\u89e3\u8bf4\u5730\u5740", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u539f\u4f5c\u8005\u8054\u7cfb\u65b9\u5f0f\uff1ashiyindebcd@gmail.com", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"qq\u4ea4\u6d41\u7fa4\uff1a483083847", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u5f00\u6e90\u534f\u8bae\uff1aGPL2.0", None))
    # retranslateUi

