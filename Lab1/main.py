"""
Лабораторная работа 1
Лапшин В.  ИУ7-41Б
"""
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
import sys
import design
from math import *

points_data = []
points_rect = []
width = 1500
height = 700

def dis(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


def equation(p1, p2):
    k = (p2[1] - p1[1]) / (p2[0] - p1[0])        
    return [k, p2[1] - k * p2[0]]


def do_line(p1, p2):
    if p1[0] == p2[0]:
        return [[p1[1], 0], [p1[1], height]]
    
    if p1[1] == p2[1]:
        return [[0, p1[1]], [width, p1[1]]]
    
    k = equation(p1, p2)
    return [[-k[1] / k[0], 0], [(height - k[1]) / k[0], height]]


def is_rectangle(p1, p2, p3, p4):
    x_c = (p1[0] + p2[0] + p3[0] + p4[0]) / 4
    y_c = (p1[1] + p2[1] + p3[1] + p4[1]) / 4
    d1 = dis(p1, (x_c,  y_c))
    d2 = dis(p2, (x_c,  y_c))
    d3 = dis(p3, (x_c,  y_c))
    d4 = dis(p4, (x_c,  y_c))

    if abs((p2[0] - p1[0]) * (p4[1] - p3[1]) - (p4[0] - p3[0]) * (p2[1] - p1[1])) == 0:
        q = 1
    else:
        q = 0

    if abs((p3[0] - p2[0]) * (p4[1] - p1[1]) - (p4[0] - p1[0]) * (p3[1] - p2[1])) == 0:
        p = 1
    else:
        p = 0

    return d1 == d2 and d1 == d3 and d1 == d4 and q and p


def coord_biss(p1, p2, p3):
    a = dis(p1, p2)
    b = dis(p2, p3)
    c = dis(p3, p1)
    px = (a * p3[0] + b * p1[0] + c * p2[0]) / (a + b + c)
    py = (a * p3[1] + b * p1[1] + c * p2[1]) / (a + b + c)
    return [px, py]


def points_on_line(p1, p2, p3):
    if (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1]) == 0:
        return 1
    
    return 0


def ans_center(p1, p2, p3, p4, p5, p6, p7):
    centr_x = (p1[0] + p2[0] + p3[0] + p4[0] + p5[0] + p6[0] + p7[0]) / 7
    centr_y = (p1[1] + p2[1] + p3[1] + p4[1] + p5[1] + p6[1] + p7[1]) / 7
    return [centr_x, centr_y]


