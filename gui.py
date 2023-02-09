from PyQt6 import QtWidgets, uic    
from file import File
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('gui-for-parser.ui', self) # Load the .ui file

        file = File()

        # button mapping
        self.button1 = self.findChild(QtWidgets.QPushButton, 'load_button')
        # map button to method
        self.button1.setCheckable(True)
        # self.button.clicked.connect(self.the_button_was_clicked)
        self.button1.clicked.connect(lambda: file.loadFile())

        # map lineedit input
        self.fileName = self.findChild(QtWidgets.QLineEdit, 'line_input')
        # remove lines button
        self.button2 = self.findChild(QtWidgets.QPushButton, 'remove_lines_button')
        self.button2.setCheckable(True)
        self.button2.clicked.connect(lambda: file.fileRead(self.fileName))