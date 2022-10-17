# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateBackTestProcess_dark.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1350, 800)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(1350, 800))
        Form.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(1350, 800))
        self.frame_3.setMaximumSize(QSize(1350, 800))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(170, 0, 255);	\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
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
        self.label_tital_6.setStyleSheet(u"font: 700 18pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_tital_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_info = QLabel(self.frame_2)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setMinimumSize(QSize(200, 0))
        self.label_info.setStyleSheet(u"font: 700 16pt \"\u7b49\u7ebf\";\n"
"color: rgb(0, 255, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_info)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.Btn_open_with_chrome = QPushButton(self.frame_2)
        self.Btn_open_with_chrome.setObjectName(u"Btn_open_with_chrome")
        self.Btn_open_with_chrome.setMinimumSize(QSize(250, 30))
        self.Btn_open_with_chrome.setMaximumSize(QSize(300, 30))
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.Btn_open_with_chrome.setFont(font)
        self.Btn_open_with_chrome.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(40, 40, 70, 0);\n"
"	color: rgb(85, 255, 0);\n"
"	\n"
"	font: 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-left: 3px solid rgb(255, 85, 0);\n"
"	border-right: 3px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 25, 25);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/chrome.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_open_with_chrome.setIcon(icon)
        self.Btn_open_with_chrome.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.Btn_open_with_chrome)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

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
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/\u6700\u5c0f\u5316.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_min_window.setIcon(icon1)
        self.Btn_min_window.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.Btn_min_window)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

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
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/\u5173\u95ed.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_close_window.setIcon(icon2)
        self.Btn_close_window.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.Btn_close_window)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_93 = QFrame(self.frame)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(430, 400))
        self.frame_93.setMaximumSize(QSize(450, 16333512))
        self.frame_93.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_93)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_93)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QFrame {	\n"
"	border: none;\n"
"}\n"
"QFrame:hover {\n"
"	border:none;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.upper_left_4 = QFrame(self.frame_8)
        self.upper_left_4.setObjectName(u"upper_left_4")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upper_left_4.sizePolicy().hasHeightForWidth())
        self.upper_left_4.setSizePolicy(sizePolicy)
        self.upper_left_4.setMinimumSize(QSize(185, 0))
        self.upper_left_4.setMaximumSize(QSize(185, 1000))
        self.upper_left_4.setStyleSheet(u"border:none")
        self.upper_left_4.setFrameShape(QFrame.StyledPanel)
        self.upper_left_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.upper_left_4)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_select_tq_account = QLabel(self.upper_left_4)
        self.label_select_tq_account.setObjectName(u"label_select_tq_account")
        self.label_select_tq_account.setEnabled(True)
        self.label_select_tq_account.setMinimumSize(QSize(180, 40))
        self.label_select_tq_account.setMaximumSize(QSize(180, 40))
        self.label_select_tq_account.setStyleSheet(u"QLabel {\n"
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
        self.label_select_tq_account.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_select_tq_account)

        self.label_select_strategy = QLabel(self.upper_left_4)
        self.label_select_strategy.setObjectName(u"label_select_strategy")
        self.label_select_strategy.setEnabled(True)
        self.label_select_strategy.setMinimumSize(QSize(180, 40))
        self.label_select_strategy.setMaximumSize(QSize(180, 40))
        self.label_select_strategy.setStyleSheet(u"QLabel {\n"
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
        self.label_select_strategy.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_select_strategy)

        self.label_exchange = QLabel(self.upper_left_4)
        self.label_exchange.setObjectName(u"label_exchange")
        self.label_exchange.setMinimumSize(QSize(180, 40))
        self.label_exchange.setMaximumSize(QSize(180, 40))
        self.label_exchange.setStyleSheet(u"QLabel {\n"
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
        self.label_exchange.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_exchange)

        self.label_5 = QLabel(self.upper_left_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(180, 40))
        self.label_5.setMaximumSize(QSize(180, 40))
        self.label_5.setStyleSheet(u"QLabel {\n"
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
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_5)

        self.label_symbol = QLabel(self.upper_left_4)
        self.label_symbol.setObjectName(u"label_symbol")
        self.label_symbol.setMinimumSize(QSize(180, 40))
        self.label_symbol.setMaximumSize(QSize(180, 40))
        self.label_symbol.setStyleSheet(u"QLabel {\n"
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
        self.label_symbol.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_symbol)

        self.label_symbol_period = QLabel(self.upper_left_4)
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

        self.verticalLayout_54.addWidget(self.label_symbol_period)

        self.label_initial_capital = QLabel(self.upper_left_4)
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

        self.verticalLayout_54.addWidget(self.label_initial_capital)

        self.label_web_port = QLabel(self.upper_left_4)
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

        self.verticalLayout_54.addWidget(self.label_web_port)

        self.label_orientation = QLabel(self.upper_left_4)
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

        self.verticalLayout_54.addWidget(self.label_orientation)

        self.label_contract_multiples = QLabel(self.upper_left_4)
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

        self.verticalLayout_54.addWidget(self.label_contract_multiples)

        self.label_margin_rate = QLabel(self.upper_left_4)
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

        self.verticalLayout_54.addWidget(self.label_margin_rate)


        self.horizontalLayout_5.addWidget(self.upper_left_4)

        self.upper_right_4 = QFrame(self.frame_8)
        self.upper_right_4.setObjectName(u"upper_right_4")
        sizePolicy.setHeightForWidth(self.upper_right_4.sizePolicy().hasHeightForWidth())
        self.upper_right_4.setSizePolicy(sizePolicy)
        self.upper_right_4.setMinimumSize(QSize(205, 0))
        self.upper_right_4.setMaximumSize(QSize(205, 1000))
        self.upper_right_4.setStyleSheet(u"border:none")
        self.upper_right_4.setFrameShape(QFrame.StyledPanel)
        self.upper_right_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.upper_right_4)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.comboBox_select_tq_account = QComboBox(self.upper_right_4)
        self.comboBox_select_tq_account.setObjectName(u"comboBox_select_tq_account")
        self.comboBox_select_tq_account.setMinimumSize(QSize(200, 40))
        self.comboBox_select_tq_account.setMaximumSize(QSize(200, 40))
        self.comboBox_select_tq_account.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 1px 1px 5px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 14pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid rgb(65, 51, 156);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: rgb(200, 200, 200);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(13, 9, 36);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"	border:none;\n"
