# -*- coding: utf-8 -*-

THEME = "dark"      # 皮肤选择 这里的THEME改为 dark 为深色模式,改为  light 为浅色模式

from MainWindows_Inheritance import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec())





