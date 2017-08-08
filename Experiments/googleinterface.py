from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from random import randint, choice
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGUI()


    def initGUI(self):
        self.button = QPushButton("Search")
        self.text = QLineEdit()
        self.button.clicked.connect(self.line_value)


        layout = QHBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.setWindowTitle("Google 2.0")
        self.show()

    def line_value(self):
        print self.text
        self.text.clear()
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
sys.exit(app.exec_())