"    height: 35px; \n"
"}\n"
"QComboBox QAbstractItemView::item:hover{\n"
"	border: none;	\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(65, 49, 188);\n"
"\n"
"}\n"
"QComboBox"
                        " QAbstractItemView::item:selected{\n"
"	border: none;\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	image: url(:/icon/icons/\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 20px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
""
                        "    width: 30px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6 */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*\u53f3\u8fb9\u7684\u6ed1\u52a8\u6761*/\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 17px 0 17px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:"
                        "vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 0px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: transparent;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     backgroun"
                        "d: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")

        self.verticalLayout_55.addWidget(self.comboBox_select_tq_account)

        self.comboBox_select_strategy = QComboBox(self.upper_right_4)
        self.comboBox_select_strategy.setObjectName(u"comboBox_select_strategy")
        self.comboBox_select_strategy.setMinimumSize(QSize(200, 40))
        self.comboBox_select_strategy.setMaximumSize(QSize(200, 40))
        self.comboBox_select_strategy.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 1px 1px 5px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 14pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid rgb(65, 51, 156);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: rgb(200, 200, 200);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(13, 9, 36);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"	border:none;\n"
"    height: 35px; \n"
"}\n"
"QComboBox QAbstractItemView::item:hover{\n"
"	border: none;	\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(65, 49, 188);\n"
"\n"
"}\n"
"QComboBox"
                        " QAbstractItemView::item:selected{\n"
"	border: none;\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	image: url(:/icon/icons/\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 20px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
""
                        "    width: 30px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6 */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*\u53f3\u8fb9\u7684\u6ed1\u52a8\u6761*/\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 17px 0 17px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:"
                        "vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 0px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: transparent;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     backgroun"
                        "d: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")

        self.verticalLayout_55.addWidget(self.comboBox_select_strategy)

        self.comboBox_exchange = QComboBox(self.upper_right_4)
        self.comboBox_exchange.addItem("")
        self.comboBox_exchange.addItem("")
        self.comboBox_exchange.addItem("")
        self.comboBox_exchange.addItem("")
        self.comboBox_exchange.addItem("")
        self.comboBox_exchange.setObjectName(u"comboBox_exchange")
        self.comboBox_exchange.setMinimumSize(QSize(200, 40))
        self.comboBox_exchange.setMaximumSize(QSize(200, 40))
        self.comboBox_exchange.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 1px 1px 5px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 14pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid rgb(65, 51, 156);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: rgb(200, 200, 200);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(13, 9, 36);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"	border:none;\n"
"    height: 35px; \n"
"}\n"
"QComboBox QAbstractItemView::item:hover{\n"
"	border: none;	\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(65, 49, 188);\n"
"\n"
"}\n"
"QComboBox"
                        " QAbstractItemView::item:selected{\n"
