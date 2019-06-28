from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt_graph1 import *
import pyqtgraph as pg

x = []
y = []



class MyFirstGuiProgram(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.graphicsView.setBackground('#11ffff')
        self.graphicsView.plot(x, pen=pg.mkPen('r', width=2),
            style=QtCore.Qt.DashLine, symbol=('o'),
            symbolBrush='r')
        self.graphicsView_2.setBackground('#ffffff')
        self.graphicsView_2.plot(y, pen='#0000ff', symbol='x')
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyFirstGuiProgram()
    w.show()
    sys.exit(app.exec_())
