import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 300, 300)
        self.setWindowTitle('PyQt5')
        self.setWindowIcon(QtGui.QIcon('image/bird.png'))
        self.show()


app = QtWidgets.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