"	border: none;\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	image: url(:/icon/icons/\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 20px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
""
                        "    width: 30px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6 */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*\u53f3\u8fb9\u7684\u6ed1\u52a8\u6761*/\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 17px 0 17px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:"
                        "vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 0px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: transparent;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     backgroun"
                        "d: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.comboBox_exchange.setFrame(True)
        self.comboBox_exchange.setModelColumn(0)

        self.verticalLayout_55.addWidget(self.comboBox_exchange)

        self.comboBox_contract_type = QComboBox(self.upper_right_4)
        self.comboBox_contract_type.addItem("")
        self.comboBox_contract_type.addItem("")
        self.comboBox_contract_type.addItem("")
        self.comboBox_contract_type.addItem("")
        self.comboBox_contract_type.addItem("")
        self.comboBox_contract_type.setObjectName(u"comboBox_contract_type")
        self.comboBox_contract_type.setMinimumSize(QSize(200, 40))
        self.comboBox_contract_type.setMaximumSize(QSize(200, 40))
        self.comboBox_contract_type.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 1px 1px 5px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 14pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid rgb(65, 51, 156);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: rgb(200, 200, 200);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(13, 9, 36);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"	border:none;\n"
"    height: 35px; \n"
"}\n"
"QComboBox QAbstractItemView::item:hover{\n"
"	border: none;	\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(65, 49, 188);\n"
"\n"
"}\n"
"QComboBox"
                        " QAbstractItemView::item:selected{\n"
"	border: none;\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	image: url(:/icon/icons/\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 20px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
""
                        "    width: 30px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6 */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*\u53f3\u8fb9\u7684\u6ed1\u52a8\u6761*/\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 17px 0 17px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:"
                        "vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 0px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: transparent;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     backgroun"
                        "d: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")

        self.verticalLayout_55.addWidget(self.comboBox_contract_type)

        self.comboBox_symbol = QComboBox(self.upper_right_4)
        self.comboBox_symbol.setObjectName(u"comboBox_symbol")
        self.comboBox_symbol.setMinimumSize(QSize(200, 40))
        self.comboBox_symbol.setMaximumSize(QSize(200, 40))
        self.comboBox_symbol.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 1px 1px 5px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 14pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid rgb(65, 51, 156);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: rgb(200, 200, 200);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(13, 9, 36);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"	border:none;\n"
"    height: 35px; \n"
"}\n"
"QComboBox QAbstractItemView::item:hover{\n"
"	border: none;	\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(65, 49, 188);\n"
"\n"
"}\n"
"QComboBox"
                        " QAbstractItemView::item:selected{\n"
"	border: none;\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	image: url(:/icon/icons/\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 20px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
""
                        "    width: 30px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6 */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*\u53f3\u8fb9\u7684\u6ed1\u52a8\u6761*/\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 17px 0 17px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:"
                        "vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 0px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"     height: 15px;\n"
