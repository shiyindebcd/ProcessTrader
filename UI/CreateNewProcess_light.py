# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateNewProcess_light.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
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
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(100, 100, 100);	\n"
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
        self.label_tital_6.setMaximumSize(QSize(16777215, 50))
        self.label_tital_6.setStyleSheet(u"font: 700 20pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_tital_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

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
        icon.addFile(u":/icon/icons/\u7f29\u5c0f.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_min_window.setIcon(icon)
        self.Btn_min_window.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.Btn_min_window)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.Btn_close_window = QPushButton(self.frame_2)
        self.Btn_close_window.setObjectName(u"Btn_close_window")
        self.Btn_close_window.setMinimumSize(QSize(35, 35))
        self.Btn_close_window.setMaximumSize(QSize(35, 35))
        self.Btn_close_window.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/\u5173\u95ed (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_close_window.setIcon(icon1)
        self.Btn_close_window.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.Btn_close_window)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 10)
        self.frame_56 = QFrame(self.frame)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(430, 0))
        self.frame_56.setMaximumSize(QSize(450, 16777215))
        self.frame_56.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
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
"color: rgb(0, 170, 0);\n"
"border: none;")

        self.verticalLayout_39.addWidget(self.label_tital_4)


        self.verticalLayout_38.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_56)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMaximumSize(QSize(450, 16777215))
        self.frame_58.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(248, 248, 219);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
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
        self.label_select_clients_name1 = QLabel(self.upper_left_3)
        self.label_select_clients_name1.setObjectName(u"label_select_clients_name1")
        self.label_select_clients_name1.setMinimumSize(QSize(180, 40))
        self.label_select_clients_name1.setMaximumSize(QSize(180, 40))
        self.label_select_clients_name1.setStyleSheet(u"QLabel {\n"
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
        self.label_select_clients_name1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_select_clients_name1)

        self.label_select_tq_account = QLabel(self.upper_left_3)
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

        self.verticalLayout_32.addWidget(self.label_select_tq_account)

        self.label_select_strategy = QLabel(self.upper_left_3)
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

        self.verticalLayout_32.addWidget(self.label_select_strategy)

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

        self.label_exchange = QLabel(self.upper_left_3)
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

        self.verticalLayout_32.addWidget(self.label_exchange)

        self.label_5 = QLabel(self.upper_left_3)
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

        self.verticalLayout_32.addWidget(self.label_5)


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
        self.comboBox_select_clients_name = QComboBox(self.upper_right_3)
        self.comboBox_select_clients_name.setObjectName(u"comboBox_select_clients_name")
        self.comboBox_select_clients_name.setMinimumSize(QSize(200, 40))
        self.comboBox_select_clients_name.setMaximumSize(QSize(200, 16777215))
        self.comboBox_select_clients_name.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
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
"    color: rgb(0, 0, 0);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(255, 255, 240);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
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
"QComboBox Q"
                        "AbstractItemView::item:selected{\n"
"	color: rgb(0, 0, 0);\n"
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
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3"
                        "\u4e0a\uff09 */\n"
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
""
                        " QScrollBar::handle:vertical {	\n"
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
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical "
                        "{\n"
"     background: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")

        self.verticalLayout_33.addWidget(self.comboBox_select_clients_name)

        self.comboBox_select_tq_account = QComboBox(self.upper_right_3)
        self.comboBox_select_tq_account.setObjectName(u"comboBox_select_tq_account")
        self.comboBox_select_tq_account.setMinimumSize(QSize(200, 40))
        self.comboBox_select_tq_account.setMaximumSize(QSize(200, 16777215))
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
"    color: rgb(0, 0, 0);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(255, 255, 240);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
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
"QComboBox Q"
                        "AbstractItemView::item:selected{\n"
"	color: rgb(0, 0, 0);\n"
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
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3"
                        "\u4e0a\uff09 */\n"
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
""
                        " QScrollBar::handle:vertical {	\n"
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
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical "
                        "{\n"
