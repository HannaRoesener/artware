import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.initGUI()
        self.list1 = []

    def initGUI(self):
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("First Try")
        search = QLineEdit(self)
        btn = QPushButton("Search", self)
        btn.clicked.connect(self.add_keyword)

        layout = QHBoxLayout()
        layout.addWidget(search)
        layout.addWidget(btn)
        self.setLayout(layout)


    def add_keyword(self):
        list1 = []
        for i in range(10):
            list1.append('search'(i + 1))
            return self.list1.text()
            # or print list1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
