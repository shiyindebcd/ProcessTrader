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
from datetime import datetime, date
from multiprocessing import Process, Manager
import PySide6
import pyqtgraph as pg
from PySide6 import QtCore, QtGui
from PySide6.QtCharts import QChart
from PySide6.QtCore import QEventLoop, QStringListModel, QTimer, Signal, QThread
from PySide6.QtGui import QCursor, QStandardItem, QStandardItemModel, Qt, QPixmap
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QTableWidgetItem, QWidget, QDialog, QMenu)
from PySide6.QtWidgets import QMessageBox, QHeaderView
from tqsdk import TqApi, TqAuth, TargetPosTask, TqKq, TqBacktest, ta, tafunc
from dtview import DonutWidget
import mainwindows_dark
import mainwindows_light
from Main_Process_Function import *
from K_Chart_Widget import KLineWidget
from read_write_file import ReadWriteCsv

THEME = "dark"      # 皮肤选择 这里的THEME改为 dark 为深色模式,改为  light 为浅色模式



if THEME == "dark":
    ui, _ = loadUiType('mainwindows_dark.ui')
elif THEME == "light":
    ui, _ = loadUiType('mainwindows_light.ui')
else:
    pass

class Main_window(QMainWindow, ui, Main_Process_Function):                    # 创建主窗口类方式一，通过loadUiType()函数直接加载UI文件
    def __init__(self):
        super(Main_window, self).__init__()


