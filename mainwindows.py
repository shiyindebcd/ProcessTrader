# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindows.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QCheckBox,
    QComboBox, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListView,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QToolBox, QTreeView, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1350, 900)
        MainWindow.setMinimumSize(QSize(1350, 900))
        MainWindow.setMaximumSize(QSize(1920, 1000))
        MainWindow.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
"border-radius:20px;\n"
"border: 1px solid rgb(170, 0, 255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_32 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_32.setSpacing(5)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(5, 5, 5, 5)
        self.frame_38 = QFrame(self.centralwidget)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(40, 0))
        self.frame_38.setMaximumSize(QSize(40, 16777215))
        self.frame_38.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 60);\n"
"	border:none;\n"
"	border-radius: 15px;\n"
"}")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_38)
        self.verticalLayout_40.setSpacing(5)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 5, 0, -1)
        self.Btn_switch_left_panel = QPushButton(self.frame_38)
        self.Btn_switch_left_panel.setObjectName(u"Btn_switch_left_panel")
        self.Btn_switch_left_panel.setMinimumSize(QSize(40, 40))
        self.Btn_switch_left_panel.setMaximumSize(QSize(40, 40))
        self.Btn_switch_left_panel.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 0, 255);\n"
"	border: 2px solid rgb(65, 51, 156);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(20, 9, 70);\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 18, 100);\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(21, 21, 21)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/\u56fe\u6807/icons/\u83dc\u5355.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_switch_left_panel.setIcon(icon)
        self.Btn_switch_left_panel.setIconSize(QSize(30, 30))

        self.verticalLayout_40.addWidget(self.Btn_switch_left_panel, 0, Qt.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_40.addItem(self.verticalSpacer_5)

        self.Btn_homepage = QPushButton(self.frame_38)
        self.Btn_homepage.setObjectName(u"Btn_homepage")
        self.Btn_homepage.setMinimumSize(QSize(30, 90))
        self.Btn_homepage.setMaximumSize(QSize(30, 120))
        self.Btn_homepage.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 255, 255), stop:0.284091 rgba(255, 0, 255, 255), stop:0.727273 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	border-color: none;\n"
"	}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: green;\n"
"	border-color: rgb(255, 0, 0);    \n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.0284091 rgba(255, 0, 0, 255), stop:0.375 rgba(255, 0, 127, 255), stop:0.642045 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 255, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"	color: rgb(31, 31, 31);\n"
"    background-color: rgb(152, 152, 152);\n"
"}")

        self.verticalLayout_40.addWidget(self.Btn_homepage, 0, Qt.AlignHCenter)

        self.Btn_account_manage = QPushButton(self.frame_38)
        self.Btn_account_manage.setObjectName(u"Btn_account_manage")
        self.Btn_account_manage.setMinimumSize(QSize(30, 90))
        self.Btn_account_manage.setMaximumSize(QSize(30, 120))
        self.Btn_account_manage.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.142045 rgba(255, 0, 0, 255), stop:0.698864 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 0, 255));\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	border-color: none;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: green;\n"
"	border-color: rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 0, 255), stop:0.301136 rgba(255, 255, 0, 255), stop:0.698864 rgba(255, 0, 0, 255), stop:0.988636 rgba(255, 0, 0, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"	color: rgb(31, 31, 31);\n"
"    background-color: rgb(152, 152, 152);\n"
"}")

        self.verticalLayout_40.addWidget(self.Btn_account_manage, 0, Qt.AlignHCenter)

        self.Btn_trading_log = QPushButton(self.frame_38)
        self.Btn_trading_log.setObjectName(u"Btn_trading_log")
        self.Btn_trading_log.setMinimumSize(QSize(30, 90))
        self.Btn_trading_log.setMaximumSize(QSize(30, 120))
        self.Btn_trading_log.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 0, 255), stop:0.454545 rgba(255, 255, 0, 255), stop:0.795455 rgba(0, 255, 0, 255), stop:1 rgba(0, 255, 0, 255));\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	border-color: none;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: green;\n"
"	border-color: rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 255, 0, 255), stop:0.255682 rgba(0, 255, 0, 255), stop:0.585227 rgba(255, 255, 0, 255), stop:0.988636 rgba(255, 255, 0, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"	color: rgb(31, 31, 31);\n"
"    background-color: rgb(152, 152, 152);\n"
"}")

        self.verticalLayout_40.addWidget(self.Btn_trading_log, 0, Qt.AlignHCenter)

        self.Btn_chart_details = QPushButton(self.frame_38)
        self.Btn_chart_details.setObjectName(u"Btn_chart_details")
        self.Btn_chart_details.setMinimumSize(QSize(30, 90))
        self.Btn_chart_details.setMaximumSize(QSize(30, 120))
        self.Btn_chart_details.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 255, 0, 255), stop:0.193182 rgba(0, 255, 0, 255), stop:0.613636 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 255, 255));\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	border-color: none;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: green;\n"
"	border-color: rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 255, 255, 255), stop:0.380682 rgba(0, 255, 255, 255), stop:0.795455 rgba(0, 255, 0, 255), stop:0.982955 rgba(0, 255, 0, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"	color: rgb(31, 31, 31);\n"
"    background-color: rgb(152, 152, 152);\n"
"}")

        self.verticalLayout_40.addWidget(self.Btn_chart_details, 0, Qt.AlignHCenter)

        self.Btn_strategy_backtest = QPushButton(self.frame_38)
        self.Btn_strategy_backtest.setObjectName(u"Btn_strategy_backtest")
        self.Btn_strategy_backtest.setMinimumSize(QSize(30, 90))
        self.Btn_strategy_backtest.setMaximumSize(QSize(30, 120))
        self.Btn_strategy_backtest.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 255, 255, 255), stop:0.335227 rgba(0, 255, 255, 255), stop:0.778409 rgba(0, 0, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	border-color: none;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(255, 85, 0); \n"
"}\n"
"QPushButton:pressed{\n"
"	color: green;\n"
"	border-color: rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.261364 rgba(0, 0, 255, 255), stop:0.664773 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 255, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"	color: rgb(31, 31, 31);\n"
"    background-color: rgb(152, 152, 152);\n"
"}")

        self.verticalLayout_40.addWidget(self.Btn_strategy_backtest, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_40.addItem(self.verticalSpacer_2)

        self.Btn_previous_page = QPushButton(self.frame_38)
        self.Btn_previous_page.setObjectName(u"Btn_previous_page")
        self.Btn_previous_page.setMinimumSize(QSize(30, 80))
        self.Btn_previous_page.setMaximumSize(QSize(30, 16777215))
        self.Btn_previous_page.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.193182 rgba(0, 0, 255, 255), stop:0.653409 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 255, 255));\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	border-color: none;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: green;\n"
"	border-color: rgb(255, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 255, 255), stop:0.340909 rgba(255, 0, 255, 255), stop:0.778409 rgba(20, 20, 255, 255), stop:1 rgba(0, 0, 255, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"	color: rgb(31, 31, 31);\n"
"    background-color: rgb(152, 152, 152);\n"
"}")

        self.verticalLayout_40.addWidget(self.Btn_previous_page, 0, Qt.AlignHCenter)

        self.Btn_next_page = QPushButton(self.frame_38)
        self.Btn_next_page.setObjectName(u"Btn_next_page")
        self.Btn_next_page.setMinimumSize(QSize(30, 80))
        self.Btn_next_page.setMaximumSize(QSize(30, 16777215))
        self.Btn_next_page.setStyleSheet(u"QPushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 255, 255), stop:0.318182 rgba(255, 0, 255, 255), stop:0.619318 rgba(255, 0, 127, 255), stop:1 rgba(255, 0, 0, 255));\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	border-color: none;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"	color: green;\n"
"	border-color: rgb(255, 0, 0);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.0284091 rgba(255, 0, 0, 255), stop:0.375 rgba(255, 0, 127, 255), stop:0.642045 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 255, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"	color: rgb(31, 31, 31);\n"
"    background-color: rgb(152, 152, 152);\n"
"}")

        self.verticalLayout_40.addWidget(self.Btn_next_page, 0, Qt.AlignHCenter)


        self.horizontalLayout_32.addWidget(self.frame_38, 0, Qt.AlignHCenter)

        self.frame_55 = QFrame(self.centralwidget)
        self.frame_55.setObjectName(u"frame_55")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_55.sizePolicy().hasHeightForWidth())
        self.frame_55.setSizePolicy(sizePolicy)
        self.frame_55.setMinimumSize(QSize(300, 0))
        self.frame_55.setStyleSheet(u"border: none;")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_55)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Headerframe = QFrame(self.frame_55)
        self.Headerframe.setObjectName(u"Headerframe")
        self.Headerframe.setMinimumSize(QSize(0, 50))
        self.Headerframe.setMaximumSize(QSize(16777215, 50))
        self.Headerframe.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.Headerframe.setFrameShape(QFrame.StyledPanel)
        self.Headerframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Headerframe)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, 0, 10, 0)
        self.horizontalSpacer_10 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)

        self.frame_68 = QFrame(self.Headerframe)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(120, 0))
        self.frame_68.setMaximumSize(QSize(120, 50))
        self.frame_68.setContextMenuPolicy(Qt.CustomContextMenu)
        self.frame_68.setStyleSheet(u"")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_logo = QLabel(self.frame_68)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setScaledContents(True)

        self.horizontalLayout_39.addWidget(self.label_logo)


        self.horizontalLayout_7.addWidget(self.frame_68)

        self.horizontalSpacer_2 = QSpacerItem(130, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.label_tital = QLabel(self.Headerframe)
        self.label_tital.setObjectName(u"label_tital")
        self.label_tital.setStyleSheet(u"font: 700 22pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 0);\n"
"border: none;")

        self.horizontalLayout_7.addWidget(self.label_tital)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.Btn_setting = QPushButton(self.Headerframe)
        self.Btn_setting.setObjectName(u"Btn_setting")
        self.Btn_setting.setMinimumSize(QSize(80, 30))
        self.Btn_setting.setMaximumSize(QSize(80, 30))
        self.Btn_setting.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(40, 40, 70, 80);\n"
"	color: rgb(255, 85, 0);	\n"
"	\n"
"	font: 700 10pt \"\u7b49\u7ebf\";\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/\u56fe\u6807/icons/\u8bbe\u7f6e.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_setting.setIcon(icon1)
        self.Btn_setting.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.Btn_setting)

        self.Btn_donation = QPushButton(self.Headerframe)
        self.Btn_donation.setObjectName(u"Btn_donation")
        self.Btn_donation.setMinimumSize(QSize(100, 30))
        self.Btn_donation.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.Btn_donation.setFont(font)
        self.Btn_donation.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(40, 40, 70, 80);\n"
"	color: rgb(255, 85, 0);	\n"
"	\n"
"	font: 700 10pt \"\u7b49\u7ebf\";\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/\u56fe\u6807/icons/\u4f5c\u8005.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_donation.setIcon(icon2)
        self.Btn_donation.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.Btn_donation)

        self.Btn_warning = QPushButton(self.Headerframe)
        self.Btn_warning.setObjectName(u"Btn_warning")
        self.Btn_warning.setMinimumSize(QSize(80, 30))
        self.Btn_warning.setMaximumSize(QSize(80, 30))
        self.Btn_warning.setFont(font)
        self.Btn_warning.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(40, 40, 70, 80);\n"
"	color: rgb(255, 85, 0);	\n"
"	\n"
"	font: 700 10pt \"\u7b49\u7ebf\";\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/\u56fe\u6807/icons/\u8b66\u544a.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_warning.setIcon(icon3)
        self.Btn_warning.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.Btn_warning)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.Btn_min_window = QPushButton(self.Headerframe)
        self.Btn_min_window.setObjectName(u"Btn_min_window")
        self.Btn_min_window.setMinimumSize(QSize(40, 40))
        self.Btn_min_window.setMaximumSize(QSize(40, 40))
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
        icon4 = QIcon()
        icon4.addFile(u":/\u56fe\u6807/icons/\u6700\u5c0f\u5316.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_min_window.setIcon(icon4)
        self.Btn_min_window.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.Btn_min_window)

        self.Btn_normal_max_window = QPushButton(self.Headerframe)
        self.Btn_normal_max_window.setObjectName(u"Btn_normal_max_window")
        self.Btn_normal_max_window.setMinimumSize(QSize(40, 40))
        self.Btn_normal_max_window.setMaximumSize(QSize(40, 40))
        self.Btn_normal_max_window.setStyleSheet(u"QPushButton {\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/\u56fe\u6807/icons/\u6700\u5927\u5316-\u8fd8\u539f.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_normal_max_window.setIcon(icon5)
        self.Btn_normal_max_window.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.Btn_normal_max_window)

        self.Btn_close_window = QPushButton(self.Headerframe)
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
        icon6 = QIcon()
        icon6.addFile(u":/\u56fe\u6807/icons/\u5173\u95ed.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_close_window.setIcon(icon6)
        self.Btn_close_window.setIconSize(QSize(35, 35))

        self.horizontalLayout_7.addWidget(self.Btn_close_window)


        self.verticalLayout.addWidget(self.Headerframe)

        self.body = QFrame(self.frame_55)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"QFrame {\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 20px;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.body)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 5, 0, 0)
        self.left_panel = QFrame(self.body)
        self.left_panel.setObjectName(u"left_panel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_panel.sizePolicy().hasHeightForWidth())
        self.left_panel.setSizePolicy(sizePolicy1)
        self.left_panel.setMinimumSize(QSize(0, 0))
        self.left_panel.setMaximumSize(QSize(350, 16777215))
        self.left_panel.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 20px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"\n"
"")
        self.left_panel.setFrameShape(QFrame.StyledPanel)
        self.left_panel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.left_panel)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.left_panel)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"\n"
