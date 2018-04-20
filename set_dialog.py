from PyQt5 import QtWidgets
from Ui_time import Ui_Dialog
from PyQt5.QtCore import QDateTime
import json

class set_Dialog(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.exit)

    def confirm(self):
        need = {}
        with open('time.json','w') as f :
            time = self.dateTimeEdit.dateTime()
            need['time'] =time.toString('yyyy-MM-dd HH:mm:ss')
            json.dump(need,f)
            QtWidgets.QMessageBox.information(self,'提示','已定时')
        self.close()

    def exit(self):
        self.close()
