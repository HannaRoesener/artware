# References:
# Google Logo - https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.sv
# Google Icon - https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg
###############################################################################
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QShortcut, QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QFont, QIcon
from random import randint

class MyWin(QWidget):
    height = 600
    width = 1000

    def __init__(self):
        super(MyWin,self).__init__()
        self.initGUI()
        self.searchterms = []
        self.setWindowTitle('Google')
        self.setWindowIcon(QIcon('googleicon.png'))
        self.setGeometry(40,40, self.width, self.height)
        self.setFixedWidth(950)
        self.setFixedHeight(550)
        self.show()

    def initGUI(self):

        # Widgets
        self.copy = QLabel(self)
        self.search = QLineEdit(self)
        self.search.setFixedWidth(450)

        btn0 = QPushButton("Google Search")
        btn1 = QPushButton("I'm feeling Lucky")
        btn0.clicked.connect(self.newQLabel)
        btn1.clicked.connect(self.sorry)
        btn0.setFont(QFont('Arial', 13, QFont.Bold))
        btn1.setFont(QFont('Arial', 13, QFont.Bold))
        btn0.setStyleSheet("""
            QPushButton {
                background-color: #F1F1F1;
                color: #757575;
                margin-left: 310px;
                padding-left: 15px;
                padding-right: 15px;
                padding-top: 10px;
                padding-bottom: 10px;
                margin-top: 20px;
                margin-bottom: 100px;
                border: none;
            }
            QPushButton:hover {
            color: black;
            border: 1px solid darkgrey;
            }
        """)

        btn1.setStyleSheet("""
            QPushButton {
                background-color: #F1F1F1;
                color: #757575;
                margin-right: 310px;
                font-style: Arial Bold;
                padding-left: 15px;
                padding-right: 15px;
                padding-top: 10px;
                padding-bottom: 10px;
                margin-top: 20px;
                margin-bottom: 100px;
                border: none;
            }
            QPushButton:hover {
            color: black;
            border: 1px solid darkgrey;
            }
        """)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.search.setGraphicsEffect(self.shadow)

        self.search.setStyleSheet("""
            QLineEdit {
            border: 1px solid #C9C9C9;
            padding: 12px;
            font-size: 15px;
            }
        """)
        self.image = QLabel(self)
        pixmap = QPixmap('googlelogo.png')
        pixmap = pixmap.scaledToWidth(300)
        self.image.setStyleSheet ("""
            QLabel {
            padding-bottom: 30px;
            qproperty-alignment: AlignCenter;
            }
        """)
        self.image.setPixmap(pixmap)


        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image, alignment=Qt.AlignBottom)
        layout.addWidget(self.search, alignment=Qt.AlignJustify)
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(btn0, alignment=Qt.AlignLeft)
        buttonLayout.addWidget(btn1, alignment=Qt.AlignRight)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)
        self.show()


    def newQLabel(self):
        newlabel = QLabel(self.search.text(), self)
        newlabel.move(randint(30,920), randint(30,520))
        self.searchterms.append(newlabel)
        newlabel.setMaximumWidth(100) # I could not get this to work... Some Queries get cut off.
        newlabel.setStyleSheet ("""
            QLabel {
                font-size: 15px;
            }
            """)
        newlabel.show()
        self.search.clear()


    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Return:
            self.newQLabel()

    def sorry(self):
        QMessageBox.about(self, "Sorry!", "Service currently not available. \nWe are working hard on getting it fixed. \nSorry for any inconvenience.")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    Google = MyWin()
    p = Google.palette()
    p.setColor(Google.backgroundRole(), Qt.white)
    Google.setPalette(p)
    sys.exit(app.exec_())
