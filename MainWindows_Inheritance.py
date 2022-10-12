# -*- coding: utf-8 -*-
import sys
import datetime
import importlib
import PySide6
from multiprocessing import Process, Manager
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QApplication, QMainWindow
from Main_Process_Function import *
from PySide6.QtUiTools import loadUiType
from read_write_file import ReadWriteCsv
from RightButtonMenu import RightButtonMenu
from UI.mainwindows_light import Ui_MainWindow as light_windows
from UI.mainwindows_dark import Ui_MainWindow as dark_windows
from KChart.K_Chart_Widget import KLineWidget
from TQ_Services import TQServices

from main import THEME



if THEME == "dark":                                    # 创建主窗口类方式一，通过loadUiType()函数直接加载UI文件
    UI, _ = loadUiType('./UI/mainwindows_dark.ui')
else:
    UI, _ = loadUiType('./UI/mainwindows_light.ui')

# if THEME == "dark":                                  # 创建主窗口类方式二，通过继承Ui_MainWindow类
#     UI = dark_windows
# else:
#     UI = light_windows


class Main_window(QMainWindow, UI, Main_Process_Function):
    def __init__(self):
        super(Main_window, self).__init__()

        # 将主进程的控制台输出重定向到textBrowser中显示
        sys.stdout = EmittingStr()
        sys.stdout.textWritten.connect(self.outputWritten)

        self.setupUi(self)
        self.setWindowOpacity(0.98)                                     # 设置窗口透明度
        self.start_time = datetime.now()                                # 记录程序开始时间
        self.main_tq_account = None                                       # 主账户
        self.main_tq__pwd = None                                          # 主账户密码
        self.Quote_klines_dict = {}                                     # 自选合约字典,用来存放所有的自选合约klines


        self.ioModule = ReadWriteCsv()                                   # 实例化 csv 读写类
        self.KLineWidget = KLineWidget()                                # 实例化K线图widget部件
        self.RightBtbMenu = RightButtonMenu(self)                       # 右键菜单类
        self.verticalLayout_klines.addWidget(self.KLineWidget)          # 添加K线图部件到布局中
        self.whether_the_folder_and_files_exists()                      # 判断必需的文件夹和文件是否存在，不存在则创建

        self.Quantity = 0 - self.get_inactivated_process_quantity()
        self.cwd = os.getcwd()                                          # 获取当前路径

        self.Process_dict = {}                                          # 创建进程字典，用于存储子进程的pid
        self.Process_start_time_dict = {}                               # 各进程启动次数字典,用来记录各策略进程重启次数
        self.process_list_row = []                                      # 当前活着的进程名列表,用于刷新 process_listview
        self.TQ_services_pid = None                                     # 用来记录天勤数据服务进程的pid
        self.current_dissplayed_Kline = None                            # 当前显示的k线品种

        self.quote_dict = {}                                            # 当前行情切片字典
        self.self_selection = {}                                        # 自选合约字典

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
        self.parameters_refresh.timeout.connect(self.add_paramer_to_container_by_timer)  # 刷新面板各参数
        self.parameters_refresh.timeout.connect(self.check_TQ_Services_Status)           # 检查天勤数据服务进程状态
        self.parameters_refresh.start(1000)

        self.Define_slot_functions()                                # 定义槽函数
        self.hide_items()                                           # 隐藏控件
        self.add_paramer_to_combobox()                              # 将参数添加到下拉框
        self.set_tableWidget()                                      # 设置表格
        self.add_paramer_to_container_by_timer()                    # 将参数添加到容器
        self.add_paramer_to_container_by_hand()
        self.other_item_settings()                                  # 其他控件设置
        self.process_dict_update()                                  # 更新进程字典
        self.show_file_in_treeview()                                # 显示文件到树状图
        self.load_deal_detials_data()                               # 加载交易明细数据
        self.load_process_config()                                  # 加载进程配置数据
        self.draw_dount_chart()                                     # 绘制饼图
        # self.start_inactivated_process()                            # 启动未激活的进程


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

    def whether_the_folder_and_files_exists(self):    # 检查必要的文件及文件夹是否存在，不存在则创建
        # 判断文件夹是否存在，不存在则创建
        self.ioModule.judge_dirs_exist(dirs='./data')
        self.ioModule.judge_dirs_exist(dirs='./log')
        self.ioModule.judge_dirs_exist(dirs='./clients_photo')
        self.ioModule.judge_dirs_exist(dirs='./Klines_Data')
        self.ioModule.judge_dirs_exist(dirs='./available_contracts')

        # 判断配置文件是否存在，不存在则创建
        self.ioModule.judge_file_exist(path='./data/deal_detials.csv')
        self.ioModule.judge_file_exist(path='./data/config.csv')
        self.ioModule.judge_file_exist(path='./data/clients.csv')
        self.ioModule.judge_file_exist(path='./data/tq_account.csv')
        self.ioModule.judge_file_exist(path='./data/main_tq_account.csv')
        self.ioModule.judge_file_exist(path='./data/self_selection.csv')


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

        self.Btn_homepage.setFocusPolicy(Qt.NoFocus)            # 隐藏各种按钮点击时的虚线框
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
        self.Btn_add_self_selection_contracts.clicked.connect(self.add_self_selection_list)
        self.Btn_draw_line_order.clicked.connect(self.KLineWidget.draw_line_by_mouse)
        self.Btn_draw_line_style.clicked.connect(self.KLineWidget.set_draw_line_style)
        self.Btn_start_TQ_services.clicked.connect(self.start_TQ_services)
        self.Btn_stop_TQ_services.clicked.connect(self.stop_TQ_services)
        self.treeview_log.clicked.connect(self.on_tree_licked)

        self.comboBox_add_quote_exchange.activated.connect(self.add_contracts_to_comboBox_symbol)  # comboBox 信号槽函数
        self.comboBox_contract_type.activated.connect(self.add_contracts_to_comboBox_symbol)

        self.Btn_klines_1min.clicked.connect(self.show_1min_kline)
        self.Btn_klines_15min.clicked.connect(self.show_15min_kline)
        self.Btn_klines_30min.clicked.connect(self.show_30min_kline)
        self.Btn_klines_1hour.clicked.connect(self.show_1hour_kline)
        self.Btn_klines_2hour.clicked.connect(self.show_2hour_kline)
        self.Btn_klines_4hour.clicked.connect(self.show_4hour_kline)
        self.Btn_klines_daily.clicked.connect(self.show_1day_kline)

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
        self.tableWidget_process.setRowCount(45)
        self.tableWidget_process.setColumnCount(10)

        # 第二行随内容自动调整行高
        self.tableWidget_process.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget_process.verticalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)

        # 随内容分配列宽
        # self.tableWidget_deal_detials.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget_process.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget_process.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        # tablewidget单击选中整行,SelectItems为仅单选,SelectColumns为选中列,SelectRows为选中行
        self.tableWidget_deal_detials.setSelectionBehavior(PySide6.QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_process.setSelectionBehavior(PySide6.QtWidgets.QAbstractItemView.SelectionBehavior.SelectColumns)

        # # tablewidget 只允许选中一个格子,禁止拖动多选
        # self.tableWidget_deal_detials.setSelectionMode(PySide6.QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        # self.tableWidget_process.setSelectionMode(PySide6.QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)

        # tablewidget 设置水平表头高度
        self.tableWidget_deal_detials.horizontalHeader().setFixedHeight(30)
        self.tableWidget_process.horizontalHeader().setFixedHeight(50)
        # self.tableWidget_process.horizontalHeader().setAutoScroll()

        # # tablewidget 设置右键菜单
        self.clients_listview.setContextMenuPolicy(Qt.CustomContextMenu)              # 允许单击右键响应
        self.clients_listview2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tq_account_listview.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tq_account_listview2.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.strategy_listview.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.quote_listview.setContextMenuPolicy(Qt.CustomContextMenu)
        self.process_listview.setContextMenuPolicy(Qt.CustomContextMenu)
        self.self_selection_listview.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_process.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.tableWidget_deal_detials.setContextMenuPolicy(Qt.CustomContextMenu)

        self.clients_listview.customContextMenuRequested.connect(self.RightBtbMenu.clients_listview_menu)      # 构建右键的点击事件
        self.clients_listview2.customContextMenuRequested.connect(self.RightBtbMenu.clients_listview2_menu)
        self.tq_account_listview.customContextMenuRequested.connect(self.RightBtbMenu.tq_account_listview_menu)
        self.tq_account_listview2.customContextMenuRequested.connect(self.RightBtbMenu.tq_account_listview2_menu)
        self.self_selection_listview.customContextMenuRequested.connect(self.RightBtbMenu.self_selection_listview_menu)
        # self.strategy_listview.customContextMenuRequested.connect(self.strategy_listview_menu)
        # self.quote_listview.customContextMenuRequested.connect(self.generate_general_list_del_menu)
        self.process_listview.customContextMenuRequested.connect(self.RightBtbMenu.process_listview_menu)
        self.tableWidget_process.customContextMenuRequested.connect(self.RightBtbMenu.precess_table_menu)
        # self.tableWidget_deal_detials.customContextMenuRequested.connect(self.generate_deal_detials_table_menu)

        # QlistView 设置右键菜单
        # self.process_listview.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.process_listview.customContextMenuRequested[QtCore.QPoint].connect(lambda: self.process_listview_menu(x,y))





    def other_item_settings(self):    # 其他设置
        self.m_drag = False
        self.label_logo.setPixmap(QPixmap('./logo/logo.png'))           # 加载logo图片
        self.label_logo.setScaledContents(True)                         # 设置图片自适应
        self.label_client_photo_show.setScaledContents(True)
        self.stackedWidget.setCurrentIndex(0)                           # 设置第一页
        print('\n\n\n\n欢迎使用\n\n进程交易者  程序化期货交易框架\n\n\n\n\n\n\n')
        print('\n\n\n\n\n\n策略实例进程将在主程序启动一分钟后，按 config.csv 文件中的配置逐个尝试启动\n\n\n')


    def show_setting_dialog(self):  # 显示设置窗口
        from Setting_Inheritance import SettingDialog
        self.setting_dialog = SettingDialog(self)
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
        self.create_process_strategy = NewProcessWindow(self)
        self.create_process_strategy.show()

    def show_create_backtest_window(self):      # 弹出新建策略回测进程窗口
        from CreateBackTestProcess_Inheritance import BackTestWindow
        self.create_backtest_window = BackTestWindow(self)
        self.create_backtest_window.show()

    def chack_main_tq_account(self):            # 检查天勤主账号是否存在
        path = './data/main_tq_account.csv'
        if os.path.exists(path):
            data = self.ioModule.read_csv_file(path=path)
            if data.empty:                                     # 判断self.data是否为空
                print('\n\nmain_tq_account.csv文件里没有帐户，请先在设置里添加天勤主账号和密码')
            else:
                self.main_tq_account = data.loc[0, 'tq_account']
                self.main_tq_psd = data.loc[0, 'qt_psd']


    def start_TQ_services(self):    # 开启天勤数据行情服务
        self.chack_main_tq_account()
        if self.main_tq_account and self.main_tq_psd:
            self.self_selection = Manager().list()          #  自选合约列表,该列表将和天勤数据服务进程共享
            self.quote_dict = Manager().dict()              #  当前显示的合约品种行情切片,主进程通过与天勤数据服务进程共享此字典获取数据
            self.current_Kline = Manager().list()           #  当前显示的合约列表,该列表只有一项,该列表将和天勤数据服务进程共享
            self.current_Kline.append(self.current_dissplayed_Kline)
            data = self.ioModule.read_csv_file(path='./data/self_selection.csv')
            for index, row in data.iterrows():
                self.self_selection.append(row['quote'])
            t = TQServices(args=(self.self_selection, self.quote_dict, self.current_Kline, self.main_tq_account, self.main_tq_psd))
            t.start()
            self.TQ_services_pid = t.pid
            self.label_TQ_services_info.setText('天勤数据行情服务正在运行中')


    def stop_TQ_services(self):     # 关闭天勤数据行情服务
        if self.TQ_services_pid:
            # self.kill_process(self.TQ_services_pid)
            try:
                parent_proc = psutil.Process(self.TQ_services_pid)
                for child_proc in parent_proc.children(recursive=True):
                    child_proc.kill()
                parent_proc.kill()

                print('\npid为 ' + str(self.TQ_services_pid) + ' 的子进程 关闭成功 ！！！\n')
            except Exception as e:
                print('\npid为 ' + str(self.TQ_services_pid) + ' 的子进程 关闭失败 ！！！\n')
                print(e, '\n')

            self.TQ_services_pid = None
        self.label_TQ_services_info.setText('天勤数据行情服务已关闭')
        self.clear_quote_paramer_panel()



    #####################################################################
    #####################下面这个函数是进程自启的核心代码 #####################

    def start_inactivated_process(self):  # 根据 csv 文件启动未运行的策略
        living_pid_list = self.get_alive_process_pid_list()

        path = './data/config.csv'
        data = self.ioModule.read_csv_file(path)

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

                        m = importlib.import_module(module)  # 导入模块
                        my_class = getattr(m, strategy_class_name)  # 获取类

                        t = my_class(args=(index, data.iloc[index]))  # 实例化类
                        t.name = item['process_name']  # 设置进程名称
                        t.start()  # 启动进程
                        self.Process_dict[item['process_name']] = t.pid

                        if item['process_name'] in self.Process_start_time_dict:
                            self.Process_start_time_dict[item['process_name']] += 1
                            print('\n进程 ', item['process_name'], '  已自动重启!!!,  目前该策略实例重启次数:   ', self.Process_start_time_dict[item['process_name']])
                            print('重启时间: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '\n\n')
                        else:
                            self.Process_start_time_dict[item['process_name']] = 1
                            print('\n进程实例  ', item['process_name'], '  已启动, 本次为框架运行以来第一次启动!')
                            print('启动时间:  ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '\n\n')

                        self.Quantity += 1
                        if self.Quantity > 0:
                            self.label_process_reboot_quantity.setText(str(self.Quantity))
                        elif self.Quantity == 0:
                            self.label_process_reboot_quantity.setText('进程已全部启动')
                        else:
                            self.label_process_reboot_quantity.setText('进程启动中\n还没启动完')

                        self.add_paramer_to_container_by_timer()
                else:
                    pass


    def start_single_process(self, index, tmp_dict):         # 启动单个策略实例进程

        module = 'strategys' + '.' + tmp_dict['strategy']
        strategy_class_name = tmp_dict['strategy']

        mod = importlib.import_module(module)  # 导入模块
        my_class = getattr(mod, strategy_class_name)  # 获取类

        t = my_class(args=(index, tmp_dict))  # 实例化类
        t.name = tmp_dict['process_name']  # 设置进程名称
        t.start()  # 启动进程
        self.Process_dict[tmp_dict['process_name']] = t.pid

        if tmp_dict['process_name'].split('-',3) == '回测':
            print('\n回测进程的启动不计入策略进程总重启次数')
        else:
            if tmp_dict['process_name'] in self.Process_start_time_dict:
                self.Process_start_time_dict[tmp_dict['process_name']] += 1
                self.Quantity += 1
                print('\n进程 ', tmp_dict['process_name'], '  已手动重启!!!,  目前该策略实例重启次数:   ', self.Process_start_time_dict[tmp_dict['process_name']])
                print('重启时间: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '\n\n')
            else:
                self.Process_start_time_dict[tmp_dict['process_name']] = 1
                print('\n进程实例  ', tmp_dict['process_name'], '  已手动启动, 本次为框架运行以来第一次启动!')
                print('启动时间:  ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '\n\n')

        if self.Quantity > 0:
            self.label_process_reboot_quantity.setText(str(self.count_process_reboot_times()))