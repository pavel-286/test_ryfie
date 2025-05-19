from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

import instr

import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(instr.win_width, instr.win_height)
        self.move(instr.win_x, instr.win_y)

        self.setWindowTitle('Тест Руфье')

        self.vline = QVBoxLayout()
        self.btn = QPushButton()
        self.btn.setText(instr.txt_next)
        self.btn.clicked.connect(self.button_click)
        self.text1 = QLabel()
        self.text1.setText(instr.txt_hello)
        self.text2 = QLabel()
        self.text2.setText(instr.txt_instruction)

        self.vline.addWidget(self.text1, alignment = Qt.AlignLeft)
        self.vline.addWidget(self.text2, alignment = Qt.AlignLeft)
        self.vline.addWidget(self.btn, alignment = Qt.AlignCenter)
        
        self.setLayout(self.vline)

        self.show()

    def button_click(self):
        pass

app = QApplication(sys.argv)
win = Window()

sys.exit(app.exec_())