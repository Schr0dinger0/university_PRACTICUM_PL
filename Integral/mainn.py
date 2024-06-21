import sys
import os
from check import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QMessageBox  # Это необходимые библиотеки
from PyQt5.QtCore import QSize
import math as m


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.integral)
        self.ui.action.triggered.connect(self.info)

    def info(self):
        QMessageBox.about(self, "Об авторе "," Программа была написана \nстудентом \nКорязовым Дмитрием")

    def integral(self):
        self.ui.label_5.setText(' ')
        s1 = 1
        s2 = 0
        iter_ = 0
        a = int(self.ui.textEdit.toPlainText());
        b = int(self.ui.textEdit_2.toPlainText())
        n = 4
        i = 0
        eps = float(self.ui.textEdit_3.toPlainText())
        while abs(s2 - s1) >= eps:
            s1 = s2;
            s2 = 0
            n = n * 2
            h = (b - a) / n
            iter_ += 1
            i = 0
            while i < n:
                x = a + h * (i + 0.5)
                k = (m.e ** (m.sqrt(1 + x + 0.2 * (x ** 2))))  # тут должна быть функция
                s2 += k * h
                i += 1
        answer = 'Значение интеграла: ' + str("%.3f" % (s2)) + "\nКоличество итераций: " + str(iter_)
        self.ui.label_5.setText(answer)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