"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 20px;\n"
"	border: none;\n"
"}\n"
"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_18)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.Veiw_Box = QToolBox(self.frame_18)
        self.Veiw_Box.setObjectName(u"Veiw_Box")
        self.Veiw_Box.setStyleSheet(u"\n"
"QToolBox{\n"
"background-color: rgb(13, 9, 27);/*\u80cc\u666f\u8272-\u7a7a\u9699\u989c\u8272*/\n"
"border: none;\n"
"}\n"
"QToolBox>QAbstractButton{/*\u6807\u9898\u680f*/\n"
"	min-height:30px;\n"
"}\n"
"QToolBox::tab{\n"
"	font: 16pt \"\u7b49\u7ebf\";	\n"
"	color: rgb(200, 200, 200);	\n"
"	background-color: rgb(85, 0, 255);\n"
"	border-radius: 15px;\n"
"	border: none;\n"
"	padding:3px 3px 3px 10px;\n"
"}\n"
"QToolBox::tab:hover{\n"
"color:black;\n"
"background-color: rgb(255, 170, 0);\n"
"}\n"
"QToolBox::tab:selected{\n"
"font: 700 16pt \"\u7b49\u7ebf\";\n"
"color:rgb(255, 0, 127);\n"
"border: 2px solid rgb(255, 85, 0);\n"
"}\n"
"QToolBox::tab:selected:hover{\n"
"color:black;\n"
"}\n"
"")
        self.clients_list_page = QWidget()
        self.clients_list_page.setObjectName(u"clients_list_page")
        self.clients_list_page.setGeometry(QRect(0, 0, 83, 66))
        self.verticalLayout_13 = QVBoxLayout(self.clients_list_page)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.clients_listview = QListView(self.clients_list_page)
        self.clients_listview.setObjectName(u"clients_listview")
        font1 = QFont()
        font1.setFamilies([u"\u7b49\u7ebf"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.clients_listview.setFont(font1)
        self.clients_listview.setAutoFillBackground(False)
        self.clients_listview.setStyleSheet(u"QListView {	\n"
"	font:  16pt \"\u7b49\u7ebf\";\n"
"	color: rgb(170, 0, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	padding:5px;\n"
"}\n"
"QListView::item {\n"
"	min-height:35px;\n"
"     border-radius: 15px;\n"
"	padding-left: 20px;\n"
"	background-color: rgb(13, 9, 36);\n"
"}\n"
"\n"
"QListView::item:selected {   \n"
"	border: none;\n"
"	background-color: rgb(170, 0, 255);\n"
"}\n"
"\n"
"QListView::item:hover { \n"
"	background-color: rgb(0, 70, 0);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
"QScro"
                        "llBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	bor"
                        "der-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")
        self.clients_listview.setFrameShadow(QFrame.Sunken)
        self.clients_listview.setLineWidth(1)
        self.clients_listview.setBatchSize(200)

        self.verticalLayout_13.addWidget(self.clients_listview)

        self.Veiw_Box.addItem(self.clients_list_page, u"\u7528\u6237\u5217\u8868")
        self.tq_account_list_page = QWidget()
        self.tq_account_list_page.setObjectName(u"tq_account_list_page")
        self.tq_account_list_page.setGeometry(QRect(0, 0, 83, 66))
        self.verticalLayout_37 = QVBoxLayout(self.tq_account_list_page)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.tq_account_listview = QListView(self.tq_account_list_page)
        self.tq_account_listview.setObjectName(u"tq_account_listview")
        self.tq_account_listview.setStyleSheet(u"QListView {	\n"
"	font:  16pt \"\u7b49\u7ebf\";\n"
"	color: rgb(255, 85, 0);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	padding:5px;\n"
"}\n"
"QListView::item {\n"
"	min-height:35px;\n"
"     border-radius: 15px;\n"
"	padding-left: 20px;\n"
"	background-color: rgb(13, 9, 36);\n"
"}\n"
"\n"
"QListView::item:selected {   \n"
"	border: none;\n"
"	background-color: rgb(170, 0, 255);\n"
"}\n"
"\n"
"QListView::item:hover { \n"
"	background-color: rgb(0, 70, 0);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
"QScrol"
                        "lBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	bord"
                        "er-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")

        self.verticalLayout_37.addWidget(self.tq_account_listview)

        self.Veiw_Box.addItem(self.tq_account_list_page, u"\u5929\u52e4\u5e10\u6237\u5217\u8868")
        self.strategy_list_page = QWidget()
        self.strategy_list_page.setObjectName(u"strategy_list_page")
        self.strategy_list_page.setGeometry(QRect(0, 0, 83, 66))
        self.verticalLayout_16 = QVBoxLayout(self.strategy_list_page)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.strategy_listview = QListView(self.strategy_list_page)
        self.strategy_listview.setObjectName(u"strategy_listview")
        self.strategy_listview.setFont(font1)
        self.strategy_listview.setAutoFillBackground(False)
        self.strategy_listview.setStyleSheet(u"QListView {	\n"
"	font:  16pt \"\u7b49\u7ebf\";\n"
"	color: rgb(255, 255, 0);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	padding:5px;\n"
"}\n"
"QListView::item {\n"
"	min-height:35px;\n"
"     border-radius: 15px;\n"
"	padding-left: 20px;\n"
"	background-color: rgb(13, 9, 36);\n"
"}\n"
"\n"
"QListView::item:selected {   \n"
"	border: none;\n"
"	background-color: rgb(170, 0, 255);\n"
"}\n"
"\n"
"QListView::item:hover { \n"
"	background-color: rgb(0, 70, 0);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
"QScro"
                        "llBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	bor"
                        "der-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")
        self.strategy_listview.setFrameShadow(QFrame.Plain)
        self.strategy_listview.setBatchSize(200)

        self.verticalLayout_16.addWidget(self.strategy_listview)

        self.Veiw_Box.addItem(self.strategy_list_page, u"\u7b56\u7565\u5217\u8868")
        self.qoute_list_page = QWidget()
        self.qoute_list_page.setObjectName(u"qoute_list_page")
        self.qoute_list_page.setGeometry(QRect(0, 0, 83, 66))
        self.verticalLayout_15 = QVBoxLayout(self.qoute_list_page)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.qoute_listview = QListView(self.qoute_list_page)
        self.qoute_listview.setObjectName(u"qoute_listview")
        font2 = QFont()
        font2.setFamilies([u"\u7b49\u7ebf"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.qoute_listview.setFont(font2)
        self.qoute_listview.setAutoFillBackground(False)
        self.qoute_listview.setStyleSheet(u"QListView {	\n"
"	font:  12pt \"\u7b49\u7ebf\";\n"
"	color: rgb(0, 255, 0);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	padding:5px;\n"
"}\n"
"QListView::item {\n"
"	min-height:30px;\n"
"     border-radius: 15px;\n"
"	padding-left: 20px;\n"
"	background-color: rgb(13, 9, 36);\n"
"}\n"
"\n"
"QListView::item:selected {   \n"
"	border: none;\n"
"	background-color: rgb(170, 0, 255);\n"
"}\n"
"\n"
"QListView::item:hover { \n"
"	background-color: rgb(0, 70, 0);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
"QScroll"
                        "Bar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	borde"
                        "r-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")
        self.qoute_listview.setFrameShadow(QFrame.Plain)
        self.qoute_listview.setBatchSize(200)

        self.verticalLayout_15.addWidget(self.qoute_listview)

        self.Veiw_Box.addItem(self.qoute_list_page, u"\u8ba2\u9605\u884c\u60c5\u5217\u8868")
        self.process_list_page = QWidget()
        self.process_list_page.setObjectName(u"process_list_page")
        self.process_list_page.setGeometry(QRect(0, 0, 238, 443))
        self.verticalLayout_14 = QVBoxLayout(self.process_list_page)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.process_listview = QListView(self.process_list_page)
        self.process_listview.setObjectName(u"process_listview")
        self.process_listview.setFont(font2)
        self.process_listview.setAutoFillBackground(False)
        self.process_listview.setStyleSheet(u"QListView {	\n"
"	font:  12pt \"\u7b49\u7ebf\";\n"
"	color: rgb(255, 0, 127);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	padding:5px;\n"
"}\n"
"QListView::item {\n"
"	min-height:30px;\n"
"     border-radius: 15px;\n"
"	padding-left: 5px;\n"
"	background-color: rgb(13, 9, 36);\n"
"}\n"
"\n"
"QListView::item:selected {   \n"
"	border: none;\n"
"	background-color: rgb(170, 0, 255);\n"
"}\n"
"\n"
"QListView::item:hover { \n"
"	background-color: rgb(0, 70, 0);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
"QScrol"
                        "lBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	bord"
                        "er-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")
        self.process_listview.setFrameShadow(QFrame.Plain)
        self.process_listview.setBatchSize(200)

        self.verticalLayout_14.addWidget(self.process_listview)

        self.Veiw_Box.addItem(self.process_list_page, u"\u8fd0\u884c\u4e2d\u7684\u8fdb\u7a0b\u5217\u8868")

        self.verticalLayout_12.addWidget(self.Veiw_Box)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.Btn_kill_all_process = QPushButton(self.frame_18)
        self.Btn_kill_all_process.setObjectName(u"Btn_kill_all_process")
        self.Btn_kill_all_process.setMinimumSize(QSize(0, 40))
        self.Btn_kill_all_process.setMaximumSize(QSize(16777215, 40))
        self.Btn_kill_all_process.setStyleSheet(u"QPushButton{\n"
"	color: rgb(13, 9, 36);\n"
"	background-color:rgb(255, 0, 127);\n"
"	font: 700 16pt \"\u7b49\u7ebf\";\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(255, 85, 0); \n"
"}\n"
"QPushButton:pressed{\n"
"	color: green;\n"
"	border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.Btn_kill_all_process)


        self.verticalLayout_11.addWidget(self.frame_18)

        self.frame_28 = QFrame(self.left_panel)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 100))
        self.frame_28.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 20px;\n"
"	border: none;\n"
"}\n"
"\n"
"")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_28)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_28)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 30))
        self.frame_17.setStyleSheet(u"border: none;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, -1, -1, -1)
        self.Btn_start_all_stoped_strategy = QPushButton(self.frame_17)
        self.Btn_start_all_stoped_strategy.setObjectName(u"Btn_start_all_stoped_strategy")
        self.Btn_start_all_stoped_strategy.setMinimumSize(QSize(180, 40))
        self.Btn_start_all_stoped_strategy.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setFamilies([u"\u7b49\u7ebf"])
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setItalic(False)
        self.Btn_start_all_stoped_strategy.setFont(font3)
        self.Btn_start_all_stoped_strategy.setStyleSheet(u"QPushButton{\n"
"	color: rgb(13, 9, 36);\n"
"	background-color:rgb(0, 255, 0);\n"
"	font: 700 16pt \"\u7b49\u7ebf\";\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 2px solid rgb(255, 85, 0); \n"
"}\n"
"QPushButton:pressed{\n"
"	color: green;\n"
"	border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.Btn_start_all_stoped_strategy)


        self.verticalLayout_25.addWidget(self.frame_17)


        self.verticalLayout_11.addWidget(self.frame_28)


        self.horizontalLayout.addWidget(self.left_panel)

        self.Container = QFrame(self.body)
        self.Container.setObjectName(u"Container")
        self.Container.setStyleSheet(u"background-color: rgb(15, 8, 31);\n"
"border: none;")
        self.Container.setFrameShape(QFrame.StyledPanel)
        self.Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.Container)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border: none;")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.main_page.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border: none;")
        self.verticalLayout_3 = QVBoxLayout(self.main_page)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.main_page)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMinimumSize(QSize(1000, 0))
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy4)
        self.frame_10.setMaximumSize(QSize(16777215, 16777215))
        self.frame_10.setStyleSheet(u"QFrame {\n"
"	background-color:rgb(0, 0, 0);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 4)
        self.frame_15 = QFrame(self.frame_10)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 40))
        self.frame_15.setMaximumSize(QSize(16777215, 40))
        self.frame_15.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, 0, 20, 0)
        self.label_22 = QLabel(self.frame_15)
        self.label_22.setObjectName(u"label_22")
        font4 = QFont()
        font4.setFamilies([u"\u7b49\u7ebf"])
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_22.setFont(font4)
        self.label_22.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(30, 30, 40, 0);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	color: rgb(255, 0, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"}\n"
"")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_22, 0, Qt.AlignLeft)

        self.Btn_opne_in_excel1 = QPushButton(self.frame_15)
        self.Btn_opne_in_excel1.setObjectName(u"Btn_opne_in_excel1")
        self.Btn_opne_in_excel1.setMinimumSize(QSize(180, 30))
        self.Btn_opne_in_excel1.setMaximumSize(QSize(180, 30))
        font5 = QFont()
        font5.setFamilies([u"\u7b49\u7ebf"])
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setItalic(False)
        self.Btn_opne_in_excel1.setFont(font5)
        self.Btn_opne_in_excel1.setStyleSheet(u"QPushButton {\n"
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
        icon7 = QIcon()
        icon7.addFile(u":/\u56fe\u6807/icons/Excel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_opne_in_excel1.setIcon(icon7)
        self.Btn_opne_in_excel1.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.Btn_opne_in_excel1, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_6.addWidget(self.frame_15)

        self.frame_29 = QFrame(self.frame_10)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_29)
        self.verticalLayout_26.setSpacing(1)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(1, 1, 1, 1)
        self.frame_65 = QFrame(self.frame_29)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: none;\n"
"}")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_deal_detials = QTableWidget(self.frame_65)
        self.tableWidget_deal_detials.setObjectName(u"tableWidget_deal_detials")
        font6 = QFont()
        font6.setFamilies([u"\u7b49\u7ebf"])
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setItalic(False)
        self.tableWidget_deal_detials.setFont(font6)
        self.tableWidget_deal_detials.setStyleSheet(u"QTableWidget{\n"
"font: 11pt \"\u7b49\u7ebf\";\n"
"color:rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"/*alternate-background-color:rgb(35, 18, 90);/*\u4ea4\u9519\u989c\u8272*/\n"
"gridline-color:transparent;\n"
"border: none;\n"
"padding: 5px 5px 5px 5px;\n"
"}\n"
"QTableWidget:hover{\n"
"border: none;\n"
"}\n"
"QTableWidget::item {\n"
"background-color: rgb(13, 9, 37);\n"
"border: 1px solid rgba(140, 140, 140, 50);\n"
"border-radius: 13px;\n"
"}\n"
"/*\u9009\u4e2ditem*/\n"
"QTableWidget::item:selected{\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"color:rgb(0, 255, 0);\n"
"background:rgb(126, 0, 95);\n"
"border: none;\n"
"}\n"
"/*\n"
"\u60ac\u6d6eitem*/\n"
"QTableWidget::item:hover{\n"
"color:rgb(0, 255, 0);\n"
"background:rgb(100, 0, 80);\n"
"}\n"
"/*\u8868\u5934*/\n"
"QHeaderView::section:horizontal{\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background:rgb(140, 45, 0);\n"
"border-left-width:0;\n"
"border-top-width:0;\n"
"border-radius: 13px;\n"
"}\n"
""
                        "QHeaderView::section:hover:horizontal{\n"
"border: none;\n"
"}\n"
"QHeaderView::section:vertical{\n"
"border: none;\n"
"text-align:center;\n"
"background:rgb(13, 9, 37);\n"
"color: rgb(13, 9, 37);\n"
"}\n"
"/*\u8868\u5934\u6700\u5de6\u4e0a\u89d2\u7684\u65b9\u5757*/\n"
"QTableCornerButton:section{\n"
"border-left-width:0;\n"
"border-top-width:0;\n"
"border-bottom-width:0;\n"
"border-right-width:0;\n"
"text-align:center;\n"
"background:transparent;\n"
"margin:-5px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"QTableCornerButton::section:hover{\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"backgroun"
                        "d:rgb(150, 0, 150);\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);"
                        "\n"
"    min-height: 30px;\n"
"	border-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"")
        self.tableWidget_deal_detials.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableWidget_deal_detials.setDragEnabled(True)
        self.tableWidget_deal_detials.setDragDropMode(QAbstractItemView.DragOnly)
        self.tableWidget_deal_detials.setDefaultDropAction(Qt.MoveAction)
        self.tableWidget_deal_detials.horizontalHeader().setMinimumSectionSize(5)
        self.tableWidget_deal_detials.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_deal_detials.verticalHeader().setVisible(False)
        self.tableWidget_deal_detials.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_deal_detials.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_deal_detials.verticalHeader().setProperty("showSortIndicator", True)

        self.horizontalLayout_37.addWidget(self.tableWidget_deal_detials)


        self.verticalLayout_26.addWidget(self.frame_65)


        self.verticalLayout_6.addWidget(self.frame_29)


        self.horizontalLayout_3.addWidget(self.frame_10)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(356, 390))
        self.frame_4.setMaximumSize(QSize(356, 16777215))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 20px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(2, 0, 0, 5)
        self.frame_53 = QFrame(self.frame_4)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_53)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(10, 0, 5, 0)
        self.frame_6 = QFrame(self.frame_53)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(160, 120))
        self.frame_6.setMaximumSize(QSize(160, 120))
        self.frame_6.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 40))
        self.label_4.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(0, 255, 0);\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_4)

        self.label_runing_process_quantity = QLabel(self.frame_6)
        self.label_runing_process_quantity.setObjectName(u"label_runing_process_quantity")
        self.label_runing_process_quantity.setMinimumSize(QSize(140, 50))
        self.label_runing_process_quantity.setMaximumSize(QSize(140, 50))
        self.label_runing_process_quantity.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 14pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")
        self.label_runing_process_quantity.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_runing_process_quantity)


        self.verticalLayout_21.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_53)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(160, 120))
        self.frame_8.setMaximumSize(QSize(160, 120))
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
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(120, 40))
        self.label_10.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(0, 255, 0);\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_10)

        self.label_total_profit = QLabel(self.frame_8)
        self.label_total_profit.setObjectName(u"label_total_profit")
        self.label_total_profit.setMinimumSize(QSize(140, 50))
        self.label_total_profit.setMaximumSize(QSize(140, 50))
        self.label_total_profit.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 14pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")
        self.label_total_profit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_total_profit)


        self.verticalLayout_21.addWidget(self.frame_8)

        self.frame_27 = QFrame(self.frame_53)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(160, 120))
        self.frame_27.setMaximumSize(QSize(160, 120))
        self.frame_27.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_27)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(9, 9, 9, 9)
        self.label_12 = QLabel(self.frame_27)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(120, 40))
        self.label_12.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(0, 255, 0);\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_12)

        self.label_process_reboot_quantity = QLabel(self.frame_27)
        self.label_process_reboot_quantity.setObjectName(u"label_process_reboot_quantity")
        self.label_process_reboot_quantity.setMinimumSize(QSize(140, 50))
        self.label_process_reboot_quantity.setMaximumSize(QSize(200, 50))
        self.label_process_reboot_quantity.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 14pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")
        self.label_process_reboot_quantity.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_process_reboot_quantity)


        self.verticalLayout_21.addWidget(self.frame_27)


        self.horizontalLayout_28.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.frame_4)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_54)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(5, 0, 5, 0)
        self.frame_7 = QFrame(self.frame_54)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(160, 120))
        self.frame_7.setMaximumSize(QSize(160, 120))
        self.frame_7.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(120, 40))
        self.label_7.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(0, 255, 0);\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_7)

        self.label_tq_account_quantity = QLabel(self.frame_7)
        self.label_tq_account_quantity.setObjectName(u"label_tq_account_quantity")
        self.label_tq_account_quantity.setMinimumSize(QSize(140, 50))
        self.label_tq_account_quantity.setMaximumSize(QSize(140, 50))
        self.label_tq_account_quantity.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 14pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")
        self.label_tq_account_quantity.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_tq_account_quantity)


        self.verticalLayout_35.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.frame_54)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(160, 120))
        self.frame_9.setMaximumSize(QSize(160, 120))
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
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_26 = QLabel(self.frame_9)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(120, 40))
        self.label_26.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(0, 255, 0);\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_26)

        self.label_cpu_occupancy = QLabel(self.frame_9)
        self.label_cpu_occupancy.setObjectName(u"label_cpu_occupancy")
        self.label_cpu_occupancy.setMinimumSize(QSize(140, 50))
        self.label_cpu_occupancy.setMaximumSize(QSize(140, 50))
        self.label_cpu_occupancy.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 14pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")
        self.label_cpu_occupancy.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_cpu_occupancy)


        self.verticalLayout_35.addWidget(self.frame_9)

        self.frame_26 = QFrame(self.frame_54)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(160, 120))
        self.frame_26.setMaximumSize(QSize(160, 120))
        self.frame_26.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_26)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_6 = QLabel(self.frame_26)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(120, 40))
        self.label_6.setStyleSheet(u"background-color: rgbA(0, 0, 0, 0);\n"
"color: rgb(0, 255, 0);\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_6)

        self.label_frame_runing_time = QLabel(self.frame_26)
        self.label_frame_runing_time.setObjectName(u"label_frame_runing_time")
        sizePolicy3.setHeightForWidth(self.label_frame_runing_time.sizePolicy().hasHeightForWidth())
        self.label_frame_runing_time.setSizePolicy(sizePolicy3)
        self.label_frame_runing_time.setMinimumSize(QSize(140, 50))
        self.label_frame_runing_time.setMaximumSize(QSize(200, 80))
        self.label_frame_runing_time.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 700 14pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")
        self.label_frame_runing_time.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_frame_runing_time)


        self.verticalLayout_35.addWidget(self.frame_26)


        self.horizontalLayout_28.addWidget(self.frame_54)


        self.horizontalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_4.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(1000, 0))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setMidLineWidth(-1)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setSpacing(2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 5, 0, 0)
        self.frame_19 = QFrame(self.frame_2)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy1.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy1)
        self.frame_19.setMinimumSize(QSize(0, 0))
        self.frame_19.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_19)
        self.verticalLayout_17.setSpacing(8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 5, 0)
        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 40))
        self.frame_21.setMaximumSize(QSize(16777215, 40))
        self.frame_21.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(20, 0, 20, 0)
        self.label_23 = QLabel(self.frame_21)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 40))
        self.label_23.setMaximumSize(QSize(200, 16777215))
        self.label_23.setFont(font4)
        self.label_23.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(30, 30, 40, 0);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	color: rgb(255, 0, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"}\n"
"")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_23, 0, Qt.AlignLeft)

        self.pushButton_cleartext = QPushButton(self.frame_21)
        self.pushButton_cleartext.setObjectName(u"pushButton_cleartext")
        self.pushButton_cleartext.setMinimumSize(QSize(180, 30))
        self.pushButton_cleartext.setMaximumSize(QSize(180, 30))
        self.pushButton_cleartext.setFont(font5)
        self.pushButton_cleartext.setStyleSheet(u"QPushButton {\n"
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
        icon8 = QIcon()
        icon8.addFile(u":/\u56fe\u6807/icons/\u6e05\u5c4f.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_cleartext.setIcon(icon8)
        self.pushButton_cleartext.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.pushButton_cleartext)


        self.verticalLayout_17.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_terminal = QTextBrowser(self.frame_22)
        self.textBrowser_terminal.setObjectName(u"textBrowser_terminal")
        self.textBrowser_terminal.setStyleSheet(u"QTextBrowser{\n"
"background-color: rgba(170, 0, 120, 50);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"/*padding-left: 20px;\n"
"padding-right: 20px;*/\n"
"padding: 5px 5px 5px 20px;\n"
"border: none;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::s"
                        "ub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55"
                        ", 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")

        self.horizontalLayout_12.addWidget(self.textBrowser_terminal)


        self.verticalLayout_17.addWidget(self.frame_22)


        self.horizontalLayout_11.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_2)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy2.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy2)
        self.frame_20.setMinimumSize(QSize(350, 0))
        self.frame_20.setMaximumSize(QSize(350, 16777215))
        self.frame_20.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_20)
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 0, 7, 0)
        self.frame_11 = QFrame(self.frame_20)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(300, 40))
        self.frame_11.setMaximumSize(QSize(16777215, 40))
        self.frame_11.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 0, 0, 0)
        self.label_24 = QLabel(self.frame_11)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 40))
        self.label_24.setMaximumSize(QSize(150, 16777215))
        self.label_24.setFont(font4)
        self.label_24.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(30, 30, 40, 0);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	color: rgb(255, 0, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"}\n"
"")
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_24)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_20)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_12)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_12)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"	\n"
"	border: none;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"	border: none;\n"
"}")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.pieCard = QVBoxLayout()
        self.pieCard.setSpacing(6)
        self.pieCard.setObjectName(u"pieCard")
        self.pieCard.setSizeConstraint(QLayout.SetMaximumSize)

        self.horizontalLayout_16.addLayout(self.pieCard)


        self.verticalLayout_18.addWidget(self.frame_30)


        self.verticalLayout_5.addWidget(self.frame_12)


        self.horizontalLayout_11.addWidget(self.frame_20)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.frame)

        self.stackedWidget.addWidget(self.main_page)
        self.second_page = QWidget()
        self.second_page.setObjectName(u"second_page")
        self.second_page.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
