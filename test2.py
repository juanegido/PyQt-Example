from PyQt5 import QtWidgets
import sys


class PegGameWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle('Triangle Peg Game')
        self.setToolTip("Play this game!!")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = PegGameWindow()
    app.exec_()
