from PyQt5.QtWidgets import *
# QApplication, QMainWindow, qApp, QGridLayout, QHBoxLayout, QAbstractItemView, QComboBox, QSpinBox, QListWidget, QLineEdit, QPlainTextEdit, QPushButton, QWidget, QRadioButton, QCheckBox, QGroupBox, QProgressBar, QSlider, QMessageBox
from PyQt5.QtCore import Qt
from random import randint
import sys

class SignupWin(QMainWindow):
    def __init__(self):
        super(SignupWin, self).__init__()
        self.initGUI()

    def initGUI(self):
        mainLayout = QVBoxLayout()
        centerWidget = QWidget()
        centerWidget.setObjectName("parent")
        centerWidget.setLayout(mainLayout)
        self.setCentralWidget(centerWidget)
        self.setWindowTitle("Google Registration")

        # genderPicker

        self.genderPicker = QComboBox() # is that what I want it to be?
        self.genderPicker.addItem("Female")
        self.genderPicker.addItem("Male")
        self.genderPicker.addItem("Other")
        self.genderPicker.addItem("Rather not say")
        self.genderPicker.setCurrentIndex(0)

        #BirthdayPicker

        self.bdayPicker = QComboBox()
        self.bdayPicker.addItem("January")
        self.bdayPicker.addItem("February")
        self.bdayPicker.addItem("March")
        self.bdayPicker.addItem("April")
        self.bdayPicker.addItem("May")
        self.bdayPicker.addItem("June")
        self.bdayPicker.addItem("July")
        self.bdayPicker.addItem("August")
        self.bdayPicker.addItem("September")
        self.bdayPicker.addItem("October")
        self.bdayPicker.addItem("November")
        self.bdayPicker.addItem("December")
        self.bdayPicker.setCurrentIndex(0)

        #LocationPicker

        self.locationPicker = QComboBox()
        pass

        layForm = QFormLayout()
        layForm.addRow(QLabel("Name"), QLineEdit())
        layForm.addRow(QLabel("Choose your username"), QLineEdit())
        layForm.addRow(QLabel("Create a password"), QLineEdit())
        layForm.addRow(QLabel("Confirm your password"), QLineEdit())
        layForm.addRow(QLabel("Birthday"), self.bdayPicker)
        layForm.addRow(QLabel("Gender"), self.genderPicker)
        layForm.addRow(QLabel("Mobile phone"), QLineEdit())
        layForm.addRow(QLabel("Your current email address"), QLineEdit())
        layForm.addRow(QLabel("Location"), self.locationPicker)
        formGroupBox = QGroupBox()
        formGroupBox.setObjectName("fromquestions")
        formGroupBox.setLayout(layForm)
        mainLayout.addWidget(formGroupBox)

        btn = QPushButton("Next Step")
        btn.setObjectName("btn")
        btn.setStyleSheet("""
            QPushButton {
            background-color: blue;
            color: white;
            font-style: bold;
            padding: 20px;
            }
            """)

        layh = QHBoxLayout()
        layh.addWidget(btn)
        hGroupbox = QGroupBox()
        hGroupbox.setObjectName("registration")
        hGroupbox.setLayout(layh)
        mainLayout.addWidget(hGroupbox)


if __name__=="__main__":
    app = QApplication(sys.argv)
    win = SignupWin()
    win.show()
sys.exit(app.exec_())
