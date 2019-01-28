from PyQt5 import QtWidgets


'''
(QApplication, QComboBox, QDialog, QDialogButtonBox, QFormLayout, 
QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox,
QTextEdit, QVBoxLayout)
'''
import sys


class Dialog(QtWidgets.QDialog):
    NumGridRows = 2
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()


        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle('Form Layout')


    def createFormGroupBox(self):
        self.formGroupBox = QtWidgets.QGroupBox('Form layout')
        layout = QtWidgets.QFormLayout()
        layout.addRow(QtWidgets.QLabel("Item:"), QtWidgets.QLineEdit())
        layout.addRow(QtWidgets.QLabel("Url:"), QtWidgets.QLineEdit())
        
        self.formGroupBox.setLayout(layout)
        print(QtWidgets.QLineEdit("Item:"))

    
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())

'''
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
        
'''