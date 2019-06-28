# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clac.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(597, 300)
        self.ClearButton = QtWidgets.QPushButton(Dialog)
        self.ClearButton.setGeometry(QtCore.QRect(100, 150, 121, 51))
        self.ClearButton.setObjectName("ClearButton")
        self.CalcButton = QtWidgets.QPushButton(Dialog)
        self.CalcButton.setGeometry(QtCore.QRect(300, 150, 131, 51))
        self.CalcButton.setObjectName("CalcButton")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 40, 503, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input1 = QtWidgets.QLineEdit(self.widget)
        self.input1.setObjectName("input1")
        self.horizontalLayout.addWidget(self.input1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.input2 = QtWidgets.QLineEdit(self.widget)
        self.input2.setObjectName("input2")
        self.horizontalLayout.addWidget(self.input2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.result = QtWidgets.QLineEdit(self.widget)
        self.result.setObjectName("result")
        self.horizontalLayout.addWidget(self.result)

        self.retranslateUi(Dialog)
        self.ClearButton.clicked.connect(self.result.clear)
        self.ClearButton.clicked.connect(self.input2.clear)
        self.ClearButton.clicked.connect(self.input1.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ClearButton.setText(_translate("Dialog", "Clear"))
        self.CalcButton.setText(_translate("Dialog", "Calculate"))
        self.comboBox.setItemText(0, _translate("Dialog", "+"))
        self.comboBox.setItemText(1, _translate("Dialog", "-"))
        self.comboBox.setItemText(2, _translate("Dialog", "*"))
        self.comboBox.setItemText(3, _translate("Dialog", "/"))
        self.label.setText(_translate("Dialog", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

