from PyQt5 import QtWidgets, QtCore

class PegGameWindow(QtWidgets.QMainWindow):
    def __init__(self):

    def setup(self):

        self.central_widget = QtWidgets.QWidget(self)
        self.new_button = StartNewGameBtn(self.central_widget)
        self.quit_button = QuitBtn(self.central_widget)
        self.setCentralWidget(self.central_widget)
        exit_action = QtWidgets.QAction('Exit', self)
        exit_action.triggered.connect(QtWidgets.qApp.quit)
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_action)
        self.show()



