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

        self.win()

        pass

    def win(self):
        self.resize(instr.win_width, instr.win_height)
        self.move(instr.win_x, instr.win_y)
        self.setWindowTitle('Тест Руфье')