#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
 
from PySide.QtGui import QApplication

import gui    
         
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = gui.MainWindow()
    window.show()
    sys.exit(app.exec_())
