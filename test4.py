from PyQt5 import QtWidgets
import sys


class PegGameWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setup()

    def setup(self):
        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle('Triangle Peg Game')
        self.setToolTip("Play the triangle peg game!")
        self.new_button = StartNewGameBtn(self)
        self.quit_button = QuitBtn(self)
        self.show()

    def closeEvent(self, event):
        reply = QuitMessage().exec_()
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class StartNewGameBtn(QtWidgets.QPushButton):
    def __init__(self, parent):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setText("Start New Game")
        self.move(20, 160)


class QuitMessage(QtWidgets.QMessageBox):
    def __init__(self):
        QtWidgets.QMessageBox.__init__(self)
        self.setText("Do you really want to quit?")
        self.addButton(self.No)
        self.addButton(self.Yes)




class QuitBtn(QtWidgets.QPushButton):
    def __init__(self, parent):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setText("Quit")
        self.move(150, 160)
        self.clicked.connect(QtWidgets.qApp.quit)
        self.setToolTip("Close the triangle peg game.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = PegGameWindow()
    app.exec_()