def ans_massh(p1, p2, p3, p4, p5, p6, p7, center):
    min_x = min(p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], 0) - center[0]
    min_y = min(p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], 0) - center[1]
    max_x = max(p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], 0) - center[0]
    max_y = max(p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], 0) - center[1]
    k_x = 0.5 * width / (max(fabs(max_x), fabs(min_x)))
    k_y = 0.5 * height / (max(fabs(max_y), fabs(min_y)))
    return min(k_x, k_y) * 0.9


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.Add_point.clicked.connect(self.add_rect_point)
        self.Add_point_2.clicked.connect(self.add_point)
        self.Del_points.clicked.connect(self.del_rect_point)
        self.Del_points_2.clicked.connect(self.del_point)
        self.Solve.clicked.connect(self.solve)
        self.Author.triggered.connect(self.message_autor)
        self.Task.triggered.connect(self.message_task)
        self.Func.triggered.connect(self.message_func_of_prog)
        self.clear()


    def clear(self):
        canvas = QtGui.QPixmap(width, height)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)


    def draw_point(self, x, y, k):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(4)
        if k == 1:
            pen.setColor(QtGui.QColor('red'))
        elif k == 2:
            pen.setColor(QtGui.QColor('green'))
        else:
            pen.setColor(QtGui.QColor('blue'))
        painter.setPen(pen)
        painter.drawPoint(round(x), height - round(y))
        self.update()
        painter.end()

    def draw_line(self, x1, y1, x2, y2, k):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(2)
        if k == 1:
            pen.setColor(QtGui.QColor('red'))
        elif k == 2:
            pen.setColor(QtGui.QColor('green'))
        elif k == 3:
            pen.setColor(QtGui.QColor('yellow'))
        elif k ==4:
            pen.setColor(QtGui.QColor('blue'))
        else:
            pen.setColor(QtGui.QColor('black'))
        
        painter.setPen(pen)
        painter.drawLine(round(x1), height - round(y1), round(x2), height - round(y2))
        self.update()
        painter.end()

    
    def draw_text(self, x, y):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        painter.setPen(pen)
        painter.setFont(QtGui.QFont("Times New Roman", 10, 1, 1))
        text =  "X"
        painter.drawText(QtCore.QPoint(x, height - y), text)
        self.update()
        painter.end()


    def add_point(self):
        x = self.X_in.text()
        y = self.Y_in.text()
        num = self.Point_num.text()

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
            self.X_in.setText("")
            self.Y_in.setText("")
            return
        
        if len(num) != 0:
            q = 1
            try:
                num = int(num)
            except:
                QtWidgets.QMessageBox.warning(self, "Ошибка!", "Введены некорректные данные! (№ точки)",  QtWidgets.QMessageBox.Cancel)
                self.Point_num.setText("")
                return
        else:
            q = 0

        if q == 1:
            if num < 1 or num > len(points_data):
                QtWidgets.QMessageBox.warning(self, "Ошибка!", "Введен неверный индекс точки!",  QtWidgets.QMessageBox.Cancel)
                self.Point_num.setText("")
                return
            points_data[num - 1] = [x, y]
        else:
            points_data.append([x, y])

        self.rewrite_table()

        self.X_in.setText("")
        self.Y_in.setText("")
        self.Point_num.setText("")


    def add_rect_point(self):
        x = self.X_in.text()
        y = self.Y_in.text()
        num = self.Point_num.text()

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
            self.X_in.setText("")
            self.Y_in.setText("")
            return
        
        if len(num) != 0:
            q = 1
            try:
                num = int(num)
            except:
                QtWidgets.QMessageBox.warning(self, "Ошибка!", "Введены некорректные данные! (№ точки)",  QtWidgets.QMessageBox.Cancel)
                self.Point_num.setText("")
                return
        else:
            q = 0

        if q == 1:
            if num < 1 or num > len(points_rect):
                QtWidgets.QMessageBox.warning(self, "Ошибка!", "Введен неверный индекс точки!",  QtWidgets.QMessageBox.Cancel)
                self.Point_num.setText("")
                return
            else:
                points_rect[num - 1] = [x, y]
        else:
            if len(points_rect) >= 4:
                QtWidgets.QMessageBox.warning(self, "Ошибка!", "Уже добавлены 4 точки прямоугольника",  QtWidgets.QMessageBox.Cancel)
                return
            else:
                points_rect.append([x, y])

        self.rewrite_rect_table()
    
        self.X_in.setText("")
        self.Y_in.setText("")
        self.Point_num.setText("")


    def del_point(self):
        idx = self.Point_num.text()
        if len(idx) != 0:
            try:
                idx = int(idx)
            except:
                QtWidgets.QMessageBox.warning(self, "Ошибка!", "Введены некорректные данные! (№ точки)",  QtWidgets.QMessageBox.Cancel)
                self.Point_num.setText("")
                return
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Не введён номер точки для удаления!",  QtWidgets.QMessageBox.Cancel)
            return
            
        if idx < 1 or idx > len(points_data):
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Введен неверный индекс точки!",  QtWidgets.QMessageBox.Cancel)
            self.Point_num.setText("")
            return
        else: 
            points_data.pop(idx - 1)
        self.rewrite_table()
        if len(points_data) == 0:
            self.Table_2.setRowCount(1)


    def del_rect_point(self):
        idx = self.Point_num.text()
        if len(idx) != 0:
            try:
                idx = int(idx)
            except:
                QtWidgets.QMessageBox.warning(self, "Ошибка!", "Введены некорректные данные! (№ точки)",  QtWidgets.QMessageBox.Cancel)
                self.Point_num.setText("")
                return
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Не введён номер точки для удаления!",  QtWidgets.QMessageBox.Cancel)
            return
            

        if idx < 1 or idx > len(points_rect):
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Введен неверный индекс точки!",  QtWidgets.QMessageBox.Cancel)
            self.Point_num.setText("")
            return
        else: 
            points_rect.pop(idx - 1)
        self.rewrite_rect_table()


    def solve(self):
        self.clear()
        m = len(points_rect)
        n = len(points_data)
        if m < 4:
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Недостаточно точек для прямоугольника!",  QtWidgets.QMessageBox.Cancel)
            return
        
        if n < 3:
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Недостаточно точек множества для постоения треугольника!",  QtWidgets.QMessageBox.Cancel)
            return
        
        if is_rectangle(points_rect[0], points_rect[1], points_rect[2], points_rect[3]) == 0:
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Точки не составляют прямоугольник!",  QtWidgets.QMessageBox.Cancel)
            return
        

        center = [(points_rect[0][0] + points_rect[1][0] + points_rect[2][0] + points_rect[3][0]) / 4,
        (points_rect[0][1] + points_rect[1][1] + points_rect[2][1] + points_rect[3][1]) / 4]

        q = 0
        ans = pi * 1.1
        ans_points = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if points_on_line(points_data[i], points_data[j], points_data[k]) == 0:
                        point = coord_biss(points_data[i], points_data[j], points_data[k])

                        if point == center:
                            continue

                        if point[0] == center[0]:
                            direction = pi / 2
                        else:     
                            direction = atan((point[1] - center[1]) / (point[0] - center[0]))

                        q = 1
                        if direction < 0:
                            direction += pi

                        if direction < ans:
                            ans = direction
                            ans_points = [points_data[i], points_data[j], points_data[k]]

        if q == 0:
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Нельзя построить ни одного подходящего треугольника!",  QtWidgets.QMessageBox.Cancel)
            return
        
        zero_coord = ans_center(ans_points[0], ans_points[1], ans_points[2], points_rect[0], points_rect[1], points_rect[2], points_rect[3])
        real_center = [750, 350]
        k = ans_massh(ans_points[0], ans_points[1], ans_points[2], points_rect[0], points_rect[1], points_rect[2], points_rect[3], zero_coord)
        point = coord_biss([real_center[0] - (zero_coord[0] - ans_points[0][0]) * k, real_center[1] - (zero_coord[1] - ans_points[0][1]) * k], \
                        [real_center[0] - (zero_coord[0] - ans_points[1][0]) * k, real_center[1] - (zero_coord[1] - ans_points[1][1]) * k], \
                        [real_center[0] - (zero_coord[0] - ans_points[2][0]) * k, real_center[1] - (zero_coord[1] - ans_points[2][1]) * k])
        
        self.draw_line(0, real_center[1] - zero_coord[1] * k, width, real_center[1] - zero_coord[1] * k, 5)
        self.draw_line(1490, real_center[1] - zero_coord[1] * k + 5, width, real_center[1] - zero_coord[1] * k, 5)
        self.draw_line(1490, real_center[1] - zero_coord[1] * k - 5, width, real_center[1] - zero_coord[1] * k, 5)
        self.draw_text(1485, real_center[1] - zero_coord[1] * k + 10)

        
        for i in range(4):
            self.draw_line(real_center[0] - (zero_coord[0] - points_rect[i][0]) * k, real_center[1] - (zero_coord[1] - points_rect[i][1]) * k,\
                        real_center[0] - (zero_coord[0] - points_rect[(i + 1) % 4][0]) * k, real_center[1] - (zero_coord[1] - points_rect[(i + 1) % 4][1]) * k, 2)

        for i in range(3):
            self.draw_line(real_center[0] - (zero_coord[0] - ans_points[i][0]) * k, real_center[1] - (zero_coord[1] - ans_points[i][1]) * k,\
                        real_center[0] - (zero_coord[0] - ans_points[(i + 1) % 3][0]) * k, real_center[1] - (zero_coord[1] - ans_points[(i + 1) % 3][1]) * k, 3)

        center_1, point_1 = do_line([real_center[0] - (zero_coord[0] - center[0]) * k, real_center[1] - (zero_coord[1] - center[1]) * k], point)
        self.draw_line(center_1[0], center_1[1], point_1[0], point_1[1], 4)
        
        
        self.draw_point(real_center[0] - (zero_coord[0] - center[0]) * k, real_center[1] - (zero_coord[1] - center[1]) * k, 1)
        self.draw_point(point[0], point[1], 1)

        for i in range(3):
            self.draw_point(real_center[0] - (zero_coord[0] - ans_points[i][0]) * k, real_center[1] - (zero_coord[1] - ans_points[i][1]) * k, 1)

        for i in range(4):
            self.draw_point(real_center[0] - (zero_coord[0] - points_rect[i][0]) * k, real_center[1] - (zero_coord[1] - points_rect[i][1]) * k, 1)
            
        
    def message_autor(self):
        text = "Автор: Лапшин Вячеслав\nГруппа: ИУ7-41Б\nУниверситет: МГТУ им. Баумана."
        QtWidgets.QMessageBox.information(self, "Автор", text,  QtWidgets.QMessageBox.Cancel)


    def message_task(self):
        text = "На плоскости задан прямоугольник координатами (по порядку обхода) вершин и множество точек. Найти такой треугольник "
        text += "с вершинами в точках множества, для которого прямая, соединяющая центр прямоугольника и точку пересечения биссектрис "
        text += "треугольника образует минимальный угол с осью абсцисс."
        QtWidgets.QMessageBox.information(self, "Условие задачи", text,  QtWidgets.QMessageBox.Cancel)


    def message_func_of_prog(self):
        text = "Существует возможность добавить точку в список множества точек или точек прямоугольника в конец или по индексу (через № точек). "
        text += "Можно удалить точку по индексу из любого из списков. Чтобы получить решение задачи нужно нажать на кнопку \"Вычислить результат\"."
        QtWidgets.QMessageBox.information(self, "Функционал программы", text,  QtWidgets.QMessageBox.Cancel)


    def rewrite_table(self):
        n = len(points_data)
        self.Table_2.setRowCount(n)
        self.Table_2.setColumnCount(2)
        for i in range(n):
            item1 = QtWidgets.QTableWidgetItem(str(points_data[i][0]))
            item1.setFlags(QtCore.Qt.ItemIsEnabled)
            self.Table_2.setItem(i, 0, item1)
            item2 = QtWidgets.QTableWidgetItem(str(points_data[i][1]))
            item2.setFlags(QtCore.Qt.ItemIsEnabled)
            self.Table_2.setItem(i, 1, item2)


    def rewrite_rect_table(self):
        self.Table.setRowCount(0)
        n = len(points_rect)
        self.Table.setRowCount(4)
        self.Table.setColumnCount(2)
        for i in range(n):
            item1 = QtWidgets.QTableWidgetItem(str(points_rect[i][0]))
            item1.setFlags(QtCore.Qt.ItemIsEnabled)
            self.Table.setItem(i, 0, item1)
            item2 = QtWidgets.QTableWidgetItem(str(points_rect[i][1]))
            item2.setFlags(QtCore.Qt.ItemIsEnabled)
            self.Table.setItem(i, 1, item2)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
