# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LineStyle_dark.ui'
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
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 260)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(170, 0, 255);	\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 5, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setStyleSheet(u"font: 700 18pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.Btn_close_window = QPushButton(self.frame_2)
        self.Btn_close_window.setObjectName(u"Btn_close_window")
        self.Btn_close_window.setMinimumSize(QSize(35, 35))
        self.Btn_close_window.setMaximumSize(QSize(35, 35))
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

        self.horizontalLayout_2.addWidget(self.Btn_close_window)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;	\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(13, -1, 13, -1)
        self.Btn_change_color = QPushButton(self.frame_5)
        self.Btn_change_color.setObjectName(u"Btn_change_color")
        self.Btn_change_color.setMinimumSize(QSize(0, 60))
        self.Btn_change_color.setMaximumSize(QSize(16777215, 60))
        self.Btn_change_color.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(0, 255, 0);\n"
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

        self.verticalLayout_2.addWidget(self.Btn_change_color)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame {\n"
"	border: none;	\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 20))
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setStyleSheet(u"font: 700 14pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 127);\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.spinBox_linewidth = QSpinBox(self.frame_7)
        self.spinBox_linewidth.setObjectName(u"spinBox_linewidth")
        self.spinBox_linewidth.setMinimumSize(QSize(110, 40))
        self.spinBox_linewidth.setMaximumSize(QSize(110, 40))
        self.spinBox_linewidth.setStyleSheet(u"QSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"	padding-left: 15px;\n"
"    padding-right: 10px;\n"
"    border: 1px solid rgb(64,64,64);\n"
"    border-radius: 15px;\n"
"	color: rgb(0,0,0);\n"
"    background-color: rgb(255,255,255);\n"
"	selection-color: rgb(255,0,0);\n"
"	selection-background-color: rgb(83,121,180);	\n"
"	font: 700 20pt \"\u7b49\u7ebf\";\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    background-color: rgb(240,240,240);\n"
"}\n"
"\n"
"QSpinBox::up-button { /* \u5411\u4e0a\u6309\u94ae */\n"
"	subcontrol-origin: border; /* \u8d77\u59cb\u4f4d\u7f6e */\n"
"	subcontrol-position: top right; /* \u5c45\u4e8e\u53f3\u4e0a\u89d2 */\n"
"	border: none;\n"
"	width: 30px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover {\n"
"	border: none;\n"
"}\n"
"\n"
"QSpinBox::up-arrow { /* \u5411\u4e0a\u7bad\u5934 */\n"
"	width: 20px;\n"
"	image: url(:/\u56fe\u6807/icons/\u4e0a.svg);\n"
"}\n"
"\n"
"QSpinBox::up-arrow:hover {\n"
"}\n"
"\n"
"QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off {\n"
"	\n"
"}\n"
""
                        "\n"
"QSpinBox::down-button { /* \u5411\u4e0b\u6309\u94ae */\n"
"	subcontrol-origin: border;\n"
"	subcontrol-position: bottom right;\n"
"	border: none;\n"
"	width: 30px;\n"
"}\n"
"\n"
"QSpinBox::down-button:hover {\n"
"	border: none;\n"
"}\n"
"\n"
"QSpinBox::down-arrow { /* \u5411\u4e0b\u7bad\u5934 */\n"
"	width: 20px;\n"
"	image: url(:/\u56fe\u6807/icons/\u4e0b.svg);\n"
"}\n"
"\n"
"QSpinBox::down-arrow:hover {\n"
"	\n"
"}\n"
"\n"
"QSpinBox::down-arrow:disabled, QSpinBox::down-arrow:off {\n"
"	\n"
"}")

        self.verticalLayout_4.addWidget(self.spinBox_linewidth, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Btn_linewidth_check = QPushButton(self.frame_8)
        self.Btn_linewidth_check.setObjectName(u"Btn_linewidth_check")
        self.Btn_linewidth_check.setMinimumSize(QSize(0, 30))
        self.Btn_linewidth_check.setMaximumSize(QSize(16777215, 30))
        self.Btn_linewidth_check.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 3px solid rgb(255, 200, 0);  \n"
"}\n"
"QPushButton:pressed{\n"
"	color: green;\n"
"	border-color: blueviolet;\n"
"    background-color: rgb(85, 0, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"	color: rgb(31, 31, 31);\n"
"    background-color: rgb(152, 152, 152);\n"
"}")

        self.verticalLayout_5.addWidget(self.Btn_linewidth_check)

        self.Btn_previous_step = QPushButton(self.frame_8)
        self.Btn_previous_step.setObjectName(u"Btn_previous_step")
        self.Btn_previous_step.setMinimumSize(QSize(0, 30))
        self.Btn_previous_step.setMaximumSize(QSize(16777215, 30))
        self.Btn_previous_step.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(0, 255, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
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

        self.verticalLayout_5.addWidget(self.Btn_previous_step)


        self.horizontalLayout_4.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Form)
        self.Btn_close_window.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u753b\u7ebf\u6837\u5f0f", None))
        self.Btn_close_window.setText("")
        self.Btn_change_color.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u989c\u8272(\u5f53\u524d\u4e3a\u9ed8\u8ba4\u8272)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u753b\u7ebf\u5bbd\u5ea6", None))
        self.Btn_linewidth_check.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.Btn_previous_step.setText(QCoreApplication.translate("Form", u"\u64a4\u6d88", None))
    # retranslateUi

