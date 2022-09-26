# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QMenu


class RightButtonMenu:      # 主界面用到的各种右键菜单

    def generate_precess_table_menu(self, pos):
        # print(pos)
        # 获得右键所点击的索引值
        for i in self.tableWidget_process.selectionModel().selection().indexes():
            # 获得当前点击的行和列的值
            rowIndex = i.row()
            columnIndex = i.column()
            if rowIndex < 50:  # 如果选择的索引小于50, 弹出上下文菜单
                menu = QMenu()  # 构造菜单
                menu.setStyleSheet(  # 设置整个菜单框的边界高亮厚度# 整个边框的颜色
                        u"QMenu{background:transparent;\n   font: 700 14pt \"\u7b49\u7ebf\";\n   border-radius: 0px;\n  border-color: none;\n    border:none;\n}\n"
                        "QMenu::item{padding:2px 15px 2px 15px;\n height:30px;\n  color:blue;\n   margin:1px 1px 1px 1px;\n"
                        "background-color: rgb(161,160,160);\n  border-radius: none;}\n"  # 选项     
                        "QMenu::item:selected:enabled{background:lightgray;\n   color:red;\n    background:rgb(255,255,255);}\n"
                        "QMenu::separator{height:1px;\n width:50px;\n   background:blue;\n  margin:0px 0px 0px 0px;}\n"  # 要在两个选项设置self.groupBox_menu.addSeparator()才有用
                )
                # 添加菜单的选项
                item1 = menu.addAction("临时停止策略")
                item2 = menu.addAction("永久停止策略")
                item3 = menu.addAction("重启策略")
                item4 = menu.addAction("修改策略参数")
                item5 = menu.addAction("停止并删除策略")

                screenPos = self.tableWidget_process.mapToGlobal(pos)  # 获得相对屏幕的位置

                action = menu.exec(screenPos)  # 被阻塞, 执行菜单
                if action == item1:
                    print("\n\n选择了--临时停止策略", '\n点击的单元格坐标为:  ', rowIndex, columnIndex)
                    if self.tableWidget_process.item(rowIndex, columnIndex):
                        print('  单元格的值为:  ', self.tableWidget_process.item(rowIndex, columnIndex).text())
                elif action == item2:
                    print("\n\n选择了--永久停止策略", '\n点击的单元格坐标为:  ', rowIndex, columnIndex)
                    if self.tableWidget_process.item(rowIndex, columnIndex):
                        print('  单元格的值为:  ', self.tableWidget_process.item(rowIndex, columnIndex).text())
                elif action == item3:
                    print("\n\n选择了--重启策略", '\n点击的单元格坐标为:  ', rowIndex, columnIndex)
                    if self.tableWidget_process.item(rowIndex, columnIndex):
                        print('  单元格的值为:  ', self.tableWidget_process.item(rowIndex, columnIndex).text())
                elif action == item4:
                    print('\n\n选择了--修改策略参数', '\n点击的单元格坐标为:  ', rowIndex, columnIndex)
                    if self.tableWidget_process.item(rowIndex, columnIndex):
                        print('  单元格的值为:  ', self.tableWidget_process.item(rowIndex, columnIndex).text())
                elif action == item5:
                    print('\n\n选择了--停止并删除策略', '\n点击的单元格坐标为:  ', rowIndex, columnIndex)
                    if self.tableWidget_process.item(rowIndex, columnIndex):
                        print('  单元格的值为:  ', self.tableWidget_process.item(rowIndex, columnIndex).text())
            else:
                return
            break

    def generate_deal_detials_table_menu(self, pos):
        # print(pos)
        # 获得右键所点击的索引值
        for i in self.tableWidget_deal_detials.selectionModel().selection().indexes():
            # 获得当前点击的行和列的值
            rowIndex = i.row()
            columnIndex = i.column()
            if rowIndex < 500:  # 如果选择的索引小于50, 弹出上下文菜单
                menu = QMenu()  # 构造菜单
                menu.setStyleSheet(  # 设置整个菜单框的边界高亮厚度# 整个边框的颜色
                        u"QMenu{background:transparent;\n   font: 700 14pt \"\u7b49\u7ebf\";\n   border-radius: 0px;\n  border-color: none;\n    border:none;\n}\n"
                        "QMenu::item{padding:2px 15px 2px 15px;\n height:30px;\n  color:blue;\n   margin:1px 1px 1px 1px;\n"
                        "background-color: rgb(161,160,160);\n  border-radius: none;}\n"  # 选项     
                        "QMenu::item:selected:enabled{background:lightgray;\n   color:red;\n    background:rgb(255,255,255);}\n"
                        "QMenu::separator{height:1px;\n width:50px;\n   background:blue;\n  margin:0px 0px 0px 0px;}\n"  # 要在两个选项设置self.groupBox_menu.addSeparator()才有用
                )
                # 添加菜单的选项
                item1 = menu.addAction("临时停止策略")
                item2 = menu.addAction("永久停止策略")
                item3 = menu.addAction("重启策略")
                item4 = menu.addAction("修改策略参数")
                item5 = menu.addAction("停止并删除策略")

                screenPos = self.tableWidget_deal_detials.mapToGlobal(pos)  # 获得相对屏幕的位置
                # menu.setCursor(screenPos)
                action = menu.exec(screenPos)  # 被阻塞, 执行菜单
                if action == item1:
                    print("\n\n选择了--临时停止策略", '\n点击的单元格坐标为:  ', rowIndex, columnIndex)
                    if self.tableWidget_deal_detials.item(rowIndex, columnIndex):
                        print('  单元格的值为:  ', self.tableWidget_deal_detials.item(rowIndex, columnIndex).text())
                elif action == item2:
                    print("\n\n选择了--永久停止策略", '\n点击的单元格坐标为:  ', rowIndex, columnIndex)
                    if self.tableWidget_deal_detials.item(rowIndex, columnIndex):
                        print('  单元格的值为:  ', self.tableWidget_deal_detials.item(rowIndex, columnIndex).text())
                elif action == item3:
                    print("\n\n选择了--重启策略", '\n点击的单元格坐标为:  ', rowIndex, columnIndex)
                    if self.tableWidget_deal_detials.item(rowIndex, columnIndex):
                        print('  单元格的值为:  ', self.tableWidget_deal_detials.item(rowIndex, columnIndex).text())
                elif action == item4:
                    print('\n\n选择了--修改策略参数', '\n点击的单元格坐标为:  ', rowIndex, columnIndex)
                    if self.tableWidget_deal_detials.item(rowIndex, columnIndex):
                        print('  单元格的值为:  ', self.tableWidget_deal_detials.item(rowIndex, columnIndex).text())
                elif action == item5:
                    print('\n\n选择了--停止并删除策略', '\n点击的单元格坐标为:  ', rowIndex, columnIndex)
                    if self.tableWidget_deal_detials.item(rowIndex, columnIndex):
                        print('  单元格的值为:  ', self.tableWidget_deal_detials.item(rowIndex, columnIndex).text())
            else:
                return
            break

    def process_listview_menu(self, point):
        popMenu = QMenu()
        popMenu.setStyleSheet(  # 设置整个菜单框的边界高亮厚度# 整个边框的颜色
                u"QMenu{background:transparent;\n   font: 700 14pt \"\u7b49\u7ebf\";\n   border-radius: 10px;\n  border-color: none;\n    border:none;\n}\n"
                "QMenu::item{padding:2px 15px 2px 15px;\n height:30px;\n  color:blue;\n   margin:2px 1px 2px 1px;\n"
                "background-color: rgb(200,200,200);\n  border-radius: 15px;}\n"  # 选项背景     
                "QMenu::item:selected:enabled{background:lightgray;\n   color:red;\n    background:rgb(255,255,255);}\n"
                "QMenu::separator{height:1px;\n width:50px;\n   background:blue;\n  margin:0px 0px 0px 0px;}\n"  # 要在两个选项设置self.groupBox_menu.addSeparator()才有用
        )
        popMenu.addAction(QtGui.QAction(u'停止策略', self))
        popMenu.addAction(QtGui.QAction(u'重启策略', self))
        popMenu.addAction(QtGui.QAction(u'删除策略', self))

        popMenu.exec(QtGui.QCursor.pos())
        item = listWidget.itemAt(x, y)