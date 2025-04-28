from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout

#создаём объект приложения
app = QApplication([])
# создаём объект главного окна
my_win = QWidget()
# создаём название главного окна
my_win.setWindowTitle('Моё первое приложение')
# задаём точку появления окна на экране компьютера
my_win.move(900, 70)
# задаём размер окна
my_win.resize(400, 200)
# даём команду окну показаться
my_win.show()

v_line = QVBoxLayout()
h_line = QHBoxLayout()
label = QLabel('Победитель:')
v_line.addWidget(label, alignment=Qt.AlignCenter)
my_win.setLayout(v_line)
app.exec_()