# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wish.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from sqlite3 import Error
from db_setup import database, insert_data, show_data, create_connection, close_connection

class Ui_MainWindow(object):
    conn = create_connection(database)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(473, 399)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_dialog)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 10, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        #self.pushButton_2.clicked.connect(self.updaterow)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 10, 111, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        #self.pushButton_3.clicked.connect(self.widget_content)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(15, 81, 431, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 473, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_3.setText(_translate("MainWindow", "Удалить"))
        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "item"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "URL"))
    

    def open_dialog(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.ui.buttonBox.accepted.connect(self.addrow)
        self.Dialog.show()
        
        
       
    '''
    def create_connection(self):
        try:
            conn = sqlite3.connect("D:\Защита информации\DEV\CRUD\\testdb.db")
            return(conn)
            
        except Error as e:
            print(e)
    '''    

    def widget_content(self):
        query = 'SELECT * FROM items'
        c = self.conn.cursor()
        response = c.execute(query)
        rows = response.fetchall()
        for row in rows:
            index = rows.index(row)
            self.tableWidget.insertRow(index)
            self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(row[1]))
        
    
        
        #print( [(rowid, item, url) for rowid, item,url in response] )


    def addrow(self):        
        rowPosition = self.tableWidget.rowCount()
        str1 = self.ui.lineEdit.text()
        str2 = self.ui.lineEdit_2.text()
        if len(str1) > 0 and len(str2) >0:
            insert_data(create_connection(database), str1, str2)
            close_connection(create_connection(database))

            #self.tableWidget.insertRow(rowPosition)
            #self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str1))
            #self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(str2))        

    
    '''
    def deleterow(self):
        item = QtWidgets.QTableWidgetItem()
        if self.tableWidget.cellPressed == True:
            self.tableWidget.removeRow()
    '''   



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 136)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        #self.buttonBox.accepted.connect(self.pprint) 
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 60, 231, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(46, 20, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 61, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        param1 = self.lineEdit.text()
        param2 = self.lineEdit_2.text()
    '''
    def pprint(self):
        param1 = self.lineEdit.text()
        param2 = self.lineEdit_2.text()
        parameters = [param1, param2]
        return parameters
    '''

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Param1"))
        self.label_2.setText(_translate("Dialog", "Param2"))

    


'''    
    def addrow(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem('text1'))
        self.tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem('text1'))

        self.pushButton.clicked.connect(self.addrow)
'''      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.widget_content()
    sys.exit(app.exec_())

