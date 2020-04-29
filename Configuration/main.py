# -*- coding: utf-8 -*-


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from Code.MainWindow import *

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
