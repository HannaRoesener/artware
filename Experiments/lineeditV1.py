import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QShortcut, QListWidget
from PyQt5.QtCore import Qt

class MyWin(QWidget):

    def __init__(self):
        super(MyWin,self).__init__()

        self.initGUI()


    def initGUI(self):

        # Widgets
        self.copy0 = QLabel(self)
        self.copy1 = QLabel(self)
        self.search = QLineEdit(self)
        btn0 = QPushButton("Google Search")
        btn1 = QPushButton("I'm feeling lucky!")
        btn0.clicked.connect(self.newQLabel)
        # QShortcut.setKey(self.enterEvent).connect(self.newQLabel)


        # position QLabels
        self.copy0.move(0, 0)
        self.copy1.move(0, 30)
        # etc.

        # Layout 
        layout = QVBoxLayout()
        layout.addWidget(self.search)
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(btn0, alignment=Qt.AlignLeft)
        buttonLayout.addWidget(btn1, alignment=Qt.AlignLeft)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)
        self.show()


    def newQLabel(self):
        # self.search.displayText()
        searchterms = []
        searchterms.append(self.search.text())
        print searchterms
        self.search.clear()

        # self.LabelList = QListWidget(self)
        # item = QLabel(self)
        # self.LabelList.addItem(self, item)
        # self.LabelList.show()


        # Window Basics

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Google Search')
        self.show()

    #
    # def onChanged(self, text):
    #
    #     self.copy0.setText(text)
    #     self.copy0.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    Google = MyWin()
    sys.exit(app.exec_())
