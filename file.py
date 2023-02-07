import re
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class File: 

    def __init__(self):
        self.filename = '/home/peterleitmann/git/personal/caption-parser/test (1).txt'

    def loadFile(self):
        # print("clicked")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.FileMode.ExistingFile)
        # dlg.setFilter("Text files (*.txt)")
        if dlg.exec():
            filename = dlg.selectedFiles()
            print(filename)

    def file_print(self):
        # print(self.filename)
        with open(self.filename, "r+") as file1:
            # Reading from a file
            print(file1.read())

    def file_read(self):
        print(self.filename)
        with open(self.filename, "r+") as file1:
            # Reading from a file
            self.no_lines_to_file(file1.read())

    # plan is to set name of file by a timestamp
    def no_lines_to_file(self, file):
        with open(self.filename + '_output', 'x') as f:
            f.write(file.replace('\n\n','\n'))
        #print(file.replace('\n\n','\n'))

    def clicked():
        print("clicked")