"border: none;")
        self.horizontalLayout_9 = QHBoxLayout(self.second_page)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 5, 0)
        self.tabWidget_account = QTabWidget(self.second_page)
        self.tabWidget_account.setObjectName(u"tabWidget_account")
        self.tabWidget_account.setMinimumSize(QSize(0, 450))
        self.tabWidget_account.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_account.setAutoFillBackground(False)
        self.tabWidget_account.setStyleSheet(u"QTabWidget::pane{\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"		margin:3px;\n"
"		border-top-left-radius: 30px;\n"
"         border-top-right-radius: 30px;         \n"
" 		width:200px; \n"
"		height:30px;\n"
"         font: 700 14pt \"\u7b49\u7ebf\";\n"
"		color: rgb(255, 255, 255);\n"
"         padding: 0px;	\n"
"		background-color: rgb(20, 9, 70);\n"
"		border: 1px solid rgb(50, 24, 97);\n"
"                 }\n"
"QTabBar::tab:hover{\n"
"         color: rgb(255, 0, 127);\n"
"		border-left: 2px solid rgb(255, 85, 0) ;\n"
"		border-top: 2px solid rgb(255, 85, 0) ;\n"
"		border-right: 2px solid rgb(255, 85, 0);		\n"
"}\n"
"QTabBar::tab:selected {\n"
"		height: 35px;\n"
"		width: 250px;\n"
"         margin-left: 5; margin-right: 5;\n"
"		font: 700 16pt \"\u7b49\u7ebf\";\n"
"         color: rgb(255, 0, 0);\n"
"		border-left: 2px solid rgb(255, 85, 0) ;\n"
"		border-top: 2px solid rgb(255, 85, 0) ;\n"
""
                        "		border-right: 2px solid rgb(255, 85, 0);\n"
" }\n"
"")
        self.tabWidget_account.setTabPosition(QTabWidget.North)
        self.tabWidget_account.setTabShape(QTabWidget.Rounded)
        self.tabWidget_account.setIconSize(QSize(30, 30))
        self.tabWidget_account.setElideMode(Qt.ElideMiddle)
        self.tabWidget_account.setUsesScrollButtons(False)
        self.tab_user_manage = QWidget()
        self.tab_user_manage.setObjectName(u"tab_user_manage")
        self.tab_user_manage.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.horizontalLayout_13 = QHBoxLayout(self.tab_user_manage)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_103 = QFrame(self.tab_user_manage)
        self.frame_103.setObjectName(u"frame_103")
        sizePolicy3.setHeightForWidth(self.frame_103.sizePolicy().hasHeightForWidth())
        self.frame_103.setSizePolicy(sizePolicy3)
        self.frame_103.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_103)
        self.verticalLayout_68.setSpacing(1)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(1, 1, 1, 1)
        self.frame_115 = QFrame(self.frame_103)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMinimumSize(QSize(250, 30))
        self.frame_115.setMaximumSize(QSize(250, 30))
        self.frame_115.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)

        self.verticalLayout_68.addWidget(self.frame_115, 0, Qt.AlignHCenter)

        self.frame_116 = QFrame(self.frame_103)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setMinimumSize(QSize(300, 300))
        self.frame_116.setStyleSheet(u"border: none;")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_116)
        self.verticalLayout_69.setSpacing(1)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(1, 1, 1, 1)
        self.label_client_photo_show = QLabel(self.frame_116)
        self.label_client_photo_show.setObjectName(u"label_client_photo_show")
        self.label_client_photo_show.setMinimumSize(QSize(300, 300))
        self.label_client_photo_show.setMaximumSize(QSize(16777215, 16777215))
        self.label_client_photo_show.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")

        self.verticalLayout_69.addWidget(self.label_client_photo_show, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_68.addWidget(self.frame_116)

        self.frame_117 = QFrame(self.frame_103)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_117)
        self.verticalLayout_70.setSpacing(1)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(1, 1, 1, 1)
        self.frame_118 = QFrame(self.frame_117)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMinimumSize(QSize(0, 50))
        self.frame_118.setMaximumSize(QSize(16777215, 50))
        self.frame_118.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_118)
        self.horizontalLayout_51.setSpacing(1)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(10, 1, 1, 1)
        self.label_clent_details = QLabel(self.frame_118)
        self.label_clent_details.setObjectName(u"label_clent_details")
        self.label_clent_details.setStyleSheet(u"font: 700 16pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 127);\n"
"border: none;")

        self.horizontalLayout_51.addWidget(self.label_clent_details)


        self.verticalLayout_70.addWidget(self.frame_118)

        self.frame_119 = QFrame(self.frame_117)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_119)
        self.verticalLayout_71.setSpacing(1)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(1, 1, 1, 1)
        self.textBrowser_clients_details = QTextBrowser(self.frame_119)
        self.textBrowser_clients_details.setObjectName(u"textBrowser_clients_details")
        self.textBrowser_clients_details.setMaximumSize(QSize(16777215, 16777215))
        self.textBrowser_clients_details.setStyleSheet(u"QTextBrowser{\n"
"color: rgb(255, 85, 0);\n"
"border-radius: 15px;\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"/*padding-left: 20px;\n"
"padding-right: 20px;*/\n"
"padding: 5px 5px 5px 20px;\n"
"border: none;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
" "
                        "   background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bo"
                        "ttom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")

        self.verticalLayout_71.addWidget(self.textBrowser_clients_details)


        self.verticalLayout_70.addWidget(self.frame_119)


        self.verticalLayout_68.addWidget(self.frame_117)


        self.horizontalLayout_13.addWidget(self.frame_103, 0, Qt.AlignHCenter)

        self.frame_13 = QFrame(self.tab_user_manage)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(250, 0))
        self.frame_13.setMaximumSize(QSize(250, 16777215))
        self.frame_13.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_13)
        self.verticalLayout_63.setSpacing(1)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(1, 1, 1, 1)
        self.frame_109 = QFrame(self.frame_13)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMinimumSize(QSize(0, 50))
        self.frame_109.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)

        self.verticalLayout_63.addWidget(self.frame_109)

        self.frame_110 = QFrame(self.frame_13)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_110)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.clients_listview2 = QListView(self.frame_110)
        self.clients_listview2.setObjectName(u"clients_listview2")
        self.clients_listview2.setStyleSheet(u"QListView {	\n"
"	font:  16pt \"\u7b49\u7ebf\";\n"
"	color: rgb(170, 0, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	padding:5px;\n"
"}\n"
"QListView::item {\n"
"	min-height:35px;\n"
"     border-radius: 15px;\n"
"	padding-left: 20px;\n"
"	background-color: rgb(13, 9, 36);\n"
"}\n"
"\n"
"QListView::item:selected {   \n"
"	border: none;\n"
"	background-color: rgb(170, 0, 255);\n"
"}\n"
"\n"
"QListView::item:hover { \n"
"	background-color: rgb(0, 70, 0);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
"QScro"
                        "llBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	bor"
                        "der-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")

        self.verticalLayout_62.addWidget(self.clients_listview2)


        self.verticalLayout_63.addWidget(self.frame_110)

        self.frame_108 = QFrame(self.frame_13)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(0, 200))
        self.frame_108.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)

        self.verticalLayout_63.addWidget(self.frame_108)


        self.horizontalLayout_13.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.tab_user_manage)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(450, 0))
        self.frame_14.setMaximumSize(QSize(450, 1000))
        self.frame_14.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_14)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(1, 1, 1, 1)
        self.frame_51 = QFrame(self.frame_14)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 40))
        self.frame_51.setMaximumSize(QSize(16777215, 40))
        self.frame_51.setStyleSheet(u"border:none")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 10, -1, 5)
        self.label_tital_2 = QLabel(self.frame_51)
        self.label_tital_2.setObjectName(u"label_tital_2")
        self.label_tital_2.setStyleSheet(u"font: 700 20pt \"\u7b49\u7ebf\";\n"
"color: rgb(0, 255, 0);\n"
"border: none;")

        self.horizontalLayout_24.addWidget(self.label_tital_2, 0, Qt.AlignTop)


        self.verticalLayout_19.addWidget(self.frame_51)

        self.frame_32 = QFrame(self.frame_14)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy5)
        self.frame_32.setMinimumSize(QSize(0, 360))
        self.frame_32.setMaximumSize(QSize(450, 360))
        self.frame_32.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(15, 0, 10, 0)
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(205, 0))
        self.frame_33.setMaximumSize(QSize(205, 16777215))
        self.frame_33.setStyleSheet(u"border:none")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_33)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_add_clients_name = QLabel(self.frame_33)
        self.label_add_clients_name.setObjectName(u"label_add_clients_name")
        self.label_add_clients_name.setMinimumSize(QSize(200, 40))
        self.label_add_clients_name.setMaximumSize(QSize(200, 40))
        self.label_add_clients_name.setStyleSheet(u"QLabel {\n"
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
        self.label_add_clients_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_add_clients_name)

        self.label_clients_ID = QLabel(self.frame_33)
        self.label_clients_ID.setObjectName(u"label_clients_ID")
        self.label_clients_ID.setMinimumSize(QSize(200, 40))
        self.label_clients_ID.setMaximumSize(QSize(200, 40))
        self.label_clients_ID.setStyleSheet(u"QLabel {\n"
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
        self.label_clients_ID.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_clients_ID)

        self.label_clients_tel = QLabel(self.frame_33)
        self.label_clients_tel.setObjectName(u"label_clients_tel")
        self.label_clients_tel.setMinimumSize(QSize(200, 40))
        self.label_clients_tel.setMaximumSize(QSize(200, 40))
        self.label_clients_tel.setStyleSheet(u"QLabel {\n"
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
        self.label_clients_tel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_clients_tel)

        self.label_clients_address = QLabel(self.frame_33)
        self.label_clients_address.setObjectName(u"label_clients_address")
        self.label_clients_address.setMinimumSize(QSize(200, 40))
        self.label_clients_address.setMaximumSize(QSize(200, 40))
        self.label_clients_address.setStyleSheet(u"QLabel {\n"
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
        self.label_clients_address.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_clients_address)


        self.horizontalLayout_14.addWidget(self.frame_33, 0, Qt.AlignHCenter)

        self.frame_46 = QFrame(self.frame_32)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(205, 0))
        self.frame_46.setMaximumSize(QSize(205, 16777215))
        self.frame_46.setStyleSheet(u"border:none")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_46)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.clients_name = QLineEdit(self.frame_46)
        self.clients_name.setObjectName(u"clients_name")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.clients_name.sizePolicy().hasHeightForWidth())
        self.clients_name.setSizePolicy(sizePolicy6)
        self.clients_name.setMinimumSize(QSize(200, 40))
        self.clients_name.setMaximumSize(QSize(200, 40))
        self.clients_name.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_30.addWidget(self.clients_name)

        self.clients_id = QLineEdit(self.frame_46)
        self.clients_id.setObjectName(u"clients_id")
        sizePolicy6.setHeightForWidth(self.clients_id.sizePolicy().hasHeightForWidth())
        self.clients_id.setSizePolicy(sizePolicy6)
        self.clients_id.setMinimumSize(QSize(200, 40))
        self.clients_id.setMaximumSize(QSize(200, 40))
        self.clients_id.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_30.addWidget(self.clients_id)

        self.clients_tel = QLineEdit(self.frame_46)
        self.clients_tel.setObjectName(u"clients_tel")
        sizePolicy6.setHeightForWidth(self.clients_tel.sizePolicy().hasHeightForWidth())
        self.clients_tel.setSizePolicy(sizePolicy6)
        self.clients_tel.setMinimumSize(QSize(200, 40))
        self.clients_tel.setMaximumSize(QSize(200, 40))
        self.clients_tel.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_30.addWidget(self.clients_tel)

        self.clients_address = QLineEdit(self.frame_46)
        self.clients_address.setObjectName(u"clients_address")
        sizePolicy6.setHeightForWidth(self.clients_address.sizePolicy().hasHeightForWidth())
        self.clients_address.setSizePolicy(sizePolicy6)
        self.clients_address.setMinimumSize(QSize(200, 40))
        self.clients_address.setMaximumSize(QSize(200, 40))
        self.clients_address.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_30.addWidget(self.clients_address)


        self.horizontalLayout_14.addWidget(self.frame_46, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.frame_32)

        self.frame_89 = QFrame(self.frame_14)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(0, 150))
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_89)
        self.verticalLayout_65.setSpacing(10)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(5, 5, 5, 5)
        self.Btn_select_clients_photo_address = QPushButton(self.frame_89)
        self.Btn_select_clients_photo_address.setObjectName(u"Btn_select_clients_photo_address")
        self.Btn_select_clients_photo_address.setMinimumSize(QSize(300, 40))
        self.Btn_select_clients_photo_address.setMaximumSize(QSize(300, 40))
        self.Btn_select_clients_photo_address.setStyleSheet(u"QPushButton{	\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 127);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 3px solid rgb(0, 255, 0); \n"
"}\n"
"QPushButton:pressed{\n"
"	color: green;\n"
"	border-color: blueviolet;\n"
"    background-color: rgb(85, 0, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"")

        self.verticalLayout_65.addWidget(self.Btn_select_clients_photo_address, 0, Qt.AlignHCenter)

        self.clients_photo_address = QLineEdit(self.frame_89)
        self.clients_photo_address.setObjectName(u"clients_photo_address")
        sizePolicy6.setHeightForWidth(self.clients_photo_address.sizePolicy().hasHeightForWidth())
        self.clients_photo_address.setSizePolicy(sizePolicy6)
        self.clients_photo_address.setMinimumSize(QSize(0, 40))
        self.clients_photo_address.setMaximumSize(QSize(16777215, 40))
        self.clients_photo_address.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	border-radius: 15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);	\n"
"	color: rgb(0, 0, 0);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
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

        self.verticalLayout_65.addWidget(self.clients_photo_address)


        self.verticalLayout_19.addWidget(self.frame_89)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_4)

        self.frame_47 = QFrame(self.frame_14)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(0, 60))
        self.frame_47.setMaximumSize(QSize(16777215, 100))
        self.frame_47.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 10)
        self.frame_48 = QFrame(self.frame_47)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.Btn_add_clients = QPushButton(self.frame_48)
        self.Btn_add_clients.setObjectName(u"Btn_add_clients")
        self.Btn_add_clients.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.Btn_add_clients.sizePolicy().hasHeightForWidth())
        self.Btn_add_clients.setSizePolicy(sizePolicy7)
        self.Btn_add_clients.setMinimumSize(QSize(180, 40))
        self.Btn_add_clients.setMaximumSize(QSize(180, 40))
        self.Btn_add_clients.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	border-radius: 20px;\n"
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
        self.Btn_add_clients.setIconSize(QSize(20, 20))
        self.Btn_add_clients.setCheckable(True)
        self.Btn_add_clients.setChecked(False)

        self.horizontalLayout_25.addWidget(self.Btn_add_clients, 0, Qt.AlignVCenter)


        self.horizontalLayout_23.addWidget(self.frame_48, 0, Qt.AlignBottom)

        self.frame_52 = QFrame(self.frame_47)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.Btn_cancel_input_clients = QPushButton(self.frame_52)
        self.Btn_cancel_input_clients.setObjectName(u"Btn_cancel_input_clients")
        self.Btn_cancel_input_clients.setEnabled(True)
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.Btn_cancel_input_clients.sizePolicy().hasHeightForWidth())
        self.Btn_cancel_input_clients.setSizePolicy(sizePolicy8)
        self.Btn_cancel_input_clients.setMinimumSize(QSize(180, 40))
        self.Btn_cancel_input_clients.setMaximumSize(QSize(180, 40))
        self.Btn_cancel_input_clients.setStyleSheet(u"QPushButton{	\n"
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
        self.Btn_cancel_input_clients.setIconSize(QSize(19, 20))

        self.horizontalLayout_27.addWidget(self.Btn_cancel_input_clients, 0, Qt.AlignVCenter)


        self.horizontalLayout_23.addWidget(self.frame_52, 0, Qt.AlignBottom)


        self.verticalLayout_19.addWidget(self.frame_47, 0, Qt.AlignBottom)


        self.horizontalLayout_13.addWidget(self.frame_14)

        self.tabWidget_account.addTab(self.tab_user_manage, "")
        self.tab_tq_account_mamnage = QWidget()
        self.tab_tq_account_mamnage.setObjectName(u"tab_tq_account_mamnage")
        self.tab_tq_account_mamnage.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.horizontalLayout_18 = QHBoxLayout(self.tab_tq_account_mamnage)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_104 = QFrame(self.tab_tq_account_mamnage)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frame_104)

        self.frame_111 = QFrame(self.tab_tq_account_mamnage)
        self.frame_111.setObjectName(u"frame_111")
        sizePolicy3.setHeightForWidth(self.frame_111.sizePolicy().hasHeightForWidth())
        self.frame_111.setSizePolicy(sizePolicy3)
        self.frame_111.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_111)
        self.verticalLayout_66.setSpacing(1)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(1, 1, 1, 1)
        self.frame_113 = QFrame(self.frame_111)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMinimumSize(QSize(0, 50))
        self.frame_113.setMaximumSize(QSize(16777215, 50))
        self.frame_113.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(10, 0, 0, 0)
        self.label_tq_account_details = QLabel(self.frame_113)
        self.label_tq_account_details.setObjectName(u"label_tq_account_details")
        self.label_tq_account_details.setStyleSheet(u"font: 700 16pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 127);\n"
"border: none;")

        self.horizontalLayout_48.addWidget(self.label_tq_account_details)


        self.verticalLayout_66.addWidget(self.frame_113)

        self.frame_114 = QFrame(self.frame_111)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_114)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_tq_account_details = QTextBrowser(self.frame_114)
        self.textBrowser_tq_account_details.setObjectName(u"textBrowser_tq_account_details")
        self.textBrowser_tq_account_details.setStyleSheet(u"QTextBrowser{\n"
"	color: rgb(170, 0, 255);\n"
"border-radius: 15px;\n"
"font: 14pt \"\u7b49\u7ebf\";\n"
"/*padding-left: 20px;\n"
"padding-right: 20px;*/\n"
"padding: 5px 5px 5px 20px;\n"
"border: none;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
""
                        "    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-b"
                        "ottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")

        self.verticalLayout_67.addWidget(self.textBrowser_tq_account_details)


        self.verticalLayout_66.addWidget(self.frame_114)


        self.horizontalLayout_18.addWidget(self.frame_111)

        self.frame_35 = QFrame(self.tab_tq_account_mamnage)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(250, 0))
        self.frame_35.setMaximumSize(QSize(250, 16777215))
        self.frame_35.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_35)
        self.verticalLayout_53.setSpacing(1)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(1, 1, 1, 1)
        self.frame_66 = QFrame(self.frame_35)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(0, 50))
        self.frame_66.setMaximumSize(QSize(16777215, 50))
        self.frame_66.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.verticalLayout_53.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_35)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_67)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.tq_account_listview2 = QListView(self.frame_67)
        self.tq_account_listview2.setObjectName(u"tq_account_listview2")
        self.tq_account_listview2.setStyleSheet(u"QListView {	\n"
"	font:  16pt \"\u7b49\u7ebf\";\n"
"	color: rgb(255, 85, 0);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	padding:5px;\n"
"}\n"
"QListView::item {\n"
"	min-height:35px;\n"
"     border-radius: 15px;\n"
"	padding-left: 20px;\n"
"	background-color: rgb(13, 9, 36);\n"
"}\n"
"\n"
"QListView::item:selected {   \n"
"	border: none;\n"
"	background-color: rgb(170, 0, 255);\n"
"}\n"
"\n"
"QListView::item:hover { \n"
"	background-color: rgb(0, 70, 0);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
"QScrol"
                        "lBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	bord"
                        "er-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")

        self.verticalLayout_61.addWidget(self.tq_account_listview2)


        self.verticalLayout_53.addWidget(self.frame_67)

        self.frame_102 = QFrame(self.frame_35)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setMinimumSize(QSize(0, 200))
        self.frame_102.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)

        self.verticalLayout_53.addWidget(self.frame_102)


        self.horizontalLayout_18.addWidget(self.frame_35)

        self.frame_37 = QFrame(self.tab_tq_account_mamnage)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(450, 0))
        self.frame_37.setMaximumSize(QSize(450, 16777215))
        self.frame_37.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_37)
        self.verticalLayout_36.setSpacing(10)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(1, 1, 1, 1)
        self.frame_41 = QFrame(self.frame_37)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 40))
        self.frame_41.setMaximumSize(QSize(16777215, 40))
        self.frame_41.setStyleSheet(u"border:none")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_41)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(-1, 10, -1, 5)
        self.label_tital_3 = QLabel(self.frame_41)
        self.label_tital_3.setObjectName(u"label_tital_3")
        sizePolicy2.setHeightForWidth(self.label_tital_3.sizePolicy().hasHeightForWidth())
        self.label_tital_3.setSizePolicy(sizePolicy2)
        self.label_tital_3.setMaximumSize(QSize(16777215, 50))
        self.label_tital_3.setStyleSheet(u"font: 700 20pt \"\u7b49\u7ebf\";\n"
"color: rgb(0, 255, 0);\n"
"border: none;")
        self.label_tital_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_42.addWidget(self.label_tital_3)


        self.verticalLayout_36.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame_37)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy1.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy1)
        self.frame_42.setMinimumSize(QSize(0, 540))
        self.frame_42.setMaximumSize(QSize(450, 540))
        self.frame_42.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_34.setSpacing(15)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(15, 0, 10, 0)
        self.frame_63 = QFrame(self.frame_42)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setStyleSheet(u"border:none")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_63)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_63)
        self.frame_49.setObjectName(u"frame_49")
        sizePolicy5.setHeightForWidth(self.frame_49.sizePolicy().hasHeightForWidth())
        self.frame_49.setSizePolicy(sizePolicy5)
        self.frame_49.setMinimumSize(QSize(205, 0))
        self.frame_49.setMaximumSize(QSize(205, 16777215))
        self.frame_49.setStyleSheet(u"border:none")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_49)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_select_clients_name0 = QLabel(self.frame_49)
        self.label_select_clients_name0.setObjectName(u"label_select_clients_name0")
        self.label_select_clients_name0.setEnabled(True)
        self.label_select_clients_name0.setMinimumSize(QSize(200, 40))
        self.label_select_clients_name0.setMaximumSize(QSize(200, 40))
        self.label_select_clients_name0.setStyleSheet(u"QLabel {\n"
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
        self.label_select_clients_name0.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_select_clients_name0)

        self.label_tq_account = QLabel(self.frame_49)
        self.label_tq_account.setObjectName(u"label_tq_account")
        self.label_tq_account.setEnabled(True)
        self.label_tq_account.setMinimumSize(QSize(200, 40))
        self.label_tq_account.setMaximumSize(QSize(200, 40))
        self.label_tq_account.setStyleSheet(u"QLabel {\n"
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
        self.label_tq_account.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_tq_account)

        self.label_tq_psd = QLabel(self.frame_49)
        self.label_tq_psd.setObjectName(u"label_tq_psd")
        self.label_tq_psd.setEnabled(True)
        self.label_tq_psd.setMinimumSize(QSize(200, 40))
        self.label_tq_psd.setMaximumSize(QSize(200, 40))
        self.label_tq_psd.setStyleSheet(u"QLabel {\n"
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
        self.label_tq_psd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_tq_psd)

        self.label_futures_company = QLabel(self.frame_49)
        self.label_futures_company.setObjectName(u"label_futures_company")
        self.label_futures_company.setEnabled(True)
        self.label_futures_company.setMinimumSize(QSize(200, 40))
        self.label_futures_company.setMaximumSize(QSize(200, 40))
        self.label_futures_company.setStyleSheet(u"QLabel {\n"
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
        self.label_futures_company.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_futures_company)

        self.label_futures_account = QLabel(self.frame_49)
        self.label_futures_account.setObjectName(u"label_futures_account")
        self.label_futures_account.setEnabled(True)
        self.label_futures_account.setMinimumSize(QSize(200, 40))
        self.label_futures_account.setMaximumSize(QSize(200, 40))
        self.label_futures_account.setStyleSheet(u"QLabel {\n"
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
        self.label_futures_account.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_futures_account)

        self.label_futures_psd = QLabel(self.frame_49)
        self.label_futures_psd.setObjectName(u"label_futures_psd")
        self.label_futures_psd.setEnabled(True)
        self.label_futures_psd.setMinimumSize(QSize(200, 40))
        self.label_futures_psd.setMaximumSize(QSize(200, 40))
        self.label_futures_psd.setStyleSheet(u"QLabel {\n"
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
        self.label_futures_psd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_futures_psd)


        self.verticalLayout_43.addWidget(self.frame_49, 0, Qt.AlignHCenter)


        self.horizontalLayout_34.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.frame_42)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setStyleSheet(u"border:none")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_64)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.frame_64)
        self.frame_50.setObjectName(u"frame_50")
        sizePolicy5.setHeightForWidth(self.frame_50.sizePolicy().hasHeightForWidth())
        self.frame_50.setSizePolicy(sizePolicy5)
        self.frame_50.setMinimumSize(QSize(205, 0))
        self.frame_50.setMaximumSize(QSize(205, 16777215))
        self.frame_50.setStyleSheet(u"border:none")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_50)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.comboBox_select_clients_name0 = QComboBox(self.frame_50)
        self.comboBox_select_clients_name0.setObjectName(u"comboBox_select_clients_name0")
        self.comboBox_select_clients_name0.setMinimumSize(QSize(200, 40))
        self.comboBox_select_clients_name0.setMaximumSize(QSize(200, 40))
        self.comboBox_select_clients_name0.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 18px 1px 3px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 18pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    \n"
