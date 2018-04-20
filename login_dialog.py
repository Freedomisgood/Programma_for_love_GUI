from PyQt5 import QtWidgets
from login import Ui_Dialog
import webbrowser
import requests

class login_Dialog(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.load)
        self.pushButton.clicked.connect(self.register)

    def load(self):
        pass
        #QtWidgets.QMessageBox.information(self,'')

    def register(self):
        #webbrowser.open()
        pass
        self.close()

