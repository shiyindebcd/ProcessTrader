# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setting_light.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 400)
        Dialog.setMinimumSize(QSize(500, 400))
        Dialog.setMaximumSize(QSize(500, 400))
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid rgb(100, 100, 100);	\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 5, -1, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(251, 238, 254);\n"
"	border: none;	\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, 0, 5, 5)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setStyleSheet(u"font: 700 18pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 0);\n"
"border: none;")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.Btn_clear_main_tq_account = QPushButton(self.frame_2)
        self.Btn_clear_main_tq_account.setObjectName(u"Btn_clear_main_tq_account")
        self.Btn_clear_main_tq_account.setMinimumSize(QSize(120, 35))
        self.Btn_clear_main_tq_account.setMaximumSize(QSize(120, 35))
        self.Btn_clear_main_tq_account.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(0, 255, 255);\n"
"	font: 700 16pt \"\u7b49\u7ebf\";\n"
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

        self.horizontalLayout_2.addWidget(self.Btn_clear_main_tq_account)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        icon = QIcon()
        icon.addFile(u":/icon/icons/\u5173\u95ed (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_close_window.setIcon(icon)
        self.Btn_close_window.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.Btn_close_window)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.frame_3.setMaximumSize(QSize(16777215, 120))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(255, 255, 222);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.label_1 = QLabel(self.frame_3)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(0, 30))
        self.label_1.setMaximumSize(QSize(450, 60))
        self.label_1.setStyleSheet(u"font: 700 12pt \"\u7b49\u7ebf\";\n"
"color: rgb(0, 170, 0);\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.label_1)

        self.label_Account = QLabel(self.frame_3)
        self.label_Account.setObjectName(u"label_Account")
        self.label_Account.setMinimumSize(QSize(0, 30))
        self.label_Account.setMaximumSize(QSize(450, 30))
        self.label_Account.setStyleSheet(u"font: 700 14pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 0);\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.label_Account)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(226, 252, 227);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame {\n"
"	background-color: none;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_Main_tqaccount = QLabel(self.frame_6)
        self.label_Main_tqaccount.setObjectName(u"label_Main_tqaccount")
        self.label_Main_tqaccount.setMinimumSize(QSize(200, 40))
        self.label_Main_tqaccount.setMaximumSize(QSize(200, 40))
        self.label_Main_tqaccount.setStyleSheet(u"QLabel {\n"
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
        self.label_Main_tqaccount.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_Main_tqaccount)

        self.label_main_tqpsd = QLabel(self.frame_6)
        self.label_main_tqpsd.setObjectName(u"label_main_tqpsd")
        self.label_main_tqpsd.setMinimumSize(QSize(200, 40))
        self.label_main_tqpsd.setMaximumSize(QSize(200, 40))
        self.label_main_tqpsd.setStyleSheet(u"QLabel {\n"
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
        self.label_main_tqpsd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_main_tqpsd)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QFrame {\n"
"	background-color: none;\n"
"	border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.main_tq_account = QLineEdit(self.frame_7)
        self.main_tq_account.setObjectName(u"main_tq_account")
        self.main_tq_account.setMinimumSize(QSize(200, 40))
        self.main_tq_account.setMaximumSize(QSize(200, 40))
        self.main_tq_account.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_4.addWidget(self.main_tq_account)

        self.main_tq_psd = QLineEdit(self.frame_7)
        self.main_tq_psd.setObjectName(u"main_tq_psd")
        self.main_tq_psd.setMinimumSize(QSize(200, 40))
        self.main_tq_psd.setMaximumSize(QSize(200, 40))
        self.main_tq_psd.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_4.addWidget(self.main_tq_psd)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"	border: none;	\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Btn_clear_input = QPushButton(self.frame_8)
        self.Btn_clear_input.setObjectName(u"Btn_clear_input")
        self.Btn_clear_input.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_clear_input.sizePolicy().hasHeightForWidth())
        self.Btn_clear_input.setSizePolicy(sizePolicy)
        self.Btn_clear_input.setMinimumSize(QSize(180, 40))
        self.Btn_clear_input.setMaximumSize(QSize(180, 40))
        self.Btn_clear_input.setStyleSheet(u"QPushButton{	\n"
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
        self.Btn_clear_input.setIconSize(QSize(19, 20))

        self.horizontalLayout_6.addWidget(self.Btn_clear_input)


        self.horizontalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Btn_Determine_add = QPushButton(self.frame_9)
        self.Btn_Determine_add.setObjectName(u"Btn_Determine_add")
        self.Btn_Determine_add.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Btn_Determine_add.sizePolicy().hasHeightForWidth())
        self.Btn_Determine_add.setSizePolicy(sizePolicy1)
        self.Btn_Determine_add.setMinimumSize(QSize(180, 40))
        self.Btn_Determine_add.setMaximumSize(QSize(180, 40))
        self.Btn_Determine_add.setStyleSheet(u"QPushButton{	\n"
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
        self.Btn_Determine_add.setIconSize(QSize(20, 20))
        self.Btn_Determine_add.setCheckable(True)
        self.Btn_Determine_add.setChecked(False)

        self.horizontalLayout_5.addWidget(self.Btn_Determine_add)


        self.horizontalLayout_4.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)

#if QT_CONFIG(shortcut)
        self.label_Main_tqaccount.setBuddy(self.main_tq_account)
        self.label_main_tqpsd.setBuddy(self.main_tq_psd)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)
        self.Btn_close_window.clicked.connect(Dialog.close)
        self.Btn_clear_main_tq_account.clicked.connect(self.main_tq_account.clear)
        self.Btn_clear_main_tq_account.clicked.connect(self.main_tq_psd.clear)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u8bf7\u8f93\u5165\u4e3b\u5929\u52e4\u8d26\u6237\u53ca\u5bc6\u7801", None))
        self.Btn_clear_main_tq_account.setText(QCoreApplication.translate("Dialog", u"\u5220\u9664\u8d26\u6237", None))
        self.Btn_close_window.setText("")
        self.label_1.setText(QCoreApplication.translate("Dialog", u"\u8be5\u5929\u52e4\u8d26\u6237\u7528\u4e8e\u5728\u4e3b\u7a0b\u5e8f\u4e2d\u663e\u793ak\u7ebf\uff0c\u5efa\u8bae\u5355\u72ec\u8bbe\u7f6e\u4e00\u4e2a\u8d26\u6237\uff0c\n"
"\u4e0d\u8981\u548c\u5b50\u8fdb\u7a0b\u7b56\u7565\u4e2d\u7684\u5929\u52e4\u8d26\u6237\u5171\u7528\uff0c\u4ee5\u514d\u5f15\u8d77\u4e00\u4e9b\u672a\u77e5\u7684\u95ee\u9898", None))
        self.label_Account.setText(QCoreApplication.translate("Dialog", u"\u5f53\u524d\u4e3b\u7a0b\u5e8f\u8fd8\u672a\u8bbe\u7f6e\u4e3b\u5929\u52e4\u8d26\u6237\uff01", None))
        self.label_Main_tqaccount.setText(QCoreApplication.translate("Dialog", u"\u5929\u52e4\u8d26\u6237", None))
        self.label_main_tqpsd.setText(QCoreApplication.translate("Dialog", u"\u5929\u52e4\u5bc6\u7801", None))
        self.Btn_clear_input.setText(QCoreApplication.translate("Dialog", u"\u6e05\u9664\u8f93\u5165", None))
        self.Btn_Determine_add.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a\u6dfb\u52a0", None))
    # retranslateUi