"	border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: transparent;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     backgroun"
                        "d: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.comboBox_symbol.setEditable(True)
        self.comboBox_symbol.setMaxVisibleItems(20)

        self.verticalLayout_55.addWidget(self.comboBox_symbol)

        self.symbol_period = QLineEdit(self.upper_right_4)
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

        self.verticalLayout_55.addWidget(self.symbol_period)

        self.initial_capital = QLineEdit(self.upper_right_4)
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

        self.verticalLayout_55.addWidget(self.initial_capital)

        self.web_port = QLineEdit(self.upper_right_4)
        self.web_port.setObjectName(u"web_port")
        self.web_port.setMinimumSize(QSize(200, 40))
        self.web_port.setMaximumSize(QSize(200, 40))
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

        self.verticalLayout_55.addWidget(self.web_port)

        self.orientation = QLineEdit(self.upper_right_4)
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

        self.verticalLayout_55.addWidget(self.orientation)

        self.contract_multiples = QLineEdit(self.upper_right_4)
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

        self.verticalLayout_55.addWidget(self.contract_multiples)

        self.margin_rate = QLineEdit(self.upper_right_4)
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

        self.verticalLayout_55.addWidget(self.margin_rate)


        self.horizontalLayout_5.addWidget(self.upper_right_4)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_93)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 60))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Btn_stop_backtest = QPushButton(self.frame_9)
        self.Btn_stop_backtest.setObjectName(u"Btn_stop_backtest")
        self.Btn_stop_backtest.setMinimumSize(QSize(180, 40))
        self.Btn_stop_backtest.setMaximumSize(QSize(180, 40))
        self.Btn_stop_backtest.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb( 0, 250, 0);\n"
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

        self.horizontalLayout_7.addWidget(self.Btn_stop_backtest)

        self.Btn_clear_backtest_parameters = QPushButton(self.frame_9)
        self.Btn_clear_backtest_parameters.setObjectName(u"Btn_clear_backtest_parameters")
        self.Btn_clear_backtest_parameters.setMinimumSize(QSize(180, 40))
        self.Btn_clear_backtest_parameters.setMaximumSize(QSize(180, 40))
        self.Btn_clear_backtest_parameters.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 85, 0);\n"
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

        self.horizontalLayout_7.addWidget(self.Btn_clear_backtest_parameters)


        self.verticalLayout_7.addWidget(self.frame_9)


        self.horizontalLayout.addWidget(self.frame_93)

        self.frame_25 = QFrame(self.frame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(430, 0))
        self.frame_25.setMaximumSize(QSize(450, 16777215))
        self.frame_25.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_25)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_25)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame {	\n"
"	border: none;\n"
"}\n"
"QFrame:hover {\n"
"	border:none;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.upper_left_6 = QFrame(self.frame_6)
        self.upper_left_6.setObjectName(u"upper_left_6")
        sizePolicy.setHeightForWidth(self.upper_left_6.sizePolicy().hasHeightForWidth())
        self.upper_left_6.setSizePolicy(sizePolicy)
        self.upper_left_6.setMinimumSize(QSize(185, 0))
        self.upper_left_6.setMaximumSize(QSize(185, 1000))
        self.upper_left_6.setStyleSheet(u"border:none")
        self.upper_left_6.setFrameShape(QFrame.StyledPanel)
        self.upper_left_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.upper_left_6)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_stop_loss = QLabel(self.upper_left_6)
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

        self.verticalLayout_53.addWidget(self.label_stop_loss)

        self.label_stop_profit = QLabel(self.upper_left_6)
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

        self.verticalLayout_53.addWidget(self.label_stop_profit)

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


        self.horizontalLayout_4.addWidget(self.upper_left_6)

        self.upper_right_6 = QFrame(self.frame_6)
        self.upper_right_6.setObjectName(u"upper_right_6")
        sizePolicy.setHeightForWidth(self.upper_right_6.sizePolicy().hasHeightForWidth())
        self.upper_right_6.setSizePolicy(sizePolicy)
        self.upper_right_6.setMinimumSize(QSize(205, 0))
        self.upper_right_6.setMaximumSize(QSize(205, 1000))
        self.upper_right_6.setStyleSheet(u"border:none")
        self.upper_right_6.setFrameShape(QFrame.StyledPanel)
        self.upper_right_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.upper_right_6)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.stop_loss = QLineEdit(self.upper_right_6)
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

        self.verticalLayout_42.addWidget(self.stop_loss)

        self.stop_profit = QLineEdit(self.upper_right_6)
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

        self.verticalLayout_42.addWidget(self.stop_profit)

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


        self.horizontalLayout_4.addWidget(self.upper_right_6)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_25)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 60))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Btn_start_backtest = QPushButton(self.frame_7)
        self.Btn_start_backtest.setObjectName(u"Btn_start_backtest")
        self.Btn_start_backtest.setMinimumSize(QSize(200, 40))
        self.Btn_start_backtest.setMaximumSize(QSize(300, 40))
        self.Btn_start_backtest.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 0, 0);\n"
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

        self.horizontalLayout_6.addWidget(self.Btn_start_backtest)


        self.verticalLayout_6.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame_25)

        self.frame_97 = QFrame(self.frame)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMinimumSize(QSize(450, 0))
        self.frame_97.setMaximumSize(QSize(450, 16777215))
        self.frame_97.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_97)
        self.verticalLayout_58.setSpacing(10)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_77 = QFrame(self.frame_97)
        self.frame_77.setObjectName(u"frame_77")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_77.sizePolicy().hasHeightForWidth())
        self.frame_77.setSizePolicy(sizePolicy1)
        self.frame_77.setMinimumSize(QSize(0, 240))
        self.frame_77.setMaximumSize(QSize(16777215, 240))
        self.frame_77.setStyleSheet(u"QFrame {	\n"
"	border: none;\n"
"}\n"
"QFrame:hover {\n"
"	border:none;\n"
"}")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_44.setSpacing(20)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_77)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(185, 0))
        self.frame_4.setMaximumSize(QSize(185, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lable_whether_open_line = QLabel(self.frame_4)
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

        self.verticalLayout_4.addWidget(self.lable_whether_open_line)

        self.label_open_line_Coordinates = QLabel(self.frame_4)
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

        self.verticalLayout_4.addWidget(self.label_open_line_Coordinates)

        self.label_whether_close_line = QLabel(self.frame_4)
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

        self.verticalLayout_4.addWidget(self.label_whether_close_line)

        self.label_close_line_Coordinates = QLabel(self.frame_4)
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

        self.verticalLayout_4.addWidget(self.label_close_line_Coordinates)


        self.horizontalLayout_44.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_77)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.checkBox_whether_open_line = QCheckBox(self.frame_5)
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

        self.verticalLayout_5.addWidget(self.checkBox_whether_open_line)

        self.open_line_Coordinates = QLineEdit(self.frame_5)
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

        self.verticalLayout_5.addWidget(self.open_line_Coordinates)

        self.checkBox_whether_close_line = QCheckBox(self.frame_5)
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

        self.verticalLayout_5.addWidget(self.checkBox_whether_close_line)

        self.close_line_Coordinates = QLineEdit(self.frame_5)
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

        self.verticalLayout_5.addWidget(self.close_line_Coordinates)


        self.horizontalLayout_44.addWidget(self.frame_5)


        self.verticalLayout_58.addWidget(self.frame_77, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_58.addItem(self.verticalSpacer)

        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        sizePolicy1.setHeightForWidth(self.frame_98.sizePolicy().hasHeightForWidth())
        self.frame_98.setSizePolicy(sizePolicy1)
        self.frame_98.setMinimumSize(QSize(0, 350))
        self.frame_98.setStyleSheet(u"QFrame {	\n"
"	background-color: transparent;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_55.setSpacing(10)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(10, 10, 10, 10)
        self.frame_94 = QFrame(self.frame_98)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(0, 0))
        self.frame_94.setMaximumSize(QSize(240, 600))
        self.frame_94.setStyleSheet(u"border: none;")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_94)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_94)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 40))
        self.label_2.setMaximumSize(QSize(200, 40))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	\n"
