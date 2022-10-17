# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ModifyParameters_dark.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1350, 800)
        Form.setMaximumSize(QSize(1350, 800))
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(1350, 800))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid rgb(170, 0, 255);	\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.label_tital_6 = QLabel(self.frame_2)
        self.label_tital_6.setObjectName(u"label_tital_6")
        self.label_tital_6.setMinimumSize(QSize(0, 40))
        self.label_tital_6.setMaximumSize(QSize(16777215, 40))
        self.label_tital_6.setStyleSheet(u"font: 700 20pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_tital_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 16pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 127);")

        self.horizontalLayout_2.addWidget(self.label)

        self.label_info = QLabel(self.frame_2)
        self.label_info.setObjectName(u"label_info")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy)
        self.label_info.setMinimumSize(QSize(200, 0))
        self.label_info.setStyleSheet(u"font: 700 16pt \"\u7b49\u7ebf\";\n"
"color: rgb(0, 255, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_info)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.Btn_min_window = QPushButton(self.frame_2)
        self.Btn_min_window.setObjectName(u"Btn_min_window")
        self.Btn_min_window.setMinimumSize(QSize(35, 35))
        self.Btn_min_window.setMaximumSize(QSize(35, 35))
        self.Btn_min_window.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/icon/icons/\u6700\u5c0f\u5316.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_min_window.setIcon(icon)
        self.Btn_min_window.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.Btn_min_window)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

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
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/\u5173\u95ed.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_close_window.setIcon(icon1)
        self.Btn_close_window.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.Btn_close_window)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_56 = QFrame(self.frame)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(430, 0))
        self.frame_56.setMaximumSize(QSize(430, 16777215))
        self.frame_56.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_56)
        self.verticalLayout_38.setSpacing(1)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(1, 1, 1, 1)
        self.frame_57 = QFrame(self.frame_56)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(0, 50))
        self.frame_57.setMaximumSize(QSize(16777215, 50))
        self.frame_57.setStyleSheet(u"border:none")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_57)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_tital_4 = QLabel(self.frame_57)
        self.label_tital_4.setObjectName(u"label_tital_4")
        self.label_tital_4.setMaximumSize(QSize(16777215, 50))
        self.label_tital_4.setStyleSheet(u"font: 700 16pt \"\u7b49\u7ebf\";\n"
"color: rgb(0, 255, 0);\n"
"border: none;")

        self.verticalLayout_39.addWidget(self.label_tital_4)


        self.verticalLayout_38.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_56)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMaximumSize(QSize(450, 16777215))
        self.frame_58.setStyleSheet(u"QFrame {\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_26.setSpacing(15)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(15, 0, 10, 0)
        self.upper_left_3 = QFrame(self.frame_58)
        self.upper_left_3.setObjectName(u"upper_left_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.upper_left_3.sizePolicy().hasHeightForWidth())
        self.upper_left_3.setSizePolicy(sizePolicy1)
        self.upper_left_3.setMinimumSize(QSize(185, 0))
        self.upper_left_3.setMaximumSize(QSize(185, 1000))
        self.upper_left_3.setStyleSheet(u"border:none")
        self.upper_left_3.setFrameShape(QFrame.StyledPanel)
        self.upper_left_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.upper_left_3)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_whether_self_start = QLabel(self.upper_left_3)
        self.label_whether_self_start.setObjectName(u"label_whether_self_start")
        self.label_whether_self_start.setMinimumSize(QSize(180, 40))
        self.label_whether_self_start.setMaximumSize(QSize(180, 40))
        self.label_whether_self_start.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_whether_self_start.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_whether_self_start)

        self.label_whether_live_futures_trading = QLabel(self.upper_left_3)
        self.label_whether_live_futures_trading.setObjectName(u"label_whether_live_futures_trading")
        self.label_whether_live_futures_trading.setEnabled(True)
        self.label_whether_live_futures_trading.setMinimumSize(QSize(180, 40))
        self.label_whether_live_futures_trading.setMaximumSize(QSize(180, 40))
        self.label_whether_live_futures_trading.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_whether_live_futures_trading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_whether_live_futures_trading)

        self.label_trading_status = QLabel(self.upper_left_3)
        self.label_trading_status.setObjectName(u"label_trading_status")
        self.label_trading_status.setMinimumSize(QSize(180, 40))
        self.label_trading_status.setMaximumSize(QSize(180, 40))
        self.label_trading_status.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_trading_status.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_trading_status)

        self.label_whether_open_web_services = QLabel(self.upper_left_3)
        self.label_whether_open_web_services.setObjectName(u"label_whether_open_web_services")
        self.label_whether_open_web_services.setMinimumSize(QSize(180, 40))
        self.label_whether_open_web_services.setMaximumSize(QSize(180, 40))
        self.label_whether_open_web_services.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_whether_open_web_services.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_whether_open_web_services)

        self.label_web_port = QLabel(self.upper_left_3)
        self.label_web_port.setObjectName(u"label_web_port")
        self.label_web_port.setMinimumSize(QSize(180, 40))
        self.label_web_port.setMaximumSize(QSize(180, 40))
        self.label_web_port.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_web_port.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_web_port)

        self.label_symbol_period = QLabel(self.upper_left_3)
        self.label_symbol_period.setObjectName(u"label_symbol_period")
        self.label_symbol_period.setMinimumSize(QSize(180, 40))
        self.label_symbol_period.setMaximumSize(QSize(180, 40))
        self.label_symbol_period.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_symbol_period.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_symbol_period)

        self.label_initial_capital = QLabel(self.upper_left_3)
        self.label_initial_capital.setObjectName(u"label_initial_capital")
        self.label_initial_capital.setMinimumSize(QSize(180, 40))
        self.label_initial_capital.setMaximumSize(QSize(180, 40))
        self.label_initial_capital.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_initial_capital.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_initial_capital)

        self.label_orientation = QLabel(self.upper_left_3)
        self.label_orientation.setObjectName(u"label_orientation")
        self.label_orientation.setMinimumSize(QSize(180, 40))
        self.label_orientation.setMaximumSize(QSize(180, 40))
        self.label_orientation.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_orientation.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_orientation)

        self.label_contract_multiples = QLabel(self.upper_left_3)
        self.label_contract_multiples.setObjectName(u"label_contract_multiples")
        self.label_contract_multiples.setMinimumSize(QSize(180, 40))
        self.label_contract_multiples.setMaximumSize(QSize(180, 40))
        self.label_contract_multiples.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_contract_multiples.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_contract_multiples)


        self.horizontalLayout_26.addWidget(self.upper_left_3, 0, Qt.AlignHCenter)

        self.upper_right_3 = QFrame(self.frame_58)
        self.upper_right_3.setObjectName(u"upper_right_3")
        sizePolicy1.setHeightForWidth(self.upper_right_3.sizePolicy().hasHeightForWidth())
        self.upper_right_3.setSizePolicy(sizePolicy1)
        self.upper_right_3.setMinimumSize(QSize(205, 0))
        self.upper_right_3.setMaximumSize(QSize(205, 1000))
        self.upper_right_3.setStyleSheet(u"border:none")
        self.upper_right_3.setFrameShape(QFrame.StyledPanel)
        self.upper_right_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.upper_right_3)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.checkBox_whether_self_start = QCheckBox(self.upper_right_3)
        self.checkBox_whether_self_start.setObjectName(u"checkBox_whether_self_start")
        self.checkBox_whether_self_start.setEnabled(True)
        self.checkBox_whether_self_start.setMinimumSize(QSize(200, 40))
        self.checkBox_whether_self_start.setMaximumSize(QSize(200, 40))
        self.checkBox_whether_self_start.setStyleSheet(u"QCheckBox{	\n"
"	color: rgb(255, 0, 127);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	padding:3px 3px 3px 7px;\n"
"}\n"
"QCheckBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 45px;\n"
"    height: 25px;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(0, 200, 0);\n"
"    border: 3px solid rgb(255, 0, 0);\n"
"	image: url(:/icon/icons/\u52fe\u9009.svg);\n"
" }\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:rgb(136, 136, 136);\n"
"    border:2px solid rgb(80, 80, 80);\n"
"}\n"
"QCheckBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.checkBox_whether_self_start.setChecked(True)

        self.verticalLayout_33.addWidget(self.checkBox_whether_self_start)

        self.checkBox_whether_live_futures_trading = QCheckBox(self.upper_right_3)
        self.checkBox_whether_live_futures_trading.setObjectName(u"checkBox_whether_live_futures_trading")
        self.checkBox_whether_live_futures_trading.setMinimumSize(QSize(200, 40))
        self.checkBox_whether_live_futures_trading.setMaximumSize(QSize(200, 40))
        self.checkBox_whether_live_futures_trading.setStyleSheet(u"QCheckBox{	\n"
"	color: rgb(255, 0, 127);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	padding:3px 3px 3px 7px;\n"
"}\n"
"QCheckBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 45px;\n"
"    height: 25px;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(0, 200, 0);\n"
"    border: 3px solid rgb(255, 0, 0);\n"
"	image: url(:/icon/icons/\u52fe\u9009.svg);\n"
" }\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:rgb(136, 136, 136);\n"
"    border:2px solid rgb(80, 80, 80);\n"
"}\n"
"QCheckBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_33.addWidget(self.checkBox_whether_live_futures_trading)

        self.checkBox_trading_status = QCheckBox(self.upper_right_3)
        self.checkBox_trading_status.setObjectName(u"checkBox_trading_status")
        self.checkBox_trading_status.setMinimumSize(QSize(200, 40))
        self.checkBox_trading_status.setMaximumSize(QSize(200, 40))
        self.checkBox_trading_status.setStyleSheet(u"QCheckBox{	\n"
"	color: rgb(255, 0, 127);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	padding:3px 3px 3px 7px;\n"
"}\n"
"QCheckBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 45px;\n"
"    height: 25px;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(0, 200, 0);\n"
"    border: 3px solid rgb(255, 0, 0);\n"
"	image: url(:/icon/icons/\u52fe\u9009.svg);\n"
" }\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:rgb(136, 136, 136);\n"
"    border:2px solid rgb(80, 80, 80);\n"
"}\n"
"QCheckBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_33.addWidget(self.checkBox_trading_status)

        self.checkBox_whether_open_web_services = QCheckBox(self.upper_right_3)
        self.checkBox_whether_open_web_services.setObjectName(u"checkBox_whether_open_web_services")
        self.checkBox_whether_open_web_services.setMinimumSize(QSize(200, 40))
        self.checkBox_whether_open_web_services.setMaximumSize(QSize(200, 40))
        self.checkBox_whether_open_web_services.setStyleSheet(u"QCheckBox{	\n"
"	color: rgb(255, 0, 127);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	padding:3px 3px 3px 7px;\n"
"}\n"
"QCheckBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 45px;\n"
"    height: 25px;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(0, 200, 0);\n"
"    border: 3px solid rgb(255, 0, 0);\n"
"	image: url(:/icon/icons/\u52fe\u9009.svg);\n"
" }\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:rgb(136, 136, 136);\n"
"    border:2px solid rgb(80, 80, 80);\n"
"}\n"
"QCheckBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_33.addWidget(self.checkBox_whether_open_web_services)

        self.web_port = QLineEdit(self.upper_right_3)
        self.web_port.setObjectName(u"web_port")
        self.web_port.setEnabled(False)
        self.web_port.setMinimumSize(QSize(0, 40))
        self.web_port.setMaximumSize(QSize(200, 40))
        self.web_port.setMouseTracking(True)
        self.web_port.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.web_port.setDragEnabled(False)

        self.verticalLayout_33.addWidget(self.web_port)

        self.symbol_period = QLineEdit(self.upper_right_3)
        self.symbol_period.setObjectName(u"symbol_period")
        self.symbol_period.setMinimumSize(QSize(200, 40))
        self.symbol_period.setMaximumSize(QSize(200, 40))
        self.symbol_period.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_33.addWidget(self.symbol_period)

        self.initial_capital = QLineEdit(self.upper_right_3)
        self.initial_capital.setObjectName(u"initial_capital")
        self.initial_capital.setMinimumSize(QSize(200, 40))
        self.initial_capital.setMaximumSize(QSize(200, 40))
        self.initial_capital.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_33.addWidget(self.initial_capital)

        self.orientation = QLineEdit(self.upper_right_3)
        self.orientation.setObjectName(u"orientation")
        self.orientation.setMinimumSize(QSize(200, 40))
        self.orientation.setMaximumSize(QSize(200, 40))
        self.orientation.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_33.addWidget(self.orientation)

        self.contract_multiples = QLineEdit(self.upper_right_3)
        self.contract_multiples.setObjectName(u"contract_multiples")
        self.contract_multiples.setMinimumSize(QSize(200, 40))
        self.contract_multiples.setMaximumSize(QSize(200, 40))
        self.contract_multiples.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_33.addWidget(self.contract_multiples)


        self.horizontalLayout_26.addWidget(self.upper_right_3, 0, Qt.AlignHCenter)


        self.verticalLayout_38.addWidget(self.frame_58)

        self.frame_24 = QFrame(self.frame_56)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 70))
        self.frame_24.setMaximumSize(QSize(16777215, 100))
        self.frame_24.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}\n"
"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.verticalLayout_38.addWidget(self.frame_24)


        self.horizontalLayout.addWidget(self.frame_56)

        self.frame_36 = QFrame(self.frame)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy)
        self.frame_36.setMinimumSize(QSize(430, 0))
        self.frame_36.setMaximumSize(QSize(430, 16777215))
        self.frame_36.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_36)
        self.verticalLayout_20.setSpacing(1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(1, 1, 1, 1)
        self.frame_16 = QFrame(self.frame_36)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 50))
        self.frame_16.setStyleSheet(u"border: none;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_20.addWidget(self.frame_16)

        self.frame_23 = QFrame(self.frame_36)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"QFrame {\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(15, 0, 10, 0)
        self.upper_left_5 = QFrame(self.frame_23)
        self.upper_left_5.setObjectName(u"upper_left_5")
        sizePolicy1.setHeightForWidth(self.upper_left_5.sizePolicy().hasHeightForWidth())
        self.upper_left_5.setSizePolicy(sizePolicy1)
        self.upper_left_5.setMinimumSize(QSize(185, 0))
        self.upper_left_5.setMaximumSize(QSize(185, 1000))
        self.upper_left_5.setStyleSheet(u"border:none")
        self.upper_left_5.setFrameShape(QFrame.StyledPanel)
        self.upper_left_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.upper_left_5)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_margin_rate = QLabel(self.upper_left_5)
        self.label_margin_rate.setObjectName(u"label_margin_rate")
        self.label_margin_rate.setMinimumSize(QSize(180, 40))
        self.label_margin_rate.setMaximumSize(QSize(180, 40))
        self.label_margin_rate.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_margin_rate.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_margin_rate)

        self.label_stop_loss = QLabel(self.upper_left_5)
        self.label_stop_loss.setObjectName(u"label_stop_loss")
        self.label_stop_loss.setMinimumSize(QSize(180, 40))
        self.label_stop_loss.setMaximumSize(QSize(180, 40))
        self.label_stop_loss.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_stop_loss.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_stop_loss)

        self.label_stop_profit = QLabel(self.upper_left_5)
        self.label_stop_profit.setObjectName(u"label_stop_profit")
        self.label_stop_profit.setMinimumSize(QSize(180, 40))
        self.label_stop_profit.setMaximumSize(QSize(180, 40))
        self.label_stop_profit.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_stop_profit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_stop_profit)

        self.lable_whether_open_line = QLabel(self.upper_left_5)
        self.lable_whether_open_line.setObjectName(u"lable_whether_open_line")
        self.lable_whether_open_line.setMinimumSize(QSize(180, 40))
        self.lable_whether_open_line.setMaximumSize(QSize(180, 40))
        self.lable_whether_open_line.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.lable_whether_open_line.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.lable_whether_open_line)

        self.label_open_line_Coordinates = QLabel(self.upper_left_5)
        self.label_open_line_Coordinates.setObjectName(u"label_open_line_Coordinates")
        self.label_open_line_Coordinates.setMinimumSize(QSize(180, 40))
        self.label_open_line_Coordinates.setMaximumSize(QSize(180, 40))
        self.label_open_line_Coordinates.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_open_line_Coordinates.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_open_line_Coordinates)

        self.label_whether_close_line = QLabel(self.upper_left_5)
        self.label_whether_close_line.setObjectName(u"label_whether_close_line")
        self.label_whether_close_line.setMinimumSize(QSize(180, 40))
        self.label_whether_close_line.setMaximumSize(QSize(180, 40))
        self.label_whether_close_line.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_whether_close_line.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_whether_close_line)

        self.label_close_line_Coordinates = QLabel(self.upper_left_5)
        self.label_close_line_Coordinates.setObjectName(u"label_close_line_Coordinates")
        self.label_close_line_Coordinates.setMinimumSize(QSize(180, 40))
        self.label_close_line_Coordinates.setMaximumSize(QSize(180, 40))
        self.label_close_line_Coordinates.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_close_line_Coordinates.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_close_line_Coordinates)

        self.label_long_add_times = QLabel(self.upper_left_5)
        self.label_long_add_times.setObjectName(u"label_long_add_times")
        self.label_long_add_times.setMinimumSize(QSize(180, 40))
        self.label_long_add_times.setMaximumSize(QSize(180, 40))
        self.label_long_add_times.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_long_add_times.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_long_add_times)

        self.label_short_add_times = QLabel(self.upper_left_5)
        self.label_short_add_times.setObjectName(u"label_short_add_times")
        self.label_short_add_times.setMinimumSize(QSize(180, 40))
        self.label_short_add_times.setMaximumSize(QSize(180, 40))
        self.label_short_add_times.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_short_add_times.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_short_add_times)


        self.horizontalLayout_5.addWidget(self.upper_left_5)

        self.upper_right_5 = QFrame(self.frame_23)
        self.upper_right_5.setObjectName(u"upper_right_5")
        sizePolicy1.setHeightForWidth(self.upper_right_5.sizePolicy().hasHeightForWidth())
        self.upper_right_5.setSizePolicy(sizePolicy1)
        self.upper_right_5.setMinimumSize(QSize(205, 0))
        self.upper_right_5.setMaximumSize(QSize(205, 1000))
        self.upper_right_5.setStyleSheet(u"border:none")
        self.upper_right_5.setFrameShape(QFrame.StyledPanel)
        self.upper_right_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.upper_right_5)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.margin_rate = QLineEdit(self.upper_right_5)
        self.margin_rate.setObjectName(u"margin_rate")
        self.margin_rate.setMinimumSize(QSize(200, 40))
        self.margin_rate.setMaximumSize(QSize(200, 40))
        self.margin_rate.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_41.addWidget(self.margin_rate)

        self.stop_loss = QLineEdit(self.upper_right_5)
        self.stop_loss.setObjectName(u"stop_loss")
        self.stop_loss.setMinimumSize(QSize(200, 40))
        self.stop_loss.setMaximumSize(QSize(200, 40))
        self.stop_loss.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_41.addWidget(self.stop_loss)

        self.stop_profit = QLineEdit(self.upper_right_5)
        self.stop_profit.setObjectName(u"stop_profit")
        self.stop_profit.setMinimumSize(QSize(200, 40))
        self.stop_profit.setMaximumSize(QSize(200, 40))
        self.stop_profit.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_41.addWidget(self.stop_profit)

        self.checkBox_whether_open_line = QCheckBox(self.upper_right_5)
        self.checkBox_whether_open_line.setObjectName(u"checkBox_whether_open_line")
        self.checkBox_whether_open_line.setMinimumSize(QSize(200, 40))
        self.checkBox_whether_open_line.setMaximumSize(QSize(200, 40))
        self.checkBox_whether_open_line.setStyleSheet(u"QCheckBox{	\n"
"	color: rgb(255, 0, 127);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	padding:3px 3px 3px 7px;\n"
"}\n"
"QCheckBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 45px;\n"
"    height: 25px;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(0, 200, 0);\n"
"    border: 3px solid rgb(255, 0, 0);\n"
"	image: url(:/icon/icons/\u52fe\u9009.svg);\n"
" }\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:rgb(136, 136, 136);\n"
"    border:2px solid rgb(80, 80, 80);\n"
"}\n"
"QCheckBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.checkBox_whether_open_line.setChecked(False)

        self.verticalLayout_41.addWidget(self.checkBox_whether_open_line)

        self.open_line_Coordinates = QLineEdit(self.upper_right_5)
        self.open_line_Coordinates.setObjectName(u"open_line_Coordinates")
        self.open_line_Coordinates.setEnabled(False)
        self.open_line_Coordinates.setMinimumSize(QSize(200, 40))
        self.open_line_Coordinates.setMaximumSize(QSize(200, 40))
        self.open_line_Coordinates.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_41.addWidget(self.open_line_Coordinates)

        self.checkBox_whether_close_line = QCheckBox(self.upper_right_5)
        self.checkBox_whether_close_line.setObjectName(u"checkBox_whether_close_line")
        self.checkBox_whether_close_line.setMinimumSize(QSize(200, 40))
        self.checkBox_whether_close_line.setMaximumSize(QSize(200, 40))
        self.checkBox_whether_close_line.setStyleSheet(u"QCheckBox{	\n"
"	color: rgb(255, 0, 127);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	padding:3px 3px 3px 7px;\n"
"}\n"
"QCheckBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 45px;\n"
"    height: 25px;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(0, 200, 0);\n"
"    border: 3px solid rgb(255, 0, 0);\n"
"	image: url(:/icon/icons/\u52fe\u9009.svg);\n"
" }\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:rgb(136, 136, 136);\n"
"    border:2px solid rgb(80, 80, 80);\n"
"}\n"
"QCheckBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_41.addWidget(self.checkBox_whether_close_line)

        self.close_line_Coordinates = QLineEdit(self.upper_right_5)
        self.close_line_Coordinates.setObjectName(u"close_line_Coordinates")
        self.close_line_Coordinates.setEnabled(False)
        self.close_line_Coordinates.setMinimumSize(QSize(200, 40))
        self.close_line_Coordinates.setMaximumSize(QSize(200, 40))
        self.close_line_Coordinates.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_41.addWidget(self.close_line_Coordinates)

        self.long_add_times = QLineEdit(self.upper_right_5)
        self.long_add_times.setObjectName(u"long_add_times")
        self.long_add_times.setMinimumSize(QSize(200, 40))
        self.long_add_times.setMaximumSize(QSize(200, 40))
        self.long_add_times.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_41.addWidget(self.long_add_times)

        self.short_add_times = QLineEdit(self.upper_right_5)
        self.short_add_times.setObjectName(u"short_add_times")
        self.short_add_times.setMinimumSize(QSize(200, 40))
        self.short_add_times.setMaximumSize(QSize(200, 40))
        self.short_add_times.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_41.addWidget(self.short_add_times)


        self.horizontalLayout_5.addWidget(self.upper_right_5)


        self.verticalLayout_20.addWidget(self.frame_23)

        self.frame_59 = QFrame(self.frame_36)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(0, 70))
        self.frame_59.setMaximumSize(QSize(16777215, 100))
        self.frame_59.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}\n"