"     background: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")

        self.verticalLayout_33.addWidget(self.comboBox_select_tq_account)

        self.comboBox_select_strategy = QComboBox(self.upper_right_3)
        self.comboBox_select_strategy.setObjectName(u"comboBox_select_strategy")
        self.comboBox_select_strategy.setMinimumSize(QSize(200, 40))
        self.comboBox_select_strategy.setMaximumSize(QSize(200, 16777215))
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
"    color: rgb(0, 0, 0);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(255, 255, 240);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
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
"QComboBox Q"
                        "AbstractItemView::item:selected{\n"
"	color: rgb(0, 0, 0);\n"
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
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3"
                        "\u4e0a\uff09 */\n"
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
""
                        " QScrollBar::handle:vertical {	\n"
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
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical "
                        "{\n"
"     background: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")

        self.verticalLayout_33.addWidget(self.comboBox_select_strategy)

        self.checkBox_whether_self_start = QCheckBox(self.upper_right_3)
        self.checkBox_whether_self_start.setObjectName(u"checkBox_whether_self_start")
        self.checkBox_whether_self_start.setMinimumSize(QSize(200, 40))
        self.checkBox_whether_self_start.setMaximumSize(QSize(200, 40))
        self.checkBox_whether_self_start.setStyleSheet(u"QCheckBox{	\n"
"	color: rgb(255, 0, 127);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border:2px solid rgb(45, 45, 45);\n"
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
"	border:2px solid rgb(45, 45, 45);\n"
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

        self.checkBox_whether_open_web_services = QCheckBox(self.upper_right_3)
        self.checkBox_whether_open_web_services.setObjectName(u"checkBox_whether_open_web_services")
        self.checkBox_whether_open_web_services.setMinimumSize(QSize(200, 40))
        self.checkBox_whether_open_web_services.setMaximumSize(QSize(200, 40))
        self.checkBox_whether_open_web_services.setStyleSheet(u"QCheckBox{	\n"
"	color: rgb(255, 0, 127);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border:2px solid rgb(45, 45, 45);\n"
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

        self.comboBox_exchange = QComboBox(self.upper_right_3)
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
"    color: rgb(0, 0, 0);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(255, 255, 240);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
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
"QComboBox Q"
                        "AbstractItemView::item:selected{\n"
"	color: rgb(0, 0, 0);\n"
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
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3"
                        "\u4e0a\uff09 */\n"
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
""
                        " QScrollBar::handle:vertical {	\n"
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
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical "
                        "{\n"
"     background: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.comboBox_exchange.setFrame(True)
        self.comboBox_exchange.setModelColumn(0)

        self.verticalLayout_33.addWidget(self.comboBox_exchange)

        self.comboBox_contract_type = QComboBox(self.upper_right_3)
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
"    color: rgb(0, 0, 0);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(255, 255, 240);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
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
"QComboBox Q"
                        "AbstractItemView::item:selected{\n"
"	color: rgb(0, 0, 0);\n"
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
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3"
                        "\u4e0a\uff09 */\n"
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
""
                        " QScrollBar::handle:vertical {	\n"
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
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical "
                        "{\n"
"     background: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")

        self.verticalLayout_33.addWidget(self.comboBox_contract_type)


        self.horizontalLayout_26.addWidget(self.upper_right_3, 0, Qt.AlignHCenter)


        self.verticalLayout_38.addWidget(self.frame_58)

        self.frame_24 = QFrame(self.frame_56)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 70))
        self.frame_24.setMaximumSize(QSize(16777215, 100))
        self.frame_24.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	border-radius: 20px;\n"
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
        self.frame_36.setMaximumSize(QSize(450, 16777215))
        self.frame_36.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
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
        self.frame_16.setStyleSheet(u"font: 700 20pt \"\u7b49\u7ebf\";\n"
"color: rgb(0, 255, 0);\n"
"border: none;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_20.addWidget(self.frame_16)

        self.frame_23 = QFrame(self.frame_36)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(248, 248, 219);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
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
        self.label_symbol = QLabel(self.upper_left_5)
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

        self.verticalLayout_52.addWidget(self.label_symbol)

        self.label_symbol_period = QLabel(self.upper_left_5)
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

        self.verticalLayout_52.addWidget(self.label_symbol_period)

        self.label_initial_capital = QLabel(self.upper_left_5)
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

        self.verticalLayout_52.addWidget(self.label_initial_capital)

        self.label_orientation = QLabel(self.upper_left_5)
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

        self.verticalLayout_52.addWidget(self.label_orientation)

        self.label_trading_status = QLabel(self.upper_left_5)
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

        self.verticalLayout_52.addWidget(self.label_trading_status)

        self.label_contract_multiples = QLabel(self.upper_left_5)
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

        self.verticalLayout_52.addWidget(self.label_contract_multiples)

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
        self.comboBox_symbol = QComboBox(self.upper_right_5)
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
"    color: rgb(0, 0, 0);\n"
"	border-radius: 0px;\n"
"    background-color: rgb(255, 255, 240);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
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
"QComboBox Q"
                        "AbstractItemView::item:selected{\n"
"	border: none;\n"
"	color: rgb(0, 0, 0);\n"
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
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3"
                        "\u4e0a\uff09 */\n"
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
""
                        " QScrollBar::handle:vertical {	\n"
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
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical "
                        "{\n"
"     background: transparent;\n"
" }\n"
"QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed\n"
"{	\n"
"	background-color: transparent;\n"
"}\n"
"")
        self.comboBox_symbol.setEditable(True)
        self.comboBox_symbol.setMaxVisibleItems(20)

        self.verticalLayout_41.addWidget(self.comboBox_symbol)

        self.symbol_period = QLineEdit(self.upper_right_5)
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

        self.verticalLayout_41.addWidget(self.symbol_period)

        self.initial_capital = QLineEdit(self.upper_right_5)
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

        self.verticalLayout_41.addWidget(self.initial_capital)

        self.orientation = QLineEdit(self.upper_right_5)
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

        self.verticalLayout_41.addWidget(self.orientation)

        self.checkBox_trading_status = QCheckBox(self.upper_right_5)
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
        self.checkBox_trading_status.setChecked(True)

        self.verticalLayout_41.addWidget(self.checkBox_trading_status)

        self.contract_multiples = QLineEdit(self.upper_right_5)
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

        self.verticalLayout_41.addWidget(self.contract_multiples)

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


        self.horizontalLayout_5.addWidget(self.upper_right_5)


        self.verticalLayout_20.addWidget(self.frame_23)

        self.frame_59 = QFrame(self.frame_36)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(0, 70))
        self.frame_59.setMaximumSize(QSize(16777215, 100))
        self.frame_59.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
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
        self.frame_37.setMaximumSize(QSize(450, 16777215))
        self.frame_37.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
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
"	background-color: rgb(248, 248, 219);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
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

        self.label_Customized_parameters = QLabel(self.upper_left_6)
        self.label_Customized_parameters.setObjectName(u"label_Customized_parameters")
        self.label_Customized_parameters.setMinimumSize(QSize(180, 40))
        self.label_Customized_parameters.setMaximumSize(QSize(180, 40))
        self.label_Customized_parameters.setStyleSheet(u"QLabel {\n"
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
        self.label_Customized_parameters.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_Customized_parameters)

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
"	background-color: rgb(240, 240, 240);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
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
        self.frame_40.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Btn_add_process_param = QPushButton(self.frame_40)
        self.Btn_add_process_param.setObjectName(u"Btn_add_process_param")
        self.Btn_add_process_param.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Btn_add_process_param.sizePolicy().hasHeightForWidth())
        self.Btn_add_process_param.setSizePolicy(sizePolicy2)
        self.Btn_add_process_param.setMinimumSize(QSize(180, 40))
        self.Btn_add_process_param.setMaximumSize(QSize(180, 40))
        self.Btn_add_process_param.setStyleSheet(u"QPushButton{	\n"
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
        self.Btn_add_process_param.setIconSize(QSize(20, 20))
        self.Btn_add_process_param.setCheckable(True)
        self.Btn_add_process_param.setChecked(False)

        self.horizontalLayout_21.addWidget(self.Btn_add_process_param, 0, Qt.AlignVCenter)


        self.horizontalLayout_32.addWidget(self.frame_40)

        self.frame_46 = QFrame(self.frame_60)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.Btn_clear_input_process_param = QPushButton(self.frame_46)
        self.Btn_clear_input_process_param.setObjectName(u"Btn_clear_input_process_param")
        self.Btn_clear_input_process_param.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Btn_clear_input_process_param.sizePolicy().hasHeightForWidth())
        self.Btn_clear_input_process_param.setSizePolicy(sizePolicy3)
        self.Btn_clear_input_process_param.setMinimumSize(QSize(180, 40))
        self.Btn_clear_input_process_param.setMaximumSize(QSize(180, 40))
        self.Btn_clear_input_process_param.setStyleSheet(u"QPushButton{	\n"
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
        self.Btn_clear_input_process_param.setIconSize(QSize(19, 20))

        self.horizontalLayout_33.addWidget(self.Btn_clear_input_process_param, 0, Qt.AlignVCenter)


        self.horizontalLayout_32.addWidget(self.frame_46)


        self.verticalLayout_21.addWidget(self.frame_60)


        self.horizontalLayout.addWidget(self.frame_37)


        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout_3.addWidget(self.frame_3)

#if QT_CONFIG(shortcut)
        self.label_select_clients_name1.setBuddy(self.comboBox_select_clients_name)
        self.label_select_tq_account.setBuddy(self.comboBox_select_tq_account)
        self.label_select_strategy.setBuddy(self.comboBox_select_strategy)
        self.label_whether_self_start.setBuddy(self.checkBox_whether_self_start)
        self.label_whether_live_futures_trading.setBuddy(self.checkBox_whether_live_futures_trading)
        self.label_whether_open_web_services.setBuddy(self.checkBox_whether_open_web_services)
        self.label_web_port.setBuddy(self.web_port)
        self.label_exchange.setBuddy(self.comboBox_exchange)
        self.label_symbol_period.setBuddy(self.symbol_period)
        self.label_initial_capital.setBuddy(self.initial_capital)
        self.label_orientation.setBuddy(self.orientation)
        self.label_contract_multiples.setBuddy(self.contract_multiples)
        self.label_margin_rate.setBuddy(self.margin_rate)
        self.label_stop_loss.setBuddy(self.stop_loss)
        self.label_stop_profit.setBuddy(self.stop_profit)
        self.label_Customized_parameters2.setBuddy(self.symbol_period)
        self.label_Customized_parameters3.setBuddy(self.initial_capital)
        self.label_Customized_parameters4.setBuddy(self.orientation)
        self.label_Customized_parameters5.setBuddy(self.contract_multiples)
        self.label_Customized_parameters6.setBuddy(self.margin_rate)
        self.label_Customized_parameters7.setBuddy(self.stop_loss)
        self.label_Customized_parameters.setBuddy(self.stop_profit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.comboBox_select_clients_name, self.comboBox_select_tq_account)
        QWidget.setTabOrder(self.comboBox_select_tq_account, self.comboBox_select_strategy)
        QWidget.setTabOrder(self.comboBox_select_strategy, self.checkBox_whether_self_start)
        QWidget.setTabOrder(self.checkBox_whether_self_start, self.checkBox_whether_live_futures_trading)
        QWidget.setTabOrder(self.checkBox_whether_live_futures_trading, self.checkBox_whether_open_web_services)
        QWidget.setTabOrder(self.checkBox_whether_open_web_services, self.web_port)
        QWidget.setTabOrder(self.web_port, self.comboBox_exchange)
        QWidget.setTabOrder(self.comboBox_exchange, self.symbol_period)
        QWidget.setTabOrder(self.symbol_period, self.initial_capital)
        QWidget.setTabOrder(self.initial_capital, self.orientation)
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
        QWidget.setTabOrder(self.Customized_parameters8, self.Btn_add_process_param)
        QWidget.setTabOrder(self.Btn_add_process_param, self.Btn_clear_input_process_param)
        QWidget.setTabOrder(self.Btn_clear_input_process_param, self.Btn_close_window)

        self.retranslateUi(Form)
        self.Btn_close_window.clicked.connect(Form.close)
        self.checkBox_whether_open_web_services.toggled.connect(self.web_port.setEnabled)
        self.Btn_min_window.clicked.connect(Form.showMinimized)

        self.comboBox_contract_type.setCurrentIndex(-1)
        self.comboBox_symbol.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_tital_6.setText(QCoreApplication.translate("Form", u"\u521b\u5efa\u65b0\u7684\u7b56\u7565\u5b9e\u4f8b\u8fdb\u7a0b", None))
        self.label_info.setText("")
        self.Btn_min_window.setText("")
        self.Btn_close_window.setText("")
        self.label_tital_4.setText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u7b56\u7565\u5b9e\u4f8b\u8fdb\u7a0b\u8fd0\u884c\u6240\u9700\u8981\u7684\u53c2\u6570", None))
        self.label_select_clients_name1.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u7528\u6237 ", None))
        self.label_select_tq_account.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u5929\u52e4\u8d26\u6237", None))
        self.label_select_strategy.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u7b56\u7565", None))
        self.label_whether_self_start.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u4e3a\u81ea\u542f\u8fdb\u7a0b", None))
        self.label_whether_live_futures_trading.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u4e3a\u5b9e\u76d8", None))
        self.label_whether_open_web_services.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u5f00\u542fweb", None))
        self.label_web_port.setText(QCoreApplication.translate("Form", u"web\u7aef\u53e3\u53f7", None))
        self.label_exchange.setText(QCoreApplication.translate("Form", u"\u4ea4\u6613\u6240", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5408\u7ea6\u7c7b\u578b", None))
        self.checkBox_whether_self_start.setText(QCoreApplication.translate("Form", u"\u52fe\u9009\u4e3a\u81ea\u542f", None))
        self.checkBox_whether_live_futures_trading.setText(QCoreApplication.translate("Form", u"\u52fe\u9009\u4e3a\u5b9e\u76d8", None))
        self.checkBox_whether_open_web_services.setText(QCoreApplication.translate("Form", u"\u52fe\u9009\u5f00\u542fweb", None))
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

        self.label_symbol.setText(QCoreApplication.translate("Form", u"\u5408\u7ea6\u540d", None))
        self.label_symbol_period.setText(QCoreApplication.translate("Form", u"\u5408\u7ea6\u5468\u671f(\u5206\u949f)", None))
        self.label_initial_capital.setText(QCoreApplication.translate("Form", u"\u7b56\u7565\u521d\u59cb\u8d44\u91d1", None))
        self.label_orientation.setText(QCoreApplication.translate("Form", u"\u4ea4\u6613\u65b9\u5411", None))
        self.label_trading_status.setText(QCoreApplication.translate("Form", u"\u4ea4\u6613\u72b6\u6001", None))
        self.label_contract_multiples.setText(QCoreApplication.translate("Form", u"\u5408\u7ea6\u500d\u6570", None))
        self.label_margin_rate.setText(QCoreApplication.translate("Form", u"\u4fdd\u8bc1\u91d1\u7387\uff08%\uff09", None))
        self.label_stop_loss.setText(QCoreApplication.translate("Form", u"\u6b62\u635f\u4f4d\uff08%\uff09", None))
        self.label_stop_profit.setText(QCoreApplication.translate("Form", u"\u6b62\u76c8\u4f4d\uff08%\uff09", None))
        self.checkBox_trading_status.setText(QCoreApplication.translate("Form", u"\u52fe\u9009\u6b63\u5e38\u4ea4\u6613", None))
        self.contract_multiples.setText("")
        self.margin_rate.setText("")
        self.label_Customized_parameters1.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65701", None))
        self.label_Customized_parameters2.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65702", None))
        self.label_Customized_parameters3.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65703", None))
        self.label_Customized_parameters4.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65704", None))
        self.label_Customized_parameters5.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65705", None))
        self.label_Customized_parameters6.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65706", None))
        self.label_Customized_parameters7.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65707", None))
        self.label_Customized_parameters.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65708", None))
        self.label_Customized_parameters9.setText(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u53c2\u65709", None))
        self.Customized_parameters5.setText("")
        self.Customized_parameters6.setText("")
        self.Btn_add_process_param.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a\u6dfb\u52a0", None))
        self.Btn_clear_input_process_param.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u8f93\u5165", None))
    # retranslateUi