"    border: 1px solid yellow;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: black;\n"
"	border-radius: 3px;\n"
"    background-color: rgb(225, 225, 225);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"    selection-background-color: lightgreen;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u4e2d\u9879\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	image: url(:/\u56fe\u6807/icons/"
                        "\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 30px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
"    width: 30px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6"
                        " */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QComboBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_34.addWidget(self.comboBox_select_clients_name0)

        self.tq_account = QLineEdit(self.frame_50)
        self.tq_account.setObjectName(u"tq_account")
        sizePolicy6.setHeightForWidth(self.tq_account.sizePolicy().hasHeightForWidth())
        self.tq_account.setSizePolicy(sizePolicy6)
        self.tq_account.setMinimumSize(QSize(200, 40))
        self.tq_account.setMaximumSize(QSize(200, 40))
        self.tq_account.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_34.addWidget(self.tq_account)

        self.tq_psd = QLineEdit(self.frame_50)
        self.tq_psd.setObjectName(u"tq_psd")
        sizePolicy6.setHeightForWidth(self.tq_psd.sizePolicy().hasHeightForWidth())
        self.tq_psd.setSizePolicy(sizePolicy6)
        self.tq_psd.setMinimumSize(QSize(200, 40))
        self.tq_psd.setMaximumSize(QSize(200, 40))
        self.tq_psd.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_34.addWidget(self.tq_psd)

        self.futures_company = QLineEdit(self.frame_50)
        self.futures_company.setObjectName(u"futures_company")
        sizePolicy6.setHeightForWidth(self.futures_company.sizePolicy().hasHeightForWidth())
        self.futures_company.setSizePolicy(sizePolicy6)
        self.futures_company.setMinimumSize(QSize(200, 40))
        self.futures_company.setMaximumSize(QSize(200, 40))
        self.futures_company.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_34.addWidget(self.futures_company)

        self.futures_account = QLineEdit(self.frame_50)
        self.futures_account.setObjectName(u"futures_account")
        sizePolicy6.setHeightForWidth(self.futures_account.sizePolicy().hasHeightForWidth())
        self.futures_account.setSizePolicy(sizePolicy6)
        self.futures_account.setMinimumSize(QSize(200, 40))
        self.futures_account.setMaximumSize(QSize(200, 40))
        self.futures_account.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_34.addWidget(self.futures_account)

        self.futures_psd = QLineEdit(self.frame_50)
        self.futures_psd.setObjectName(u"futures_psd")
        sizePolicy6.setHeightForWidth(self.futures_psd.sizePolicy().hasHeightForWidth())
        self.futures_psd.setSizePolicy(sizePolicy6)
        self.futures_psd.setMinimumSize(QSize(200, 40))
        self.futures_psd.setMaximumSize(QSize(200, 40))
        self.futures_psd.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_34.addWidget(self.futures_psd)


        self.verticalLayout_44.addWidget(self.frame_50, 0, Qt.AlignHCenter)


        self.horizontalLayout_34.addWidget(self.frame_64)


        self.verticalLayout_36.addWidget(self.frame_42)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_3)

        self.frame_43 = QFrame(self.frame_37)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 60))
        self.frame_43.setMaximumSize(QSize(16777215, 100))
        self.frame_43.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 10)
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.Btn_add_tq_account = QPushButton(self.frame_44)
        self.Btn_add_tq_account.setObjectName(u"Btn_add_tq_account")
        self.Btn_add_tq_account.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.Btn_add_tq_account.sizePolicy().hasHeightForWidth())
        self.Btn_add_tq_account.setSizePolicy(sizePolicy7)
        self.Btn_add_tq_account.setMinimumSize(QSize(180, 40))
        self.Btn_add_tq_account.setMaximumSize(QSize(180, 40))
        self.Btn_add_tq_account.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	border-radius: 20px;\n"
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
        self.Btn_add_tq_account.setIconSize(QSize(20, 20))
        self.Btn_add_tq_account.setCheckable(True)
        self.Btn_add_tq_account.setChecked(False)

        self.horizontalLayout_29.addWidget(self.Btn_add_tq_account, 0, Qt.AlignVCenter)


        self.horizontalLayout_22.addWidget(self.frame_44, 0, Qt.AlignBottom)

        self.frame_62 = QFrame(self.frame_43)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.Btn_cancel_input_tq_account = QPushButton(self.frame_62)
        self.Btn_cancel_input_tq_account.setObjectName(u"Btn_cancel_input_tq_account")
        self.Btn_cancel_input_tq_account.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.Btn_cancel_input_tq_account.sizePolicy().hasHeightForWidth())
        self.Btn_cancel_input_tq_account.setSizePolicy(sizePolicy8)
        self.Btn_cancel_input_tq_account.setMinimumSize(QSize(180, 40))
        self.Btn_cancel_input_tq_account.setMaximumSize(QSize(180, 40))
        self.Btn_cancel_input_tq_account.setStyleSheet(u"QPushButton{	\n"
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
        self.Btn_cancel_input_tq_account.setIconSize(QSize(19, 20))

        self.horizontalLayout_33.addWidget(self.Btn_cancel_input_tq_account, 0, Qt.AlignVCenter)


        self.horizontalLayout_22.addWidget(self.frame_62, 0, Qt.AlignBottom)


        self.verticalLayout_36.addWidget(self.frame_43)


        self.horizontalLayout_18.addWidget(self.frame_37)

        self.tabWidget_account.addTab(self.tab_tq_account_mamnage, "")
        self.tab_add_strategy = QWidget()
        self.tab_add_strategy.setObjectName(u"tab_add_strategy")
        self.tab_add_strategy.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.horizontalLayout_19 = QHBoxLayout(self.tab_add_strategy)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.tab_add_strategy)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy9)
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_105 = QFrame(self.frame_40)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_21.addWidget(self.frame_105)

        self.frame_56 = QFrame(self.frame_40)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(450, 0))
        self.frame_56.setMaximumSize(QSize(450, 16777215))
        self.frame_56.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
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
        self.label_tital_4.setStyleSheet(u"font: 700 20pt \"\u7b49\u7ebf\";\n"
"color: rgb(0, 255, 0);\n"
"border: none;")

        self.verticalLayout_39.addWidget(self.label_tital_4)


        self.verticalLayout_38.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_56)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMaximumSize(QSize(450, 16777215))
        self.frame_58.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
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
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.upper_left_3.sizePolicy().hasHeightForWidth())
        self.upper_left_3.setSizePolicy(sizePolicy10)
        self.upper_left_3.setMinimumSize(QSize(205, 0))
        self.upper_left_3.setMaximumSize(QSize(205, 1000))
        self.upper_left_3.setStyleSheet(u"border:none")
        self.upper_left_3.setFrameShape(QFrame.StyledPanel)
        self.upper_left_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.upper_left_3)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_select_clients_name1 = QLabel(self.upper_left_3)
        self.label_select_clients_name1.setObjectName(u"label_select_clients_name1")
        self.label_select_clients_name1.setMinimumSize(QSize(200, 40))
        self.label_select_clients_name1.setMaximumSize(QSize(200, 40))
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
        self.label_select_tq_account.setMinimumSize(QSize(200, 40))
        self.label_select_tq_account.setMaximumSize(QSize(20, 40))
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
        self.label_select_strategy.setMinimumSize(QSize(200, 40))
        self.label_select_strategy.setMaximumSize(QSize(200, 40))
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
        self.label_whether_self_start.setMinimumSize(QSize(200, 40))
        self.label_whether_self_start.setMaximumSize(QSize(200, 40))
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
        self.label_whether_live_futures_trading.setMinimumSize(QSize(200, 40))
        self.label_whether_live_futures_trading.setMaximumSize(QSize(200, 40))
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

        self.label_whether_web_services = QLabel(self.upper_left_3)
        self.label_whether_web_services.setObjectName(u"label_whether_web_services")
        self.label_whether_web_services.setMinimumSize(QSize(200, 40))
        self.label_whether_web_services.setMaximumSize(QSize(200, 40))
        self.label_whether_web_services.setStyleSheet(u"QLabel {\n"
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
        self.label_whether_web_services.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_whether_web_services)

        self.label_web_port = QLabel(self.upper_left_3)
        self.label_web_port.setObjectName(u"label_web_port")
        self.label_web_port.setMinimumSize(QSize(200, 40))
        self.label_web_port.setMaximumSize(QSize(200, 40))
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
        self.label_exchange.setMinimumSize(QSize(200, 40))
        self.label_exchange.setMaximumSize(QSize(200, 40))
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


        self.horizontalLayout_26.addWidget(self.upper_left_3, 0, Qt.AlignHCenter)

        self.upper_right_3 = QFrame(self.frame_58)
        self.upper_right_3.setObjectName(u"upper_right_3")
        sizePolicy10.setHeightForWidth(self.upper_right_3.sizePolicy().hasHeightForWidth())
        self.upper_right_3.setSizePolicy(sizePolicy10)
        self.upper_right_3.setMinimumSize(QSize(205, 0))
        self.upper_right_3.setMaximumSize(QSize(205, 1000))
        self.upper_right_3.setStyleSheet(u"border:none")
        self.upper_right_3.setFrameShape(QFrame.StyledPanel)
        self.upper_right_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.upper_right_3)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.comboBox_select_clients_name1 = QComboBox(self.upper_right_3)
        self.comboBox_select_clients_name1.setObjectName(u"comboBox_select_clients_name1")
        self.comboBox_select_clients_name1.setMinimumSize(QSize(200, 40))
        self.comboBox_select_clients_name1.setMaximumSize(QSize(200, 16777215))
        self.comboBox_select_clients_name1.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 18px 1px 3px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 18pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    \n"