"")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 20, 0, 10)

        self.verticalLayout_20.addWidget(self.frame_59)


        self.horizontalLayout.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy)
        self.frame_37.setMinimumSize(QSize(430, 0))
        self.frame_37.setMaximumSize(QSize(430, 16777215))
        self.frame_37.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_37)
        self.verticalLayout_21.setSpacing(1)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(1, 1, 1, 1)
        self.frame_17 = QFrame(self.frame_37)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 50))
        self.frame_17.setStyleSheet(u"font: 700 20pt \"\u7b49\u7ebf\";\n"
"color: rgb(0, 255, 0);\n"
"border: none;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout_21.addWidget(self.frame_17)

        self.frame_25 = QFrame(self.frame_37)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"QFrame {\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(15, 0, 10, 0)
        self.upper_left_6 = QFrame(self.frame_25)
        self.upper_left_6.setObjectName(u"upper_left_6")
        sizePolicy1.setHeightForWidth(self.upper_left_6.sizePolicy().hasHeightForWidth())
        self.upper_left_6.setSizePolicy(sizePolicy1)
        self.upper_left_6.setMinimumSize(QSize(185, 0))
        self.upper_left_6.setMaximumSize(QSize(185, 1000))
        self.upper_left_6.setStyleSheet(u"border:none")
        self.upper_left_6.setFrameShape(QFrame.StyledPanel)
        self.upper_left_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.upper_left_6)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_Customized_parameters1 = QLabel(self.upper_left_6)
        self.label_Customized_parameters1.setObjectName(u"label_Customized_parameters1")
        self.label_Customized_parameters1.setMinimumSize(QSize(180, 40))
        self.label_Customized_parameters1.setMaximumSize(QSize(180, 40))
        self.label_Customized_parameters1.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_Customized_parameters1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_Customized_parameters1)

        self.label_Customized_parameters2 = QLabel(self.upper_left_6)
        self.label_Customized_parameters2.setObjectName(u"label_Customized_parameters2")
        self.label_Customized_parameters2.setMinimumSize(QSize(180, 40))
        self.label_Customized_parameters2.setMaximumSize(QSize(180, 40))
        self.label_Customized_parameters2.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_Customized_parameters2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_Customized_parameters2)

        self.label_Customized_parameters3 = QLabel(self.upper_left_6)
        self.label_Customized_parameters3.setObjectName(u"label_Customized_parameters3")
        self.label_Customized_parameters3.setMinimumSize(QSize(180, 40))
        self.label_Customized_parameters3.setMaximumSize(QSize(180, 40))
        self.label_Customized_parameters3.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_Customized_parameters3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_Customized_parameters3)

        self.label_Customized_parameters4 = QLabel(self.upper_left_6)
        self.label_Customized_parameters4.setObjectName(u"label_Customized_parameters4")
        self.label_Customized_parameters4.setMinimumSize(QSize(180, 40))
        self.label_Customized_parameters4.setMaximumSize(QSize(180, 40))
        self.label_Customized_parameters4.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_Customized_parameters4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_Customized_parameters4)

        self.label_Customized_parameters5 = QLabel(self.upper_left_6)
        self.label_Customized_parameters5.setObjectName(u"label_Customized_parameters5")
        self.label_Customized_parameters5.setMinimumSize(QSize(180, 40))
        self.label_Customized_parameters5.setMaximumSize(QSize(180, 40))
        self.label_Customized_parameters5.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_Customized_parameters5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_Customized_parameters5)

        self.label_Customized_parameters6 = QLabel(self.upper_left_6)
        self.label_Customized_parameters6.setObjectName(u"label_Customized_parameters6")
        self.label_Customized_parameters6.setMinimumSize(QSize(180, 40))
        self.label_Customized_parameters6.setMaximumSize(QSize(180, 40))
        self.label_Customized_parameters6.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_Customized_parameters6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_Customized_parameters6)

        self.label_Customized_parameters7 = QLabel(self.upper_left_6)
        self.label_Customized_parameters7.setObjectName(u"label_Customized_parameters7")
        self.label_Customized_parameters7.setMinimumSize(QSize(180, 40))
        self.label_Customized_parameters7.setMaximumSize(QSize(180, 40))
        self.label_Customized_parameters7.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_Customized_parameters7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_Customized_parameters7)

        self.label_Customized_parameters8 = QLabel(self.upper_left_6)
        self.label_Customized_parameters8.setObjectName(u"label_Customized_parameters8")
        self.label_Customized_parameters8.setMinimumSize(QSize(180, 40))
        self.label_Customized_parameters8.setMaximumSize(QSize(180, 40))
        self.label_Customized_parameters8.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_Customized_parameters8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_Customized_parameters8)

        self.label_Customized_parameters9 = QLabel(self.upper_left_6)
        self.label_Customized_parameters9.setObjectName(u"label_Customized_parameters9")
        self.label_Customized_parameters9.setMinimumSize(QSize(180, 40))
        self.label_Customized_parameters9.setMaximumSize(QSize(180, 40))
        self.label_Customized_parameters9.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_Customized_parameters9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_Customized_parameters9)


        self.horizontalLayout_6.addWidget(self.upper_left_6)

        self.upper_right_6 = QFrame(self.frame_25)
        self.upper_right_6.setObjectName(u"upper_right_6")
        sizePolicy1.setHeightForWidth(self.upper_right_6.sizePolicy().hasHeightForWidth())
        self.upper_right_6.setSizePolicy(sizePolicy1)
        self.upper_right_6.setMinimumSize(QSize(205, 0))
        self.upper_right_6.setMaximumSize(QSize(205, 1000))
        self.upper_right_6.setStyleSheet(u"border:none")
        self.upper_right_6.setFrameShape(QFrame.StyledPanel)
        self.upper_right_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.upper_right_6)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.Customized_parameters1 = QLineEdit(self.upper_right_6)
        self.Customized_parameters1.setObjectName(u"Customized_parameters1")
        self.Customized_parameters1.setMinimumSize(QSize(200, 40))
        self.Customized_parameters1.setMaximumSize(QSize(200, 40))
        self.Customized_parameters1.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_42.addWidget(self.Customized_parameters1)

        self.Customized_parameters2 = QLineEdit(self.upper_right_6)
        self.Customized_parameters2.setObjectName(u"Customized_parameters2")
        self.Customized_parameters2.setMinimumSize(QSize(200, 40))
        self.Customized_parameters2.setMaximumSize(QSize(200, 40))
        self.Customized_parameters2.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_42.addWidget(self.Customized_parameters2)

        self.Customized_parameters3 = QLineEdit(self.upper_right_6)
        self.Customized_parameters3.setObjectName(u"Customized_parameters3")
        self.Customized_parameters3.setMinimumSize(QSize(200, 40))
        self.Customized_parameters3.setMaximumSize(QSize(200, 40))
        self.Customized_parameters3.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_42.addWidget(self.Customized_parameters3)

        self.Customized_parameters4 = QLineEdit(self.upper_right_6)
        self.Customized_parameters4.setObjectName(u"Customized_parameters4")
        self.Customized_parameters4.setMinimumSize(QSize(200, 40))
        self.Customized_parameters4.setMaximumSize(QSize(200, 40))
        self.Customized_parameters4.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_42.addWidget(self.Customized_parameters4)

        self.Customized_parameters5 = QLineEdit(self.upper_right_6)
        self.Customized_parameters5.setObjectName(u"Customized_parameters5")
        self.Customized_parameters5.setMinimumSize(QSize(200, 40))
        self.Customized_parameters5.setMaximumSize(QSize(200, 40))
        self.Customized_parameters5.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_42.addWidget(self.Customized_parameters5)

        self.Customized_parameters6 = QLineEdit(self.upper_right_6)
        self.Customized_parameters6.setObjectName(u"Customized_parameters6")
        self.Customized_parameters6.setMinimumSize(QSize(200, 40))
        self.Customized_parameters6.setMaximumSize(QSize(200, 40))
        self.Customized_parameters6.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_42.addWidget(self.Customized_parameters6)

        self.Customized_parameters7 = QLineEdit(self.upper_right_6)
        self.Customized_parameters7.setObjectName(u"Customized_parameters7")
        self.Customized_parameters7.setMinimumSize(QSize(200, 40))
        self.Customized_parameters7.setMaximumSize(QSize(200, 40))
        self.Customized_parameters7.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_42.addWidget(self.Customized_parameters7)

        self.Customized_parameters8 = QLineEdit(self.upper_right_6)
        self.Customized_parameters8.setObjectName(u"Customized_parameters8")
        self.Customized_parameters8.setMinimumSize(QSize(200, 40))
        self.Customized_parameters8.setMaximumSize(QSize(200, 40))
        self.Customized_parameters8.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_42.addWidget(self.Customized_parameters8)

        self.Customized_parameters9 = QLineEdit(self.upper_right_6)
        self.Customized_parameters9.setObjectName(u"Customized_parameters9")
        self.Customized_parameters9.setMinimumSize(QSize(200, 40))
        self.Customized_parameters9.setMaximumSize(QSize(200, 40))
        self.Customized_parameters9.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"	color: rgb(255, 0, 0);\n"
