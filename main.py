# -*- coding: utf-8 -*-

from RewriteMainWindows import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec())