"    border: 1px solid yellow;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: black;\n"
"	border-radius: 3px;\n"
"    background-color: rgb(225, 225, 225);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"    selection-background-color: lightgreen;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u4e2d\u9879\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	image: url(:/\u56fe\u6807/icons/"
                        "\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 30px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
"    width: 30px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6"
                        " */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QComboBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_33.addWidget(self.comboBox_select_clients_name1)

        self.comboBox_select_tq_account = QComboBox(self.upper_right_3)
        self.comboBox_select_tq_account.setObjectName(u"comboBox_select_tq_account")
        self.comboBox_select_tq_account.setMinimumSize(QSize(200, 40))
        self.comboBox_select_tq_account.setMaximumSize(QSize(200, 16777215))
        self.comboBox_select_tq_account.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 18px 1px 3px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 18pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    \n"
"    border: 1px solid yellow;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: black;\n"
"	border-radius: 3px;\n"
"    background-color: rgb(225, 225, 225);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"    selection-background-color: lightgreen;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u4e2d\u9879\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	image: url(:/\u56fe\u6807/icons/"
                        "\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 30px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
"    width: 30px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6"
                        " */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QComboBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_33.addWidget(self.comboBox_select_tq_account)

        self.comboBox_select_strategy = QComboBox(self.upper_right_3)
        self.comboBox_select_strategy.setObjectName(u"comboBox_select_strategy")
        self.comboBox_select_strategy.setMinimumSize(QSize(200, 40))
        self.comboBox_select_strategy.setMaximumSize(QSize(200, 16777215))
        self.comboBox_select_strategy.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 18px 1px 3px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 18pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    \n"
"    border: 1px solid yellow;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: black;\n"
"	border-radius: 3px;\n"
"    background-color: rgb(225, 225, 225);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"    selection-background-color: lightgreen;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u4e2d\u9879\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	image: url(:/\u56fe\u6807/icons/"
                        "\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 30px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
"    width: 30px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6"
                        " */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QComboBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_33.addWidget(self.comboBox_select_strategy)

        self.checkBox_whether_self_start = QCheckBox(self.upper_right_3)
        self.checkBox_whether_self_start.setObjectName(u"checkBox_whether_self_start")
        self.checkBox_whether_self_start.setMinimumSize(QSize(200, 40))
        self.checkBox_whether_self_start.setMaximumSize(QSize(200, 40))
        self.checkBox_whether_self_start.setStyleSheet(u"QCheckBox{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 700 16pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	padding:3px 3px 3px 7px;\n"
"}\n"
"QCheckBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 0, 0);\n"
"    border: 3px solid rgb(255, 0, 255);\n"
"}\n"
" \n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:rgb(136, 136, 136);\n"
"    border:3px solid black;\n"
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
"	background-color: rgb(255, 255, 255);\n"
"	font: 700 16pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	padding:3px 3px 3px 7px;\n"
"}\n"
"QCheckBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 0, 0);\n"
"    border: 3px solid rgb(255, 0, 255);\n"
"}\n"
" \n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:rgb(136, 136, 136);\n"
"    border:3px solid black;\n"
"}\n"
"QCheckBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_33.addWidget(self.checkBox_whether_live_futures_trading)

        self.checkBox_whether_whether_web_services = QCheckBox(self.upper_right_3)
        self.checkBox_whether_whether_web_services.setObjectName(u"checkBox_whether_whether_web_services")
        self.checkBox_whether_whether_web_services.setMinimumSize(QSize(200, 40))
        self.checkBox_whether_whether_web_services.setMaximumSize(QSize(200, 40))
        self.checkBox_whether_whether_web_services.setStyleSheet(u"QCheckBox{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 700 16pt \"\u7b49\u7ebf\";\n"
"	border-radius: 15px;\n"
"	padding:3px 3px 3px 7px;\n"
"}\n"
"QCheckBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius:10px;\n"
"}\n"
" \n"
"QCheckBox::indicator:checked {\n"
"    background-color:rgb(255, 0, 0);\n"
"    border: 3px solid rgb(255, 0, 255);\n"
"}\n"
" \n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:rgb(136, 136, 136);\n"
"    border:3px solid black;\n"
"}\n"
"QCheckBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_33.addWidget(self.checkBox_whether_whether_web_services)

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
"    padding: 1px 18px 1px 3px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 18pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    \n"
"    border: 1px solid yellow;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: black;\n"
"	border-radius: 3px;\n"
"    background-color: rgb(225, 225, 225);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"    selection-background-color: lightgreen;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u4e2d\u9879\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	image: url(:/\u56fe\u6807/icons/"
                        "\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 30px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
"    width: 30px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6"
                        " */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QComboBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.comboBox_exchange.setFrame(True)
        self.comboBox_exchange.setModelColumn(0)

        self.verticalLayout_33.addWidget(self.comboBox_exchange)


        self.horizontalLayout_26.addWidget(self.upper_right_3, 0, Qt.AlignHCenter)


        self.verticalLayout_38.addWidget(self.frame_58)

        self.frame_24 = QFrame(self.frame_56)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 70))
        self.frame_24.setMaximumSize(QSize(16777215, 100))
        self.frame_24.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.verticalLayout_38.addWidget(self.frame_24)


        self.horizontalLayout_21.addWidget(self.frame_56)

        self.frame_36 = QFrame(self.frame_40)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy3.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy3)
        self.frame_36.setMinimumSize(QSize(450, 0))
        self.frame_36.setMaximumSize(QSize(450, 16777215))
        self.frame_36.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
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
"	background-color: rgb(13, 9, 36);\n"
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
        sizePolicy10.setHeightForWidth(self.upper_left_5.sizePolicy().hasHeightForWidth())
        self.upper_left_5.setSizePolicy(sizePolicy10)
        self.upper_left_5.setMinimumSize(QSize(205, 0))
        self.upper_left_5.setMaximumSize(QSize(205, 1000))
        self.upper_left_5.setStyleSheet(u"border:none")
        self.upper_left_5.setFrameShape(QFrame.StyledPanel)
        self.upper_left_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.upper_left_5)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_symbol = QLabel(self.upper_left_5)
        self.label_symbol.setObjectName(u"label_symbol")
        self.label_symbol.setMinimumSize(QSize(200, 40))
        self.label_symbol.setMaximumSize(QSize(200, 40))
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
        self.label_symbol_period.setMinimumSize(QSize(200, 40))
        self.label_symbol_period.setMaximumSize(QSize(200, 40))
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
        self.label_initial_capital.setMinimumSize(QSize(200, 40))
        self.label_initial_capital.setMaximumSize(QSize(200, 40))
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
        self.label_orientation.setMinimumSize(QSize(200, 40))
        self.label_orientation.setMaximumSize(QSize(200, 40))
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

        self.label_contract_multiples = QLabel(self.upper_left_5)
        self.label_contract_multiples.setObjectName(u"label_contract_multiples")
        self.label_contract_multiples.setMinimumSize(QSize(200, 40))
        self.label_contract_multiples.setMaximumSize(QSize(200, 40))
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
        self.label_margin_rate.setMinimumSize(QSize(200, 40))
        self.label_margin_rate.setMaximumSize(QSize(200, 40))
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
        self.label_stop_loss.setMinimumSize(QSize(200, 40))
        self.label_stop_loss.setMaximumSize(QSize(200, 40))
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
        self.label_stop_profit.setMinimumSize(QSize(200, 40))
        self.label_stop_profit.setMaximumSize(QSize(200, 40))
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
        sizePolicy10.setHeightForWidth(self.upper_right_5.sizePolicy().hasHeightForWidth())
        self.upper_right_5.setSizePolicy(sizePolicy10)
        self.upper_right_5.setMinimumSize(QSize(205, 0))
        self.upper_right_5.setMaximumSize(QSize(205, 1000))
        self.upper_right_5.setStyleSheet(u"border:none")
        self.upper_right_5.setFrameShape(QFrame.StyledPanel)
        self.upper_right_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.upper_right_5)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.symbol = QLineEdit(self.upper_right_5)
        self.symbol.setObjectName(u"symbol")
        self.symbol.setMinimumSize(QSize(200, 40))
        self.symbol.setMaximumSize(QSize(200, 40))
        self.symbol.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_41.addWidget(self.symbol)

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
        self.frame_59.setMinimumSize(QSize(0, 60))
        self.frame_59.setMaximumSize(QSize(16777215, 100))
        self.frame_59.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
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
        self.frame_39 = QFrame(self.frame_59)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.Btn_add_process_param = QPushButton(self.frame_39)
        self.Btn_add_process_param.setObjectName(u"Btn_add_process_param")
        self.Btn_add_process_param.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.Btn_add_process_param.sizePolicy().hasHeightForWidth())
        self.Btn_add_process_param.setSizePolicy(sizePolicy7)
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

        self.horizontalLayout_20.addWidget(self.Btn_add_process_param, 0, Qt.AlignVCenter)


        self.horizontalLayout_31.addWidget(self.frame_39)

        self.frame_45 = QFrame(self.frame_59)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.Btn_cancel_input_process_param = QPushButton(self.frame_45)
        self.Btn_cancel_input_process_param.setObjectName(u"Btn_cancel_input_process_param")
        self.Btn_cancel_input_process_param.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.Btn_cancel_input_process_param.sizePolicy().hasHeightForWidth())
        self.Btn_cancel_input_process_param.setSizePolicy(sizePolicy8)
        self.Btn_cancel_input_process_param.setMinimumSize(QSize(180, 40))
        self.Btn_cancel_input_process_param.setMaximumSize(QSize(180, 40))
        self.Btn_cancel_input_process_param.setStyleSheet(u"QPushButton{	\n"
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
        self.Btn_cancel_input_process_param.setIconSize(QSize(19, 20))

        self.horizontalLayout_30.addWidget(self.Btn_cancel_input_process_param, 0, Qt.AlignVCenter)


        self.horizontalLayout_31.addWidget(self.frame_45)


        self.verticalLayout_20.addWidget(self.frame_59)


        self.horizontalLayout_21.addWidget(self.frame_36)


        self.horizontalLayout_19.addWidget(self.frame_40)

        self.tabWidget_account.addTab(self.tab_add_strategy, "")
        self.tab_start_stop_strategy = QWidget()
        self.tab_start_stop_strategy.setObjectName(u"tab_start_stop_strategy")
        self.tab_start_stop_strategy.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 20px;")
        self.verticalLayout_27 = QVBoxLayout(self.tab_start_stop_strategy)
        self.verticalLayout_27.setSpacing(7)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_69 = QFrame(self.tab_start_stop_strategy)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(0, 40))
        self.frame_69.setMaximumSize(QSize(16777215, 40))
        self.frame_69.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(20, 0, 20, 0)
        self.label = QLabel(self.frame_69)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(500, 40))
        self.label.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(30, 30, 40, 0);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	color: rgb(255, 0, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"}\n"
"")

        self.horizontalLayout_40.addWidget(self.label, 0, Qt.AlignLeft)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_6)

        self.Btn_opne_in_excel2 = QPushButton(self.frame_69)
        self.Btn_opne_in_excel2.setObjectName(u"Btn_opne_in_excel2")
        self.Btn_opne_in_excel2.setMinimumSize(QSize(180, 30))
        self.Btn_opne_in_excel2.setMaximumSize(QSize(150, 30))
        self.Btn_opne_in_excel2.setStyleSheet(u"QPushButton {\n"
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
        self.Btn_opne_in_excel2.setIcon(icon7)
        self.Btn_opne_in_excel2.setIconSize(QSize(20, 20))

        self.horizontalLayout_40.addWidget(self.Btn_opne_in_excel2)


        self.verticalLayout_27.addWidget(self.frame_69)

        self.frame_31 = QFrame(self.tab_start_stop_strategy)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_35.setSpacing(1)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(1, 1, 1, 1)
        self.frame_61 = QFrame(self.frame_31)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: none;\n"
"}")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_process = QTableWidget(self.frame_61)
        self.tableWidget_process.setObjectName(u"tableWidget_process")
        self.tableWidget_process.setStyleSheet(u"QTableWidget{\n"
"font: 11pt \"\u7b49\u7ebf\";\n"
"color:rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"/*alternate-background-color:rgb(35, 18, 90);/*\u4ea4\u9519\u989c\u8272*/\n"
"gridline-color:transparent;\n"
"border: none;\n"
"padding: 5px 5px 5px 5px;\n"
"}\n"
"QTableWidget:hover{\n"
"border: none;\n"
"}\n"
"QTableWidget::item {\n"
"background-color: rgb(13, 9, 37);\n"
"border: 1px solid rgba(140, 140, 140, 50);\n"
"border-radius: 13px;\n"
"}\n"
"/*\u9009\u4e2ditem*/\n"
"QTableWidget::item:selected{\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"color:rgb(0, 255, 0);\n"
"background:rgb(126, 0, 95);\n"
"border: none;\n"
"}\n"
"/*\n"
"\u60ac\u6d6eitem*/\n"
"QTableWidget::item:hover{\n"
"color:rgb(0, 255, 0);\n"
"background:rgb(100, 0, 80);\n"
"}\n"
"/*\u8868\u5934*/\n"
"QHeaderView::section:horizontal{\n"
"font: 700 12pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background:rgb(140, 45, 0);\n"
"border-left-width:0;\n"
"border-top-width:0;\n"
"border-radius: 13px;\n"
"}\n"
""
                        "QHeaderView::section:hover:horizontal{\n"
"border: none;\n"
"}\n"
"QHeaderView::section:vertical{\n"
"border: none;\n"
"text-align:center;\n"
"background:rgb(13, 9, 37);\n"
"color: rgb(13, 9, 37);\n"
"}\n"
"/*\u8868\u5934\u6700\u5de6\u4e0a\u89d2\u7684\u65b9\u5757*/\n"
"QTableCornerButton:section{\n"
"border-left-width:0;\n"
"border-top-width:0;\n"
"border-bottom-width:0;\n"
"border-right-width:0;\n"
"text-align:center;\n"
"background:transparent;\n"
"margin:-5px;\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"QTableCornerButton::section:hover{\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"backgroun"
                        "d:rgb(150, 0, 150);\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);"
                        "\n"
"    min-height: 30px;\n"
"	border-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"")
        self.tableWidget_process.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableWidget_process.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_process.setCornerButtonEnabled(False)
        self.tableWidget_process.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget_process.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_process.horizontalHeader().setHighlightSections(False)
        self.tableWidget_process.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_process.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_process.verticalHeader().setVisible(False)
        self.tableWidget_process.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_process.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_process.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_process.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_process.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_36.addWidget(self.tableWidget_process)


        self.horizontalLayout_35.addWidget(self.frame_61)


        self.verticalLayout_27.addWidget(self.frame_31)

        self.frame_60 = QFrame(self.tab_start_stop_strategy)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 60))
        self.frame_60.setMaximumSize(QSize(16777215, 60))
        self.frame_60.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_58.setSpacing(1)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(1, 1, 1, 1)
        self.frame_107 = QFrame(self.frame_60)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_58.addWidget(self.frame_107)

        self.frame_106 = QFrame(self.frame_60)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMinimumSize(QSize(220, 0))
        self.frame_106.setMaximumSize(QSize(220, 16777215))
        self.frame_106.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.Btn_save_charge = QPushButton(self.frame_106)
        self.Btn_save_charge.setObjectName(u"Btn_save_charge")
        self.Btn_save_charge.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.Btn_save_charge.sizePolicy().hasHeightForWidth())
        self.Btn_save_charge.setSizePolicy(sizePolicy7)
        self.Btn_save_charge.setMinimumSize(QSize(200, 40))
        self.Btn_save_charge.setMaximumSize(QSize(180, 40))
        self.Btn_save_charge.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 0, 0);\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
"	border-radius: 20px;\n"
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
        self.Btn_save_charge.setIconSize(QSize(20, 20))
        self.Btn_save_charge.setCheckable(True)
        self.Btn_save_charge.setChecked(False)

        self.horizontalLayout_38.addWidget(self.Btn_save_charge, 0, Qt.AlignVCenter)


        self.horizontalLayout_58.addWidget(self.frame_106)


        self.verticalLayout_27.addWidget(self.frame_60)

        self.tabWidget_account.addTab(self.tab_start_stop_strategy, "")

        self.horizontalLayout_9.addWidget(self.tabWidget_account)

        self.stackedWidget.addWidget(self.second_page)
        self.third_page = QWidget()
        self.third_page.setObjectName(u"third_page")
        self.horizontalLayout_17 = QHBoxLayout(self.third_page)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 5, 0)
        self.frame_25 = QFrame(self.third_page)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.frame_25.setMinimumSize(QSize(550, 0))
        self.frame_25.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_25)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(1, 1, 1, 1)
        self.frame_120 = QFrame(self.frame_25)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setMinimumSize(QSize(0, 50))
        self.frame_120.setMaximumSize(QSize(16777215, 50))
        self.frame_120.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_8 = QLabel(self.frame_120)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(150, 40))
        self.label_8.setStyleSheet(u"font: 700 16pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 127);\n"
"border: none;")

        self.horizontalLayout_60.addWidget(self.label_8)

        self.label_log_file_name = QLabel(self.frame_120)
        self.label_log_file_name.setObjectName(u"label_log_file_name")
        self.label_log_file_name.setMinimumSize(QSize(150, 40))
        self.label_log_file_name.setStyleSheet(u"font: 16pt \"\u7b49\u7ebf\";\n"
"color: rgb(0, 255, 0);\n"
"border: none;")

        self.horizontalLayout_60.addWidget(self.label_log_file_name)


        self.verticalLayout_28.addWidget(self.frame_120)

        self.frame_121 = QFrame(self.frame_25)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_121)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.textBrowser_log = QTextBrowser(self.frame_121)
        self.textBrowser_log.setObjectName(u"textBrowser_log")
        self.textBrowser_log.setStyleSheet(u"QTextBrowser{\n"
"background-color: rgba(170, 0, 120, 50);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"/*padding-left: 20px;\n"
"padding-right: 20px;*/\n"
"padding: 5px 5px 5px 20px;\n"
"border: none;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-width: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::s"
                        "ub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55"
                        ", 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")

        self.verticalLayout_72.addWidget(self.textBrowser_log)


        self.verticalLayout_28.addWidget(self.frame_121)

        self.frame_122 = QFrame(self.frame_25)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setMinimumSize(QSize(0, 50))
        self.frame_122.setMaximumSize(QSize(16777215, 50))
        self.frame_122.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_61.setSpacing(5)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(10, 0, 0, 0)
        self.label_9 = QLabel(self.frame_122)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 40))
        self.label_9.setMaximumSize(QSize(100, 16777215))
        self.label_9.setStyleSheet(u"font: 700 16pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 127);\n"
"border: none;")

        self.horizontalLayout_61.addWidget(self.label_9)

        self.label_log_file_address = QLabel(self.frame_122)
        self.label_log_file_address.setObjectName(u"label_log_file_address")
        self.label_log_file_address.setMinimumSize(QSize(150, 40))
        self.label_log_file_address.setMaximumSize(QSize(656, 16777215))
        self.label_log_file_address.setStyleSheet(u"font: 10pt \"\u7b49\u7ebf\";\n"
"color: rgb(0, 255, 0);\n"
"border: none;")

        self.horizontalLayout_61.addWidget(self.label_log_file_address)


        self.verticalLayout_28.addWidget(self.frame_122)


        self.horizontalLayout_17.addWidget(self.frame_25)

        self.frame_34 = QFrame(self.third_page)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy2.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy2)
        self.frame_34.setMinimumSize(QSize(250, 0))
        self.frame_34.setMaximumSize(QSize(250, 16777215))
        self.frame_34.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_34)
        self.verticalLayout_31.setSpacing(1)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(1, 1, 1, 1)
        self.frame_91 = QFrame(self.frame_34)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(0, 50))
        self.frame_91.setMaximumSize(QSize(16777215, 50))
        self.frame_91.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_5 = QLabel(self.frame_91)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(150, 40))
        self.label_5.setStyleSheet(u"font: 700 16pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 127);\n"
"border: none;")

        self.horizontalLayout_59.addWidget(self.label_5)


        self.verticalLayout_31.addWidget(self.frame_91)

        self.frame_92 = QFrame(self.frame_34)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_92)
        self.verticalLayout_64.setSpacing(5)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(5, 10, 5, 10)
        self.treeview_log = QTreeView(self.frame_92)
        self.treeview_log.setObjectName(u"treeview_log")
        self.treeview_log.setStyleSheet(u"QTreeView {\n"
"    background: rgb(13, 9, 36);	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"\u7b49\u7ebf\";\n"
"	border: none;\n"
"}\n"
"QTreeView::item {\n"
"	min-height:30px;\n"
"     border-radius: 15px;\n"
"	padding-left: 5px;\n"
"}\n"
"QTreeView::item:open {\n"
"    background-color: rgb(0, 0, 109);\n"
"    color: rgb(255, 0, 255);\n"
"}\n"
"QTreeView::item:selected {\n"
"    background-color: rgb(117, 0, 176);\n"
"    color: rgb(255, 0, 0);\n"
"}\n"
"QTreeView::branch {\n"
"    background-color:  rgb(13, 9, 36);\n"
"}\n"
"QTreeView::branch:open {    \n"
"	\n"
"	image: url(:/icon/icons/arrow-right-bold.svg);\n"
"	\n"
"}\n"
"QTreeView::branch:closed:has-children {   \n"
"	\n"
"	image: url(:/icon/icons/arrow-down-bold.svg);\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 20px 0 20px;\n"
"	border-radius: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:rgba(249, 83, 255, 170);\n"
"    min-w"
                        "idth: 30px;\n"
"	border-radius: 3px\n"
"}\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:horizontal,QScrollBar::handle:pressed:horizontal{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-bottom-left-radius: 3px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"  "
                        "  background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 20px 0 20px 0;\n"
"	border-radius: 3px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background:rgba(249, 83, 255, 170);\n"
"    min-height: 30px;\n"
"	border-radius: 3px\n"
" }\n"
"/*\n"
"\u6ed1\u5757\u60ac\u6d6e\uff0c\u6309\u4e0b*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:rgb(150, 0, 150);\n"
"}\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:ver"
                        "tical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")
        self.treeview_log.setDragEnabled(True)
        self.treeview_log.setIconSize(QSize(20, 20))
        self.treeview_log.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.treeview_log.setAnimated(True)
        self.treeview_log.header().setVisible(False)
        self.treeview_log.header().setMinimumSectionSize(400)
        self.treeview_log.header().setDefaultSectionSize(400)

        self.verticalLayout_64.addWidget(self.treeview_log)


        self.verticalLayout_31.addWidget(self.frame_92)

        self.frame_112 = QFrame(self.frame_34)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMinimumSize(QSize(0, 50))
        self.frame_112.setMaximumSize(QSize(16777215, 50))
        self.frame_112.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_112)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.Btn_update_treeview = QPushButton(self.frame_112)
        self.Btn_update_treeview.setObjectName(u"Btn_update_treeview")
        self.Btn_update_treeview.setMinimumSize(QSize(120, 35))
        self.Btn_update_treeview.setMaximumSize(QSize(180, 35))
        self.Btn_update_treeview.setStyleSheet(u"QPushButton{	\n"
"	font: 700 16pt \"\u7b49\u7ebf\";\n"
"	background-color: rgb(255, 0, 127);\n"
"	border-radius: 17px;\n"
"}\n"
"QPushButton:hover{\n"
"	border: 3px solid rgb(0, 255, 0); \n"
"}\n"
"QPushButton:pressed{\n"
"	color: green;\n"
"	border-color: blueviolet;\n"
"    background-color: rgb(85, 0, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_52.addWidget(self.Btn_update_treeview)


        self.verticalLayout_31.addWidget(self.frame_112)


        self.horizontalLayout_17.addWidget(self.frame_34)

        self.stackedWidget.addWidget(self.third_page)
        self.fourth_page = QWidget()
        self.fourth_page.setObjectName(u"fourth_page")
        self.verticalLayout_45 = QVBoxLayout(self.fourth_page)
        self.verticalLayout_45.setSpacing(5)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 5, 0)
        self.frame_70 = QFrame(self.fourth_page)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_chart = QTabWidget(self.frame_70)
        self.tabWidget_chart.setObjectName(u"tabWidget_chart")
        self.tabWidget_chart.setStyleSheet(u"QTabWidget::pane{\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"		margin:3px;\n"
"		border-bottom-left-radius: 30px;\n"
"         border-bottom-right-radius: 30px;         \n"
" 		width:150px; \n"
"		height:30px;\n"
"         font: 700 14pt \"\u7b49\u7ebf\";\n"
"		color: rgb(255, 255, 255);\n"
"         padding: 0px;	\n"
"		background-color: rgb(20, 9, 70);\n"
"		border: 1px solid rgb(50, 24, 97);\n"
"                 }\n"
"QTabBar::tab:hover{\n"
"         color: rgb(255, 0, 127);\n"
"		border-left: 2px solid rgb(255, 85, 0) ;\n"
"		border-bottom: 2px solid rgb(255, 85, 0) ;\n"
"		border-right: 2px solid rgb(255, 85, 0);		\n"
"}\n"
"QTabBar::tab:selected {\n"
"		height: 35px;\n"
"		width: 200px;\n"
"         margin-left: 5; margin-right: 5;\n"
"		font: 700 16pt \"\u7b49\u7ebf\";\n"
"         color: rgb(255, 0, 0);\n"
"		border-left: 2px solid rgb(255, 85, 0) ;\n"
"		border-bottom: 2px solid rgb(255,"
                        " 85, 0) ;\n"
"		border-right: 2px solid rgb(255, 85, 0);\n"
" }\n"
"")
        self.tabWidget_chart.setTabPosition(QTabWidget.South)
        self.tabWidget_chart.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_46 = QVBoxLayout(self.tab)
        self.verticalLayout_46.setSpacing(5)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_75 = QFrame(self.tab)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(0, 40))
        self.frame_75.setMaximumSize(QSize(16777215, 40))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.pushButton_account_manage_5 = QPushButton(self.frame_75)
        self.pushButton_account_manage_5.setObjectName(u"pushButton_account_manage_5")
        self.pushButton_account_manage_5.setMinimumSize(QSize(500, 35))
        self.pushButton_account_manage_5.setMaximumSize(QSize(1000, 16777215))
        self.pushButton_account_manage_5.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(242, 97, 255);\n"
