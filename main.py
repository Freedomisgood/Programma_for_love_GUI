# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'main.py'
# Created by: PyQt5 UI code generator 5.10.1
# WARNING! All changes made in this file will be lost!
import sys
import caofunction
from PyQt5.QtWidgets import QApplication, QMainWindow,QSplashScreen
from PyQt5.QtGui import QPixmap
import time
if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(':/load/loading.jpg'))
    splash.show()
    splash.showMessage('正在加载请稍等..')
    time.sleep(0.5)
    app.processEvents()
    ui = caofunction.MyWindow()
    ui.show()
    splash.finish(ui)
    sys.exit(app.exec_())
