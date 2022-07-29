# -*- coding: utf-8 -*-

import datetime
from os import path
import sys
import time
import multiprocessing
import PySide6
import pandas as pd
import importlib
from pandas import DataFrame
from datetime import datetime
from multiprocessing import Process, Manager
import PySide6
from PySide6 import QtCore, QtGui
from PySide6.QtCharts import QChart
from PySide6.QtCore import QEventLoop, QStringListModel, QTimer
from PySide6.QtGui import QCursor, QStandardItem, QStandardItemModel, Qt, QPixmap
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QTableWidgetItem, QWidget, QDialog)
from PySide6.QtWidgets import QMessageBox

from dtview import DonutWidget
from mainwindows import Ui_MainWindow
from Exit_dialog import Ui_Dialog
from Donation import Ui_Form
from Main_Process_Function import *
from read_write_file import ReadWriteCsv
#导入QMessageBox



class Exit_Dialog(QDialog, Ui_Dialog):                # 退出程序对话框类
    def __init__(self):
        super(Exit_Dialog, self).__init__()
        self.setupUi(self)

        # 不显示标题栏        
        self.setWindowFlags(QtCore.Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint))
        # 不显示空白边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 设置透明度
        self.setWindowOpacity(0.95)        
        

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


class Donation(QWidget, Ui_Form):                # 捐赠窗口类
    def __init__(self):
        super(Donation, self).__init__()
        self.setupUi(self)

        # 不显示标题栏
        flags = QtCore.Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        # 不显示空白边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # 设置透明度
        self.setWindowOpacity(0.95)

        self.label_5.setText('本项目github地址：  https://github.com/shiyindebcd/ProcessTrader   <a href="https://github.com/shiyindebcd/ProcessTrader">  点击跳转</a>')
        self.label_5.setOpenExternalLinks(True)  # 使其成为超链接
        self.label_5.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.label_6.setText('本项目gitee地址：  https://gitee.com/shiyindebcd/ProcessTrader   <a href="https://gitee.com/shiyindebcd/ProcessTrader">  点击跳转</a>')
        self.label_6.setOpenExternalLinks(True)  
        self.label_6.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.label_7.setText('B站软件用法详细解说地址：  https://www.bilibili.com   <a href="https://www.bilibili.com/video/BV1tY4y177sv?share_source=copy_web&vd_source=0f0ae5e8365c85cd112830a14d80cef6">  点击跳转</a>')
        self.label_7.setOpenExternalLinks(True)  
        self.label_7.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.label_8.setText('YouTube软件详细解说地址：  https://www.youtube.com   <a href="https://www.youtube.com">  点击跳转</a>')
        self.label_8.setOpenExternalLinks(True)  
        self.label_8.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.label_9.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_10.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_11.setTextInteractionFlags(Qt.TextBrowserInteraction)

        
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


