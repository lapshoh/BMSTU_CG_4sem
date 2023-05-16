"""
Лабораторная работа 3
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

start_coord = [550, 400]
width = 1100
height = 800
METHODS = ["Брезенхема (с целыми)", "Брезенхема (с дробными)", "Брезенхема (сглаживание)", "Ву",
           "ЦДА", "Библиотечные функции"]
COLOURS = ["Чёрный", "Белый", "Синий", "Зелёный", "Красный"]


class Colour:
    def __init__(self, red=0, green=0, blue=0):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        res = '#'
        res += '0' + hex(self.red)[2:] if self.red < 16 else hex(self.red)[2:]
        res += '0' + hex(self.green)[2:] if self.green < 16 else hex(self.green)[2:]
        res += '0' + hex(self.blue)[2:] if self.blue < 16 else hex(self.blue)[2:]
        return res

    def intensity_apply(self, percent):
        red = int(self.red + (WHITE_COLOUR.red - self.red) * (1 - percent))
        green = int(self.green + (WHITE_COLOUR.green - self.green) * (1 - percent))
        blue = int(self.blue + (WHITE_COLOUR.blue - self.blue) * (1 - percent))
        return Colour(red, green, blue)


class Point:
    def __init__(self, x=0, y=0, colour=Colour()):
        self.x = x
        self.y = y
        self.colour = colour


WHITE_COLOUR = Colour(255, 255, 255)
BLACK_COLOUR = Colour()
GREEN_COLOUR = Colour(green=255)
RED_COLOUR = Colour(red=255)
BLUE_COLOUR = Colour(blue=255)
COLOURS_CODES = [BLACK_COLOUR, WHITE_COLOUR, BLUE_COLOUR, GREEN_COLOUR, RED_COLOUR] 
sections = [list() for _ in range(6)]


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.methods = [self.brezenham_int, self.brezenham_float, self.brezenham_double, self.vu, self.cda, self.library]
        self.author.triggered.connect(self.message_autor)
        self.task.triggered.connect(self.message_task)
        self.func.triggered.connect(self.message_func_of_prog)
        self.Compare.clicked.connect(self.compare_methods)
        self.Make_seg.clicked.connect(self.make_seg)
        self.Make_sheaf.clicked.connect(self.make_sheaf)
        self.Clear.clicked.connect(self.clear)
        self.Change_background.clicked.connect(self.change_bkg)
        self.Explore_gradation.clicked.connect(self.explore_gradation)
        self.clear("white", delete=True)

    def clear(self, color, delete=True):
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
            for i in range(6):
                sections[i].clear()
        self.label.setPixmap(canvas)


    def change_bkg(self):
        colour_bkg_index = COLOURS.index(self.Background_color_in.currentText())
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

        for i in range(len(sections) - 1):
            for j in range(len(sections[i])):
                self.draw_section(sections[i][j])
        for i in range(len(sections[5])):
            self.draw_line(sections[5][i][1], sections[5][i][2], sections[5][i][3], sections[5][i][4], str(sections[5][i][0]))

    
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


    def cda(self, colour, xb, yb, xe, ye):
        section = list()
        dx, dy = xe - xb, ye - yb
        delta_x, delta_y = abs(dx), abs(dy)
        l = delta_x if delta_x > delta_y else delta_y
        dx /= l
        dy /= l
        x, y = xb, yb
        for _ in range(l + 1):
            section.append(Point(round(x), round(y), colour))
            x += dx
            y += dy
        return section


    def brezenham_float(self, colour, xb, yb, xe, ye):
        section = list()

        x, y = xb, yb
        dx = xe - xb
        dy = ye - yb

        sx = int(np.sign(dx))
        sy = int(np.sign(dy))
        dx, dy = abs(dx), abs(dy)

        if dx > dy:
            change = 0
        else:
            change = 1
            dx, dy = dy, dx

        m = dy / dx
        e = m - 1 / 2

        if not change:
            for _ in range(dx + 1):
                section.append(Point(int(x), int(y), colour))

                if e >= 0:
                    y += sy
                    e -= 1
                x += sx
                e += m
        else:
            for _ in range(dx + 1):
                section.append(Point(int(x), int(y), colour))

                if e >= 0:
                    x += sx
                    e -= 1
                y += sy
                e += m

        return section


    def brezenham_int(self, colour, xb: int, yb: int, xe: int, ye: int):
        section = list()

        x, y = xb, yb
        dx = xe - xb
        dy = ye - yb
        
        sx = int(np.sign(dx))
        sy = int(np.sign(dy))
        dx, dy = abs(dx), abs(dy)

        if dx > dy:
            change = 0
        else:
            change = 1
            dx, dy = dy, dx

        e = dy + dy - dx

        if not change:
            for _ in range(dx + 1):
                section.append(Point(x, y, colour))

                if e >= 0:
                    y += sy
                    e -= dx + dx
                x += sx
                e += dy + dy
        else:
            for _ in range(dx + 1):
                section.append(Point(x, y, colour))

                if e >= 0:
                    x += sx
                    e -= dx + dx
                y += sy
                e += dy + dy

        return section


    def brezenham_double(self, colour, xb, yb, xe, ye):
        section = list()
        x, y = xb, yb
        dx = xe - xb
        dy = ye - yb
        sx = int(np.sign(dx))
        sy = int(np.sign(dy))
        dx, dy = abs(dx), abs(dy)

        if dx > dy:
            change = 0
        else:
            change = 1
            dx, dy = dy, dx

        m = dy / dx
        e = 1 / 2
        w = 1 - m

        if not change:
            for _ in range(dx + 1):
                section.append(Point(int(x), int(y), 
                                    colour.intensity_apply(e)))
                if e >= w:
                    y += sy
                    e -= w
                else:
                    e += m
                x += sx
        else:
            for _ in range(dx + 1):
                section.append(Point(int(x), int(y), 
                                    colour.intensity_apply(e)))
                if e >= w:
                    x += sx
                    e -= w
                else:
                    e += m
                y += sy

        return section


    def vu(self, colour, xb, yb, xe, ye):
        section = list()    
        x, y = xb, yb
        dx = xe - xb
        dy = ye - yb
        sx = 1 if dx == 0 else int(np.sign(dx))
        sy = 1 if dy == 0 else int(np.sign(dy))
        dx, dy = abs(dx), abs(dy)

        if dx > dy:
            change = 0
        else:
            change = 1
            dx, dy = dy, dx

        m = dy / dx
        e = -1

        if not change:
            for _ in range(dx + 1):
                section.append(Point(round(x), round(y), 
                                    colour.intensity_apply(-e)))
                section.append(Point(round(x), int(y + sy), 
                                    colour.intensity_apply(1 + e)))

                e += m
                if e >= 0:
                    y += sy
                    e -= 1
                x += sx
        else:
            for _ in range(dx + 1):
                section.append(Point(round(x), round(y), 
                                    colour.intensity_apply(-e)))
                section.append(Point(int(x + sx), round(y), 
                                    colour.intensity_apply(1 + e)))

                e += m
                if e >= 0:
                    x += sx
                    e -= 1
                y += sy

        return section

       
    def library(self, colour, xb, yb, xe, ye):
        self.draw_line(xb, yb, xe, ye, str(colour))
        return list()
    
    def explore_gradation(self):
        xb = 0
        yb = 0
        r = 1000
        angle = 1
        cur_angle = 0
        colour_index = 0
        
        steps = [[0] for _ in range(5)]
        anglesList = [i for i in range(0, 91, 1)]

        while (cur_angle < 91):
            xe, ye = int(xb + r * cos(radians(cur_angle))), int(yb + r * sin(radians(cur_angle)))
            for i in range(5):
                new_sec = list()
                new_sec = self.methods[i](COLOURS_CODES[colour_index],
                                                        xb, yb, xe, ye)
                cur_steps = 0
                if i != 3:
                    for j in range(1, len(new_sec)):
                        if new_sec[j - 1].x < new_sec[j].x and new_sec[j - 1].y < new_sec[j].y:
                            cur_steps += 1
                else:
                    for j in range(1, len(steps[i - 1])):
                        cur_steps = steps[i - 1][j] + 2 - j % 2

                
                steps[i].append(cur_steps)
            
            cur_angle += angle
        
        steps = [i[1:] for i in steps]
        self.clear("white", delete=True)
        plt.rcParams['font.size'] = '15'
        plt.figure("Исследование ступенчатости алгоритмов построение.", figsize = (12, 8))

        plt.plot(anglesList, steps[0], '*', label="Брензенхем с вещественными коэффицентами")
        plt.plot(anglesList, steps[1], '--', label="Брензенхем с целыми коэффицентами")
        plt.plot(anglesList, steps[2], '.', label="Брензенхем со сглаживанием")
        plt.plot(anglesList, steps[3], '-.', label="By")
        plt.plot(anglesList, steps[4], label="ЦДА")
        plt.title("Исследование ступенчатости.\n{0} - длина отрезка".format(r))
        plt.xticks([i for i in range(0, 91, 5)])
        plt.legend()
        plt.ylabel("Количество ступенек")
        plt.xlabel("Угол в градусах")
        plt.show()

    
    def make_sheaf(self):
        try:
            r = int(self.Rad_in.text())
            angle = int(self.Inter_in.text())
            if angle >= 360 or angle <= 0 or r <= 0:
                raise ArithmeticError
        except ValueError:
            self.message_errors("Неверный формат.\nВведите натуральные числа в поля ввода.")
            return
        except ArithmeticError:
            self.message_errors("Неверный формат.\nВведите корректное значение угла (0 < angle < 360).")
            return
        
        try:
            xb, yb = int(self.X_in.text()), int(self.Y_in.text())
        except:
            self.message_errors("Ошибка ввода\nВведите целые числа в поля ввода")
            return 
        
        colour_index = COLOURS.index(self.Seg_color_in.currentText())
        method_index = METHODS.index(self.Alg_in.currentText())

        global sections
        for t in np.arange(0, 2 * pi, pi * angle / 180):
            xe, ye = int(xb + r * cos(t)), int(yb - r * sin(t))
            if method_index != 5:
                new_sec = list()
                new_sec = self.methods[method_index](COLOURS_CODES[colour_index],
                                                        xb, yb, xe, ye)
                sections[method_index].append(new_sec)
                self.draw_section(sections[method_index][len(sections[method_index]) - 1])
            else:
                self.methods[method_index](COLOURS_CODES[colour_index], xb, yb, xe, ye)
                sections[method_index].append([COLOURS_CODES[colour_index], xb, yb, xe, ye])


    def compare_methods(self):
        RUNS = 100
        xb = 0
        yb = 0
        stepAngle = 10
        r = 100
        colour_index = 0

        times = []
        for i in range(6):
            startTime = 0
            endTime = 0

            for _ in range(RUNS):
                cur_angle = 0

                while (cur_angle < 360):
                    xe, ye = int(xb + r * cos(cur_angle)), int(yb + r * sin(cur_angle))

                    startTime += time.time()
                    self.methods[i](COLOURS_CODES[colour_index],
                                                        xb, yb, xe, ye)
                    endTime += time.time()
    

                    cur_angle += stepAngle

            times.append((endTime - startTime) / RUNS)

        self.clear("white", delete=True)
        plt.figure(figsize = (12, 8))
        plt.rcParams['font.size'] = '15'
        plt.title("Замеры времени для построения спектров различными методами")

        positions = [i for i in range(6)]
        methods = ["Брезенхем\n(int)", "Брезенхем\n(float)",
                "Брезенхем\n(со сглаж)", "Ву", "ЦДА", "Библиотечная\nфункция"]

        plt.xticks(positions, methods)
        plt.ylabel("Время")

        plt.bar(positions, times, align = "center", alpha = 1)
        plt.show()


    def make_seg(self):
        try:
            xb, yb = int(self.X1_in.text()), int(self.Y1_in.text())
            xe, ye = int(self.X2_in.text()), int(self.Y2_in.text())
        except:
            self.message_errors("Ошибка ввода\nВведите целые числа в поля ввода")
            return

        colour_index = COLOURS.index(self.Seg_color_in.currentText())
        method_index = METHODS.index(self.Alg_in.currentText())

        global sections

        if method_index != 5:
            new_sec = list()
            new_sec = self.methods[method_index](COLOURS_CODES[colour_index],
                                                        xb, yb, xe, ye)
            sections[method_index].append(new_sec)
            self.draw_section(sections[method_index][len(sections[method_index]) - 1])
        else:
            self.methods[method_index](COLOURS_CODES[colour_index], xb, yb, xe, ye)
            sections[method_index].append([COLOURS_CODES[colour_index], xb, yb, xe, ye])


    def draw_section(self, section):
        for p in section:
            self.draw_pixel(p)
        

    def draw_pixel(self, p: Point):
        self.draw_line(p.x, p.y, p.x, p.y, str(p.colour))


    def message_autor(self):
        text = "Автор: Лапшин Вячеслав\nГруппа: ИУ7-41Б\nУниверситет: МГТУ им. Баумана."
        QtWidgets.QMessageBox.information(self, "Автор", text,  QtWidgets.QMessageBox.Cancel)


    def message_task(self):
        text = "Реализовать различные алгоритмы построения отрезков, сравнить их."
        QtWidgets.QMessageBox.information(self, "Условие задачи", text,  QtWidgets.QMessageBox.Cancel)


    def message_func_of_prog(self):
        text = "Можно выбирать цвета фона и отрезка или пучка, их координаты. "
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