from file import File
import gui
import sys
import os
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QLineEdit, QFormLayout

def main():
    """PyCalc's main function."""
    
    captionApp = QApplication([])
    guiWindow = gui.Ui()
    guiWindow.show()
    sys.exit(captionApp.exec())

    file1 = file.File()
    file = file1.file_read()
    # file1.no_lines_to_file(file)

if __name__ == "__main__":

    main()