"	font: 700 20pt \"\u7b49\u7ebf\";\n"
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

        self.horizontalLayout_43.addWidget(self.pushButton_account_manage_5)


        self.verticalLayout_46.addWidget(self.frame_75)

        self.frame_74 = QFrame(self.tab)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)

        self.verticalLayout_46.addWidget(self.frame_74)

        self.frame_76 = QFrame(self.tab)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMaximumSize(QSize(16777215, 100))
        self.frame_76.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)

        self.verticalLayout_46.addWidget(self.frame_76)

        self.tabWidget_chart.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_47 = QVBoxLayout(self.tab_2)
        self.verticalLayout_47.setSpacing(5)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_71 = QFrame(self.tab_2)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(0, 40))
        self.frame_71.setMaximumSize(QSize(16777215, 40))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.pushButton_account_manage_3 = QPushButton(self.frame_71)
        self.pushButton_account_manage_3.setObjectName(u"pushButton_account_manage_3")
        self.pushButton_account_manage_3.setMinimumSize(QSize(500, 35))
        self.pushButton_account_manage_3.setMaximumSize(QSize(1000, 16777215))
        self.pushButton_account_manage_3.setStyleSheet(u"QPushButton{	\n"
"	\n"
"	background-color: rgb(230, 115, 0);\n"
"	font: 700 20pt \"\u7b49\u7ebf\";\n"
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

        self.horizontalLayout_42.addWidget(self.pushButton_account_manage_3)


        self.verticalLayout_47.addWidget(self.frame_71)

        self.frame_72 = QFrame(self.tab_2)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.frame_72)

        self.frame_73 = QFrame(self.tab_2)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMaximumSize(QSize(16777215, 100))
        self.frame_73.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.frame_73)

        self.tabWidget_chart.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_49 = QVBoxLayout(self.tab_4)
        self.verticalLayout_49.setSpacing(5)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_80 = QFrame(self.tab_4)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(0, 40))
        self.frame_80.setMaximumSize(QSize(16777215, 40))
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.pushButton_account_manage_7 = QPushButton(self.frame_80)
        self.pushButton_account_manage_7.setObjectName(u"pushButton_account_manage_7")
        self.pushButton_account_manage_7.setMinimumSize(QSize(500, 35))
        self.pushButton_account_manage_7.setMaximumSize(QSize(1000, 16777215))
        self.pushButton_account_manage_7.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(0, 255, 0);\n"
"	font: 700 20pt \"\u7b49\u7ebf\";\n"
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

        self.horizontalLayout_45.addWidget(self.pushButton_account_manage_7)


        self.verticalLayout_49.addWidget(self.frame_80)

        self.frame_82 = QFrame(self.tab_4)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)

        self.verticalLayout_49.addWidget(self.frame_82)

        self.frame_81 = QFrame(self.tab_4)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMaximumSize(QSize(16777215, 100))
        self.frame_81.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)

        self.verticalLayout_49.addWidget(self.frame_81)

        self.tabWidget_chart.addTab(self.tab_4, "")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.verticalLayout_50 = QVBoxLayout(self.widget)
        self.verticalLayout_50.setSpacing(5)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_83 = QFrame(self.widget)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(0, 40))
        self.frame_83.setMaximumSize(QSize(16777215, 40))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.pushButton_account_manage_8 = QPushButton(self.frame_83)
        self.pushButton_account_manage_8.setObjectName(u"pushButton_account_manage_8")
        self.pushButton_account_manage_8.setMinimumSize(QSize(500, 35))
        self.pushButton_account_manage_8.setMaximumSize(QSize(1000, 16777215))
        self.pushButton_account_manage_8.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(85, 0, 255);\n"
"	font: 700 20pt \"\u7b49\u7ebf\";\n"
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

        self.horizontalLayout_46.addWidget(self.pushButton_account_manage_8)


        self.verticalLayout_50.addWidget(self.frame_83)

        self.frame_85 = QFrame(self.widget)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)

        self.verticalLayout_50.addWidget(self.frame_85)

        self.frame_84 = QFrame(self.widget)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMaximumSize(QSize(16777215, 100))
        self.frame_84.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)

        self.verticalLayout_50.addWidget(self.frame_84)

        self.tabWidget_chart.addTab(self.widget, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_51 = QVBoxLayout(self.tab_6)
        self.verticalLayout_51.setSpacing(5)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_86 = QFrame(self.tab_6)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(0, 40))
        self.frame_86.setMaximumSize(QSize(16777215, 40))
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.pushButton_account_manage_9 = QPushButton(self.frame_86)
        self.pushButton_account_manage_9.setObjectName(u"pushButton_account_manage_9")
        self.pushButton_account_manage_9.setMinimumSize(QSize(500, 35))
        self.pushButton_account_manage_9.setMaximumSize(QSize(1000, 16777215))
        self.pushButton_account_manage_9.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 0);\n"
"	font: 700 20pt \"\u7b49\u7ebf\";\n"
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

        self.horizontalLayout_47.addWidget(self.pushButton_account_manage_9)


        self.verticalLayout_51.addWidget(self.frame_86)

        self.frame_88 = QFrame(self.tab_6)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)

        self.verticalLayout_51.addWidget(self.frame_88)

        self.frame_87 = QFrame(self.tab_6)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMaximumSize(QSize(16777215, 100))
        self.frame_87.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)

        self.verticalLayout_51.addWidget(self.frame_87)

        self.tabWidget_chart.addTab(self.tab_6, "")

        self.horizontalLayout_41.addWidget(self.tabWidget_chart)


        self.verticalLayout_45.addWidget(self.frame_70)

        self.stackedWidget.addWidget(self.fourth_page)
        self.fifth_page = QWidget()
        self.fifth_page.setObjectName(u"fifth_page")
        self.verticalLayout_48 = QVBoxLayout(self.fifth_page)
        self.verticalLayout_48.setSpacing(5)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 5, 0)
        self.frame_90 = QFrame(self.fifth_page)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(0, 40))
        self.frame_90.setMaximumSize(QSize(16777215, 40))
        self.frame_90.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(20, 0, 0, 0)
        self.frame_79 = QFrame(self.frame_90)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setStyleSheet(u"QFrame {	\n"
"	background-color: transparent;\n"
"	border-radius: 15px;\n"
"	border: none;\n"
"}\n"
"QFrame:hover {\n"
"	border:none;\n"
"}")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_79)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 40))
        self.label_27.setMaximumSize(QSize(200, 16777215))
        self.label_27.setFont(font4)
        self.label_27.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(30, 30, 40, 0);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	color: rgb(255, 0, 255);\n"
"	font: 700 14pt \"\u7b49\u7ebf\";\n"
"}\n"
"")
        self.label_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_49.addWidget(self.label_27)


        self.horizontalLayout_50.addWidget(self.frame_79, 0, Qt.AlignLeft)

        self.frame_96 = QFrame(self.frame_90)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setStyleSheet(u"QFrame {	\n"
"	background-color: transparent;\n"
"	border-radius: 15px;\n"
"	border: none;\n"
"}\n"
"QFrame:hover {\n"
"	border:none;\n"
"}")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_96)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 20, 0)
        self.Btn_open_with_chrome = QPushButton(self.frame_96)
        self.Btn_open_with_chrome.setObjectName(u"Btn_open_with_chrome")
        self.Btn_open_with_chrome.setMinimumSize(QSize(250, 30))
        self.Btn_open_with_chrome.setMaximumSize(QSize(300, 30))
        self.Btn_open_with_chrome.setFont(font5)
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
        icon9 = QIcon()
        icon9.addFile(u":/\u56fe\u6807/icons/chrome.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_open_with_chrome.setIcon(icon9)
        self.Btn_open_with_chrome.setIconSize(QSize(25, 25))

        self.horizontalLayout_57.addWidget(self.Btn_open_with_chrome)


        self.horizontalLayout_50.addWidget(self.frame_96, 0, Qt.AlignRight)


        self.verticalLayout_48.addWidget(self.frame_90)

        self.frame_78 = QFrame(self.fifth_page)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(1000, 400))
        self.frame_78.setMaximumSize(QSize(16777215, 16777215))
        self.frame_78.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_7)

        self.frame_93 = QFrame(self.frame_78)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(450, 400))
        self.frame_93.setMaximumSize(QSize(450, 16333512))
        self.frame_93.setStyleSheet(u"QFrame {	\n"
"	background-color: transparent;\n"
"	border-radius: 15px;\n"
"	border: none;\n"
"}\n"
"QFrame:hover {\n"
"	border:none;\n"
"}")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.upper_left_4 = QFrame(self.frame_93)
        self.upper_left_4.setObjectName(u"upper_left_4")
        sizePolicy10.setHeightForWidth(self.upper_left_4.sizePolicy().hasHeightForWidth())
        self.upper_left_4.setSizePolicy(sizePolicy10)
        self.upper_left_4.setMinimumSize(QSize(205, 0))
        self.upper_left_4.setMaximumSize(QSize(205, 1000))
        self.upper_left_4.setStyleSheet(u"border:none")
        self.upper_left_4.setFrameShape(QFrame.StyledPanel)
        self.upper_left_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.upper_left_4)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_backtest_select_tq_account = QLabel(self.upper_left_4)
        self.label_backtest_select_tq_account.setObjectName(u"label_backtest_select_tq_account")
        self.label_backtest_select_tq_account.setEnabled(True)
        self.label_backtest_select_tq_account.setMinimumSize(QSize(200, 40))
        self.label_backtest_select_tq_account.setMaximumSize(QSize(200, 40))
        self.label_backtest_select_tq_account.setStyleSheet(u"QLabel {\n"
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
        self.label_backtest_select_tq_account.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_backtest_select_tq_account)

        self.label_backtest_select_strategy = QLabel(self.upper_left_4)
        self.label_backtest_select_strategy.setObjectName(u"label_backtest_select_strategy")
        self.label_backtest_select_strategy.setEnabled(True)
        self.label_backtest_select_strategy.setMinimumSize(QSize(200, 40))
        self.label_backtest_select_strategy.setMaximumSize(QSize(200, 40))
        self.label_backtest_select_strategy.setStyleSheet(u"QLabel {\n"
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
        self.label_backtest_select_strategy.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_backtest_select_strategy)

        self.label_backtest_exchange = QLabel(self.upper_left_4)
        self.label_backtest_exchange.setObjectName(u"label_backtest_exchange")
        self.label_backtest_exchange.setMinimumSize(QSize(200, 40))
        self.label_backtest_exchange.setMaximumSize(QSize(200, 40))
        self.label_backtest_exchange.setStyleSheet(u"QLabel {\n"
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
        self.label_backtest_exchange.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_backtest_exchange)

        self.label_backtest_symbol = QLabel(self.upper_left_4)
        self.label_backtest_symbol.setObjectName(u"label_backtest_symbol")
        self.label_backtest_symbol.setMinimumSize(QSize(200, 40))
        self.label_backtest_symbol.setMaximumSize(QSize(200, 40))
        self.label_backtest_symbol.setStyleSheet(u"QLabel {\n"
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
        self.label_backtest_symbol.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_backtest_symbol)

        self.label_backtest_symbol_period = QLabel(self.upper_left_4)
        self.label_backtest_symbol_period.setObjectName(u"label_backtest_symbol_period")
        self.label_backtest_symbol_period.setMinimumSize(QSize(200, 40))
        self.label_backtest_symbol_period.setMaximumSize(QSize(200, 40))
        self.label_backtest_symbol_period.setStyleSheet(u"QLabel {\n"
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
        self.label_backtest_symbol_period.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_backtest_symbol_period)

        self.label_backtest_initial_capital = QLabel(self.upper_left_4)
        self.label_backtest_initial_capital.setObjectName(u"label_backtest_initial_capital")
        self.label_backtest_initial_capital.setMinimumSize(QSize(200, 40))
        self.label_backtest_initial_capital.setMaximumSize(QSize(200, 40))
        self.label_backtest_initial_capital.setStyleSheet(u"QLabel {\n"
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
        self.label_backtest_initial_capital.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_backtest_initial_capital)

        self.label_backtest_web_port = QLabel(self.upper_left_4)
        self.label_backtest_web_port.setObjectName(u"label_backtest_web_port")
        self.label_backtest_web_port.setMinimumSize(QSize(200, 40))
        self.label_backtest_web_port.setMaximumSize(QSize(200, 40))
        self.label_backtest_web_port.setStyleSheet(u"QLabel {\n"
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
        self.label_backtest_web_port.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_backtest_web_port)

        self.label_backtest_orientation = QLabel(self.upper_left_4)
        self.label_backtest_orientation.setObjectName(u"label_backtest_orientation")
        self.label_backtest_orientation.setMinimumSize(QSize(200, 40))
        self.label_backtest_orientation.setMaximumSize(QSize(200, 40))
        self.label_backtest_orientation.setStyleSheet(u"QLabel {\n"
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
        self.label_backtest_orientation.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_backtest_orientation)

        self.label_backtest_contract_multiples = QLabel(self.upper_left_4)
        self.label_backtest_contract_multiples.setObjectName(u"label_backtest_contract_multiples")
        self.label_backtest_contract_multiples.setMinimumSize(QSize(200, 40))
        self.label_backtest_contract_multiples.setMaximumSize(QSize(200, 40))
        self.label_backtest_contract_multiples.setStyleSheet(u"QLabel {\n"
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
        self.label_backtest_contract_multiples.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_backtest_contract_multiples)

        self.label_backtest_margin_rate = QLabel(self.upper_left_4)
        self.label_backtest_margin_rate.setObjectName(u"label_backtest_margin_rate")
        self.label_backtest_margin_rate.setMinimumSize(QSize(200, 40))
        self.label_backtest_margin_rate.setMaximumSize(QSize(200, 40))
        self.label_backtest_margin_rate.setStyleSheet(u"QLabel {\n"
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
        self.label_backtest_margin_rate.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_backtest_margin_rate)

        self.label_backtest_stop_loss = QLabel(self.upper_left_4)
        self.label_backtest_stop_loss.setObjectName(u"label_backtest_stop_loss")
        self.label_backtest_stop_loss.setMinimumSize(QSize(200, 40))
        self.label_backtest_stop_loss.setMaximumSize(QSize(200, 40))
        self.label_backtest_stop_loss.setStyleSheet(u"QLabel {\n"
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
        self.label_backtest_stop_loss.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_backtest_stop_loss)

        self.label_backtest_stop_profit = QLabel(self.upper_left_4)
        self.label_backtest_stop_profit.setObjectName(u"label_backtest_stop_profit")
        self.label_backtest_stop_profit.setMinimumSize(QSize(200, 40))
        self.label_backtest_stop_profit.setMaximumSize(QSize(200, 40))
        self.label_backtest_stop_profit.setStyleSheet(u"QLabel {\n"
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
        self.label_backtest_stop_profit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_54.addWidget(self.label_backtest_stop_profit)


        self.horizontalLayout_54.addWidget(self.upper_left_4)

        self.upper_right_4 = QFrame(self.frame_93)
        self.upper_right_4.setObjectName(u"upper_right_4")
        sizePolicy10.setHeightForWidth(self.upper_right_4.sizePolicy().hasHeightForWidth())
        self.upper_right_4.setSizePolicy(sizePolicy10)
        self.upper_right_4.setMinimumSize(QSize(205, 0))
        self.upper_right_4.setMaximumSize(QSize(205, 1000))
        self.upper_right_4.setStyleSheet(u"border:none")
        self.upper_right_4.setFrameShape(QFrame.StyledPanel)
        self.upper_right_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.upper_right_4)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.comboBox_backtest_select_tq_account = QComboBox(self.upper_right_4)
        self.comboBox_backtest_select_tq_account.setObjectName(u"comboBox_backtest_select_tq_account")
        self.comboBox_backtest_select_tq_account.setMinimumSize(QSize(200, 40))
        self.comboBox_backtest_select_tq_account.setMaximumSize(QSize(200, 16777215))
        self.comboBox_backtest_select_tq_account.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 18px 1px 3px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 18pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    \n"
