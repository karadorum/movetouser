# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wish.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import ui


class App(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

       # self.pushButton.clicked.connect(self.addrow)


        
    
    
    
    


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
    
    

    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''       
        #QtWidgets.QInputDialog.getText(self, 'input dialog', 'enter your name')
        
        param1 = Dialog.lineEdit.text()
        param2 = Dialog.lineEdit_2.text()
        def save_params(param1, param2):
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(param1))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(param2))
        
        Dialog.buttonBox.accepted.connect(save_params(param1,param2))

    def inputDialog(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'input dialog', 'enter your name')

        if ok:
            print (text)


    def save_text(self):
        param1 = self.lineEdit.text()
        param2 = self.lineEdit_2.text()
        print(param1, param2)
   ''' 
    
    


