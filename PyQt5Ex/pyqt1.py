import sys
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setGeometry(0,0,300,300)
window.setWindowTitle('PyQt Window')
window.show()
sys.exit(app.exec_())