"    border: 1px solid yellow;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: black;\n"
"	border-radius: 3px;\n"
"    background-color: rgb(225, 225, 225);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"    selection-background-color: lightgreen;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u4e2d\u9879\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	image: url(:/\u56fe\u6807/icons/"
                        "\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 30px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
"    width: 30px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6"
                        " */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QComboBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_55.addWidget(self.comboBox_backtest_select_tq_account)

        self.comboBox_backtest_select_strategy = QComboBox(self.upper_right_4)
        self.comboBox_backtest_select_strategy.setObjectName(u"comboBox_backtest_select_strategy")
        self.comboBox_backtest_select_strategy.setMinimumSize(QSize(200, 40))
        self.comboBox_backtest_select_strategy.setMaximumSize(QSize(200, 16777215))
        self.comboBox_backtest_select_strategy.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 18px 1px 3px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 18pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    \n"
"    border: 1px solid yellow;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: black;\n"
"	border-radius: 3px;\n"
"    background-color: rgb(225, 225, 225);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"    selection-background-color: lightgreen;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u4e2d\u9879\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	image: url(:/\u56fe\u6807/icons/"
                        "\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 30px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
"    width: 30px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6"
                        " */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QComboBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")

        self.verticalLayout_55.addWidget(self.comboBox_backtest_select_strategy)

        self.comboBox_backtest_exchange = QComboBox(self.upper_right_4)
        self.comboBox_backtest_exchange.addItem("")
        self.comboBox_backtest_exchange.addItem("")
        self.comboBox_backtest_exchange.addItem("")
        self.comboBox_backtest_exchange.addItem("")
        self.comboBox_backtest_exchange.addItem("")
        self.comboBox_backtest_exchange.setObjectName(u"comboBox_backtest_exchange")
        self.comboBox_backtest_exchange.setMinimumSize(QSize(200, 40))
        self.comboBox_backtest_exchange.setMaximumSize(QSize(200, 40))
        self.comboBox_backtest_exchange.setStyleSheet(u"/* \u672a\u4e0b\u62c9\u65f6\uff0cQComboBox\u7684\u6837\u5f0f */\n"
"QComboBox {\n"
"    border: 2px solid gray;   /* \u8fb9\u6846 */\n"
"    border-radius: 15px;   /* \u5706\u89d2 */\n"
"    padding: 1px 18px 1px 3px;   /* \u5b57\u4f53\u586b\u886c */\n"
"    color: rgb(0, 0, 0);    \n"
"	font: 700 18pt \"\u7b49\u7ebf\";    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* \u4e0b\u62c9\u540e\uff0c\u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    \n"
"    border: 1px solid yellow;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u8fb9\u6846 */\n"
"    color: black;\n"
"	border-radius: 3px;\n"
"    background-color: rgb(225, 225, 225);   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u7684\u80cc\u666f\u8272 */\n"
"    selection-background-color: lightgreen;   /* \u6574\u4e2a\u4e0b\u62c9\u7a97\u4f53\u88ab\u9009\u4e2d\u9879\u7684\u80cc\u666f\u8272 */\n"
"}\n"
"/* \u4e0b\u62c9\u7bad\u5934\u6837\u5f0f */\n"
" QComboBox::down-arrow {\n"
"	image: url(:/\u56fe\u6807/icons/"
                        "\u53cc\u4e0b\u62c9\u7bad\u5934.svg);\n"
"	width: 30px; /* \u4e0b\u62c9\u7bad\u5934\u7684\u5bbd\u5ea6\uff08\u5efa\u8bae\u4e0e\u4e0b\u62c9\u6846drop-down\u7684\u5bbd\u5ea6\u4e00\u81f4\uff09 */ \n"
"	background: rgb(255, 255, 255); /* \u4e0b\u62c9\u7bad\u5934\u7684\u7684\u80cc\u666f\u8272 */ \n"
"	padding: 0px 0px 0px 0px; /* \u4e0a\u5185\u8fb9\u8ddd\u3001\u53f3\u5185\u8fb9\u8ddd\u3001\u4e0b\u5185\u8fb9\u8ddd\u3001\u5de6\u5185\u8fb9\u8ddd */\n"
" } \n"
"\n"
"/* \u4e0b\u62c9\u6846\u6837\u5f0f */\n"
"QComboBox::drop-down {\n"
"   /* subcontrol-origin: padding;   /* \u5b50\u63a7\u4ef6\u5728\u7236\u5143\u7d20\u4e2d\u7684\u539f\u70b9\u77e9\u5f62\u3002\u5982\u679c\u672a\u6307\u5b9a\u6b64\u5c5e\u6027\uff0c\u5219\u9ed8\u8ba4\u4e3apadding\u3002 */\n"
"   /* subcontrol-position: top right;   /* \u4e0b\u62c9\u6846\u7684\u4f4d\u7f6e\uff08\u53f3\u4e0a\uff09 */\n"
"    width: 30px;   /* \u4e0b\u62c9\u6846\u7684\u5bbd\u5ea6 */\n"
"\n"
"    border-left-width: 3px;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u5bbd\u5ea6"
                        " */\n"
"    border-left-color: darkgray;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u989c\u8272 */\n"
"    border-left-style: solid;   /* \u4e0b\u62c9\u6846\u7684\u5de6\u8fb9\u754c\u7ebf\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 10px;   /* \u4e0b\u62c9\u6846\u7684\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\uff08\u5e94\u548c\u6574\u4e2aQComboBox\u53f3\u4e0a\u8fb9\u754c\u7ebf\u7684\u5706\u89d2\u534a\u5f84\u4e00\u81f4\uff09 */\n"
"    border-bottom-right-radius: 10px;   /* \u540c\u4e0a */\n"
"}\n"
"QComboBox:hover {\n"
"	border: 3px solid rgb(255, 85, 0);\n"
"}\n"
"QComboBox:disabled{\n"
"	color: rgb(0, 0, 0);\n"
"	border-color: rgb(166, 166, 166);\n"
"    background-color: rgb(186, 186, 186);\n"
"}")
        self.comboBox_backtest_exchange.setFrame(True)
        self.comboBox_backtest_exchange.setModelColumn(0)

        self.verticalLayout_55.addWidget(self.comboBox_backtest_exchange)

        self.backtest_symbol = QLineEdit(self.upper_right_4)
        self.backtest_symbol.setObjectName(u"backtest_symbol")
        self.backtest_symbol.setMinimumSize(QSize(200, 40))
        self.backtest_symbol.setMaximumSize(QSize(200, 40))
        self.backtest_symbol.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_55.addWidget(self.backtest_symbol)

        self.backtest_symbol_period = QLineEdit(self.upper_right_4)
        self.backtest_symbol_period.setObjectName(u"backtest_symbol_period")
        self.backtest_symbol_period.setMinimumSize(QSize(200, 40))
        self.backtest_symbol_period.setMaximumSize(QSize(200, 40))
        self.backtest_symbol_period.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_55.addWidget(self.backtest_symbol_period)

        self.backtest_initial_capital = QLineEdit(self.upper_right_4)
        self.backtest_initial_capital.setObjectName(u"backtest_initial_capital")
        self.backtest_initial_capital.setMinimumSize(QSize(200, 40))
        self.backtest_initial_capital.setMaximumSize(QSize(200, 40))
        self.backtest_initial_capital.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_55.addWidget(self.backtest_initial_capital)

        self.backtest_web_port = QLineEdit(self.upper_right_4)
        self.backtest_web_port.setObjectName(u"backtest_web_port")
        self.backtest_web_port.setMinimumSize(QSize(200, 40))
        self.backtest_web_port.setMaximumSize(QSize(200, 40))
        self.backtest_web_port.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_55.addWidget(self.backtest_web_port)

        self.backtest_orientation = QLineEdit(self.upper_right_4)
        self.backtest_orientation.setObjectName(u"backtest_orientation")
        self.backtest_orientation.setMinimumSize(QSize(200, 40))
        self.backtest_orientation.setMaximumSize(QSize(200, 40))
        self.backtest_orientation.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_55.addWidget(self.backtest_orientation)

        self.backtest_contract_multiples = QLineEdit(self.upper_right_4)
        self.backtest_contract_multiples.setObjectName(u"backtest_contract_multiples")
        self.backtest_contract_multiples.setMinimumSize(QSize(200, 40))
        self.backtest_contract_multiples.setMaximumSize(QSize(200, 40))
        self.backtest_contract_multiples.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_55.addWidget(self.backtest_contract_multiples)

        self.backtest_margin_rate = QLineEdit(self.upper_right_4)
        self.backtest_margin_rate.setObjectName(u"backtest_margin_rate")
        self.backtest_margin_rate.setMinimumSize(QSize(200, 40))
        self.backtest_margin_rate.setMaximumSize(QSize(200, 40))
        self.backtest_margin_rate.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_55.addWidget(self.backtest_margin_rate)

        self.backtest_stop_loss = QLineEdit(self.upper_right_4)
        self.backtest_stop_loss.setObjectName(u"backtest_stop_loss")
        self.backtest_stop_loss.setMinimumSize(QSize(200, 40))
        self.backtest_stop_loss.setMaximumSize(QSize(200, 40))
        self.backtest_stop_loss.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_55.addWidget(self.backtest_stop_loss)

        self.backtest_stop_profit = QLineEdit(self.upper_right_4)
        self.backtest_stop_profit.setObjectName(u"backtest_stop_profit")
        self.backtest_stop_profit.setMinimumSize(QSize(200, 40))
        self.backtest_stop_profit.setMaximumSize(QSize(200, 40))
        self.backtest_stop_profit.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_55.addWidget(self.backtest_stop_profit)


        self.horizontalLayout_54.addWidget(self.upper_right_4)


        self.horizontalLayout_53.addWidget(self.frame_93)

        self.frame_97 = QFrame(self.frame_78)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMinimumSize(QSize(200, 0))
        self.frame_97.setStyleSheet(u"QFrame {	\n"
"	background-color: transparent;\n"
"	border-radius: 15px;\n"
"	border: none;\n"
"}\n"
"QFrame:hover {\n"
"	border:none;\n"
"}")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_97)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 10, 10)
        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_100 = QFrame(self.frame_98)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(30, 0))
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_100)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_55.addWidget(self.frame_100, 0, Qt.AlignVCenter)

        self.frame_94 = QFrame(self.frame_98)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(250, 0))
        self.frame_94.setMaximumSize(QSize(250, 450))
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_94)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_94)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(245, 0))
        self.label_2.setMaximumSize(QSize(245, 40))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
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

        self.verticalLayout_57.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.calendar_backtest_startdate = QCalendarWidget(self.frame_94)
        self.calendar_backtest_startdate.setObjectName(u"calendar_backtest_startdate")
        self.calendar_backtest_startdate.setMinimumSize(QSize(200, 200))
        self.calendar_backtest_startdate.setMaximumSize(QSize(245, 260))
        self.calendar_backtest_startdate.setStyleSheet(u"#qt_calendar_calendarview {\n"
"     background: rgb(174, 182, 255);\n"
"}\n"
"\n"
"#qt_calendar_navigationbar {/*\u5e74\u6708\u9009\u62e9\u680f\u80cc\u666f\u8272*/\n"
"    background:rgb(255, 255, 255);\n"
"}\n"
"#qt_calendar_yearedit {\n"
"    \n"
"	font: 14pt \"\u7b49\u7ebf\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton#qt_calendar_monthbutton,#qt_calendar_yearbutton{\n"
"    \n"
"	background-color: rgb(249, 62, 255);/*\u9009\u62e9\u6708\u4efd\u548c\u5e74\u7684\u80cc\u666f*/\n"
"	height: 30px;	\n"
"	font: 14pt \"\u7b49\u7ebf\";\n"
"	width: 80px;\n"
"	border-radius:10px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar{\n"
"    \n"
"	background-color:green;/*\u9009\u62e9\u6708\u4efd\u548c\u5e74\u4e24\u8fb9\u7684\u80cc\u666f*/\n"
"	border-radius: 10px;\n"
"}\n"
"QCalendarWidget QMenu{\n"
"    \n"
"	background-color:rgb(91, 79, 255);/*\u6708\u4efd\u4e0b\u62c9\u9009\u62e9\u83dc\u5355\u7684\u80cc\u666f*/\n"
"	font: 14pt \"\u7b49\u7ebf\";\n"
"}\n"
"QToolButton#qt_calendar_prevmo"
                        "nth{/*\u5411\u5de6\u7bad\u5934*/	\n"
"	background-color: transparent;\n"
"	icon-size:30px 30px;\n"
"	qproperty-icon: url(:/\u56fe\u6807/icons/\u7bad\u5934_\u5411\u5de6.svg);\n"
"	margin-left:0px;\n"
"}\n"
"QToolButton#qt_calendar_nextmonth{\n"
"    background-color: transparent;\n"
"	icon-size:30px 30px;	\n"
"	qproperty-icon: url(:/\u56fe\u6807/icons/\u7bad\u5934_\u5411\u53f3.svg);\n"
"}\n"
"QToolButton#qt_calendar_monthbutton::menu-indicator{/*\u6708\u4efd\u4e0b\u62c9\u7bad\u5934*/\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    right: -5px;\n"
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
"color: rgb(147, 147, 147); \n"
"}")

        self.verticalLayout_57.addWidget(self.calendar_backtest_startdate, 0, Qt.AlignHCenter)

        self.label_backtest_startdate = QLabel(self.frame_94)
        self.label_backtest_startdate.setObjectName(u"label_backtest_startdate")
        self.label_backtest_startdate.setMinimumSize(QSize(200, 40))
        self.label_backtest_startdate.setMaximumSize(QSize(200, 40))
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

        self.verticalLayout_57.addWidget(self.label_backtest_startdate, 0, Qt.AlignHCenter)


        self.horizontalLayout_55.addWidget(self.frame_94, 0, Qt.AlignHCenter)

        self.frame_101 = QFrame(self.frame_98)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMinimumSize(QSize(30, 0))
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_101)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_55.addWidget(self.frame_101, 0, Qt.AlignVCenter)

        self.frame_95 = QFrame(self.frame_98)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(250, 450))
        self.frame_95.setMaximumSize(QSize(250, 450))
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_95)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_95)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(245, 0))
        self.label_3.setMaximumSize(QSize(245, 40))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font: 700 18pt \"\u7b49\u7ebf\";\n"
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

        self.verticalLayout_56.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.calendar_backtest_enddate = QCalendarWidget(self.frame_95)
        self.calendar_backtest_enddate.setObjectName(u"calendar_backtest_enddate")
        self.calendar_backtest_enddate.setMinimumSize(QSize(245, 260))
        self.calendar_backtest_enddate.setMaximumSize(QSize(245, 260))
        self.calendar_backtest_enddate.setStyleSheet(u"#qt_calendar_calendarview {\n"
"     background: rgb(174, 182, 255);\n"
"}\n"
"\n"
"#qt_calendar_navigationbar {/*\u5e74\u6708\u9009\u62e9\u680f\u80cc\u666f\u8272*/\n"
"    background:rgb(255, 255, 255);\n"
"}\n"
"#qt_calendar_yearedit {\n"
"    \n"
"	font: 14pt \"\u7b49\u7ebf\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton#qt_calendar_monthbutton,#qt_calendar_yearbutton{\n"
"    \n"
"	background-color: rgb(249, 62, 255);/*\u9009\u62e9\u6708\u4efd\u548c\u5e74\u7684\u80cc\u666f*/\n"
"	height: 30px;	\n"
"	font: 14pt \"\u7b49\u7ebf\";\n"
"	width: 80px;\n"
"	border-radius:10px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar{\n"
"    \n"
"	background-color:green;/*\u9009\u62e9\u6708\u4efd\u548c\u5e74\u4e24\u8fb9\u7684\u80cc\u666f*/\n"
"	border-radius: 10px;\n"
"}\n"
"QCalendarWidget QMenu{\n"
"    \n"
"	background-color:rgb(91, 79, 255);/*\u6708\u4efd\u4e0b\u62c9\u9009\u62e9\u83dc\u5355\u7684\u80cc\u666f*/\n"
"	font: 14pt \"\u7b49\u7ebf\";\n"
"}\n"
"QToolButton#qt_calendar_prevmo"
                        "nth{/*\u5411\u5de6\u7bad\u5934*/	\n"
"	background-color: transparent;\n"
"	icon-size:30px 30px;\n"
"	qproperty-icon: url(:/\u56fe\u6807/icons/\u7bad\u5934_\u5411\u5de6.svg);\n"
"	margin-left:0px;\n"
"}\n"
"QToolButton#qt_calendar_nextmonth{\n"
"    background-color: transparent;\n"
"	icon-size:30px 30px;	\n"
"	qproperty-icon: url(:/\u56fe\u6807/icons/\u7bad\u5934_\u5411\u53f3.svg);\n"
"}\n"
"QToolButton#qt_calendar_monthbutton::menu-indicator{/*\u6708\u4efd\u4e0b\u62c9\u7bad\u5934*/\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    right: -5px;\n"
"    width: 30px;\n"
"}\n"
"QCalendarWidget QAbstractItemView:enabled  { /*\u8fd9\u91cc\u662f\u5f53\u6708\u6708\u4efd\u65e5\u671f\u7684\u6837\u5f0f*/\n"
"    color: black;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 174, 0);    \n"
"	font: 700 10pt \"\u7b49\u7ebf\";\n"
"}\n"
" /*\u8fd9\u91cc\u662f\u5176\u4ed6\u6708\u4efd\u65e5\u671f\u7684\u6837\u5f0f*/\n"
"QCalendarWidget QAbstractItem"
                        "View:disabled \n"
"{     \n"
"color: rgb(147, 147, 147); \n"
"}")

        self.verticalLayout_56.addWidget(self.calendar_backtest_enddate, 0, Qt.AlignHCenter)

        self.label_backtest_enddate = QLabel(self.frame_95)
        self.label_backtest_enddate.setObjectName(u"label_backtest_enddate")
        self.label_backtest_enddate.setMinimumSize(QSize(200, 40))
        self.label_backtest_enddate.setMaximumSize(QSize(200, 40))
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

        self.verticalLayout_56.addWidget(self.label_backtest_enddate, 0, Qt.AlignHCenter)


        self.horizontalLayout_55.addWidget(self.frame_95, 0, Qt.AlignHCenter)


        self.verticalLayout_58.addWidget(self.frame_98)

        self.frame_99 = QFrame(self.frame_97)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(0, 100))
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.Btn_start_backtest = QPushButton(self.frame_99)
        self.Btn_start_backtest.setObjectName(u"Btn_start_backtest")
        self.Btn_start_backtest.setMinimumSize(QSize(300, 40))
        self.Btn_start_backtest.setMaximumSize(QSize(300, 50))
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

        self.horizontalLayout_56.addWidget(self.Btn_start_backtest)


        self.verticalLayout_58.addWidget(self.frame_99)

        self.frame_77 = QFrame(self.frame_97)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(0, 100))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.Btn_clear_backtest_parameters = QPushButton(self.frame_77)
        self.Btn_clear_backtest_parameters.setObjectName(u"Btn_clear_backtest_parameters")
        self.Btn_clear_backtest_parameters.setMinimumSize(QSize(300, 40))
        self.Btn_clear_backtest_parameters.setMaximumSize(QSize(300, 50))
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

        self.horizontalLayout_44.addWidget(self.Btn_clear_backtest_parameters)


        self.verticalLayout_58.addWidget(self.frame_77)


        self.horizontalLayout_53.addWidget(self.frame_97)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_8)


        self.verticalLayout_48.addWidget(self.frame_78)

        self.stackedWidget.addWidget(self.fifth_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.Container)


        self.verticalLayout.addWidget(self.body)

        self.buttonframe = QFrame(self.frame_55)
        self.buttonframe.setObjectName(u"buttonframe")
        self.buttonframe.setMinimumSize(QSize(0, 20))
        self.buttonframe.setMaximumSize(QSize(16777215, 20))
        self.buttonframe.setStyleSheet(u"QFrame {\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"")
        self.buttonframe.setFrameShape(QFrame.StyledPanel)
        self.buttonframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.buttonframe)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 5, 0, 0)
        self.label_eduition = QLabel(self.buttonframe)
        self.label_eduition.setObjectName(u"label_eduition")
        sizePolicy3.setHeightForWidth(self.label_eduition.sizePolicy().hasHeightForWidth())
        self.label_eduition.setSizePolicy(sizePolicy3)
        self.label_eduition.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 85, 0);\n"
"font: 10pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")

        self.horizontalLayout_15.addWidget(self.label_eduition)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)

        self.label_current_time = QLabel(self.buttonframe)
        self.label_current_time.setObjectName(u"label_current_time")
        sizePolicy1.setHeightForWidth(self.label_current_time.sizePolicy().hasHeightForWidth())
        self.label_current_time.setSizePolicy(sizePolicy1)
        self.label_current_time.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 12pt \"\u7b49\u7ebf\";\n"
