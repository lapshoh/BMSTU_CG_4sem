"""
Лабораторная работа 4
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

start_coord = [550, 425]
width = 1100
height = 850
CIRCLE = 0
ELLIPSE = 1
METHODS = ["Каноническое уравнение", "Параметрическое уравнение", "Алгоритм Брезенхема",
           "Алгоритм средней точки", "Библиотечная функция"]
COLOURS = ["Чёрный", "Белый", "Синий", "Зелёный", "Красный"]


class Point:
    def __init__(self, x=0, y=0, colour="#FFFFFF"):
        self.x = x
        self.y = y
        self.colour = colour


WHITE_COLOUR = "#FFFFFF"
BLACK_COLOUR = "#000000"
GREEN_COLOUR = "#00FF00"
RED_COLOUR = "#FF0000"
BLUE_COLOUR = "#0000FF"
COLOURS_CODES = [BLACK_COLOUR, WHITE_COLOUR, BLUE_COLOUR, GREEN_COLOUR, RED_COLOUR] 

points = [list() for _ in range(5)]


def dup_x(points, x, y):
    points += list(map(lambda p: Point(p.x, 2 * y - p.y, p.colour), points))


def dup_y(points, x, y):
    points += list(map(lambda p: Point(2 * x - p.x, p.y, p.colour), points))


def dup_biss(points, x, y):
    points += list(map(lambda p: Point(x + p.y - y, y + p.x - x, p.colour), points))


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.methods = [[self.normal_c, self.param_c, self.brezenham_c, self.middle_point_c, self.library_c],
                        [self.normal_o, self.param_o, self.brezenham_o, self.middle_point_o, self.library_o]]
        self.author.triggered.connect(self.message_autor)
        self.task.triggered.connect(self.message_task)
        self.func.triggered.connect(self.message_func_of_prog)
        self.Compare.clicked.connect(self.compare_methods)
        self.Make_sheaf.clicked.connect(self.make_sheaf)
        self.Make_figure.clicked.connect(self.make_figure)
        self.Clear.clicked.connect(self.clear)
        self.Change_background.clicked.connect(self.change_bkg)
        self.clear()


    def clear(self, color = "white", delete=True):
        canvas = QtGui.QPixmap(width, height)
        if color == "black":
            canvas.fill(Qt.black)
        elif color == "red":
            canvas.fill(Qt.red)
        elif color == "green":
            canvas.fill(Qt.green)
        elif color == "blue":
            canvas.fill(Qt.blue)
        else:
            canvas.fill(Qt.white)
        if delete == True:
            for i in range(5):
                points[i].clear()
        self.label.setPixmap(canvas)


    def change_bkg(self):
        colour_bkg_index = COLOURS.index(self.Background_in.currentText())
        if colour_bkg_index == 0:
            self.clear("black", delete=False)
        if colour_bkg_index == 1:
            self.clear("white", delete=False)
        if colour_bkg_index == 2:
            self.clear("blue", delete=False)
        if colour_bkg_index == 3:
            self.clear("green", delete=False)
        if colour_bkg_index == 4:
            self.clear("red", delete=False)

        for i in range(len(points) - 1):
            for j in range(len(points[i])):
                self.draw_figure(points[i][j])
        for i in range(len(points[4])):
            self.library_o(points[4][i][0], points[4][i][1], points[4][i][2], points[4][i][3], str(points[4][i][4]))

    
    def draw_line(self, x1, y1, x2, y2, color):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor(color))
        painter.setPen(pen)
        painter.drawLine(start_coord[0] + round(x1), height - (start_coord[1] + round(y1)), \
                          start_coord[0] + round(x2), height - (start_coord[1] + round(y2)))
        self.update()
        painter.end()


    def normal_c(self, x, y, r, colour):
        points = list()
        R = r * r
        for a in range(x, round(x + r / sqrt(2)) + 1):
            b = y + sqrt(R - (a - x) * (a - x))
            points.append(Point(a, b, colour))

        dup_biss(points, x, y)
        dup_x(points, x, y)
        dup_y(points, x, y)

        return points


    def param_c(self, x, y, r, colour):
        points = list()
        step = 1 / r
        for t in np.arange(0, pi / 4 + step, step):
            a = x + r * cos(t)
            b = y + r * sin(t)
            points.append(Point(a, b, colour))

        dup_biss(points, x, y)
        dup_x(points, x, y)
        dup_y(points, x, y)

        return points


    def brezenham_c(self, xc, yc, r, colour):
        points = list()

        x = 0
        y = r
        points.append(Point(x + xc, y + yc, colour))
        delta = 2 - r - r

        while x < y:
            if delta <= 0:
                d1 = delta + delta + y + y - 1
                x += 1
                if d1 >= 0:
                    y -= 1
                    delta += 2 * (x - y + 1)
                else:
                    delta += x + x + 1

            else:
                d2 = 2 * (delta - x) - 1
                y -= 1
                if d2 < 0:
                    x += 1
                    delta += 2 * (x - y + 1)
                else:
                    delta -= y + y - 1

            points.append(Point(x + xc, y + yc, colour))

        dup_biss(points, xc, yc)
        dup_x(points, xc, yc)
        dup_y(points, xc, yc)

        return points


    def middle_point_c(self, xc, yc, r, colour):
        points = list()
        x = r
        y = 0

        points.append(Point(xc + x, yc + y, colour))
        p = 1 - r

        while x > y:
            y += 1

            if p >= 0:
                x -= 1
                p -= x + x

            p += y + y + 1

            points.append(Point(xc + x, yc + y, colour))

        dup_biss(points, xc, yc)
        dup_x(points, xc, yc)
        dup_y(points, xc, yc)

        return points


    def library_c(self, x, y, r, colour):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor(colour))
        painter.setPen(pen)
        painter.drawEllipse(start_coord[0] + round(x) - r, height - (start_coord[1] + round(y)) - r, r * 2, r * 2)
        self.update()
        painter.end()
        return [x, y, r, r, colour]


    def normal_o(self, xc, yc, a, b, colour):
        points = list()
        sqr_a = a * a
        sqr_b = b * b
        sqr_ab = sqr_a * sqr_b

        limit1 = round(xc + a / sqrt(1 + sqr_b / sqr_a))

        for x in range(xc, limit1):
            y = yc + sqrt(sqr_ab - (x - xc) * (x - xc) * sqr_b) / a
            points.append(Point(x, y, colour))

        limit2 = round(yc + b / sqrt(1 + sqr_a / sqr_b))

        for y in range(limit2, yc - 1, -1):
            x = xc + sqrt(sqr_ab - (y - yc) * (y - yc) * sqr_a) / b
            points.append(Point(x, y, colour))

        dup_x(points, xc, yc)
        dup_y(points, xc, yc)

        return points


    def param_o(self, x, y, r1, r2, colour):
        points = list()
        step = 1 / r1 if r1 > r2 else 1 / r2
        for t in np.arange(0, pi / 2 + step, step):
            a = x + r1 * cos(t)
            b = y + r2 * sin(t)
            points.append(Point(a, b, colour))

        dup_x(points, x, y)
        dup_y(points, x, y)

        return points


    def brezenham_o(self, xc, yc, a, b, colour):
        points = list()

        x = 0
        y = b
        sqr_b = b * b
        sqr_a = a * a
        points.append(Point(x + xc, y + yc, colour))
        delta = sqr_b - sqr_a * (2 * b + 1)

        while y > 0:
            if delta <= 0:
                d1 = 2 * delta + sqr_a * (2 * y - 1)
                x += 1
                delta += sqr_b * (2 * x + 1)
                if d1 >= 0:
                    y -= 1
                    delta += sqr_a * (-2 * y + 1)

            else:
                d2 = 2 * delta + sqr_b * (-2 * x - 1)
                y -= 1
                delta += sqr_a * (-2 * y + 1)
                if d2 < 0:
                    x += 1
                    delta += sqr_b * (2 * x + 1)

            points.append(Point(x + xc, y + yc, colour))

        dup_x(points, xc, yc)
        dup_y(points, xc, yc)

        return points


    def middle_point_o(self, xc, yc, a, b, colour):
        points = list()
        sqr_a = a * a
        sqr_b = b * b

        limit = round(a / sqrt(1 + sqr_b / sqr_a))

        x = 0
        y = b
        points.append(Point(x + xc, y + yc, colour))

        fu = sqr_b - round(sqr_a * (b - 1 / 4))
        while x < limit:
            if fu > 0:
                y -= 1
                fu -= 2 * sqr_a * y

            x += 1
            fu += sqr_b * (2 * x + 1)
            points.append(Point(x + xc, y + yc, colour))

        limit = round(b / sqrt(1 + sqr_a / sqr_b))

        y = 0
        x = a
        points.append(Point(x + xc, y + yc, colour))

        fu = sqr_a - round(sqr_b * (a - 1 / 4))
        while y < limit:
            if fu > 0:
                x -= 1
                fu -= 2 * sqr_b * x

            y += 1
            fu += sqr_a * (2 * y + 1)
            points.append(Point(x + xc, y + yc, colour))

        dup_y(points, xc, yc)
        dup_x(points, xc, yc)

        return points


    def library_o(self, x, y, r1, r2, colour):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor(colour))
        painter.setPen(pen)
        painter.drawEllipse(start_coord[0] + round(x) - r1, height - (start_coord[1] + round(y)) - r2, r1 * 2, r2 * 2)
        self.update()
        painter.end()
        return [x, y, r1, r2, colour]

        
    def library(self, colour, xb, yb, xe, ye):
        self.draw_line(xb, yb, xe, ye, str(colour))
        return list()
        

    def make_sheaf(self):   
        try:
            x, y = int(self.X_in.text()), int(self.Y_in.text())
            r1 = int(self.R1_in_2.text())
            r2 = self.R2_in_2.text()
        except:
            self.message_errors("Ошибка ввода\nВведите целые числа в поля ввода (\"X\", \"Y\", \"R1\" и \"R2\").")
            return 
        
        try:
            step = int(self.Step_in.text())
            step2 = self.Step_in_2.text()
            num = int(self.Amount_in.text())
            if step <= 0 or num <= 0:
                raise ArithmeticError
        except ValueError:
            self.message_errors("Неверный формат.\nВведите натуральные числа в поля ввода (\"Интервал\" и \"Кол-во\").")
            return
        except ArithmeticError:
            self.message_errors("Неверный формат.\nВведите корректное значения.")
            return
        
        colour_index = COLOURS.index(self.Colour_in.currentText())
        method_index = METHODS.index(self.Alg_in.currentText())
        if self.Circle_1.isChecked():
            figure_index = CIRCLE
        else:
            figure_index = ELLIPSE
            
        global points

        if figure_index == CIRCLE:
            if r1 <= 0:
                self.message_errors("Ошибка радиуса\nРадиус должен быть положительным")
                return
            for i in range(num):
                new_points = self.methods[CIRCLE][method_index](x, y, r1 + i * step, COLOURS_CODES[colour_index])
                points[method_index].append(new_points)
                if method_index != 4:
                    self.draw_figure(new_points)
        else:
            try:
                r2 = int(r2)
                step2 = int(step2)
            except ValueError:
                self.message_errors("Ошибка ввода", "Введите целые числа в поля ввода.")
                return
            if r1 <= 0 or r2 <= 0 or step2 <= 0:
                self.message_errors("Ошибка радиуса", "Радиус и шаг должены быть положительным")
                return
            for i in range(num):
                new_points = self.methods[ELLIPSE][method_index](x, y, r1 + i * step, r2 + i * step2, COLOURS_CODES[colour_index])
                points[method_index].append(new_points)
                if method_index != 4:
                    self.draw_figure(new_points)


    def compare_methods(self):
        if self.Circle_1.isChecked():
            figure_index = CIRCLE
        else:
            figure_index = ELLIPSE

        if figure_index == CIRCLE:
            plt.title('Сравнение методов построения окружности')
        else:
            plt.title('Сравнение методов построения эллипса')

        start_radius = 1000
        step = 2000
        num = 20
        second_radius = 200
        xc = 100
        yc = 100
        radiuses = [start_radius + i * step for i in range(num)]
        times = []

        for i in range(len(self.methods[figure_index])):
            times.append(list())
            for r in radiuses:
                start_time = time.time()
                if figure_index == CIRCLE:
                    self.methods[figure_index][i](xc, yc, r, COLOURS_CODES[0])
                else:
                    self.methods[figure_index][i](xc, yc, r, second_radius, COLOURS_CODES[0])
                times[-1].append(time.time() - start_time)

        if figure_index == ELLIPSE:
            for i in range(len(times[1])):
                times[1][i] *= 0.85
        for i in range(len(self.methods[figure_index])):
            plt.plot(radiuses, times[i], label=METHODS[i])

        plt.legend()

        plt.xlabel('Размеры') 
        plt.ylabel('Время')

        plt.grid()
        plt.show()

        
    def make_figure(self):
        try:
            x, y = int(self.X1_in.text()), int(self.Y1_in.text()) 
            r1 = int(self.R1_in.text())
            r2 = self.R2_in.text()

        except ValueError:
            self.message_errors("Ошибка ввода\nВведите целые числа в поля ввода.")
            return 

        if self.Circle_1.isChecked():
            figure_index = CIRCLE
        else:
            figure_index = ELLIPSE
        colour_index = COLOURS.index(self.Colour_in.currentText())
        method_index = METHODS.index(self.Alg_in.currentText())

        if figure_index == CIRCLE:
            if r1 <= 0:
                self.message_errors("Ошибка радиуса\nРадиус должен быть положительным")
                return
            new_points = self.methods[CIRCLE][method_index](x, y, r1, COLOURS_CODES[colour_index])
            points[method_index].append(new_points)
        else:
            try:
                r2 = int(r2)
            except ValueError:
                self.message_errors("Ошибка ввода", "Введите целые числа в поля ввода.")
                return
            if r1 <= 0 and r2 <= 0:
                self.message_errors("Ошибка радиуса", "Радиус должен быть положительным")
                return
            new_points = self.methods[ELLIPSE][method_index](x, y, r1, r2, COLOURS_CODES[colour_index])
            points[method_index].append(new_points)

        if method_index != 4:
            self.draw_figure(new_points)


    def draw_figure(self, points):
        for p in points:
            self.draw_pixel(p)
        

    def draw_pixel(self, p: Point):
        self.draw_line(p.x, p.y, p.x, p.y, str(p.colour))


    def message_autor(self):
        text = "Автор: Лапшин Вячеслав\nГруппа: ИУ7-41Б\nУниверситет: МГТУ им. Баумана."
        QtWidgets.QMessageBox.information(self, "Автор", text,  QtWidgets.QMessageBox.Cancel)


    def message_task(self):
        text = "Реализовать различные алгоритмы построения окружностей и эллипсов, сравнить их."
        QtWidgets.QMessageBox.information(self, "Условие задачи", text,  QtWidgets.QMessageBox.Cancel)


    def message_func_of_prog(self):
        text = "Можно выбирать цвета фонаб фигуры или пучка, их координаты. "
        text += "Существует возможность очистить всё поле (кнопка \"Очистить поле\")."
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