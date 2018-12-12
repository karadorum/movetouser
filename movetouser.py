# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movetouser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 130)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Movetouser = QtWidgets.QPushButton(self.centralwidget)
        self.Movetouser.setGeometry(QtCore.QRect(30, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Movetouser.setFont(font)
        self.Movetouser.setObjectName("Movetouser")
        self.Movetoall = QtWidgets.QPushButton(self.centralwidget)
        self.Movetoall.setGeometry(QtCore.QRect(520, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Movetoall.setFont(font)
        self.Movetoall.setObjectName("Movetoall")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(210, 30, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage('Сейчас в каталоге Пользователь: {}'.format(self.check_empty()))


        self.Movetouser.clicked.connect(self.move_to_user)
        self.Movetoall.clicked.connect(self.move_back)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Movetouser.setText(_translate("MainWindow", "MoveToUser"))
        self.Movetoall.setText(_translate("MainWindow", "MoveToAll"))
        self.comboBox.setItemText(0, _translate("MainWindow", "user1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "user2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "dima"))
        self.comboBox.currentText()

        #username = self.comboBox.currentText()

    def move_to_user(self):
        username = (self.comboBox.currentText())
        os.rename('C:\\1\\all\{}'.format(username), 'C:\\1\\user\\{}'.format(username))

    def move_back(self):
        user_name = os.listdir('C:\\1\\user')[0]
        os.rename('C:\\1\\user\\{}'.format(user_name), 'C:\\1\\all\\{}'.format(user_name))

    def check_empty(self):
        while True:
            try:
                folder = os.listdir('C:\\1\\user')[0]
            except IndexError:
                return 'Пусто'
            return folder



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

