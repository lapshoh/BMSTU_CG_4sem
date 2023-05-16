"""
Лабораторная работа 2
Лапшин В.  ИУ7-41Б
"""
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
import sys
import design
import copy
from math import *

data = []
start_coord = [550, 350]

start_picture = [[[-120, -150], [120, -150], [120, 60], [-120, 60]], [[-150, 60], [-120, 120], [120, 120], [150, 60]], \
                [[-90, -150], [-30, -150], [-30, 0], [-90, 0]], [[-45, -90], [-39, -90], [-39, -60], [-45, -60]], \
                [[60, -30], 30, 30, [60, 0], [60, -60], [30, -30], [90, -30]], [0, 0]]
current_picture = copy.deepcopy(start_picture)
ell_points = []
current_ell_points = copy.deepcopy(ell_points)
status = 0


def move_point(coord, dx, dy):
    newx = coord[0] + dx
    newy = coord[1] + dy
    return [newx, newy]


def rotate_point(coord, cx, cy, a):
    angle = radians(a)
    newx = cos(angle) * (coord[0] - cx) - sin(angle) * (coord[1] - cy) + cx
    newy = sin(angle) * (coord[0] - cx) + cos(angle) * (coord[1] - cy) + cy
    return [newx, newy]


def scale_point(coord, cx, cy, kx, ky):
    newx = (coord[0] - cx) * kx + cx
    newy = (coord[1] - cy) * ky + cy
    return [newx, newy]


