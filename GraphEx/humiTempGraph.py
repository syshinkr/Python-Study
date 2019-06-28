# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'humiTempGraph.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(705, 362)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(320, 300, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(340, 50, 321, 221))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 90, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 140, 31, 16))
        self.label_2.setObjectName("label_2")
        self.tempEdit = QtWidgets.QLineEdit(Dialog)
        self.tempEdit.setGeometry(QtCore.QRect(150, 90, 113, 20))
        self.tempEdit.setObjectName("tempEdit")
        self.humiEdit = QtWidgets.QLineEdit(Dialog)
        self.humiEdit.setGeometry(QtCore.QRect(150, 140, 113, 20))
        self.humiEdit.setObjectName("humiEdit")
        self.LEDBtn1 = QtWidgets.QPushButton(Dialog)
        self.LEDBtn1.setGeometry(QtCore.QRect(150, 200, 75, 23))
        self.LEDBtn1.setObjectName("LEDBtn1")
        self.LEDBtn2 = QtWidgets.QPushButton(Dialog)
        self.LEDBtn2.setGeometry(QtCore.QRect(150, 240, 75, 23))
        self.LEDBtn2.setObjectName("LEDBtn2")
        self.LEDBtn3 = QtWidgets.QPushButton(Dialog)
        self.LEDBtn3.setGeometry(QtCore.QRect(150, 280, 75, 23))
        self.LEDBtn3.setObjectName("LEDBtn3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "온도"))
        self.label_2.setText(_translate("Dialog", "습도"))
        self.LEDBtn1.setText(_translate("Dialog", "LED_1"))
        self.LEDBtn2.setText(_translate("Dialog", "LED_2"))
        self.LEDBtn3.setText(_translate("Dialog", "LED_3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