"}\n"
"QLineEdit:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_42.addWidget(self.Customized_parameters9)


        self.horizontalLayout_6.addWidget(self.upper_right_6)


        self.verticalLayout_21.addWidget(self.frame_25)

        self.frame_60 = QFrame(self.frame_37)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 60))
        self.frame_60.setMaximumSize(QSize(16777215, 100))
        self.frame_60.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"}\n"
"")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 20, 0, 10)
        self.frame_40 = QFrame(self.frame_60)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Btn_submit_changes = QPushButton(self.frame_40)
        self.Btn_submit_changes.setObjectName(u"Btn_submit_changes")
        self.Btn_submit_changes.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Btn_submit_changes.sizePolicy().hasHeightForWidth())
        self.Btn_submit_changes.setSizePolicy(sizePolicy2)
        self.Btn_submit_changes.setMinimumSize(QSize(180, 40))
        self.Btn_submit_changes.setMaximumSize(QSize(180, 40))
        self.Btn_submit_changes.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	border-radius: 18px;\n"
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
        self.Btn_submit_changes.setIconSize(QSize(20, 20))
        self.Btn_submit_changes.setCheckable(True)
        self.Btn_submit_changes.setChecked(False)

        self.horizontalLayout_21.addWidget(self.Btn_submit_changes, 0, Qt.AlignVCenter)


        self.horizontalLayout_32.addWidget(self.frame_40)

        self.frame_46 = QFrame(self.frame_60)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.Btn_cancel_and_exit = QPushButton(self.frame_46)
        self.Btn_cancel_and_exit.setObjectName(u"Btn_cancel_and_exit")
        self.Btn_cancel_and_exit.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Btn_cancel_and_exit.sizePolicy().hasHeightForWidth())
        self.Btn_cancel_and_exit.setSizePolicy(sizePolicy3)
        self.Btn_cancel_and_exit.setMinimumSize(QSize(180, 40))
        self.Btn_cancel_and_exit.setMaximumSize(QSize(180, 40))
        self.Btn_cancel_and_exit.setStyleSheet(u"QPushButton{	\n"
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
        self.Btn_cancel_and_exit.setIconSize(QSize(19, 20))

        self.horizontalLayout_33.addWidget(self.Btn_cancel_and_exit, 0, Qt.AlignVCenter)


        self.horizontalLayout_32.addWidget(self.frame_46)


        self.verticalLayout_21.addWidget(self.frame_60)


        self.horizontalLayout.addWidget(self.frame_37)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_3.addWidget(self.frame_3)

#if QT_CONFIG(shortcut)
        self.label_whether_self_start.setBuddy(self.checkBox_whether_self_start)
        self.label_whether_live_futures_trading.setBuddy(self.checkBox_whether_live_futures_trading)
        self.label_whether_open_web_services.setBuddy(self.checkBox_whether_open_web_services)
        self.label_web_port.setBuddy(self.web_port)
        self.label_symbol_period.setBuddy(self.symbol_period)
        self.label_initial_capital.setBuddy(self.initial_capital)
        self.label_orientation.setBuddy(self.orientation)
        self.label_contract_multiples.setBuddy(self.contract_multiples)
        self.label_margin_rate.setBuddy(self.margin_rate)
        self.label_stop_loss.setBuddy(self.stop_loss)
        self.label_stop_profit.setBuddy(self.stop_profit)
        self.label_open_line_Coordinates.setBuddy(self.open_line_Coordinates)
        self.label_close_line_Coordinates.setBuddy(self.close_line_Coordinates)
        self.label_Customized_parameters1.setBuddy(self.Customized_parameters1)
        self.label_Customized_parameters2.setBuddy(self.Customized_parameters2)
        self.label_Customized_parameters3.setBuddy(self.Customized_parameters3)
        self.label_Customized_parameters4.setBuddy(self.Customized_parameters4)
        self.label_Customized_parameters5.setBuddy(self.Customized_parameters5)
        self.label_Customized_parameters6.setBuddy(self.Customized_parameters6)
        self.label_Customized_parameters7.setBuddy(self.Customized_parameters7)
        self.label_Customized_parameters8.setBuddy(self.Customized_parameters8)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.checkBox_whether_self_start, self.checkBox_whether_live_futures_trading)
        QWidget.setTabOrder(self.checkBox_whether_live_futures_trading, self.checkBox_trading_status)
        QWidget.setTabOrder(self.checkBox_trading_status, self.checkBox_whether_open_web_services)
        QWidget.setTabOrder(self.checkBox_whether_open_web_services, self.web_port)
        QWidget.setTabOrder(self.web_port, self.symbol_period)
        QWidget.setTabOrder(self.symbol_period, self.initial_capital)
        QWidget.setTabOrder(self.initial_capital, self.orientation)
        QWidget.setTabOrder(self.orientation, self.margin_rate)
        QWidget.setTabOrder(self.margin_rate, self.stop_loss)
        QWidget.setTabOrder(self.stop_loss, self.stop_profit)
        QWidget.setTabOrder(self.stop_profit, self.checkBox_whether_open_line)
        QWidget.setTabOrder(self.checkBox_whether_open_line, self.open_line_Coordinates)
        QWidget.setTabOrder(self.open_line_Coordinates, self.checkBox_whether_close_line)
        QWidget.setTabOrder(self.checkBox_whether_close_line, self.close_line_Coordinates)
        QWidget.setTabOrder(self.close_line_Coordinates, self.Customized_parameters1)
        QWidget.setTabOrder(self.Customized_parameters1, self.Customized_parameters2)
        QWidget.setTabOrder(self.Customized_parameters2, self.Customized_parameters3)
        QWidget.setTabOrder(self.Customized_parameters3, self.Customized_parameters4)
        QWidget.setTabOrder(self.Customized_parameters4, self.Customized_parameters5)
        QWidget.setTabOrder(self.Customized_parameters5, self.Customized_parameters6)
        QWidget.setTabOrder(self.Customized_parameters6, self.Customized_parameters7)
        QWidget.setTabOrder(self.Customized_parameters7, self.Customized_parameters8)
        QWidget.setTabOrder(self.Customized_parameters8, self.Btn_submit_changes)
        QWidget.setTabOrder(self.Btn_submit_changes, self.Btn_cancel_and_exit)
        QWidget.setTabOrder(self.Btn_cancel_and_exit, self.Btn_min_window)
        QWidget.setTabOrder(self.Btn_min_window, self.Btn_close_window)

        self.retranslateUi(Form)
        self.Btn_min_window.clicked.connect(Form.showMinimized)
        self.Btn_close_window.clicked.connect(Form.close)
        self.Btn_cancel_and_exit.clicked.connect(Form.close)
        self.Btn_submit_changes.clicked.connect(Form.close)
        self.checkBox_whether_open_web_services.toggled.connect(self.web_port.setEnabled)
        self.checkBox_whether_open_line.toggled.connect(self.open_line_Coordinates.setEnabled)
        self.checkBox_whether_close_line.toggled.connect(self.close_line_Coordinates.setEnabled)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_tital_6.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u7b56\u7565\u8fdb\u7a0b\u53c2\u6570", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5f53\u524d\u4fee\u6539\u7684\u7b56\u7565\u5b9e\u4f8b\u4e3a\uff1a", None))
        self.label_info.setText("")
        self.Btn_min_window.setText("")
        self.Btn_close_window.setText("")
        self.label_tital_4.setText(QCoreApplication.translate("Form", u"\u8bf7\u4fee\u6539\u7b56\u7565\u53c2\u6570\u5e76\u4ed4\u7ec6\u6838\u5bf9", None))
        self.label_whether_self_start.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u4e3a\u81ea\u542f\u8fdb\u7a0b", None))
        self.label_whether_live_futures_trading.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u4e3a\u5b9e\u76d8", None))
        self.label_trading_status.setText(QCoreApplication.translate("Form", u"\u4ea4\u6613\u72b6\u6001", None))
        self.label_whether_open_web_services.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u5f00\u542fweb", None))
        self.label_web_port.setText(QCoreApplication.translate("Form", u"web\u7aef\u53e3\u53f7", None))
        self.label_symbol_period.setText(QCoreApplication.translate("Form", u"\u5408\u7ea6\u5468\u671f(\u5206\u949f)", None))
        self.label_initial_capital.setText(QCoreApplication.translate("Form", u"\u7b56\u7565\u521d\u59cb\u8d44\u91d1", None))
        self.label_orientation.setText(QCoreApplication.translate("Form", u"\u4ea4\u6613\u65b9\u5411", None))
        self.label_contract_multiples.setText(QCoreApplication.translate("Form", u"\u5408\u7ea6\u500d\u6570", None))
        self.checkBox_whether_self_start.setText(QCoreApplication.translate("Form", u"\u52fe\u9009\u4e3a\u81ea\u542f", None))
        self.checkBox_whether_live_futures_trading.setText(QCoreApplication.translate("Form", u"\u52fe\u9009\u4e3a\u5b9e\u76d8", None))
        self.checkBox_trading_status.setText(QCoreApplication.translate("Form", u"\u52fe\u9009\u6b63\u5e38\u4ea4\u6613", None))
        self.checkBox_whether_open_web_services.setText(QCoreApplication.translate("Form", u"\u52fe\u9009\u5f00\u542fweb", None))
        self.contract_multiples.setText("")
        self.label_margin_rate.setText(QCoreApplication.translate("Form", u"\u4fdd\u8bc1\u91d1\u7387\uff08%\uff09", None))
        self.label_stop_loss.setText(QCoreApplication.translate("Form", u"\u6b62\u635f\u4f4d\uff08%\uff09", None))
        self.label_stop_profit.setText(QCoreApplication.translate("Form", u"\u6b62\u76c8\u4f4d\uff08%\uff09", None))
        self.lable_whether_open_line.setText(QCoreApplication.translate("Form", u"\u5b9a\u4e49\u5f00\u4ed3\u76f4\u7ebf", None))
        self.label_open_line_Coordinates.setText(QCoreApplication.translate("Form", u"\u5f00\u4ed3\u7ebf\u5750\u6807", None))
        self.label_whether_close_line.setText(QCoreApplication.translate("Form", u"\u5b9a\u4e49\u5e73\u4ed3\u76f4\u7ebf", None))
        self.label_close_line_Coordinates.setText(QCoreApplication.translate("Form", u"\u5e73\u4ed3\u7ebf\u5750\u6807", None))
        self.label_long_add_times.setText(QCoreApplication.translate("Form", u"\u591a\u5355\u52a0\u4ed3\u6b21\u6570", None))
        self.label_short_add_times.setText(QCoreApplication.translate("Form", u"\u7a7a\u5355\u52a0\u4ed3\u6b21\u6570", None))
        self.margin_rate.setText("")
        self.checkBox_whether_open_line.setText(QCoreApplication.translate("Form", u"\u52fe\u9009\u4e3a\u5df2\u6709\u76f4\u7ebf", None))
        self.checkBox_whether_close_line.setText(QCoreApplication.translate("Form", u"\u52fe\u9009\u4e3a\u5df2\u6709\u76f4\u7ebf", None))
        self.label_Customized_parameters1.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65701", None))
        self.label_Customized_parameters2.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65702", None))
        self.label_Customized_parameters3.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65703", None))
        self.label_Customized_parameters4.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65704", None))
        self.label_Customized_parameters5.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65705", None))
        self.label_Customized_parameters6.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65706", None))
        self.label_Customized_parameters7.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65707", None))
        self.label_Customized_parameters8.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65708", None))
        self.label_Customized_parameters9.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65709", None))
        self.Customized_parameters5.setText("")
        self.Customized_parameters6.setText("")
        self.Btn_submit_changes.setText(QCoreApplication.translate("Form", u"\u63d0\u4ea4\u4fee\u6539", None))
        self.Btn_cancel_and_exit.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88\u5e76\u9000\u51fa", None))
    # retranslateUi

