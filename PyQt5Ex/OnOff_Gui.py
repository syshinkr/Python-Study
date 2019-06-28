# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OnOff_Gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 239)
        Dialog.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.onButton = QtWidgets.QPushButton(Dialog)
        self.onButton.setGeometry(QtCore.QRect(60, 70, 131, 81))
        self.onButton.setStyleSheet("background: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 24pt \"Arial\";")
        self.onButton.setObjectName("onButton")
        self.offButton = QtWidgets.QPushButton(Dialog)
        self.offButton.setGeometry(QtCore.QRect(250, 70, 131, 81))
        self.offButton.setStyleSheet("background: rgb(0, 0, 255);\n"
"font: 75 24pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.offButton.setObjectName("offButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.onButton.setText(_translate("Dialog", "ON"))
        self.offButton.setText(_translate("Dialog", "OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

