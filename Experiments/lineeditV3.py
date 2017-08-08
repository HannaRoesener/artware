import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

class MyWin(QWidget):

    def __init__(self):
        super(MyWin,self).__init__()

        self.initGUI()


    def initGUI(self):

        # Widgets

        self.copy0 = QLabel(self)
        self.copy1 = QLabel(self)
        search = QLineEdit(self)
        btn0 = QPushButton("Google Search")
        btn1 = QPushButton("I'm feeling lucky!")

        # position QLabels

        self.copy0.move(0, 0)
        self.copy1.move(0, 30)

        # Layout Style

        layout = QVBoxLayout()
        layout.addWidget(search)
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(btn0, alignment=Qt.AlignLeft)
        buttonLayout.addWidget(btn1, alignment=Qt.AlignLeft)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)

        # Searchbutton


        # string


        search.textChanged[str].connect(self.onChanged)

        # Window Basics

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Google Search')
        self.show()


    def onChanged(self, text):

        self.copy0.setText(text)
        self.copy0.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    Google = MyWin()
    sys.exit(app.exec_())
