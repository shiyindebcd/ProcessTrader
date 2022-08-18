# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Donation.ui'
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
        Form.resize(600, 800)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(170, 0, 255);\n"
"	border-radius: 20px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"border:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 10, 10, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.Btn_close_window = QPushButton(self.frame_2)
        self.Btn_close_window.setObjectName(u"Btn_close_window")
        self.Btn_close_window.setMinimumSize(QSize(40, 40))
        self.Btn_close_window.setMaximumSize(QSize(40, 40))
        self.Btn_close_window.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(65, 51, 156);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(20, 9, 70);\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(31, 31, 50);\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(21, 21, 21)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/\u56fe\u6807/icons/\u5173\u95ed.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_close_window.setIcon(icon)
        self.Btn_close_window.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.Btn_close_window, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(588, 80))
        self.frame_8.setMaximumSize(QSize(588, 80))
        self.frame_8.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 9, -1, -1)
        self.label_1 = QLabel(self.frame_8)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_3.addWidget(self.label_1)

        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_3.addWidget(self.label_12)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(588, 400))
        self.frame_9.setMaximumSize(QSize(588, 400))
        self.frame_9.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_8.addWidget(self.label_4)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 300))
        self.frame_10.setMaximumSize(QSize(16777215, 300))
        self.frame_10.setStyleSheet(u"border: none;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(275, 300))
        self.frame_11.setMaximumSize(QSize(275, 300))
        self.frame_11.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 0, 0);\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 2)
        self.frame_6 = QFrame(self.frame_11)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"border: none;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(250, 250))
        self.label_15.setMaximumSize(QSize(250, 250))
        self.label_15.setPixmap(QPixmap(u"icons/453453542155.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setWordWrap(False)
        self.label_15.setMargin(0)

        self.verticalLayout_9.addWidget(self.label_15)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.frame_11)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 35))
        self.frame_3.setMaximumSize(QSize(16777215, 35))
        self.frame_3.setStyleSheet(u"border: none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"font: 700 16pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.horizontalLayout.addWidget(self.label_17, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(275, 300))
        self.frame_12.setMaximumSize(QSize(275, 300))
        self.frame_12.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 0, 0);\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_12)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 2)
        self.frame_7 = QFrame(self.frame_12)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"border:nonce;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(1, 1, 1, 0)
        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(250, 250))
        self.label_16.setPixmap(QPixmap(u"icons/1246348342.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_16)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 35))
        self.frame_13.setMaximumSize(QSize(16777215, 35))
        self.frame_13.setStyleSheet(u"border: none;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"font: 700 16pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.label_18, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_13)


        self.horizontalLayout_2.addWidget(self.frame_12)


        self.verticalLayout_8.addWidget(self.frame_10)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(588, 140))
        self.frame_4.setMaximumSize(QSize(588, 140))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, -1, -1, -1)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.label_8)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(588, 80))
        self.frame_5.setMaximumSize(QSize(588, 80))
        self.frame_5.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 5, -1, 5)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_5.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_5.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(255, 0, 255);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border: none;")

        self.verticalLayout_5.addWidget(self.label_11)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)
        self.Btn_close_window.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Btn_close_window.setText("")
        self.label_1.setText(QCoreApplication.translate("Form", u"\u672c\u5f00\u6e90\u6846\u67b6\u53ef\u968f\u610f\u4f7f\u7528\uff0c\u4e0d\u9650\u7528\u9014\uff0c\u4f7f\u7528\u672c\u8f6f\u4ef6\uff0c\u81ea\u8d1f\u76c8\u4e8f\uff0c\u4e0e\u4f5c\u8005\u6beb\u65e0\u5173\u7cfb", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4e8c\u6b21\u5f00\u53d1\u8bf7\u6ce8\u660e\u51fa\u5904", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u5f00\u6e90\u534f\u8bae\uff1aGPL-2.0", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u521b\u4f5c\u4e0d\u6613\uff0c\u5982\u679c\u672c\u8f6f\u4ef6\u8ba9\u4f60\u8d5a\u94b1\u4e86\uff0c\u6216\u89c9\u5f97\u672c\u8f6f\u4ef6\u597d\u7528\uff0c\n"
"\u6b22\u8fce\u6350\u52a9\u539f\u4f5c\u8005\uff0c\u4ee5\u9f13\u52b1\u4f5c\u8005\u7ee7\u7eed\u521b\u4f5c\uff0c\u7ee7\u7eed\u6539\u8fdb\u8f6f\u4ef6\u3002\n"
"\u5f53\u7136\uff0c\u4e0d\u6350\u52a9\u4e5f\u5b8c\u5168\u6ca1\u5173\u7cfb\uff0c\u5bf9\u8f6f\u4ef6\u4f7f\u7528\u6ca1\u6709\u4efb\u4f55\u5f71\u54cd\u3002", None))
        self.label_15.setText("")
        self.label_17.setText(QCoreApplication.translate("Form", u"\u5fae\u4fe1", None))
        self.label_16.setText("")
        self.label_18.setText(QCoreApplication.translate("Form", u"\u652f\u4ed8\u5b9d", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u9879\u76eegithub\u5730\u5740\uff1a*************************", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u9879\u76eegitee\u5730\u5740\uff1a*************************", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"B\u7ad9\u8f6f\u4ef6\u7528\u6cd5\u89c6\u9891\u89e3\u8bf4\u5730\u5740\uff1a*************************", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"youtube\u89c6\u9891\u89e3\u8bf4\u5730\u5730\u5740\uff1a*************************", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u539f\u4f5c\u8005\u8054\u7cfb\u65b9\u5f0f\uff1a shiyindebcd@gmail.com               \u5fae\u4fe1\uff1a process-trader ", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"QQ\u4ea4\u6d41\u7fa41\uff1a483083847     QQ\u4ea4\u6d41\u7fa42\uff1a148762771", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u5fae\u4fe1\u516c\u4f17\u53f7\uff1a\u641c\u7d22  \u8fdb\u7a0b\u4ea4\u6613\u8005  \u6216  ProcessTrader", None))
    # retranslateUi

