from file import File
import gui  
import sys
import os
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QLineEdit, QFormLayout
    
if __name__ == "__main__":

    captionApp = QApplication([])
    guiWindow = gui.Ui()
    guiWindow.show()
    sys.exit(captionApp.exec())