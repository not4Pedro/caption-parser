from PyQt6 import QtWidgets, uic
from file import File
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('gui-for-parser.ui', self) # Load the .ui file
        # self.show() # Show the GUI

        file = File()

        # button mapping
        self.button = self.findChild(QtWidgets.QPushButton, 'load_button')
        # map button to method
        self.button.setCheckable(True)
        # self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(lambda: file.loadFile())

        self.button = self.findChild(QtWidgets.QPushButton, 'remove_lines_button')
        self.button.setCheckable(True)
        self.button.clicked.connect(lambda: file.file_read())