"	background-color: rgba(255, 0, 127, 230);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid;\n"
"	border-color: rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.calendar_backtest_startdate = QCalendarWidget(self.frame_94)
        self.calendar_backtest_startdate.setObjectName(u"calendar_backtest_startdate")
        self.calendar_backtest_startdate.setMinimumSize(QSize(200, 250))
        self.calendar_backtest_startdate.setMaximumSize(QSize(200, 250))
        self.calendar_backtest_startdate.setStyleSheet(u"#qt_calendar_calendarview {\n"
"     background: rgb(174, 182, 255);\n"
"}\n"
"\n"
"#qt_calendar_navigationbar {/*\u5e74\u6708\u9009\u62e9\u680f\u80cc\u666f\u8272*/\n"
"    background:rgb(255, 255, 255);\n"
"}\n"
"#qt_calendar_yearedit {    \n"
"	font: 14pt \"\u7b49\u7ebf\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton#qt_calendar_monthbutton,#qt_calendar_yearbutton{    \n"
"	background-color: rgb(249, 62, 255);/*\u9009\u62e9\u6708\u4efd\u548c\u5e74\u7684\u80cc\u666f*/\n"
"	height: 30px;	\n"
"	font: 14pt \"\u7b49\u7ebf\";\n"
"	width: 80px;\n"
"	border-radius:15px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar{\n"
"    \n"
"	background-color:green;/*\u9009\u62e9\u6708\u4efd\u548c\u5e74\u4e24\u8fb9\u7684\u80cc\u666f*/\n"
"	border-radius: 10px;\n"
"}\n"
"QCalendarWidget QMenu{   	\n"
"	background-color:rgb(91, 79, 255);/*\u6708\u4efd\u4e0b\u62c9\u9009\u62e9\u83dc\u5355\u7684\u80cc\u666f*/\n"
"	font: 14pt \"\u7b49\u7ebf\";\n"
"}\n"
"QToolButton#qt_calendar_prevmonth{/*\u5411\u5de6"
                        "\u7bad\u5934*/	\n"
"	background-color: transparent;\n"
"	icon-size:30px 30px;\n"
"	qproperty-icon: url(:/icon/icons/\u7bad\u5934_\u5411\u5de6.svg);\n"
"	margin-left:0px;\n"
"}\n"
"QToolButton#qt_calendar_nextmonth{\n"
"    background-color: transparent;\n"
"	icon-size:30px 30px;	\n"
"	qproperty-icon: url(:/icon/icons/\u7bad\u5934_\u5411\u53f3.svg);\n"
"}\n"
"QToolButton#qt_calendar_monthbutton::menu-indicator{/*\u6708\u4efd\u4e0b\u62c9\u7bad\u5934*/\n"
"	image: url(:/icon/icons/\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    right: -4px;\n"
"    width: 30px;\n"
"}\n"
"QCalendarWidget QAbstractItemView:enabled  {\n"
"    color: black;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 174, 0);    \n"
"	font: 700 10pt \"\u7b49\u7ebf\";\n"
"}\n"
" /*\u8fd9\u91cc\u662f\u5176\u4ed6\u6708\u4efd\u7684\u6837\u5f0f*/\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{\n"
"     \n"
"color: rgb(147, 147, 1"
                        "47); \n"
"}")

        self.verticalLayout_2.addWidget(self.calendar_backtest_startdate, 0, Qt.AlignHCenter)

        self.label = QLabel(self.frame_94)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setStyleSheet(u"font: 700 16pt \"\u7b49\u7ebf\";\n"
"color: rgb(0, 255, 0);\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.label)

        self.label_backtest_startdate = QLabel(self.frame_94)
        self.label_backtest_startdate.setObjectName(u"label_backtest_startdate")
        self.label_backtest_startdate.setMinimumSize(QSize(200, 35))
        self.label_backtest_startdate.setMaximumSize(QSize(200, 35))
        self.label_backtest_startdate.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_backtest_startdate.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_backtest_startdate, 0, Qt.AlignHCenter)


        self.horizontalLayout_55.addWidget(self.frame_94, 0, Qt.AlignHCenter)

        self.frame_95 = QFrame(self.frame_98)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(0, 0))
        self.frame_95.setMaximumSize(QSize(240, 600))
        self.frame_95.setStyleSheet(u"border: none;")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_95)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_95)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 40))
        self.label_3.setMaximumSize(QSize(200, 40))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	\n"
