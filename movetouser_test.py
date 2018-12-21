# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movetouser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow, ):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 127)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Movetouser = QtWidgets.QPushButton(self.centralwidget)
        self.Movetouser.setGeometry(QtCore.QRect(10, 10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Movetouser.setFont(font)
        self.Movetouser.setObjectName("Movetouser")
        self.Movetoall = QtWidgets.QPushButton(self.centralwidget)
        self.Movetoall.setGeometry(QtCore.QRect(514, 10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Movetoall.setFont(font)
        self.Movetoall.setObjectName("Movetoall")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(250, 10, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 21))
        
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.statusbar.setFont(font)
        self.statusbar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage('Сейчас в каталоге Пользователь: {}'.format(self.check_empty()))
        

        self.Movetouser.clicked.connect(self.move_to_user)
        self.Movetoall.clicked.connect(self.move_back)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FileMove v1.0"))
        self.Movetouser.setText(_translate("MainWindow", "Переместить в \'Пользователь\'"))
        self.Movetoall.setText(_translate("MainWindow", "Переместить в общий ресурс"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Закурдаев_ДА"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Гилязетдинов_АР"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Стаценко_ВВ"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Перов_КА"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Ломакин_ИА"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Максимов_АН"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Лавров_БМ"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Иванов_АИ"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Кондалов_АВ"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Митряев_СН"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Рыблов_АВ"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Самойлов_НВ"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Николаев_АС"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Казанин_ВВ"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Зайцев_ИИ"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Брынзюк_АВ"))
        self.comboBox.setItemText(16, _translate("MainWindow", "Назаров_МЕ"))
        self.comboBox.currentText()


    def move_to_user(self):
        folder = os.listdir('D:\\Пользователь\\')
        try:
            if len(folder) > 0:
                self.statusbar.showMessage('Невозможно выполнить, в папке "Пользователь": {}.'.format(self.check_empty())) 
                pass
            else:
                username = (self.comboBox.currentText())
                os.rename('D:\\Файлы пользователей\{}'.format(username), 'D:\\Пользователь\\{}'.format(username))
                self.statusbar.showMessage('Сейчас в папке "Пользователь": {}.'.format(self.check_empty()))
        except FileNotFoundError:
            self.statusbar.showMessage('Ошибка. Проверьте наличие папки в каталоге "Файлы пользователей".')
            pass


    def move_back(self):
        try:
            user_name = os.listdir('D:\\Пользователь\\')[0]
            os.rename('D:\\Пользователь\\{}'.format(user_name), 'D:\\Файлы пользователей\\{}'.format(user_name))
            self.statusbar.showMessage('Сейчас в папке "Пользователь": {}.'.format(self.check_empty()))
        except IndexError:
            self.statusbar.showMessage('Невозможно выполнить, в папке "Пользователь" пусто.')


    def check_empty(self):
        while True:
            try:
                folder = os.listdir('D:\\Пользователь\\')[0]
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