def cathcet_len(hyp, a, ord):
    if ord == 'x':
        return hyp * cos(a * pi / 180.0)
    elif ord == 'y':
        return hyp * sin(a * pi / 180.0)
    else:
        return None


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.author.triggered.connect(self.message_autor)
        self.task.triggered.connect(self.message_task)
        self.func.triggered.connect(self.message_func_of_prog)
        self.make_new_st_coord.clicked.connect(self.make_new_coords)
        self.to_begin.clicked.connect(self.go_to_begin)
        self.pov.clicked.connect(self.make_rotate)
        self.do_per.clicked.connect(self.make_moving)
        self.do_mash.clicked.connect(self.make_scale)
        self.back.clicked.connect(self.go_back)
        self.clear()
        self.draw_picture(start_picture)

    
    def clear(self):
        canvas = QtGui.QPixmap(1500, 700)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)


    def draw_point(self, x, y):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(4)
        painter.setPen(pen)
        painter.drawPoint(start_coord[0] + round(x), 700 - (start_coord[1] + round(y)))
        self.update()
        painter.end()


    def draw_text(self, x, y):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        painter.setPen(pen)
        painter.setFont(QtGui.QFont("Times New Roman", 10, 1, 1))
        text =  "(" + str(x) + "," + str(y) + ")"
        painter.drawText(QtCore.QPoint(start_coord[0] + round(x) + 5, 700 - (start_coord[1] + round(y)) + 5), text)
        self.update()
        painter.end()


    def draw_line(self, x1, y1, x2, y2):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(start_coord[0] + round(x1), 700 - (start_coord[1] + round(y1)), start_coord[0] + round(x2), 700 - (start_coord[1] + round(y2)))
        self.update()
        painter.end()

    
    def draw_round(self, x1, y1, x2, y2):
        global ell_points, current_ell_points
        angle = 0
        point1 = [x1 + cathcet_len(x2, angle, 'x'), y1 + cathcet_len(y2, angle, 'y')]
        ell_points.append(point1)

        for i in range(1, 65):
            angle = i / 64 * 360
            point2 = [x1 + cathcet_len(x2, angle, 'x'), y1 + cathcet_len(y2, angle, 'y')]

            self.draw_line(point1[0], point1[1], point2[0], point2[1])
            point1 = point2.copy()
            ell_points.append(point1)

        current_ell_points = copy.deepcopy(ell_points)


    def draw_round_by_points(self, arr):
        n = len(arr)
        for i in range(n):
            self.draw_line(arr[i][0], arr[i][1], arr[(i + 1) % n][0], arr[(i + 1) % n][1])


    def make_new_coords(self):
        x = self.x_in_st_coord.text()
        y = self.y_in_st_coord.text()

        text = "Пустое поле "

        if len(x) == 0:
            text += "\"X\"!"
        elif len(y) == 0:
            text += "\"Y\"!"

        if text != "Пустое поле ":
            QtWidgets.QMessageBox.warning(self, "Ошибка!", text,  QtWidgets.QMessageBox.Cancel)
            return
    
        try:
            x = float(x)
            y = float(y)
        except:
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Введены некорректные данные! (x, y)",  QtWidgets.QMessageBox.Cancel)
            self.x_in_st_coord.setText("")
            self.y_in_st_coord.setText("")
            return
        
        global current_picture
        current_picture[5] = [x, y]
        self.clear()
        self.draw_picture(current_picture)
        self.x_in_st_coord.setText("")
        self.y_in_st_coord.setText("")
        text = "Текущие начальные координаты: (" + str(x) + ", " + str(y) + ")"
        self.st_coord.setText(text)

    
    def go_back(self):
        global current_picture, current_ell_points, data, status
        n = len(data)
        if n < 2:
            return
        if n == 2:
            status = 0
        back_picture = copy.deepcopy(data[n - 2][0])
        current_ell_points = copy.deepcopy(data[n - 2][1])
        text = "Текущие начальные координаты: (" + str(back_picture[5][0]) + ", " + str(back_picture[5][1]) + ")"
        self.st_coord.setText(text)
        data.pop(n - 1)
        data.pop(n - 2)
        self.clear()
        self.draw_picture(back_picture)
        current_picture = copy.deepcopy(back_picture)

    
    def go_to_begin(self):
        global current_picture, start_picture, current_ell_points, ell_points, data
        self.clear()
        data.clear()
        current_ell_points = copy.deepcopy(ell_points)
        self.draw_picture(start_picture)
        current_picture = copy.deepcopy(start_picture)


    def make_rotate(self):
        global current_picture, current_ell_points
        x = self.in_degr.text()

        text = "Пустое поле "

        if len(x) == 0:
            text += "\"Градусы\"!"

        if text != "Пустое поле ":
            QtWidgets.QMessageBox.warning(self, "Ошибка!", text,  QtWidgets.QMessageBox.Cancel)
            return
    
        try:
            x = float(x)
        except:
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Введены некорректные данные! (градусы)",  QtWidgets.QMessageBox.Cancel)
            self.x_in_st_coord.setText("")
            return

        for i in range(4):
            n = len(current_picture[i])
            for j in range(n):
                current_picture[i][j] = rotate_point(current_picture[i][j], current_picture[5][0], current_picture[5][1], x)

        current_picture[4][0] = rotate_point(current_picture[4][0], current_picture[5][0], current_picture[5][1], x)

        for i in range(3, 7):
            current_picture[4][i] = rotate_point(current_picture[4][i], current_picture[5][0], current_picture[5][1], x)

        for i in range(len(current_ell_points)):
            current_ell_points[i] = rotate_point(current_ell_points[i], current_picture[5][0], current_picture[5][1], x)

        self.clear()  
        self.draw_picture(current_picture)


    def make_moving(self):
        x = self.x_in_per.text()
        y = self.y_in_per.text()

        text = "Пустое поле "

        if len(x) == 0:
            text += "\"X\"!"
        elif len(y) == 0:
            text += "\"Y\"!"

        if text != "Пустое поле ":
            QtWidgets.QMessageBox.warning(self, "Ошибка!", text,  QtWidgets.QMessageBox.Cancel)
            return
    
        try:
            x = float(x)
            y = float(y)
        except:
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Введены некорректные данные! (x, y)",  QtWidgets.QMessageBox.Cancel)
            self.x_in_st_coord.setText("")
            self.y_in_st_coord.setText("")
            return
        
        for i in range(4):
            n = len(current_picture[i])
            for j in range(n):
                current_picture[i][j] = move_point(current_picture[i][j], x, y)

        current_picture[4][0] = move_point(current_picture[4][0], x, y)
        for i in range(3, 7):
            current_picture[4][i] = move_point(current_picture[4][i], x, y)

        for i in range(len(current_ell_points)):
            current_ell_points[i] = move_point(current_ell_points[i], x, y)

        self.clear()  
        self.draw_picture(current_picture)


    def make_scale(self):
        x = self.x_in_mash.text()
        y = self.y_in_mash.text()

        text = "Пустое поле "

        if len(x) == 0:
            text += "\"X\"!"
        elif len(y) == 0:
            text += "\"Y\"!"

        if text != "Пустое поле ":
            QtWidgets.QMessageBox.warning(self, "Ошибка!", text,  QtWidgets.QMessageBox.Cancel)
            return
    
        try:
            x = float(x)
            y = float(y)
        except:
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Введены некорректные данные! (x, y)",  QtWidgets.QMessageBox.Cancel)
            self.x_in_st_coord.setText("")
            self.y_in_st_coord.setText("")
            return
        
        for i in range(4):
            n = len(current_picture[i])
            for j in range(n):
                current_picture[i][j] = scale_point(current_picture[i][j], current_picture[5][0], current_picture[5][1], x, y)

        current_picture[4][0] = scale_point(current_picture[4][0], current_picture[5][0], current_picture[5][1], x, y)
        current_picture[4][1] *= x
        current_picture[4][2] *= y

        for i in range(3, 7):
            current_picture[4][i] = scale_point(current_picture[4][i], current_picture[5][0], current_picture[5][1], x, y)

        for i in range(len(current_ell_points)):
            current_ell_points[i] = scale_point(current_ell_points[i], current_picture[5][0], current_picture[5][1], x, y)

        self.clear()  
        self.draw_picture(current_picture)


    def draw_picture(self, picture_points):
        global status, data
        data.append([copy.deepcopy(picture_points), copy.deepcopy(current_ell_points)])
        for i in range(4):
            n = len(picture_points[i])
            for j in range(n):
                self.draw_line(picture_points[i][j][0], picture_points[i][j][1], picture_points[i][(j + 1) % n][0], picture_points[i][(j + 1) % n][1])
        
        self.draw_line(picture_points[2][0][0], picture_points[2][0][1], picture_points[2][2][0], picture_points[2][2][1])
        self.draw_line(picture_points[2][1][0], picture_points[2][1][1], picture_points[2][3][0], picture_points[2][3][1])
        if status == 0:
            self.draw_round(picture_points[4][0][0], picture_points[4][0][1], picture_points[4][1], picture_points[4][1])
        else:
            self.draw_round_by_points(current_ell_points)
        self.draw_line(picture_points[4][3][0], picture_points[4][3][1], picture_points[4][4][0], picture_points[4][4][1])
        self.draw_line(picture_points[4][5][0], picture_points[4][5][1], picture_points[4][6][0], picture_points[4][6][1])
        self.draw_point(picture_points[5][0], picture_points[5][1])
        self.draw_text(picture_points[5][0], picture_points[5][1])
        status = 1
        

    def message_autor(self):
        text = "Автор: Лапшин Вячеслав\nГруппа: ИУ7-41Б\nУниверситет: МГТУ им. Баумана."
        QtWidgets.QMessageBox.information(self, "Автор", text,  QtWidgets.QMessageBox.Cancel)


    def message_task(self):
        text = "Задан рисунок, релизовать масштабирование, перенос и поворот данного рисунка."
        QtWidgets.QMessageBox.information(self, "Условие задачи", text,  QtWidgets.QMessageBox.Cancel)


    def message_func_of_prog(self):
        text = "Можно задать любую изначальную точку, сделать масштабирование, перенос и поворот по заданным пользователем характеристикам. "
        text += "Можно вернуться к изначальной картинкой (кнопка \"В начало\")."
        QtWidgets.QMessageBox.information(self, "Функционал программы", text,  QtWidgets.QMessageBox.Cancel)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()