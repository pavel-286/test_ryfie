from PyQt5 import *
from PyQt5.QWidgets import QApplication, QLabel, QPushButton, QVBoxLayout

import instr

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(instr.win_x, instr.win_y, instr.win_width, instr.win_height)
        self.setTitle('Тест Руфье')

        self.vline = QVBoxLayout()
        self.btn = QPushButton()
        self.btn.setText(instr.txt_next)
        self.btn.clicked.connect(self.button_click)
        self.text1 = QLabel()
        self.text1.setText(instr.txt_hello)
        self.text2 = QLabel()
        self.text2.setText(instr.txt_instruction)

        self.vline.addWidget(self.text1, alignment = Qt.Alignleft)
        self.vline.addWidget(self.text2, alignment = Qt.Alignleft)
        self.vline.addWidget(self.btn, alignment = Qt.Aligncenter)
        
        self.setLayout(self.vline)

        self.show()

    def button_click(self):
        pass

app = QApplication()
win = Window()

app.exec_()