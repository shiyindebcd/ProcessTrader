# -*- coding: utf-8 -*-
from PySide6.QtCore import QEvent
from PySide6.QtGui import QCursor, Qt
from PySide6.QtWidgets import QMenu
from ExitDialog_Inheritance import DeleteWarning

class RightButtonMenu:      # 主界面用到的各种右键菜单
    def __init__(self, parent):
        self.parent = parent

        # 菜单样式 所有菜单共用一个样式
        self.my_menu_style = '''QMenu{
                                        background:transparent;\n   
                                        font: 700 14pt \"\u7b49\u7ebf\";\n   
                                        border-radius: 0px;\n  
                                        border-color: none;\n    
                                        border:none;\n
                                    }\n
                                QMenu::item{
                                        padding:2px 15px 2px 15px;\n 
                                        height:30px;\n  color:blue;\n   
                                        margin:1px 1px 1px 1px;\n
                                        background-color: rgb(200,200,200);\n  
                                        border: none;\n  border-radius: none;\n
                                    }\n
                                QMenu::item:selected:enabled{                                    
                                        background:lightgray;\n   
                                        color:red;\n    
                                        background:rgb(255,255,255);\n
                                    }\n
                                QMenu::separator{
                                        height:1px;\n 
                                        width:50px;\n   
                                        background:blue;\n  
                                        margin:0px 0px 0px 0px;\n
                                    }\n'''


    # 各个需要鼠标右键的点击的地方安装事件过滤器
    # self.clients_listview.viewport().installEventFilter(self)
    # self.clients_listview2.viewport().installEventFilter(self)
    # self.tq_account_listview.viewport().installEventFilter(self)
    # self.tq_account_listview2.viewport().installEventFilter(self)
    # self.strategy_listview.viewport().installEventFilter(self)
    # self.quote_listview.viewport().installEventFilter(self)
    # self.process_listview.viewport().installEventFilter(self)
    # self.self_selection_listview.viewport().installEventFilter(self)
    # self.tableWidget_process.viewport().installEventFilter(self)
    # self.tableWidget_deal_detials.viewport().installEventFilter(self)

    # def eventFilter(self, objwatched, event):               # 事件过滤器
    # flag = eventType == QEvent.MouseButtonPress or eventType == QEvent.KeyPress or eventType == QEvent.Close  #
    # if flag:
    #     print(f"事件类型值={eventType}，\n事件objwatched={objwatched},\nparent={objwatched.parent()},\nchild={objwatched.children()}")


    # if event.type() == QEvent.MouseButtonPress:
    #     if event.buttons() == Qt.LeftButton:
    #         print('\n\n 左单击   坐标:  ', QCursor.pos())
    #     elif event.buttons() == Qt.RightButton:
    #         print('\n\n 右单击   坐标:  ', QCursor.pos())
    #         if objwatched == self.clients_listview.viewport():
    #             print('clients_listview')
    #         elif objwatched == self.clients_listview2.viewport():
    #             print('clients_listview2')
    #         elif objwatched == self.tq_account_listview.viewport():
    #             print('tq_account_listview')
    #         elif objwatched == self.tq_account_listview2.viewport():
    #             print('tq_account_listview2')
    #         elif objwatched == self.strategy_listview.viewport():
    #             print('strategy_listview')
    #         elif objwatched == self.quote_listview.viewport():
    #             print('quote_listview')
    #         elif objwatched == self.process_listview.viewport():
    #             print('process_listview')
    #         elif objwatched == self.self_selection_listview.viewport():
    #             print('self_selection_listview')
    #         elif objwatched == self.tableWidget_process.viewport():
    #             print('tableWidget_process')
    #             self.generate_precess_table_menu(pos=QCursor.pos())
    #         elif objwatched == self.tableWidget_deal_detials.viewport():
    #             print('tableWidget_deal_detials')
    #             self.generate_deal_detials_table_menu(pos=QCursor.pos())
    #
    # ret = super().eventFilter(objwatched, event)
    # return ret

    def clients_listview_menu(self, pos):
        cell = self.parent.clients_listview.indexAt(pos)
        rowIndex = cell.row()
        if rowIndex >= 0:
            menu = QMenu()
            menu.setStyleSheet(self.my_menu_style)
            meun1 = menu.addAction('删除这个客户')
            screenPos = self.parent.clients_listview.mapToGlobal(pos)  # 获得相对屏幕的位置
            action = menu.exec(screenPos)  # 被阻塞, 执行菜单

            if action == meun1:
                self.Warning = DeleteWarning()
                self.Warning.show()
                self.Warning.Btn_determine_delete.clicked.connect(lambda: self.delete_clients(rowIndex))
                self.Warning.exec()
        else:
            return


    def clients_listview2_menu(self, pos):
        cell = self.parent.clients_listview2.indexAt(pos)
        rowIndex = cell.row()
        if rowIndex >= 0:
            menu = QMenu()
            menu.setStyleSheet(self.my_menu_style )
            meun1 = menu.addAction('删除这个客户')
            screenPos = self.parent.clients_listview2.mapToGlobal(pos)  # 获得相对屏幕的位置
            action = menu.exec(screenPos)  # 被阻塞, 执行菜单

            if action == meun1:
                self.Warning = DeleteWarning()
                self.Warning.show()
                self.Warning.Btn_determine_delete.clicked.connect(lambda: self.delete_clients(rowIndex))
                self.Warning.exec()
        else:
            return

    def delete_clients(self, index):        # 删除用户
        path = './data/clients.csv'
        data = self.parent.ioModal.read_csv_file(path)
        tmp = data.drop(index=index)
        tmp = tmp.reset_index(drop=True)      # 重建索引
        self.parent.ioModal.write_datas_to_csv_file(df_tmp=tmp, path=path)
        self.parent.label_client_photo_show.clear()
        self.parent.textBrowser_clients_details.clear()

    def tq_account_listview_menu(self, pos):
        cell = self.parent.tq_account_listview.indexAt(pos)
        rowIndex = cell.row()
        if rowIndex >= 0:
            menu = QMenu()
            menu.setStyleSheet(self.my_menu_style)
            meun1 = menu.addAction('删除这个天勤帐户')
            screenPos = self.parent.tq_account_listview.mapToGlobal(pos)  # 获得相对屏幕的位置
            action = menu.exec(screenPos)  # 被阻塞, 执行菜单

            if action == meun1:
                self.Warning = DeleteWarning()
                self.Warning.show()
                self.Warning.Btn_determine_delete.clicked.connect(lambda: self.delete_TQ_account(rowIndex))
                self.Warning.exec()
        else:
            return

    def tq_account_listview2_menu(self, pos):
        cell = self.parent.tq_account_listview2.indexAt(pos)
        rowIndex = cell.row()
        if rowIndex >= 0:
            menu = QMenu()
            menu.setStyleSheet(self.my_menu_style)
            meun1 = menu.addAction('删除这个天勤帐户')
            screenPos = self.parent.tq_account_listview2.mapToGlobal(pos)  # 获得相对屏幕的位置
            action = menu.exec(screenPos)  # 被阻塞, 执行菜单

            if action == meun1:
                self.Warning = DeleteWarning()
                self.Warning.show()
                self.Warning.Btn_determine_delete.clicked.connect(lambda: self.delete_TQ_account(rowIndex))
                self.Warning.exec()
        else:
            return
    def delete_TQ_account(self, index):     # 删除天勤帐户

        path = './data/tq_account.csv'
        data = self.parent.ioModal.read_csv_file(path)
        tmp = data.drop(index=index)
        tmp = tmp.reset_index(drop=True)      # 重建索引
        self.parent.ioModal.write_datas_to_csv_file(df_tmp=tmp, path=path)
        self.parent.textBrowser_tq_account_details.clear()

    def self_selection_listview_menu(self, pos):
        cell = self.parent.self_selection_listview.indexAt(pos)
        rowIndex = cell.row()
        if rowIndex >= 0:
            menu = QMenu()
            menu.setStyleSheet(self.my_menu_style)
            meun1 = menu.addAction('删除这个自选')
            screenPos = self.parent.self_selection_listview.mapToGlobal(pos)  # 获得相对屏幕的位置
            action = menu.exec(screenPos)  # 被阻塞, 执行菜单

            if action == meun1:
                self.delete_self_seletion(rowIndex)
        else:
            return

    def delete_self_seletion(self, index):      # 删除自选
        path = './data/self_selection.csv'
        data = self.parent.ioModal.read_csv_file(path)
        tmp = data.drop(index=index)
        tmp = tmp.reset_index(drop=True)      # 重建索引
        self.parent.ioModal.write_datas_to_csv_file(df_tmp=tmp, path=path)

    def process_listview_menu(self, pos):
        cell = self.parent.process_listview.indexAt(pos)
        rowIndex = cell.row()
        # print(cell.row())
        if rowIndex >= 0:
            menu = QMenu()
            menu.setStyleSheet(self.my_menu_style)
            meun1 = menu.addAction('临时停止此策略')
            meun2 = menu.addAction('重启此策略')
            meun3 = menu.addAction('永久停止此策略')
            meun4 = menu.addAction('删除此策略')

            screenPos = self.parent.tableWidget_process.mapToGlobal(pos)  # 获得相对屏幕的位置
            action = menu.exec(screenPos)  # 被阻塞, 执行菜单

            if action == meun1:
                print('选择了->  临时停止此策略,  在列表第    ',rowIndex, '  行', self.parent.tableWidget_process.item(rowIndex, 0))
            if action == meun2:
                print('选择了->  重启此策略,  在列表第    ', rowIndex, '  行')
            if action == meun3:
                print('选择了->  永久停止此策略,  在列表第    ', rowIndex, '  行')
            if action == meun4:
                self.Warning = DeleteWarning()
                self.Warning.show()
                self.Warning.Btn_determine_delete.clicked.connect(lambda: self.delete_process_config(rowIndex))
                self.Warning.exec()
        else:
            return

    def precess_table_menu(self, pos):
        cell = self.parent.tableWidget_process.itemAt(pos)
        if cell is not None:
            rowIndex = cell.row()
            columnIndex = cell.column()
            menu = QMenu()  # 构造菜单
            menu.setStyleSheet(self.my_menu_style)
            # 添加菜单的选项
            menu1 = menu.addAction("临时停止此策略")
            menu2 = menu.addAction("永久停止此策略")
            menu3 = menu.addAction("重启此策略")
            menu4 = menu.addAction("修改此策略参数")
            menu5 = menu.addAction("停止并删除此策略")

            screenPos = self.parent.tableWidget_process.mapToGlobal(pos)  # 获得相对屏幕的位置
            action = menu.exec(screenPos)  # 被阻塞, 执行菜单
            if action == menu1:
                if self.parent.tableWidget_process.item(rowIndex, columnIndex):
                    self.parent.label_process_right_btn_info.setText('临时停止此策略,点击的单元格坐标为:   ' + str(rowIndex) + ',' + str(columnIndex) + '    单元格的值为：     ' + str(self.parent.tableWidget_process.item(rowIndex, columnIndex).text()))
                else:
                    self.parent.label_process_right_btn_info.setText('临时停止此策略,点击的单元格坐标为:   ' + str(rowIndex) + ',' + str(columnIndex )+ '    该单元格没有内容')
            elif action == menu2:
                if self.parent.tableWidget_process.item(rowIndex, columnIndex):
                    self.parent.label_process_right_btn_info.setText('永久停止此策略,点击的单元格坐标为:   ' + str(rowIndex) + ',' + str(columnIndex) + '    单元格的值为：     ' + str(self.parent.tableWidget_process.item(rowIndex, columnIndex).text()))
                else:
                    self.parent.label_process_right_btn_info.setText('永久停止此策略,点击的单元格坐标为:   ' + str(rowIndex) + ',' + str(columnIndex) + '    该单元格没有内容')
            elif action == menu3:
                if self.parent.tableWidget_process.item(rowIndex, columnIndex):
                    self.parent.label_process_right_btn_info.setText('重启此策略,点击的单元格坐标为:   ' + str(rowIndex) + ',' + str(columnIndex) + '    单元格的值为：     ' + str(self.parent.tableWidget_process.item(rowIndex, columnIndex).text()))
                else:
                    self.parent.label_process_right_btn_info.setText('重启此策略,点击的单元格坐标为:   ' + str(rowIndex) + ',' + str(columnIndex) + '    该单元格没有内容')
            elif action == menu4:
                if self.parent.tableWidget_process.item(rowIndex, columnIndex):
                    self.parent.label_process_right_btn_info.setText('修改此策略参数,点击的单元格坐标为:   ' + str(rowIndex) + ',' + str(columnIndex) + '    单元格的值为：     ' + str(self.parent.tableWidget_process.item(rowIndex, columnIndex).text()))
                else:
                    self.parent.label_process_right_btn_info.setText('修改此策略参数,点击的单元格坐标为:   ' + str(rowIndex) + ',' + str(columnIndex) + '    该单元格没有内容')
            elif action == menu5:
                if self.parent.tableWidget_process.item(rowIndex, columnIndex):
                    self.Warning = DeleteWarning()
                    self.Warning.show()
                    self.Warning.Btn_determine_delete.clicked.connect(lambda: self.delete_process_config(columnIndex))
                    self.Warning.exec()
                else:
                    self.parent.label_process_right_btn_info.setText('该单元格没有数据')
        else:
            self.parent.label_process_right_btn_info.setText('点击的单元格没有数据')
            return

    def delete_process_config(self, index):      # 删除自选
        path = './data/config.csv'
        data = self.parent.ioModal.read_csv_file(path)
        tmp = data.drop(index=index)
        tmp = tmp.reset_index(drop=True)      # 重建索引
        self.parent.ioModal.write_datas_to_csv_file(df_tmp=tmp, path=path)
        self.parent.tableWidget_process.clear()
        self.parent.load_process_config()