"	background-color: rgba(255, 0, 127, 230);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid;\n"
"	border-color: rgb(0, 255, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.calendar_backtest_enddate = QCalendarWidget(self.frame_95)
        self.calendar_backtest_enddate.setObjectName(u"calendar_backtest_enddate")
        self.calendar_backtest_enddate.setMinimumSize(QSize(200, 250))
        self.calendar_backtest_enddate.setMaximumSize(QSize(200, 250))
        self.calendar_backtest_enddate.setStyleSheet(u"#qt_calendar_calendarview {\n"
"     background: rgb(174, 182, 255);\n"
"}\n"
"\n"
"#qt_calendar_navigationbar {/*\u5e74\u6708\u9009\u62e9\u680f\u80cc\u666f\u8272*/\n"
"    background:rgb(255, 255, 255);\n"
"}\n"
"#qt_calendar_yearedit {    \n"
"	font: 14pt \"\u7b49\u7ebf\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton#qt_calendar_monthbutton,#qt_calendar_yearbutton{    \n"
"	background-color: rgb(249, 62, 255);/*\u9009\u62e9\u6708\u4efd\u548c\u5e74\u7684\u80cc\u666f*/\n"
"	height: 30px;	\n"
"	font: 14pt \"\u7b49\u7ebf\";\n"
"	width: 80px;\n"
"	border-radius:15px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar{\n"
"    \n"
"	background-color:green;/*\u9009\u62e9\u6708\u4efd\u548c\u5e74\u4e24\u8fb9\u7684\u80cc\u666f*/\n"
"	border-radius: 10px;\n"
"}\n"
"QCalendarWidget QMenu{   	\n"
"	background-color:rgb(91, 79, 255);/*\u6708\u4efd\u4e0b\u62c9\u9009\u62e9\u83dc\u5355\u7684\u80cc\u666f*/\n"
"	font: 14pt \"\u7b49\u7ebf\";\n"
"}\n"
"QToolButton#qt_calendar_prevmonth{/*\u5411\u5de6"
                        "\u7bad\u5934*/	\n"
"	background-color: transparent;\n"
"	icon-size:30px 30px;\n"
"	qproperty-icon: url(:/icon/icons/\u7bad\u5934_\u5411\u5de6.svg);\n"
"	margin-left:0px;\n"
"}\n"
"QToolButton#qt_calendar_nextmonth{\n"
"    background-color: transparent;\n"
"	icon-size:30px 30px;	\n"
"	qproperty-icon: url(:/icon/icons/\u7bad\u5934_\u5411\u53f3.svg);\n"
"}\n"
"QToolButton#qt_calendar_monthbutton::menu-indicator{/*\u6708\u4efd\u4e0b\u62c9\u7bad\u5934*/\n"
"	image: url(:/icon/icons/\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    right: -4px;\n"
"    width: 30px;\n"
"}\n"
"QCalendarWidget QAbstractItemView:enabled  {\n"
"    color: black;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 174, 0);    \n"
"	font: 700 10pt \"\u7b49\u7ebf\";\n"
"}\n"
" /*\u8fd9\u91cc\u662f\u5176\u4ed6\u6708\u4efd\u7684\u6837\u5f0f*/\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{\n"
"     \n"
"color: rgb(147, 147, 1"
                        "47); \n"
"}")

        self.verticalLayout_3.addWidget(self.calendar_backtest_enddate, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.frame_95)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setStyleSheet(u"font: 700 16pt \"\u7b49\u7ebf\";\n"
"color: rgb(0, 255, 0);\n"
"border: none;")

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_backtest_enddate = QLabel(self.frame_95)
        self.label_backtest_enddate.setObjectName(u"label_backtest_enddate")
        self.label_backtest_enddate.setMinimumSize(QSize(200, 35))
        self.label_backtest_enddate.setMaximumSize(QSize(200, 35))
        self.label_backtest_enddate.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QLabel:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.label_backtest_enddate.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_backtest_enddate, 0, Qt.AlignHCenter)


        self.horizontalLayout_55.addWidget(self.frame_95, 0, Qt.AlignHCenter)


        self.verticalLayout_58.addWidget(self.frame_98, 0, Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_58.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_97)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_3.addWidget(self.frame_3)

