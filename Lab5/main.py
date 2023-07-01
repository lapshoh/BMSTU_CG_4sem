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

width = 1500
height = 850
start_coord = [750, 425]
points = [[]]
tempPoints = [[]]
brezPoints = []


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setMouseTracking(True)
        self.contour_colour = QtGui.QColor(0, 0, 0, 255)
        self.fill_colour = QtGui.QColor(0, 0, 0, 255)
        self.canvas_colour = QtGui.QColor(255, 255, 255, 255)
        self.author.triggered.connect(self.message_autor)
        self.task.triggered.connect(self.message_task)
        self.func.triggered.connect(self.message_func_of_prog)
        self.Clear.clicked.connect(self.clear)
        self.Add_point.clicked.connect(self.add_point)
        self.Close_figure.clicked.connect(self.close_figure)
        self.Fill.clicked.connect(self.fillFigure)
        self.Cur_colour.clicked.connect(self.curr_colour)
        self.Change_colour.clicked.connect(self.change_colours)
        self.clear()


    def find_intersections(self, startPoint, endPoint):
        if startPoint[1] == endPoint[1]:
            return []

        if startPoint[1] > endPoint[1]:
            startPoint, endPoint = endPoint, startPoint

        dy = 1
        dx = (endPoint[0] - startPoint[0]) / (endPoint[1] - startPoint[1])

        x, y = startPoint
        allPoints = []

        while y < endPoint[1]:
            allPoints.append([round(x), round(y)])

            y += dy
            x += dx

        return allPoints


    def sign(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0


    def bresenham(self, begPoint, endPoint):
        x1, y1 = begPoint
        x2, y2 = endPoint

        dx = x2 - x1
        dy = y2 - y1

        if (dx == 0) and (dy == 0):
            return [begPoint[0], begPoint[1]]

        x = x1
        y = y1

        signX = self.sign(dx)
        signY = self.sign(dy)
        dx = abs(dx)
        dy = abs(dy)

        swaped = False
        if dy > dx:
            swaped = True
            dx, dy = dy, dx

        e = 2 * dy - dx

        new_points = []

        i = 0
        while i <= dx:
            new_points.append([x, y])

            if e >= 0:
                if swaped:
                    x += signX
                else:
                    y += signY

                e -= 2 * dx

            if swaped:
                y += signY
            else:
                x += signX

            e += 2 * dy
            i += 1

        return new_points
    

    def add_point(self):
        x = self.X_in.text()
        y = self.Y_in.text()

        text = "Пустое поле "

        if len(x) == 0:
            text += "\"X\"!"
        elif len(y) == 0:
            text += "\"Y\"!"

        if text != "Пустое поле ":
            self.message_errors("Ошибка!" + text)
            return
    
        try:
            x = float(x)
            y = float(y)
        except:
            self.message_errors("Ошибка!\nВведены некорректные данные! (x, y)")
            self.X_in.setText("")
            self.Y_in.setText("")
            return
            
        points[-1].append([x, y])
        if (len(points[-1]) != 1):
            if len(points[-1]) == 1:
                self.drawPoint(points[-1][-1])
            else:
                if points[-1][-2] == points[-1][-1]:
                    points[-1].pop()
                    return
                self.drawLine(points[-1][-2], points[-1][-1])
                tempPoints[-1].extend(self.find_intersections(points[-1][-2], points[-1][-1]))

        self.rewrite_table()

        self.X_in.setText("")
        self.Y_in.setText("")


    def add_mouse_point(self, x, y):
        points[-1].append([x, y])
        if (len(points[-1]) != 1):
            if len(points[-1]) == 1:
                self.drawPoint(points[-1][-1])
            else:
                if points[-1][-2] == points[-1][-1]:
                    points[-1].pop()
                    return
                self.drawLine(points[-1][-2], points[-1][-1])
                tempPoints[-1].extend(self.find_intersections(points[-1][-2], points[-1][-1]))

        self.rewrite_table()


    def close_figure(self):
        if len(points[-1]) >= 3:
            points[-1].append(points[-1][0])
            tempPoints[-1].extend(self.find_intersections(points[-1][-2], points[-1][-1]))
            self.drawLine(points[-1][-2], points[-1][-1])

            points.append([])
            tempPoints.append([])
            self.rewrite_table()
        else:
            self.message_errors("Ошибка!\nНевозможно замкнуть фигуру!")


    def drawPoint(self, point: list):      
        painter = QtGui.QPainter(self.label.pixmap())

        painter.setPen(QtGui.QPen(self.contour_colour, 1))
        x = start_coord[0] + int(point[0])
        y = height - (start_coord[1] + int(point[1]))
        painter.drawPoint(x, y)

        painter.end() 
        self.update()   


    def drawLine(self, startPoint, endPoint):
        painter = QtGui.QPainter(self.label.pixmap())

        painter.setPen(QtGui.QPen(self.contour_colour, 1))

        points = self.bresenham(startPoint, endPoint)
        brezPoints.extend(points)

        for i in range(len(points)):
            x = start_coord[0] + int(points[i][0])
            y = height - (start_coord[1] + int(points[i][1]))
            painter.drawPoint(x, y)

        painter.end() 
        self.update() 


    def drawContours(self):
        if self.Ground.isChecked():
            self.change_colour(0)
        for i in range(len(points) - 1):
            for j in range(len(points[i]) - 1):
                br_points = self.bresenham(points[i][j], points[i][j + 1])
                brezPoints.extend(br_points)

                for point in br_points:
                    x = start_coord[0] + int(point[0])
                    y = height - (start_coord[1] + int(point[1]))
                    self.pixels.setPixelColor(x, y, self.contour_colour)
                    

    def drawWithoutDelay(self):
        for i in range(len(tempPoints) - 1):

            sum = 0
            for j in range(len(points[i]) - 1):
                sum += points[i][j][0]

            sum /= (len(points[i]) - 1)
            partion = round(sum)

            for point in tempPoints[i]:
                step = 1
                delta = 0

                if point[0] >= partion:
                    step = -1
                    delta = -1

                for x in range(point[0], partion + delta, step):
                    if [x, point[1]] not in brezPoints:
                        self.convertPixel(x, point[1]) 

        self.update()


    def drawWithDelay(self):
        curDelay = 500 - self.Delay_in.value()

        for i in range(len(tempPoints) - 1):
            sum = 0
            for j in range(len(points[i]) - 1):
                sum += points[i][j][0]

            sum /= (len(points[i]) - 1)
            partion = round(sum)

            for point in tempPoints[i]:
                step = 1
                delta = 0

                if point[0] >= partion:
                    step = -1
                    delta = -1

                for x in range(point[0], partion + delta, step):
                    if [x, point[1]] not in brezPoints:
                        self.convertPixel(x, point[1]) 

                        if curDelay == 0 and self.Delay_in.value() != 1:       
                            curDelay = 500 - self.Delay_in.value()                               
                            QtWidgets.QApplication.processEvents()
                        curDelay -= 1
                        
        self.update()


    def fillFigure(self):
        self.drawContours() 
        if self.Filling.isChecked():
            self.change_colour(1)

        if self.Delay.isChecked():
            startTime = time.time()
            self.drawWithDelay()
            endTime = time.time()
        else:
            startTime = time.time()
            self.drawWithoutDelay()
            endTime = time.time()

        finalTime = endTime - startTime

        self.Time.setText(f"{finalTime:.3f}")


    def convertPixel(self, x: int, y: int):
        painter = QtGui.QPainter(self.label.pixmap())

        x = start_coord[0] + int(x) 
        y = height - (start_coord[1] + int(y))
        pixelColor = self.pixels.pixelColor(x, y)

        if pixelColor == self.contour_colour and self.contour_colour != self.fill_colour:
            newColor = self.contour_colour
        else:
            if pixelColor == self.canvas_colour:
                newColor = self.fill_colour
            else:
                newColor = self.canvas_colour

        self.pixels.setPixelColor(x, y, newColor)
        painter.setPen(QtGui.QPen(newColor, 1))
        painter.drawPoint(x, y)
        self.update()
        painter.end()


    def clear(self):
        canvas = QtGui.QPixmap(width, height)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.pixels = canvas.toImage()
        points.clear()
        points.append([])
        tempPoints.clear()
        tempPoints.append([])
        brezPoints.clear()
        self.rewrite_table()
        self.Time.setText(f"{0:.3f}")


    def change_colours(self):
        if self.Ground.isChecked():
            self.change_colour(0)
        else:
            self.change_colour(1)


    def change_colour(self, type):
        if type == 0:
            if self.Colour_in.currentText() == "Чёрный":
                self.contour_colour = QtGui.QColor(0, 0, 0, 255)
            elif self.Colour_in.currentText() == "Зелёный":
                self.contour_colour = QtGui.QColor(0, 255, 0, 255)
            elif self.Colour_in.currentText() == "Синий":
                self.contour_colour = QtGui.QColor(0, 0, 255, 255)
            elif self.Colour_in.currentText() == "Красный":
                self.contour_colour = QtGui.QColor(255, 0, 0, 255)
            else:
                self.contour_colour = QtGui.QColor(255, 255, 255, 255)
        else:
            if self.Colour_in.currentText() == "Чёрный":
                self.fill_colour = QtGui.QColor(0, 0, 0, 255)
            elif self.Colour_in.currentText() == "Зелёный":
                self.fill_colour = QtGui.QColor(0, 255, 0, 255)
            elif self.Colour_in.currentText() == "Синий":
                self.fill_colour = QtGui.QColor(0, 0, 255, 255)
            elif self.Colour_in.currentText() == "Красный":
                self.fill_colour = QtGui.QColor(255, 0, 0, 255)
            else:
                self.fill_colour = QtGui.QColor(255, 255, 255, 255)


    def rewrite_table(self):
        n = 0
        for i in range(len(points)):
            if (len(points[i]) != 0):
                n += len(points[i])
            if (i != len(points) - 1):
                n += 1

        self.Points_table.setRowCount(n)
        self.Points_table.setColumnCount(2)
        t = 0
        for i in range(len(points)):
            for j in range(len(points[i])):
                item1 = QtWidgets.QTableWidgetItem(str(points[i][j][0]))
                item1.setFlags(QtCore.Qt.ItemIsEnabled)
                self.Points_table.setItem(t, 0, item1)
                item2 = QtWidgets.QTableWidgetItem(str(points[i][j][1]))
                item2.setFlags(QtCore.Qt.ItemIsEnabled)
                self.Points_table.setItem(t, 1, item2)
                t += 1

            if (i != len(points) - 1):
                item1 = QtWidgets.QTableWidgetItem("-------")
                item1.setFlags(QtCore.Qt.ItemIsEnabled)
                self.Points_table.setItem(t, 0, item1)
                item2 = QtWidgets.QTableWidgetItem("-------")
                item2.setFlags(QtCore.Qt.ItemIsEnabled)
                self.Points_table.setItem(t, 1, item2)
                t += 1

        if n == 0:
            self.Points_table.setRowCount(1)

    
    def curr_colour(self):
        text = ""
        if self.contour_colour == QtGui.QColor(0, 0, 0, 255):
            text += "Цвет границы: Чёрный\n"
        elif self.contour_colour == QtGui.QColor(0, 255, 0, 255):
            text += "Цвет границы: Зелёный\n"
        elif self.contour_colour == QtGui.QColor(0, 0, 255, 255):
            text += "Цвет границы: Синий\n"
        elif self.contour_colour == QtGui.QColor(255, 0, 0, 255):
            text += "Цвет границы: Красный\n"
        else:
            text += "Цвет границы: Белый\n"
            
        if self.fill_colour == QtGui.QColor(0, 0, 0, 255):
            text += "Цвет закраски: Чёрный\n"
        elif self.fill_colour == QtGui.QColor(0, 255, 0, 255):
            text += "Цвет закраски: Зелёный\n"
        elif self.fill_colour == QtGui.QColor(0, 0, 255, 255):
            text += "Цвет закраски: Синий\n"
        elif self.fill_colour == QtGui.QColor(255, 0, 0, 255):
            text += "Цвет закраски: Красный\n"
        else:
            text += "Цвет закраски: Белый\n"

        QtWidgets.QMessageBox.information(self, "Текущие цвета", text,  QtWidgets.QMessageBox.Cancel)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:

            self.add_mouse_point(event.pos().x() - start_coord[0], height - event.pos().y() - start_coord[1])
        else:
            self.close_figure()


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