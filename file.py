import datetime
import re
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class File: 

    def __init__(self):
        self.path = []

    def loadFile(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.FileMode.ExistingFile)
        if dlg.exec():
            self.path = dlg.selectedFiles()
            if (dlg.selectedFiles()[0].split('.')[-1] != 'txt'):
                return
            print(self.path)

    def fileRead(self, fileName):
        if (len(self.path) == 0):
            return
        elif (self.path[0] == ''):
            print('no file specified')
            return

        with open(self.path[0], "r+") as file1:
            # Reading from a file
            self.noLinesToFile(file1.read(), fileName)

    def noLinesToFile(self, file, fileName):
        # set name of output file
        if (fileName.text() == ''):
            newFileName = self.path[0][:-4] + datetime.datetime.now().strftime("_%d-%m-%Y_%H:%M") + '.txt'
        else: 
            newFileName = fileName.text() + '.txt'   

        with open(newFileName, 'w+') as f:
            f.write(file.replace('\n\n','\n'))