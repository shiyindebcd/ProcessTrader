# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Exit_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 250)
        Dialog.setMaximumSize(QSize(600, 250))
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(600, 250))
        self.frame.setMaximumSize(QSize(600, 250))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: 1px solid rgb(65, 51, 156);\n"
"	border-radius: 20px;\n"
"}\n"
"QFrame:hover {\n"
"	border: 2px solid rgb(255, 85, 0);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: none;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 20, 0, 10)
        self.label_tital_4 = QLabel(self.frame_4)
        self.label_tital_4.setObjectName(u"label_tital_4")
        self.label_tital_4.setMaximumSize(QSize(16777215, 50))
        self.label_tital_4.setStyleSheet(u"font: 700 18pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 127);\n"
"border: none;")
        self.label_tital_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_tital_4, 0, Qt.AlignHCenter)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 18pt \"\u7b49\u7ebf\";\n"
"color: rgb(255, 0, 0);\n"
"border: none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"}\n"
"QFrame:hover {\n"
"	border: none;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_3)
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
        self.Btn_determine_exit = QPushButton(self.frame_39)
        self.Btn_determine_exit.setObjectName(u"Btn_determine_exit")
        self.Btn_determine_exit.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_determine_exit.sizePolicy().hasHeightForWidth())
        self.Btn_determine_exit.setSizePolicy(sizePolicy)
        self.Btn_determine_exit.setMinimumSize(QSize(180, 40))
        self.Btn_determine_exit.setMaximumSize(QSize(180, 40))
        self.Btn_determine_exit.setStyleSheet(u"QPushButton{	\n"
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
        self.Btn_determine_exit.setIconSize(QSize(20, 20))
        self.Btn_determine_exit.setCheckable(True)
        self.Btn_determine_exit.setChecked(False)

        self.horizontalLayout_20.addWidget(self.Btn_determine_exit, 0, Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.frame_39)

        self.frame_45 = QFrame(self.frame_3)
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
        self.Btn_cancel_exit = QPushButton(self.frame_45)
        self.Btn_cancel_exit.setObjectName(u"Btn_cancel_exit")
        self.Btn_cancel_exit.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Btn_cancel_exit.sizePolicy().hasHeightForWidth())
        self.Btn_cancel_exit.setSizePolicy(sizePolicy1)
        self.Btn_cancel_exit.setMinimumSize(QSize(180, 40))
        self.Btn_cancel_exit.setMaximumSize(QSize(180, 40))
        self.Btn_cancel_exit.setStyleSheet(u"QPushButton{	\n"
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
        self.Btn_cancel_exit.setIconSize(QSize(19, 20))

        self.horizontalLayout_30.addWidget(self.Btn_cancel_exit, 0, Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.frame_45)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)
        self.Btn_cancel_exit.clicked.connect(Dialog.hide)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_tital_4.setText(QCoreApplication.translate("Dialog", u"\u9000\u51fa\u540e\uff0c\u6240\u6709\u6b63\u5728\u8fd0\u884c\u7684\u7b56\u7565\u90fd\u5c06\u4f1a\u5173\u95ed\u3002", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a\u8981\u9000\u51fa\uff1f", None))
        self.Btn_determine_exit.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a\u9000\u51fa", None))
        self.Btn_cancel_exit.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88\u9000\u51fa", None))
    # retranslateUi

