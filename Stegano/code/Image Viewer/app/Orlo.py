from PyQt5.QtWidgets import QApplication
from app.MainWindow import MainWindow

# For debugging
# import os
# os.environ['QT_DEBUG_PLUGINS'] = "1"

class Orlo:
    
    def __init__(self, argv):
        self.app = QApplication(argv)
        self.ex = MainWindow()

    def run(self): 
        self.app.exec_()
