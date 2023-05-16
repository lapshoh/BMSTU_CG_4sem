"""
Лабораторная работа 5
Лапшин В.  ИУ7-41Б
"""
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
import sys
import design
import numpy as np
from math import *
import time
import matplotlib.pyplot as plt

width = 1100
height = 850

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clear()


    def clear(self):
        canvas = QtGui.QPixmap(width, height)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)


    def message_autor(self):
        text = "Автор: Лапшин Вячеслав\nГруппа: ИУ7-41Б\nУниверситет: МГТУ им. Баумана."
        QtWidgets.QMessageBox.information(self, "Автор", text,  QtWidgets.QMessageBox.Cancel)


    def message_task(self):
        text = "Реализовать закраску фигуры алгоритмом заполнения с перегородкой."
        QtWidgets.QMessageBox.information(self, "Условие задачи", text,  QtWidgets.QMessageBox.Cancel)


    def message_func_of_prog(self):
        text = "Можно выбирать цвета закраски и линий, добавлять точки нажатием или кнопкой. Реализована функция замыкания "
        text += "фигуры. Существует возможность очистить всё поле (кнопка \"Очистить поле\")."
        QtWidgets.QMessageBox.information(self, "Функционал программы", text,  QtWidgets.QMessageBox.Cancel)


    def message_errors(self, text):
        QtWidgets.QMessageBox.warning(self, "Ошибка", text, QtWidgets.QMessageBox.Cancel)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()