"border-radius: 15px;\n"
"border: none;")

        self.horizontalLayout_15.addWidget(self.label_current_time, 0, Qt.AlignRight)

        self.horizontalSpacer_4 = QSpacerItem(70, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.buttonframe)


        self.horizontalLayout_32.addWidget(self.frame_55)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_add_clients_name.setBuddy(self.clients_name)
        self.label_clients_ID.setBuddy(self.clients_id)
        self.label_clients_tel.setBuddy(self.clients_tel)
        self.label_clients_address.setBuddy(self.clients_address)
        self.label_select_clients_name0.setBuddy(self.comboBox_select_clients_name0)
        self.label_tq_account.setBuddy(self.tq_account)
        self.label_tq_psd.setBuddy(self.tq_psd)
        self.label_futures_company.setBuddy(self.futures_company)
        self.label_futures_account.setBuddy(self.futures_account)
        self.label_futures_psd.setBuddy(self.futures_psd)
        self.label_select_clients_name1.setBuddy(self.comboBox_select_clients_name1)
        self.label_select_tq_account.setBuddy(self.comboBox_select_tq_account)
        self.label_select_strategy.setBuddy(self.comboBox_select_strategy)
        self.label_whether_self_start.setBuddy(self.checkBox_whether_self_start)
        self.label_whether_live_futures_trading.setBuddy(self.checkBox_whether_live_futures_trading)
        self.label_whether_web_services.setBuddy(self.checkBox_whether_whether_web_services)
        self.label_web_port.setBuddy(self.web_port)
        self.label_exchange.setBuddy(self.comboBox_exchange)
        self.label_symbol.setBuddy(self.symbol)
        self.label_symbol_period.setBuddy(self.symbol_period)
        self.label_initial_capital.setBuddy(self.initial_capital)
        self.label_orientation.setBuddy(self.orientation)
        self.label_contract_multiples.setBuddy(self.contract_multiples)
        self.label_margin_rate.setBuddy(self.margin_rate)
        self.label_stop_loss.setBuddy(self.stop_loss)
        self.label_stop_profit.setBuddy(self.stop_profit)
        self.label_backtest_select_tq_account.setBuddy(self.comboBox_backtest_select_tq_account)
        self.label_backtest_select_strategy.setBuddy(self.comboBox_backtest_select_strategy)
        self.label_backtest_exchange.setBuddy(self.comboBox_backtest_exchange)
        self.label_backtest_symbol.setBuddy(self.backtest_symbol)
        self.label_backtest_symbol_period.setBuddy(self.backtest_symbol_period)
        self.label_backtest_initial_capital.setBuddy(self.backtest_initial_capital)
        self.label_backtest_web_port.setBuddy(self.backtest_web_port)
        self.label_backtest_orientation.setBuddy(self.backtest_orientation)
        self.label_backtest_contract_multiples.setBuddy(self.backtest_contract_multiples)
        self.label_backtest_margin_rate.setBuddy(self.backtest_margin_rate)
        self.label_backtest_stop_loss.setBuddy(self.backtest_stop_loss)
        self.label_backtest_stop_profit.setBuddy(self.backtest_stop_profit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.Btn_setting, self.Btn_donation)
        QWidget.setTabOrder(self.Btn_donation, self.Btn_warning)
        QWidget.setTabOrder(self.Btn_warning, self.Btn_opne_in_excel1)
        QWidget.setTabOrder(self.Btn_opne_in_excel1, self.Btn_min_window)
        QWidget.setTabOrder(self.Btn_min_window, self.Btn_normal_max_window)
        QWidget.setTabOrder(self.Btn_normal_max_window, self.Btn_close_window)
        QWidget.setTabOrder(self.Btn_close_window, self.textBrowser_terminal)

        self.retranslateUi(MainWindow)
        self.Btn_min_window.clicked.connect(MainWindow.showMinimized)
        self.pushButton_cleartext.clicked.connect(self.textBrowser_terminal.clear)
        self.checkBox_whether_whether_web_services.toggled.connect(self.web_port.setEnabled)

        self.Veiw_Box.setCurrentIndex(4)
        self.Veiw_Box.layout().setSpacing(6)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_account.setCurrentIndex(3)
        self.tabWidget_chart.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_switch_left_panel.setText("")
        self.Btn_homepage.setText(QCoreApplication.translate("MainWindow", u"\u9996\n"
"\u9875", None))
        self.Btn_account_manage.setText(QCoreApplication.translate("MainWindow", u"\u5e10\n"
"\u6237\n"
"\u7ba1\n"
"\u7406", None))
        self.Btn_trading_log.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\n"
"\u6613\n"
"\u65e5\n"
"\u5fd7", None))
        self.Btn_chart_details.setText(QCoreApplication.translate("MainWindow", u"\u56fe\n"
"\u8868\n"
"\u8be6\n"
"\u60c5", None))
        self.Btn_strategy_backtest.setText(QCoreApplication.translate("MainWindow", u"\u7b56\n"
"\u7565\n"
"\u56de\n"
"\u6d4b", None))
        self.Btn_previous_page.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\n"
"\u4e00\n"
"\u9875", None))
        self.Btn_next_page.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\n"
"\u4e00\n"
"\u9875", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_tital.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u7a0b\u4ea4\u6613\u8005  \u7a0b\u5e8f\u5316\u671f\u8d27\u4ea4\u6613\u6846\u67b6", None))
        self.Btn_setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.Btn_donation.setText(QCoreApplication.translate("MainWindow", u"\u6350\u52a9\u4f5c\u8005", None))
        self.Btn_warning.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Btn_min_window.setText("")
        self.Btn_normal_max_window.setText("")
        self.Btn_close_window.setText("")
#if QT_CONFIG(whatsthis)
        self.Veiw_Box.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u5e10\u6237\u5217\u8868</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Veiw_Box.setItemText(self.Veiw_Box.indexOf(self.clients_list_page), QCoreApplication.translate("MainWindow", u"\u7528\u6237\u5217\u8868", None))
        self.Veiw_Box.setItemText(self.Veiw_Box.indexOf(self.tq_account_list_page), QCoreApplication.translate("MainWindow", u"\u5929\u52e4\u5e10\u6237\u5217\u8868", None))
        self.Veiw_Box.setItemText(self.Veiw_Box.indexOf(self.strategy_list_page), QCoreApplication.translate("MainWindow", u"\u7b56\u7565\u5217\u8868", None))
        self.Veiw_Box.setItemText(self.Veiw_Box.indexOf(self.qoute_list_page), QCoreApplication.translate("MainWindow", u"\u8ba2\u9605\u884c\u60c5\u5217\u8868", None))
        self.Veiw_Box.setItemText(self.Veiw_Box.indexOf(self.process_list_page), QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u4e2d\u7684\u8fdb\u7a0b\u5217\u8868", None))
        self.Btn_kill_all_process.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u6240\u6709\u7b56\u7565\u5b9e\u4f8b", None))
        self.Btn_start_all_stoped_strategy.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u6240\u6709\u7b56\u7565\u5b9e\u4f8b", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u6210\u4ea4\u8be6\u60c5:", None))
        self.Btn_opne_in_excel1.setText(QCoreApplication.translate("MainWindow", u"  \u5728Excel\u4e2d\u6253\u5f00", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u4e2d\u7684\u7b56\u7565\u6570", None))
        self.label_runing_process_quantity.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u603b\u76c8\u5229", None))
        self.label_total_profit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u7a0b\u6302\u6389\u540e\n"
"\u91cd\u542f\u6b21\u6570", None))
        self.label_process_reboot_quantity.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5929\u52e4\u5e10\u6237\u6570", None))
        self.label_tq_account_quantity.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"CPU\u5360\u7528\u7387", None))
        self.label_cpu_occupancy.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6846\u67b6\u65e0\u6545\u969c\n"
"\u8fd0\u884c\u65f6\u957f", None))
        self.label_frame_runing_time.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u7aef\u8f93\u51fa\u4fe1\u606f:", None))
        self.pushButton_cleartext.setText(QCoreApplication.translate("MainWindow", u" \u6e05\u7a7a\u663e\u793a\u5185\u5bb9", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u5e10\u6237\u7edf\u8ba1\u56fe\uff1a", None))
#if QT_CONFIG(whatsthis)
        self.tabWidget_account.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u7528\u6237\u6982\u89c8</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_client_photo_show.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_clent_details.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u8be6\u60c5\uff1a", None))
        self.label_tital_2.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u60f3\u8981\u6dfb\u52a0\u7684\u5ba2\u6237\u8d44\u6599 ", None))
        self.label_add_clients_name.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.label_clients_ID.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u8eab\u4efd\u8bc1 ", None))
        self.label_clients_tel.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u7535\u8bdd", None))
        self.label_clients_address.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u8054\u7cfb\u5730\u5740 ", None))
        self.Btn_select_clients_photo_address.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u9009\u62e9\u7528\u6237\u7167\u7247", None))
        self.Btn_add_clients.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a\u6dfb\u52a0", None))
        self.Btn_cancel_input_clients.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88\u8f93\u5165", None))
        self.tabWidget_account.setTabText(self.tabWidget_account.indexOf(self.tab_user_manage), QCoreApplication.translate("MainWindow", u"\u7528\u6237\u7ba1\u7406", None))
        self.label_tq_account_details.setText(QCoreApplication.translate("MainWindow", u"\u5929\u52e4\u5e10\u6237\u8be6\u60c5\uff1a", None))
        self.label_tital_3.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u60f3\u8981\u6dfb\u52a0\u7684\u5ba2\u6237\u7684 \u5929\u52e4\u5e10\u6237 ", None))
        self.label_select_clients_name0.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7528\u6237", None))
        self.label_tq_account.setText(QCoreApplication.translate("MainWindow", u"\u5929\u52e4\u5e10\u6237", None))
        self.label_tq_psd.setText(QCoreApplication.translate("MainWindow", u"\u5929\u52e4\u5bc6\u7801 ", None))
        self.label_futures_company.setText(QCoreApplication.translate("MainWindow", u"\u671f\u8d27\u516c\u53f8 ", None))
        self.label_futures_account.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u76d8\u8d44\u91d1\u5e10\u6237 ", None))
        self.label_futures_psd.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u76d8\u8d44\u91d1\u5bc6\u7801", None))
        self.Btn_add_tq_account.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a\u6dfb\u52a0", None))
        self.Btn_cancel_input_tq_account.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88\u8f93\u5165", None))
        self.tabWidget_account.setTabText(self.tabWidget_account.indexOf(self.tab_tq_account_mamnage), QCoreApplication.translate("MainWindow", u"\u5929\u52e4\u5e10\u6237\u7ba1\u7406", None))
        self.label_tital_4.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u7b56\u7565\u8fdb\u7a0b\u8fd0\u884c\u6240\u9700\u8981\u7684\u53c2\u6570", None))
        self.label_select_clients_name1.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7528\u6237 ", None))
        self.label_select_tq_account.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5929\u52e4\u5e10\u6237", None))
        self.label_select_strategy.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7b56\u7565", None))
        self.label_whether_self_start.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u4e3a\u81ea\u542f\u8fdb\u7a0b", None))
        self.label_whether_live_futures_trading.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u4e3a\u5b9e\u76d8", None))
        self.label_whether_web_services.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u5f00\u542fweb", None))
        self.label_web_port.setText(QCoreApplication.translate("MainWindow", u"web\u7aef\u53e3\u53f7", None))
        self.label_exchange.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613\u6240", None))
        self.checkBox_whether_self_start.setText(QCoreApplication.translate("MainWindow", u"\u6b64\u5904\u52fe\u7ea2\u4e3a\u81ea\u542f", None))
        self.checkBox_whether_live_futures_trading.setText(QCoreApplication.translate("MainWindow", u"\u6b64\u5904\u52fe\u7ea2\u4e3a\u5b9e\u76d8", None))
        self.checkBox_whether_whether_web_services.setText(QCoreApplication.translate("MainWindow", u"\u52fe\u7ea2\u5f00\u542fweb", None))
        self.comboBox_exchange.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5927\u5546\u6240 DCE", None))
        self.comboBox_exchange.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e0a\u671f\u6240 SHFE", None))
        self.comboBox_exchange.setItemText(2, QCoreApplication.translate("MainWindow", u"\u90d1\u5546\u6240 CZCE", None))
        self.comboBox_exchange.setItemText(3, QCoreApplication.translate("MainWindow", u"\u80fd\u6e90\u4ea4\u6613\u6240 INE", None))
        self.comboBox_exchange.setItemText(4, QCoreApplication.translate("MainWindow", u"\u4e2d\u91d1\u6240 CFFEX", None))

        self.label_symbol.setText(QCoreApplication.translate("MainWindow", u"\u5408\u7ea6\u540d", None))
        self.label_symbol_period.setText(QCoreApplication.translate("MainWindow", u"\u5408\u7ea6\u5468\u671f(\u5206\u949f)", None))
        self.label_initial_capital.setText(QCoreApplication.translate("MainWindow", u"\u7b56\u7565\u521d\u59cb\u8d44\u91d1", None))
        self.label_orientation.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613\u65b9\u5411", None))
        self.label_contract_multiples.setText(QCoreApplication.translate("MainWindow", u"\u5408\u7ea6\u500d\u6570", None))
        self.label_margin_rate.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u8bc1\u91d1\u7387\uff08%\uff09", None))
        self.label_stop_loss.setText(QCoreApplication.translate("MainWindow", u"\u6b62\u635f\u4f4d\uff08%\uff09", None))
        self.label_stop_profit.setText(QCoreApplication.translate("MainWindow", u"\u6b62\u76c8\u4f4d\uff08%\uff09", None))
        self.contract_multiples.setText("")
        self.margin_rate.setText("")
        self.Btn_add_process_param.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a\u6dfb\u52a0", None))
        self.Btn_cancel_input_process_param.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88\u8f93\u5165", None))
        self.tabWidget_account.setTabText(self.tabWidget_account.indexOf(self.tab_add_strategy), QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u65b0\u7b56\u7565\u8fdb\u7a0b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7ebf\u7a0b\u914d\u7f6e\u8868", None))
        self.Btn_opne_in_excel2.setText(QCoreApplication.translate("MainWindow", u"  \u5728Excel\u4e2d\u6253\u5f00", None))
        self.Btn_save_charge.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u66f4\u6539", None))
        self.tabWidget_account.setTabText(self.tabWidget_account.indexOf(self.tab_start_stop_strategy), QCoreApplication.translate("MainWindow", u"\u7b56\u7565\u53c2\u6570\u603b\u89c8", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u6587\u4ef6\u8be6\u60c5\uff1a", None))
        self.label_log_file_name.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5730\u5740\uff1a", None))
        self.label_log_file_address.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u6587\u4ef6\u5217\u8868\uff1a", None))
        self.Btn_update_treeview.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u6587\u4ef6\u5217\u8868", None))
        self.pushButton_account_manage_5.setText(QCoreApplication.translate("MainWindow", u"\u5404\u8fdb\u7a0b\u7b56\u7565\u76c8\u4e8f\u60c5\u51b5", None))
        self.tabWidget_chart.setTabText(self.tabWidget_chart.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u67f1\u72b6\u56fe", None))
        self.pushButton_account_manage_3.setText(QCoreApplication.translate("MainWindow", u"\u76c8\u4e8f\u56fe\u8868", None))
        self.tabWidget_chart.setTabText(self.tabWidget_chart.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u6298\u7ebf\u56fe", None))
        self.pushButton_account_manage_7.setText(QCoreApplication.translate("MainWindow", u"\u76c8\u4e8f\u5360\u6bd4", None))
        self.tabWidget_chart.setTabText(self.tabWidget_chart.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u997c\u72b6\u56fe", None))
        self.pushButton_account_manage_8.setText(QCoreApplication.translate("MainWindow", u"\u7b56\u7565\u5b9e\u4f8b\u5f52\u5c5e\u5173\u7cfb\u56fe", None))
        self.tabWidget_chart.setTabText(self.tabWidget_chart.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"\u6851\u57fa\u56fe", None))
        self.pushButton_account_manage_9.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u9605\u7684k\u7ebf\u56fe", None))
        self.tabWidget_chart.setTabText(self.tabWidget_chart.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"K\u7ebf\u56fe", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u56de\u6d4b\u53c2\u6570:", None))
        self.Btn_open_with_chrome.setText(QCoreApplication.translate("MainWindow", u" \u5728\u6d4f\u89c8\u5668\u4e2d\u6253\u5f00\u56de\u6d4b\u9875", None))
        self.label_backtest_select_tq_account.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5929\u52e4\u5e10\u6237", None))
        self.label_backtest_select_strategy.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7b56\u7565", None))
        self.label_backtest_exchange.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613\u6240", None))
        self.label_backtest_symbol.setText(QCoreApplication.translate("MainWindow", u"\u5408\u7ea6\u540d", None))
        self.label_backtest_symbol_period.setText(QCoreApplication.translate("MainWindow", u"\u5408\u7ea6\u5468\u671f", None))
        self.label_backtest_initial_capital.setText(QCoreApplication.translate("MainWindow", u"\u7b56\u7565\u521d\u59cb\u8d44\u91d1", None))
        self.label_backtest_web_port.setText(QCoreApplication.translate("MainWindow", u"web\u7aef\u53e3\u53f7", None))
        self.label_backtest_orientation.setText(QCoreApplication.translate("MainWindow", u"\u4ea4\u6613\u65b9\u5411", None))
        self.label_backtest_contract_multiples.setText(QCoreApplication.translate("MainWindow", u"\u5408\u7ea6\u500d\u6570", None))
        self.label_backtest_margin_rate.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u8bc1\u91d1\u7387\uff08%\uff09", None))
        self.label_backtest_stop_loss.setText(QCoreApplication.translate("MainWindow", u"\u6b62\u635f\u4f4d\uff08%\uff09", None))
        self.label_backtest_stop_profit.setText(QCoreApplication.translate("MainWindow", u"\u6b62\u76c8\u4f4d\uff08%\uff09", None))
        self.comboBox_backtest_exchange.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5927\u5546\u6240 DCE", None))
        self.comboBox_backtest_exchange.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e0a\u671f\u6240 SHFE", None))
        self.comboBox_backtest_exchange.setItemText(2, QCoreApplication.translate("MainWindow", u"\u90d1\u5546\u6240 CZCE", None))
        self.comboBox_backtest_exchange.setItemText(3, QCoreApplication.translate("MainWindow", u"\u80fd\u6e90\u4ea4\u6613\u6240 INE", None))
        self.comboBox_backtest_exchange.setItemText(4, QCoreApplication.translate("MainWindow", u"\u4e2d\u91d1\u6240 CFFEX", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u56de\u6d4b\u5f00\u59cb\u65e5\u671f", None))
        self.label_backtest_startdate.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7684\u5f00\u59cb\u65e5\u671f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u56de\u6d4b\u7ed3\u675f\u65e5\u671f", None))
        self.label_backtest_enddate.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7684\u7ed3\u675f\u65e5\u671f", None))
        self.Btn_start_backtest.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u56de\u6d4b", None))
        self.Btn_clear_backtest_parameters.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u53c2\u6570", None))
        self.label_eduition.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u7a0b\u4ea4\u6613\u8005--\u57fa\u4e8e\u5929\u52e4\u7684\u7a0b\u5e8f\u5316\u4ea4\u6613\u6846\u67b61.00", None))
        self.label_current_time.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u65f6\u95f4", None))
    # retranslateUi

