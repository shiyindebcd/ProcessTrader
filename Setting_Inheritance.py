# -*- coding: utf-8 -*-

from PySide6 import QtCore
from PySide6.QtGui import QCursor, Qt
from PySide6.QtWidgets import (QDialog)
import pandas as pd
from read_write_file import ReadWriteCsv

from UI.Setting_dark import Ui_Dialog as UI_dark
from UI.Setting_light import Ui_Dialog as UI_light

from main import THEME

if THEME == "dark":
    UI = UI_dark
else:
    UI = UI_light


class SettingDialog(QDialog, UI):
    def __init__(self):
        super(SettingDialog, self).__init__()
        self.setupUi(self)

         # 不显示标题栏        
        self.setWindowFlags(QtCore.Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint))
        # 不显示空白边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 设置透明度
        self.setWindowOpacity(0.95)  
        self.path = './data/main_tq_account.csv' 
        
        self.RW_csv = ReadWriteCsv()                            # 实例化读写csv文件的类
        self.RW_csv.judge_config_exist(path=self.path)          # 判断main_tq_account.csv是否存在,如果不存在，则创建
        self.data = self.RW_csv.read_csv_file(path=self.path)   # 读取main_tq_account.csv文件        
        
        if self.data.empty:                                     # 判断self.data是否为空
            print('当前未配置主程序天勤帐号')
        else:    
             self.label_Account.setText('已配置天勤帐号：  ' + str(self.data.iloc[0]['tq_account']) + '   无需再配置')
            

        self.Btn_Determine_add.clicked.connect(self.get_tq_account)
        self.Btn_Determine_add.setFocusPolicy(Qt.NoFocus)
        self.Btn_clear_input.clicked.connect(self.clear_input)
        self.Btn_clear_input.setFocusPolicy(Qt.NoFocus)

        

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


    def get_tq_account(self):
        dict = {}
        # 如果main_tq_account不为空，则读取main_tq_account的值
        if (self.main_tq_account.text() != "") and (self.main_tq_account.text() is not None):   #如果帐户框和密码框都有都有输入
            
            self.RW_csv.delete_file(path=self.path)         #删除原文件
            self.RW_csv.judge_config_exist(path=self.path)  # 判断main_tq_account.csv是否存在,如果不存在，则创建
            dict['tq_account'] = self.main_tq_account.text()
            dict['qt_psd'] = self.main_tq_psd.text()
            df = pd.DataFrame(dict, index=[0])
            self.RW_csv.add_dict_to_csv(df, path=self.path)
            # print(df)
            self.label_Account.setText('已配置主程序天勤帐号：   ' + self.main_tq_account.text())
        else:
            pass       

    def clear_input(self):
        self.main_tq_account.clear()
        self.main_tq_psd.clear()