#if QT_CONFIG(shortcut)
        self.label_select_tq_account.setBuddy(self.comboBox_select_tq_account)
        self.label_select_strategy.setBuddy(self.comboBox_select_strategy)
        self.label_exchange.setBuddy(self.comboBox_exchange)
        self.label_symbol_period.setBuddy(self.symbol_period)
        self.label_initial_capital.setBuddy(self.initial_capital)
        self.label_web_port.setBuddy(self.web_port)
        self.label_orientation.setBuddy(self.orientation)
        self.label_contract_multiples.setBuddy(self.contract_multiples)
        self.label_margin_rate.setBuddy(self.margin_rate)
        self.label_stop_loss.setBuddy(self.stop_loss)
        self.label_stop_profit.setBuddy(self.stop_profit)
        self.label_Customized_parameters1.setBuddy(self.Customized_parameters1)
        self.label_Customized_parameters2.setBuddy(self.Customized_parameters2)
        self.label_Customized_parameters3.setBuddy(self.Customized_parameters3)
        self.label_Customized_parameters4.setBuddy(self.Customized_parameters4)
        self.label_Customized_parameters5.setBuddy(self.Customized_parameters5)
        self.label_Customized_parameters6.setBuddy(self.Customized_parameters6)
        self.label_Customized_parameters7.setBuddy(self.Customized_parameters7)
        self.label_Customized_parameters8.setBuddy(self.Customized_parameters8)
        self.lable_whether_open_line.setBuddy(self.checkBox_whether_open_line)
        self.label_open_line_Coordinates.setBuddy(self.open_line_Coordinates)
        self.label_whether_close_line.setBuddy(self.checkBox_whether_close_line)
        self.label_close_line_Coordinates.setBuddy(self.close_line_Coordinates)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.comboBox_select_tq_account, self.comboBox_select_strategy)
        QWidget.setTabOrder(self.comboBox_select_strategy, self.comboBox_exchange)
        QWidget.setTabOrder(self.comboBox_exchange, self.initial_capital)
        QWidget.setTabOrder(self.initial_capital, self.web_port)
        QWidget.setTabOrder(self.web_port, self.orientation)
        QWidget.setTabOrder(self.orientation, self.contract_multiples)
        QWidget.setTabOrder(self.contract_multiples, self.margin_rate)
        QWidget.setTabOrder(self.margin_rate, self.stop_loss)
        QWidget.setTabOrder(self.stop_loss, self.stop_profit)
        QWidget.setTabOrder(self.stop_profit, self.Customized_parameters1)
        QWidget.setTabOrder(self.Customized_parameters1, self.Customized_parameters2)
        QWidget.setTabOrder(self.Customized_parameters2, self.Customized_parameters3)
        QWidget.setTabOrder(self.Customized_parameters3, self.Customized_parameters4)
        QWidget.setTabOrder(self.Customized_parameters4, self.Customized_parameters5)
        QWidget.setTabOrder(self.Customized_parameters5, self.Customized_parameters6)
        QWidget.setTabOrder(self.Customized_parameters6, self.Customized_parameters7)
        QWidget.setTabOrder(self.Customized_parameters7, self.Customized_parameters8)
        QWidget.setTabOrder(self.Customized_parameters8, self.checkBox_whether_open_line)
        QWidget.setTabOrder(self.checkBox_whether_open_line, self.open_line_Coordinates)
        QWidget.setTabOrder(self.open_line_Coordinates, self.checkBox_whether_close_line)
        QWidget.setTabOrder(self.checkBox_whether_close_line, self.close_line_Coordinates)
        QWidget.setTabOrder(self.close_line_Coordinates, self.calendar_backtest_startdate)
        QWidget.setTabOrder(self.calendar_backtest_startdate, self.calendar_backtest_enddate)
        QWidget.setTabOrder(self.calendar_backtest_enddate, self.Btn_open_with_chrome)
        QWidget.setTabOrder(self.Btn_open_with_chrome, self.Btn_min_window)
        QWidget.setTabOrder(self.Btn_min_window, self.Btn_close_window)

        self.retranslateUi(Form)
        self.Btn_close_window.clicked.connect(Form.close)
        self.Btn_min_window.clicked.connect(Form.showMinimized)
        self.checkBox_whether_open_line.toggled.connect(self.open_line_Coordinates.setEnabled)
        self.checkBox_whether_close_line.toggled.connect(self.close_line_Coordinates.setEnabled)

        self.comboBox_contract_type.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_tital_6.setText(QCoreApplication.translate("Form", u"\u521b\u5efa\u7b56\u7565\u56de\u6d4b\u8fdb\u7a0b", None))
        self.label_info.setText("")
        self.Btn_open_with_chrome.setText(QCoreApplication.translate("Form", u" \u5728\u6d4f\u89c8\u5668\u4e2d\u6253\u5f00\u56de\u6d4b\u9875", None))
        self.Btn_min_window.setText("")
        self.Btn_close_window.setText("")
        self.label_select_tq_account.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u5929\u52e4\u8d26\u6237", None))
        self.label_select_strategy.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u7b56\u7565", None))
        self.label_exchange.setText(QCoreApplication.translate("Form", u"\u4ea4\u6613\u6240", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5408\u7ea6\u7c7b\u578b", None))
        self.label_symbol.setText(QCoreApplication.translate("Form", u"\u5408\u7ea6\u540d", None))
        self.label_symbol_period.setText(QCoreApplication.translate("Form", u"\u5408\u7ea6\u5468\u671f", None))
        self.label_initial_capital.setText(QCoreApplication.translate("Form", u"\u7b56\u7565\u521d\u59cb\u8d44\u91d1", None))
        self.label_web_port.setText(QCoreApplication.translate("Form", u"web\u7aef\u53e3\u53f7", None))
        self.label_orientation.setText(QCoreApplication.translate("Form", u"\u4ea4\u6613\u65b9\u5411", None))
        self.label_contract_multiples.setText(QCoreApplication.translate("Form", u"\u5408\u7ea6\u500d\u6570", None))
        self.label_margin_rate.setText(QCoreApplication.translate("Form", u"\u4fdd\u8bc1\u91d1\u7387\uff08%\uff09", None))
        self.comboBox_exchange.setItemText(0, QCoreApplication.translate("Form", u"\u5927\u5546\u6240 DCE", None))
        self.comboBox_exchange.setItemText(1, QCoreApplication.translate("Form", u"\u4e0a\u671f\u6240 SHFE", None))
        self.comboBox_exchange.setItemText(2, QCoreApplication.translate("Form", u"\u90d1\u5546\u6240 CZCE", None))
        self.comboBox_exchange.setItemText(3, QCoreApplication.translate("Form", u"\u80fd\u6e90\u4ea4\u6613\u6240 INE", None))
        self.comboBox_exchange.setItemText(4, QCoreApplication.translate("Form", u"\u4e2d\u91d1\u6240 CFFEX", None))

        self.comboBox_contract_type.setItemText(0, QCoreApplication.translate("Form", u"\u4e3b\u529b\u5408\u7ea6 Main", None))
        self.comboBox_contract_type.setItemText(1, QCoreApplication.translate("Form", u"\u6240\u6709\u5408\u7ea6 Future", None))
        self.comboBox_contract_type.setItemText(2, QCoreApplication.translate("Form", u"\u4e3b\u529b\u8fde\u7eed Cont", None))
        self.comboBox_contract_type.setItemText(3, QCoreApplication.translate("Form", u"\u5408\u7ea6\u6307\u6570 Index", None))
        self.comboBox_contract_type.setItemText(4, QCoreApplication.translate("Form", u"\u671f\u6743\u5408\u7ea6 Option", None))

        self.Btn_stop_backtest.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f\u56de\u6d4b", None))
        self.Btn_clear_backtest_parameters.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u8f93\u5165", None))
        self.label_stop_loss.setText(QCoreApplication.translate("Form", u"\u6b62\u635f\u4f4d\uff08%\uff09", None))
        self.label_stop_profit.setText(QCoreApplication.translate("Form", u"\u6b62\u76c8\u4f4d\uff08%\uff09", None))
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
        self.Btn_start_backtest.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u56de\u6d4b", None))
        self.lable_whether_open_line.setText(QCoreApplication.translate("Form", u"\u5b9a\u4e49\u5f00\u4ed3\u76f4\u7ebf", None))
        self.label_open_line_Coordinates.setText(QCoreApplication.translate("Form", u"\u5f00\u4ed3\u7ebf\u5750\u6807", None))
        self.label_whether_close_line.setText(QCoreApplication.translate("Form", u"\u5b9a\u4e49\u5e73\u4ed3\u76f4\u7ebf", None))
        self.label_close_line_Coordinates.setText(QCoreApplication.translate("Form", u"\u5e73\u4ed3\u7ebf\u5750\u6807", None))
        self.checkBox_whether_open_line.setText(QCoreApplication.translate("Form", u"\u52fe\u9009\u4e3a\u5df2\u6709\u76f4\u7ebf", None))
        self.checkBox_whether_close_line.setText(QCoreApplication.translate("Form", u"\u52fe\u9009\u4e3a\u5df2\u6709\u76f4\u7ebf", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u56de\u6d4b\u5f00\u59cb\u65e5\u671f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u7684\u5f00\u59cb\u65e5\u671f\u4e3a\uff1a", None))
        self.label_backtest_startdate.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u56de\u6d4b\u7ed3\u675f\u65e5\u671f", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u7684\u7ed3\u675f\u65e5\u671f\u4e3a\uff1a", None))
        self.label_backtest_enddate.setText("")
    # retranslateUi