# ui, _ = loadUiType('mainwindows.ui')                                      
# class Main_window(QMainWindow, ui, Main_Process_Function):                    # 创建主窗口类方式一，通过loadUiType()函数直接加载UI文件
class Main_window(QMainWindow, Ui_MainWindow, Main_Process_Function):       # 创建主窗口类方式二，通过继承Ui_MainWindow类
    def __init__(self):
        super(Main_window, self).__init__()
        self.start_time = datetime.now()                                # 记录程序开始时间
        self.times = 0                                                  # 进程守护定时器计数
        # self.left_panel_statuses = 0                                   # 左侧面板状态
        
        self.setupUi(self)
        self.setWindowOpacity(0.97)                                     # 设置窗口透明度

        self.cwd = os.getcwd()                                          # 获取当前路径
        self.Process_dict = {}                                          # 创建进程字典

        # #定义进程锁
        # self.thread_lock = process.Lock()   



        # 将输出重定向到textBrowser中
        sys.stdout = EmittingStr()
        sys.stdout.textWritten.connect(self.outputWritten)
        # 将子进程的输出重定向到textBrowser中

        # 清屏定时器
        self.textBrowser_clear = QTimer(self)
        self.textBrowser_clear.timeout.connect(self.textBrowser_terminal.clear)        
        self.textBrowser_clear.start(1000 * 60 * 60 * 24)                   # 清屏定时器，每天清屏一次

        # 进程监控定时器
        self.process_timer = QTimer(self)
        self.process_timer.timeout.connect(self.start_inactivated_process)
        self.process_timer.start(1000 * 60)                               # 进程监控定时器，每分钟检查一次

        # 面板参数刷新定时器
        self.parameters_refresh = QTimer(self)
        self.parameters_refresh.timeout.connect(self.add_paramer_to_container)
        self.parameters_refresh.start(1000)

        self.ioModal = ReadWriteCsv()                                     # 实例化 csv 操作类

        self.ioModal.judge_config_exist(path='./data/deal_detials.csv')    # 判断配置文件是否存在，不存在则创建
        self.ioModal.judge_config_exist(path='./data/config.csv')
        self.ioModal.judge_config_exist(path='./data/clients.csv')
        self.ioModal.judge_config_exist(path='./data/tq_account.csv')

        self.Quantity = 0 - self.get_inactivated_process_quantity()
        self.add_paramer_to_combobox()

        self.Define_slot_functions()
        self.hide_items()
        self.set_tableWidget()
        self.start_inactivated_process()
        self.add_paramer_to_container()
        self.other_item_settings()
        self.process_dict_update()
        self.show_file_in_treeview()

    def hide_items(self):  # 隐藏各种滚动条虚线框及标题栏

        # 不显示主容器标题栏
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))
        # 不显示主窗口空白边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # self.textBrowser_terminal.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏水平滚动条
        # self.textBrowser_terminal.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏竖直滚动条
        # self.clients_listview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.tq_account_listview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.tq_account_listview2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.strategy_listview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.qoute_listview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.process_listview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # self.clients_listview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.tq_account_listview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.strategy_listview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.qoute_listview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.process_listview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.tableview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.tableWidget_deal_detials.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
         
        # # 隐藏点击时的虚线框
        self.clients_listview.setFocusPolicy(Qt.NoFocus)
        self.clients_listview2.setFocusPolicy(Qt.NoFocus)
        self.tq_account_listview.setFocusPolicy(Qt.NoFocus) 
        self.tq_account_listview2.setFocusPolicy(Qt.NoFocus)
        self.strategy_listview.setFocusPolicy(Qt.NoFocus)
        self.qoute_listview.setFocusPolicy(Qt.NoFocus)
        self.process_listview.setFocusPolicy(Qt.NoFocus)
        
        self.tableWidget_process.setFocusPolicy(Qt.NoFocus)   # QtableWidget隐藏点击时的虚线框
        self.tableWidget_deal_detials.setFocusPolicy(Qt.NoFocus)
        self.tabWidget_chart.setFocusPolicy(Qt.NoFocus)
        self.tabWidget_account.setFocusPolicy(Qt.NoFocus)
        self.clients_listview.setFocusPolicy(Qt.NoFocus)        # QListView隐藏点击时的虚线框
        self.tq_account_listview.setFocusPolicy(Qt.NoFocus)
        self.strategy_listview.setFocusPolicy(Qt.NoFocus)
        self.qoute_listview.setFocusPolicy(Qt.NoFocus)
        self.process_listview.setFocusPolicy(Qt.NoFocus)

        self.Btn_homepage.setFocusPolicy(Qt.NoFocus)            # 隐藏所有按钮点击时的虚线框
        self.Btn_account_manage.setFocusPolicy(Qt.NoFocus)
        self.Btn_trading_log.setFocusPolicy(Qt.NoFocus)
        self.Btn_chart_details.setFocusPolicy(Qt.NoFocus)
        self.Btn_strategy_backtest.setFocusPolicy(Qt.NoFocus)
        self.Btn_previous_page.setFocusPolicy(Qt.NoFocus)
        self.Btn_next_page.setFocusPolicy(Qt.NoFocus)
        self.Btn_start_all_stoped_strategy.setFocusPolicy(Qt.NoFocus)
        self.Btn_add_clients.setFocusPolicy(Qt.NoFocus)
        self.Btn_cancel_input_clients.setFocusPolicy(Qt.NoFocus)
        self.Btn_add_tq_account.setFocusPolicy(Qt.NoFocus)
        self.Btn_cancel_input_tq_account.setFocusPolicy(Qt.NoFocus)
        self.Btn_add_process_param.setFocusPolicy(Qt.NoFocus)
        self.Btn_cancel_input_process_param.setFocusPolicy(Qt.NoFocus)
        self.Btn_start_backtest.setFocusPolicy(Qt.NoFocus)
        self.Btn_clear_backtest_parameters.setFocusPolicy(Qt.NoFocus)
        self.Btn_switch_left_panel.setFocusPolicy(Qt.NoFocus)
        self.Btn_setting.setFocusPolicy(Qt.NoFocus)
        self.Btn_donation.setFocusPolicy(Qt.NoFocus)
        self.Btn_warning.setFocusPolicy(Qt.NoFocus)
        self.Btn_min_window.setFocusPolicy(Qt.NoFocus)
        self.Btn_normal_max_window.setFocusPolicy(Qt.NoFocus)
        self.Btn_close_window.setFocusPolicy(Qt.NoFocus)
        self.Btn_select_clients_photo_address.setFocusPolicy(Qt.NoFocus)
        self.Btn_opne_in_excel1.setFocusPolicy(Qt.NoFocus)
        self.Btn_opne_in_excel2.setFocusPolicy(Qt.NoFocus)
        self.Btn_update_treeview.setFocusPolicy(Qt.NoFocus)
        self.pushButton_cleartext.setFocusPolicy(Qt.NoFocus)
        self.Btn_kill_all_process.setFocusPolicy(Qt.NoFocus)
        self.treeview_log.setFocusPolicy(Qt.NoFocus)



    def set_tableWidget(self):  # 设置tableWidget

        # 隐藏竖直表头
        self.tableWidget_deal_detials.verticalHeader().setVisible(False)
        self.tableWidget_process.verticalHeader().setVisible(False)

        # tablewidget单击选中整行
        self.tableWidget_deal_detials.setSelectionBehavior(PySide6.QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_process.setSelectionBehavior(PySide6.QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)

        # tablewidget 设置水平表头高度
        self.tableWidget_deal_detials.horizontalHeader().setFixedHeight(30)
        self.tableWidget_process.horizontalHeader().setFixedHeight(30)  

        # 指定列宽
        self.tableWidget_deal_detials.setColumnWidth(0, 200)

        self.tableWidget_process.setColumnWidth(0, 40)
        self.tableWidget_process.setColumnWidth(1, 450)
        self.tableWidget_process.setColumnWidth(18, 150)

        # 设置表头标题        
        process_list_header = ['序号', '进程名（策略实例名）', '客户名', '天勤帐户', '天勤密码', '期货公司', '期货帐户', '期货资金密码', 
                                '合约名称', '合约周期', '策略名称', '是否自启', '是否实盘', '是否回测', '是否开启web', 'web端口','停止交易标志', 
                                '交易方向', '初始资金', '当前资金',  '合约倍数', '保证金率', '止损位%', '止盈位%', '多单加仓次数', '多单当前持仓', 
                                '多单首次成交价', '多单首次成交量','空单加仓次数', '空单首次成交价', '空单首次成交量', '空单当前持仓', 
                                '可选参数N1', '可选参数N2', '可选参数N3', '可选参数N4', '可选参数N5', '可选参数N6']
        self.tableWidget_process.setHorizontalHeaderLabels(process_list_header)

        


    def Define_slot_functions(self):  # 定义各种槽函数
        self.Btn_switch_left_panel.clicked.connect(lambda: self.switch_left_panel(True))
        self.Btn_normal_max_window.clicked.connect(self.maxmize_normalmize)
        self.Btn_homepage.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.Btn_account_manage.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.Btn_account_manage.clicked.connect(self.add_paramer_to_combobox)
        self.Btn_trading_log.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.Btn_chart_details.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.Btn_strategy_backtest.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.Btn_previous_page.clicked.connect(self.previous_page)
        self.Btn_next_page.clicked.connect(self.next_page)
        self.Btn_start_all_stoped_strategy.clicked.connect(self.start_inactivated_process)
        self.Btn_close_window.clicked.connect(self.show_exit_dialog)
        self.Btn_add_clients.clicked.connect(self.get_clients)
        self.Btn_cancel_input_clients.clicked.connect(self.clients_input_clear)
        self.Btn_add_tq_account.clicked.connect(self.get_tq_account)
        self.Btn_cancel_input_tq_account.clicked.connect(self.tq_account_input_clear)
        self.Btn_add_process_param.clicked.connect(self.get_process_parameters)
        self.Btn_cancel_input_process_param.clicked.connect(self.process_parameters_input_clear)
        self.Btn_donation.clicked.connect(self.show_donation_window)
        self.calendar_backtest_startdate.selectionChanged.connect(self.get_backtest_date)
        self.calendar_backtest_enddate.selectionChanged.connect(self.get_backtest_date)
        self.Btn_start_backtest.clicked.connect(self.get_backtest_parameters)
        self.Btn_clear_backtest_parameters.clicked.connect(self.backtest_parameters_input_clear)
        self.Btn_select_clients_photo_address.clicked.connect(self.choose_client_photo_File)
        self.Btn_kill_all_process.clicked.connect(self.kill_all_process)
        self.Btn_update_treeview.clicked.connect(self.show_file_in_treeview)

        self.treeview_log.clicked.connect(self.on_tree_licked)

        self.Btn_opne_in_excel1.clicked.connect(lambda: self.open_file_with_excel(path='./data/deal_detials.csv'))
        self.Btn_opne_in_excel2.clicked.connect(lambda: self.open_file_with_excel(path='./data/config.csv'))
        self.Btn_open_with_chrome.clicked.connect(self.open_sys_browser)

        #列表框槽函数
        self.clients_listview2.clicked.connect(self.show_clients_info)
        self.tq_account_listview2.clicked.connect(self.show_tq_account_info)

        self.load_deal_detials_data()
        self.load_process_config()
        self.draw_dount_chart()

    def other_item_settings(self):    # 其他设置
        self.m_drag = False
        self.label_logo.setPixmap(QPixmap('./logo/logo.png'))           # 加载logo图片     
        self.label_logo.setScaledContents(True)                         # 设置图片自适应
        self.label_client_photo_show.setScaledContents(True)   


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

    def show_exit_dialog(self):     # 退出程序
        self.exit_dialog = Exit_Dialog()
        self.exit_dialog.show()
        self.exit_dialog.Btn_determine_exit.clicked.connect(self.kill_all_process)
        self.exit_dialog.Btn_determine_exit.clicked.connect(QApplication.instance().quit)
        self.exit_dialog.exec()

    def show_donation_window(self):
        self.donation = Donation()
        self.donation.show()                   

    def start_backtest_process(self, tuple):    # 启动回测进程
        
        module = 'strategys' + '.' + tuple[1]['strategy']
        strategy_class_name = tuple[1]['strategy']

        m = importlib.import_module(module)  # 导入模块
        my_class = getattr(m, strategy_class_name)  # 获取类

        t = my_class(args=tuple)  # 实例化类
        t.setName(tuple[1]['process_name'])  # 设置进程名称
        t.start()  # 启动进程
        




    #####################################################################
    #####################下面这个函数是进程自启的核心代码 #####################


    def start_inactivated_process(self):  # 根据 csv 文件启动未运行的策略
        living_pid_list = self.get_alive_process_pid_list()
        if self.times > 0:
            self.times += 1
            path = './data/config.csv'
            data = self.ioModal.read_csv_file(path)

            if data.empty:
                print('策略实例配置文件 config.csv 为空,请添加参数后再运行...')
            else:
            
                for index, item in data.iterrows():
                    if item['whether_self_start'] == True:

                        if self.Process_dict[item['process_name']] in living_pid_list:
                            pass
                        else:
                            # 根据一个字符串的名称,自动实例化模块下的类

                            module = 'strategys' + '.' + item['strategy']
                            strategy_class_name = item['strategy']

                            m = importlib.import_module(module)             # 导入模块
                            my_class = getattr(m, strategy_class_name)      # 获取类

                            t = my_class(args=(index, data.iloc[index]))    # 实例化类                            
                            t.name = item['process_name']                 # 设置进程名称
                            t.start()  # 启动进程
                            self.Process_dict[item['process_name']] = t.pid

                            if self.Quantity < 1:                           # 区分第一次启动和非第一次启动
                                print('进程 ', item['process_name'], '  已启动!')
                                print('启动时间为: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '\n\n')
                            else:
                                print('进程 ', item['process_name'], '  意外中止,现已重启!!!')
                                print('重启时间为: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '\n\n')

                            self.Quantity += 1
                            if self.Quantity > 0:                                
                                self.label_process_reboot_quantity.setText(str(self.Quantity))
                            elif self.Quantity == 0:
                                self.label_process_reboot_quantity.setText('进程已全部启动')                                
                            else:
                                self.label_process_reboot_quantity.setText('进程启动中\n还没启动完')


                            self.add_paramer_to_container()
                            time.sleep(1)
                    else:
                        pass
        else:
            print('\n\n\n策略将在主程序启动一分钟后，按 config.csv 文件中的配置逐个启动\n\n\n')
            self.times += 1 