# if THEME == "dark":
#     UI = mainwindows_dark.Ui_MainWindow
# elif:
#     UI = mainwindows_light.Ui_MainWindow
# else:
#     pass
# class Main_window(QMainWindow, UI, Main_Process_Function):  # 创建主窗口类方式二，通过继承Ui_MainWindow类
#     def __init__(self):
#         super(Main_window, self).__init__()



        self.setupUi(self)
        self.setWindowOpacity(0.98)                                     # 设置窗口透明度
        self.start_time = datetime.now()                                # 记录程序开始时间
        self.main_tq_account = ''                                       # 主账户
        self.main_tq__pwd = ''                                          # 主账户密码
        self.current_Kline = ''                                         # 当前显示的K线
        self.Quote_klines_dict = {}                                   # 自选合约字典,用来存放所有的自选合约klines

        # 将主进程的控制台输出重定向到textBrowser中显示
        sys.stdout = EmittingStr()
        sys.stdout.textWritten.connect(self.outputWritten)

        self.ioModal = ReadWriteCsv()                                   # 实例化 csv 操作类
        self.KLineWidget = KLineWidget()                                      # 实例化K线图widget部件
        self.verticalLayout_klines.addWidget(self.KLineWidget)               # 添加K线图部件到布局中
        self.whether_the_folder_exists()                                # 判断文件夹是否存在，不存在则创建

        self.times = 0                                                  # 进程守护定时器计数
        self.Quantity = 0 - self.get_inactivated_process_quantity()


        self.cwd = os.getcwd()                                          # 获取当前路径
        self.Process_dict = {}                                          # 创建进程字典，用于存储子进程的pid


        # 清屏定时器
        self.textBrowser_clear = QTimer(self)
        self.textBrowser_clear.timeout.connect(self.textBrowser_terminal.clear)
        self.textBrowser_clear.start(1000 * 60 * 60 * 24)                # 清屏定时器，每天清屏一次

        # 进程监控定时器
        self.process_timer = QTimer(self)
        self.process_timer.timeout.connect(self.start_inactivated_process)
        self.process_timer.start(1000 * 60)                              # 进程监控定时器，每分钟检查一次

        # 面板参数刷新定时器
        self.parameters_refresh = QTimer(self)
        self.parameters_refresh.timeout.connect(self.add_paramer_to_container)
        # self.parameters_refresh.timeout.connect(self.chack_main_tq_account)
        self.parameters_refresh.start(1000)
        self.times1 = 0                                             #用来辅助计时,程序启动20秒后才登录天勤

        self.Define_slot_functions()                                # 定义槽函数
        self.hide_items()                                           # 隐藏控件
        self.add_paramer_to_combobox()                              # 将参数添加到下拉框
        self.set_tableWidget()                                      # 设置表格
        self.add_paramer_to_container()                             # 将参数添加到容器
        self.other_item_settings()                                  # 其他控件设置
        self.process_dict_update()                                  # 更新进程字典
        self.show_file_in_treeview()                                # 显示文件到树状图
        self.load_deal_detials_data()                               # 加载交易明细数据
        self.load_process_config()                                  # 加载进程配置数据
        self.draw_dount_chart()                                     # 绘制饼图
        self.start_inactivated_process()                            # 启动未激活的进程
        # pg.setConfigOption('background', QtGui.QColor(13, 9, 27))


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


    def whether_the_folder_exists(self):    # 检查必要的文件及文件夹是否存在，不存在则创建
        # 判断文件夹是否存在，不存在则创建
        if not os.path.exists('./data'):
            os.mkdir('./data')
        if not os.path.exists('./log'):
            os.mkdir('./log')
        if not os.path.exists('./clients_photo'):
            os.mkdir('./clients_photo')

        # 判断配置文件是否存在，不存在则创建
        self.ioModal.judge_config_exist(path='./data/deal_detials.csv')
        self.ioModal.judge_config_exist(path='./data/config.csv')
        self.ioModal.judge_config_exist(path='./data/clients.csv')
        self.ioModal.judge_config_exist(path='./data/tq_account.csv')
        self.ioModal.judge_config_exist(path='./data/main_tq_account.csv')
        self.ioModal.judge_config_exist(path='./data/self_selection.csv')


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
        # self.quote_listview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.process_listview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # self.clients_listview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.tq_account_listview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.strategy_listview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.quote_listview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.process_listview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.tableview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.tableWidget_deal_detials.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # # 隐藏点击时的虚线框
        self.tableWidget_process.setFocusPolicy(Qt.NoFocus)   # QtableWidget隐藏点击时的虚线框
        self.tableWidget_deal_detials.setFocusPolicy(Qt.NoFocus)
        self.tabWidget_chart.setFocusPolicy(Qt.NoFocus)
        self.tabWidget_account.setFocusPolicy(Qt.NoFocus)

        self.clients_listview.setFocusPolicy(Qt.NoFocus)        # QListView隐藏点击时的虚线框
        self.clients_listview2.setFocusPolicy(Qt.NoFocus)
        self.tq_account_listview.setFocusPolicy(Qt.NoFocus)
        self.tq_account_listview2.setFocusPolicy(Qt.NoFocus)
        self.clients_listview.setFocusPolicy(Qt.NoFocus)
        self.tq_account_listview.setFocusPolicy(Qt.NoFocus)
        self.strategy_listview.setFocusPolicy(Qt.NoFocus)
        self.quote_listview.setFocusPolicy(Qt.NoFocus)
        self.process_listview.setFocusPolicy(Qt.NoFocus)
        self.self_selection_listview.setFocusPolicy(Qt.NoFocus)

        self.Btn_homepage.setFocusPolicy(Qt.NoFocus)            # 隐藏所有按钮点击时的虚线框
        self.Btn_account_manage.setFocusPolicy(Qt.NoFocus)
        self.Btn_trading_log.setFocusPolicy(Qt.NoFocus)
        self.Btn_chart_details.setFocusPolicy(Qt.NoFocus)
        self.Btn_previous_page.setFocusPolicy(Qt.NoFocus)
        self.Btn_next_page.setFocusPolicy(Qt.NoFocus)
        self.Btn_start_all_stoped_strategy.setFocusPolicy(Qt.NoFocus)
        self.Btn_add_clients.setFocusPolicy(Qt.NoFocus)
        self.Btn_cancel_input_clients.setFocusPolicy(Qt.NoFocus)
        self.Btn_add_tq_account.setFocusPolicy(Qt.NoFocus)
        self.Btn_cancel_input_tq_account.setFocusPolicy(Qt.NoFocus)
        self.Btn_switch_left_panel.setFocusPolicy(Qt.NoFocus)
        self.Btn_setting.setFocusPolicy(Qt.NoFocus)
        self.Btn_donation.setFocusPolicy(Qt.NoFocus)
        self.Btn_min_window.setFocusPolicy(Qt.NoFocus)
        self.Btn_normal_max_window.setFocusPolicy(Qt.NoFocus)
        self.Btn_close_window.setFocusPolicy(Qt.NoFocus)
        self.Btn_select_clients_photo_address.setFocusPolicy(Qt.NoFocus)
        self.Btn_opne_in_excel1.setFocusPolicy(Qt.NoFocus)
        self.Btn_opne_in_excel2.setFocusPolicy(Qt.NoFocus)
        self.Btn_update_treeview.setFocusPolicy(Qt.NoFocus)
        self.Btn_cleartext.setFocusPolicy(Qt.NoFocus)
        self.Btn_kill_all_process.setFocusPolicy(Qt.NoFocus)
        self.treeview_log.setFocusPolicy(Qt.NoFocus)
        self.Btn_add_new_process.setFocusPolicy(Qt.NoFocus)
        self.Btn_add_backtest_process.setFocusPolicy(Qt.NoFocus)


    def Define_slot_functions(self):  # 定义各种槽函数
        self.Btn_switch_left_panel.clicked.connect(lambda: self.switch_left_panel(True))
        self.Btn_normal_max_window.clicked.connect(self.maxmize_normalmize)
        self.Btn_homepage.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.Btn_KliensChart.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.Btn_account_manage.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.Btn_account_manage.clicked.connect(self.add_paramer_to_combobox)
        self.Btn_trading_log.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.Btn_chart_details.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.Btn_previous_page.clicked.connect(self.previous_page)
        self.Btn_next_page.clicked.connect(self.next_page)
        self.Btn_start_all_stoped_strategy.clicked.connect(self.start_inactivated_process)
        self.Btn_close_window.clicked.connect(self.show_exit_dialog)
        self.Btn_add_clients.clicked.connect(self.get_clients)
        self.Btn_cleartext.clicked.connect(self.textBrowser_terminal.clear)
        self.Btn_cancel_input_clients.clicked.connect(self.clients_input_clear)
        self.Btn_add_tq_account.clicked.connect(self.get_tq_account)
        self.Btn_cancel_input_tq_account.clicked.connect(self.tq_account_input_clear)
        self.Btn_donation.clicked.connect(self.show_donation_window)
        self.Btn_setting.clicked.connect(self.show_setting_dialog)
        self.Btn_select_clients_photo_address.clicked.connect(self.choose_client_photo_File)
        self.Btn_kill_all_process.clicked.connect(self.kill_all_process)
        self.Btn_update_treeview.clicked.connect(self.show_file_in_treeview)
        self.Btn_add_new_process.clicked.connect(self.show_create_new_process_window)
        self.Btn_add_backtest_process.clicked.connect(self.show_create_backtest_window)
        self.Btn_add_optional_contracts.clicked.connect(self.add_Tq_Quote_to_csv)
        self.Btn_draw_line_order.clicked.connect(self.KLineWidget.draw_line_by_mouse)
        self.Btn_draw_line_style.clicked.connect(self.KLineWidget.set_draw_line_style)
        self.treeview_log.clicked.connect(self.on_tree_licked)

        self.Btn_opne_in_excel1.clicked.connect(lambda: self.open_file_with_excel(path='./data/deal_detials.csv'))
        self.Btn_opne_in_excel2.clicked.connect(lambda: self.open_file_with_excel(path='./data/config.csv'))

        #列表框槽函数
        self.clients_listview2.clicked.connect(self.show_clients_info)
        self.tq_account_listview2.clicked.connect(self.show_tq_account_info)
        self.self_selection_listview.clicked.connect(self.set_current_dissplayed_Kline)


    def set_tableWidget(self):  # 设置tableWidget

        # 隐藏表头
        self.tableWidget_deal_detials.verticalHeader().setVisible(False)
        self.tableWidget_process.horizontalHeader().setVisible(True)
        self.tableWidget_process.verticalHeader().setVisible(True)

        # 设置列表默认行列数量
        self.tableWidget_deal_detials.setRowCount(50)
        self.tableWidget_deal_detials.setColumnCount(8)
        self.tableWidget_process.setRowCount(44)
        self.tableWidget_process.setColumnCount(10)

        # tablewidget单击选中整行,SelectItems为仅单选,SelectColumns为选中列,SelectRows为选中行
        self.tableWidget_deal_detials.setSelectionBehavior(PySide6.QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidget_process.setSelectionBehavior(PySide6.QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems)

        # tablewidget 只允许选中一个格子,禁止拖动多选
        self.tableWidget_deal_detials.setSelectionMode(PySide6.QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_process.setSelectionMode(PySide6.QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)

        # tablewidget 设置水平表头高度
        self.tableWidget_deal_detials.horizontalHeader().setFixedHeight(30)
        self.tableWidget_process.horizontalHeader().setFixedHeight(50)
        # self.tableWidget_process.horizontalHeader().setAutoScroll()

        # tablewidget 设置右键菜单
        self.tableWidget_deal_detials.setContextMenuPolicy(Qt.CustomContextMenu)             # 允许单机右键响应
        self.tableWidget_deal_detials.customContextMenuRequested.connect(self.generateMenu)      # 构建右键的点击事件


    def other_item_settings(self):    # 其他设置
        self.m_drag = False
        self.label_logo.setPixmap(QPixmap('./logo/logo.png'))           # 加载logo图片
        self.label_logo.setScaledContents(True)                         # 设置图片自适应
        self.label_client_photo_show.setScaledContents(True)


    def show_setting_dialog(self):  # 显示设置窗口

        from Setting_Inheritance import SettingDialog

        self.setting_dialog = SettingDialog()
        self.setting_dialog.show()


    def show_exit_dialog(self):     # 退出程序

        from ExitDialog_Inheritance import Exit_Dialog

        self.exit_dialog = Exit_Dialog()
        self.exit_dialog.show()
        self.exit_dialog.Btn_determine_exit.clicked.connect(self.kill_all_process)
        self.exit_dialog.Btn_determine_exit.clicked.connect(QApplication.instance().quit)
        self.exit_dialog.exec()

    def show_donation_window(self):             # 弹出捐赠窗口

        from Donation_Inheritance import Donation
        self.donation = Donation()
        self.donation.show()

    def show_create_new_process_window(self):   # 弹出新建策略进程窗口

        from CreateNewProcess_Inheritance import NewProcessWindow
        self.create_process_strategy = NewProcessWindow()
        self.create_process_strategy.show()

    def show_create_backtest_window(self):      # 弹出新建策略回测进程窗口

        from CreateBackTestProcess_Inheritance import BackTestWindow
        self.create_backtest_window = BackTestWindow()
        self.create_backtest_window.show()


    def generateMenu(self, pos):
        # print(pos)
        #获得右键所点击的索引值
        for i in self.tableWidget_deal_detials.selectionModel().selection().indexes():
            #获得当前点击的行和列的值
            rowIndex = i.row()
            columnIndex = i.column()
            if rowIndex < 50:       #   如果选择的索引小于50, 弹出上下文菜单
                menu = QMenu()      #   构造菜单
                menu.setStyleSheet(         # 设置整个菜单框的边界高亮厚度# 整个边框的颜色
                    u"QMenu{background:transparent;\n   font: 700 14pt \"\u7b49\u7ebf\";\n   border-radius: 10px;\n  border-color: none;\n    border:none;\n}\n"                                              
                    "QMenu::item{padding:2px 15px 2px 15px;\n height:30px;\n  color:blue;\n   margin:2px 1px 2px 1px;\n"  
                                "background-color: rgb(200,200,200);\n  border-radius: 15px;}\n"  # 选项背景     
                    "QMenu::item:selected:enabled{background:lightgray;\n   color:red;\n    background:rgb(255,255,255);}\n"     
                    "QMenu::separator{height:1px;\n width:50px;\n   background:blue;\n  margin:0px 0px 0px 0px;}\n"  # 要在两个选项设置self.groupBox_menu.addSeparator()才有用
                        )
                #添加菜单的选项
                item1 = menu.addAction("临时停止策略")
                item2 = menu.addAction("永久停止策略")
                item3 = menu.addAction("重启策略")
                item4 = menu.addAction("修改策略参数")
                item5 = menu.addAction("停止并删除策略")

                screenPos = self.tableWidget_deal_detials.mapToGlobal(pos)          #   获得相对屏幕的位置

                action = menu.exec(screenPos)       #   被阻塞, 执行菜单
                if action == item1:
                    print("\n\n选择了--临时停止策略",'\n点击的单元格坐标为:  ',rowIndex, columnIndex, '  单元格的值为:  ',self.tableWidget_deal_detials.item(rowIndex,columnIndex).text())
                elif action == item2:
                    print("\n\n选择了--永久停止策略",'\n点击的单元格坐标为:  ',rowIndex, columnIndex, '  单元格的值为:  ', self.tableWidget_deal_detials.item(rowIndex,columnIndex).text())
                elif action == item3:
                    print("\n\n选择了--重启策略",'\n点击的单元格坐标为:  ',rowIndex, columnIndex, '  单元格的值为:  ', self.tableWidget_deal_detials.item(rowIndex,columnIndex).text())
                elif action == item4:
                    print('\n\n选择了--修改策略参数','\n点击的单元格坐标为:  ',rowIndex, columnIndex, '  单元格的值为:  ', self.tableWidget_deal_detials.item(rowIndex,columnIndex).text())
                elif action == item5:
                    print('\n\n选择了--停止并删除策略','\n点击的单元格坐标为:  ',rowIndex, columnIndex, '  单元格的值为:  ', self.tableWidget_deal_detials.item(rowIndex,columnIndex).text())
            else:
                return


    def chack_main_tq_account(self):            # 检查主账号是否存在
        if self.main_tq_account == '' or self.main_tq_pwd == '':
            data = self.ioModal.read_csv_file(path='./data/main_tq_account.csv')
            if data.empty:                                     # 判断self.data是否为空
                print('\n\nmain_tq_account.csv文件里没有帐户，请先在设置里添加天勤主账号和密码')
            else:
                self.main_tq_account = data.iloc[0, 0]
                self.main_tq_pwd = data.iloc[0, 1]
        else:
            self.times1 += 1

            if self.times1 == 10:       #主程序运行10秒后才登录天勤帐户,以防天勤帐户登录出问题时,主程序也打不开
                self.sign_in_tq_account()


    def sign_in_tq_account(self):  # 登录天勤账户并订阅k线
        try:
            self.api = TqApi(TqKq(),auth=TqAuth(self.main_tq_account, self.main_tq_pwd))
        except Exception as ex:
            print('登录天勤帐户时发生异常: %r' % ex)

        self_selection_quote_list = self.get_self_selection_quote_list()
        if self_selection_quote_list:
            for kl in self_selection_quote_list:
                if (kl + '_quote') not in self.Quote_klines_dict:           # 判断字典中有无该合约的订阅
                    self.ceate_TQ_klines_and_quote(kl)
                else:
                    print('合约: ', kl,' 已订阅')

            # print('\n\n\n当前字典为:',self.Quote_klines_dict, '\n\n\n\n\n')

        self.GengXin_ShuJu=UpdateTqsdkDate(self.api) #信号线程，发送数据更新
        self.GengXin_ShuJu.start()
        self.init_Klines_chart()
        # self.GengXin_ShuJu.TQ_signal.connect(self.widget.update_bar) #信号绑定更新函数update_bar
        # self.GengXin_ShuJu.TQ_signal.connect(self.updateindicator) #信号绑定更新函数updateindicator
        # self.GengXin_ShuJu.TQ_signal.connect(self.Update_quotes) #信号绑定更新quote


    def ceate_TQ_klines_and_quote(self,symbol): # 根据合约创建对应的klines和quote
        try:
            self.Quote_klines_dict['%s_quote'%symbol]  = self.api.get_quote(symbol=symbol)   # 创建quote
            self.Quote_klines_dict['%s_1_min'%symbol]  = self.api.get_kline_serial(symbol=symbol, duration_seconds=60, data_length=8000) # 订阅1分钟k线
            self.Quote_klines_dict['%s_15_min'%symbol] = self.api.get_kline_serial(symbol=symbol, duration_seconds=60*15, data_length=8000) # 订阅15分钟k线
            self.Quote_klines_dict['%s_30_min'%symbol] = self.api.get_kline_serial(symbol=symbol, duration_seconds=60*30, data_length=5000) # 订阅30分钟k线
            self.Quote_klines_dict['%s_1_hour'%symbol] = self.api.get_kline_serial(symbol=symbol, duration_seconds=60*60, data_length=2250) # 订阅1小时k线
            self.Quote_klines_dict['%s_2_hour'%symbol] = self.api.get_kline_serial(symbol=symbol, duration_seconds=60*60*2, data_length=1200) # 订阅2小时k线
            self.Quote_klines_dict['%s_4_hour'%symbol] = self.api.get_kline_serial(symbol=symbol, duration_seconds=60*60*4, data_length=600) # 订阅4小时k线
            self.Quote_klines_dict['%s_1_day'%symbol]  = self.api.get_kline_serial(symbol=symbol, duration_seconds=60*60*24, data_length=300) # 订阅日k线

            print('合约', symbol, '的K线订阅成功')


        except Exception as ex:
            print('订阅k线 ', symbol, ' 时发生错误: %r' % ex)

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
                    if item['whether_self_start']:

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



