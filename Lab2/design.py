# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1396, 848)
        MainWindow.setStyleSheet("background-color: rgb(201, 246, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 1100, 700))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1160, 50, 211, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.x_mash = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.x_mash.setMaximumSize(QtCore.QSize(100, 30))
        self.x_mash.setStyleSheet("background-color: rgb(201, 246, 255);\n"
"font: 75 italic 12pt \"Times New Roman\";")
        self.x_mash.setAlignment(QtCore.Qt.AlignCenter)
        self.x_mash.setObjectName("x_mash")
        self.horizontalLayout_4.addWidget(self.x_mash)
        self.y_mash = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.y_mash.setMaximumSize(QtCore.QSize(100, 30))
        self.y_mash.setStyleSheet("background-color: rgb(201, 246, 255);\n"
"font: 75 italic 12pt \"Times New Roman\";\n"
"")
        self.y_mash.setAlignment(QtCore.Qt.AlignCenter)
        self.y_mash.setObjectName("y_mash")
        self.horizontalLayout_4.addWidget(self.y_mash)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.x_in_mash = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_in_mash.sizePolicy().hasHeightForWidth())
        self.x_in_mash.setSizePolicy(sizePolicy)
        self.x_in_mash.setMinimumSize(QtCore.QSize(0, 35))
        self.x_in_mash.setMaximumSize(QtCore.QSize(100, 35))
        self.x_in_mash.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Times New Roman\";")
        self.x_in_mash.setObjectName("x_in_mash")
        self.horizontalLayout.addWidget(self.x_in_mash)
        self.y_in_mash = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_in_mash.sizePolicy().hasHeightForWidth())
        self.y_in_mash.setSizePolicy(sizePolicy)
        self.y_in_mash.setMinimumSize(QtCore.QSize(0, 35))
        self.y_in_mash.setMaximumSize(QtCore.QSize(100, 35))
        self.y_in_mash.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Times New Roman\";")
        self.y_in_mash.setObjectName("y_in_mash")
        self.horizontalLayout.addWidget(self.y_in_mash)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self._23 = QtWidgets.QHBoxLayout()
        self._23.setSpacing(0)
        self._23.setObjectName("_23")
        self.emp_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emp_label.sizePolicy().hasHeightForWidth())
        self.emp_label.setSizePolicy(sizePolicy)
        self.emp_label.setMinimumSize(QtCore.QSize(0, 30))
        self.emp_label.setMaximumSize(QtCore.QSize(1, 30))
        self.emp_label.setStyleSheet("")
        self.emp_label.setText("")
        self.emp_label.setObjectName("emp_label")
        self._23.addWidget(self.emp_label)
        self.do_mash = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.do_mash.sizePolicy().hasHeightForWidth())
        self.do_mash.setSizePolicy(sizePolicy)
        self.do_mash.setMinimumSize(QtCore.QSize(0, 40))
        self.do_mash.setMaximumSize(QtCore.QSize(160, 40))
        self.do_mash.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.do_mash.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.do_mash.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 12pt \"Times New Roman\";")
        self.do_mash.setObjectName("do_mash")
        self._23.addWidget(self.do_mash)
        self.verticalLayout.addLayout(self._23)
        self.emp_label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.emp_label_5.setMinimumSize(QtCore.QSize(0, 100))
        self.emp_label_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.emp_label_5.setStyleSheet("background-color: rgb(201, 246, 255);")
        self.emp_label_5.setText("")
        self.emp_label_5.setObjectName("emp_label_5")
        self.verticalLayout.addWidget(self.emp_label_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.x_per = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.x_per.setMaximumSize(QtCore.QSize(100, 30))
        self.x_per.setStyleSheet("background-color: rgb(201, 246, 255);\n"
"font: 75 italic 12pt \"Times New Roman\";")
        self.x_per.setAlignment(QtCore.Qt.AlignCenter)
        self.x_per.setObjectName("x_per")
        self.horizontalLayout_5.addWidget(self.x_per)
        self.y_per = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.y_per.setMinimumSize(QtCore.QSize(100, 0))
        self.y_per.setMaximumSize(QtCore.QSize(100, 30))
        self.y_per.setStyleSheet("background-color: rgb(201, 246, 255);\n"
"font: 75 italic 12pt \"Times New Roman\";")
        self.y_per.setAlignment(QtCore.Qt.AlignCenter)
        self.y_per.setObjectName("y_per")
        self.horizontalLayout_5.addWidget(self.y_per)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.x_in_per = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_in_per.sizePolicy().hasHeightForWidth())
        self.x_in_per.setSizePolicy(sizePolicy)
        self.x_in_per.setMinimumSize(QtCore.QSize(0, 35))
        self.x_in_per.setMaximumSize(QtCore.QSize(100, 35))
        self.x_in_per.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Times New Roman\";")
        self.x_in_per.setObjectName("x_in_per")
        self.horizontalLayout_2.addWidget(self.x_in_per)
        self.y_in_per = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_in_per.sizePolicy().hasHeightForWidth())
        self.y_in_per.setSizePolicy(sizePolicy)
        self.y_in_per.setMinimumSize(QtCore.QSize(0, 35))
        self.y_in_per.setMaximumSize(QtCore.QSize(100, 35))
        self.y_in_per.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Times New Roman\";")
        self.y_in_per.setObjectName("y_in_per")
        self.horizontalLayout_2.addWidget(self.y_in_per)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self._24 = QtWidgets.QHBoxLayout()
        self._24.setSpacing(0)
        self._24.setObjectName("_24")
        self.emp_label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emp_label_2.sizePolicy().hasHeightForWidth())
        self.emp_label_2.setSizePolicy(sizePolicy)
        self.emp_label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.emp_label_2.setMaximumSize(QtCore.QSize(1, 30))
        self.emp_label_2.setStyleSheet("")
        self.emp_label_2.setText("")
        self.emp_label_2.setObjectName("emp_label_2")
        self._24.addWidget(self.emp_label_2)
        self.do_per = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.do_per.sizePolicy().hasHeightForWidth())
        self.do_per.setSizePolicy(sizePolicy)
        self.do_per.setMinimumSize(QtCore.QSize(0, 40))
        self.do_per.setMaximumSize(QtCore.QSize(160, 40))
        self.do_per.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.do_per.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.do_per.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 12pt \"Times New Roman\";")
        self.do_per.setObjectName("do_per")
        self._24.addWidget(self.do_per)
        self.verticalLayout.addLayout(self._24)
        self.emp_label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.emp_label_4.setMinimumSize(QtCore.QSize(0, 100))
        self.emp_label_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.emp_label_4.setStyleSheet("background-color: rgb(201, 246, 255);")
        self.emp_label_4.setText("")
        self.emp_label_4.setObjectName("emp_label_4")
        self.verticalLayout.addWidget(self.emp_label_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.degr = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.degr.setMaximumSize(QtCore.QSize(200, 30))
        self.degr.setStyleSheet("background-color: rgb(201, 246, 255);\n"
"font: 75 italic 12pt \"Times New Roman\";")
        self.degr.setAlignment(QtCore.Qt.AlignCenter)
        self.degr.setObjectName("degr")
        self.horizontalLayout_6.addWidget(self.degr)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.in_degr = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_degr.sizePolicy().hasHeightForWidth())
        self.in_degr.setSizePolicy(sizePolicy)
        self.in_degr.setMinimumSize(QtCore.QSize(0, 35))
        self.in_degr.setMaximumSize(QtCore.QSize(100, 35))
        self.in_degr.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Times New Roman\";")
        self.in_degr.setObjectName("in_degr")
        self.horizontalLayout_3.addWidget(self.in_degr)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self._25 = QtWidgets.QHBoxLayout()
        self._25.setSpacing(0)
        self._25.setObjectName("_25")
        self.emp_label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emp_label_3.sizePolicy().hasHeightForWidth())
        self.emp_label_3.setSizePolicy(sizePolicy)
        self.emp_label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.emp_label_3.setMaximumSize(QtCore.QSize(1, 30))
        self.emp_label_3.setStyleSheet("")
        self.emp_label_3.setText("")
        self.emp_label_3.setObjectName("emp_label_3")
        self._25.addWidget(self.emp_label_3)
        self.pov = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pov.sizePolicy().hasHeightForWidth())
        self.pov.setSizePolicy(sizePolicy)
        self.pov.setMinimumSize(QtCore.QSize(0, 40))
        self.pov.setMaximumSize(QtCore.QSize(160, 40))
        self.pov.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pov.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pov.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 12pt \"Times New Roman\";")
        self.pov.setObjectName("pov")
        self._25.addWidget(self.pov)
        self.verticalLayout.addLayout(self._25)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(30, 740, 1315, 62))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.make_new_st_coord = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.make_new_st_coord.setMinimumSize(QtCore.QSize(160, 40))
        self.make_new_st_coord.setMaximumSize(QtCore.QSize(160, 40))
        self.make_new_st_coord.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 11pt \"Times New Roman\";")
        self.make_new_st_coord.setObjectName("make_new_st_coord")
        self.horizontalLayout_7.addWidget(self.make_new_st_coord)
        self.x_st_coord = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.x_st_coord.setMinimumSize(QtCore.QSize(40, 0))
        self.x_st_coord.setMaximumSize(QtCore.QSize(40, 30))
        self.x_st_coord.setStyleSheet("background-color: rgb(201, 246, 255);\n"
"font: 75 italic 12pt \"Times New Roman\";")
        self.x_st_coord.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x_st_coord.setObjectName("x_st_coord")
        self.horizontalLayout_7.addWidget(self.x_st_coord)
        self.x_in_st_coord = QtWidgets.QLineEdit(self.horizontalLayoutWidget_10)
        self.x_in_st_coord.setMinimumSize(QtCore.QSize(0, 35))
        self.x_in_st_coord.setMaximumSize(QtCore.QSize(100, 16777215))
        self.x_in_st_coord.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Times New Roman\";")
        self.x_in_st_coord.setObjectName("x_in_st_coord")
        self.horizontalLayout_7.addWidget(self.x_in_st_coord)
        self.y_st_coord = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.y_st_coord.setMinimumSize(QtCore.QSize(40, 0))
        self.y_st_coord.setMaximumSize(QtCore.QSize(60, 30))
        self.y_st_coord.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.y_st_coord.setStyleSheet("background-color: rgb(201, 246, 255);\n"
"font: 75 italic 12pt \"Times New Roman\";")
        self.y_st_coord.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y_st_coord.setObjectName("y_st_coord")
        self.horizontalLayout_7.addWidget(self.y_st_coord)
        self.y_in_st_coord = QtWidgets.QLineEdit(self.horizontalLayoutWidget_10)
        self.y_in_st_coord.setMinimumSize(QtCore.QSize(0, 35))
        self.y_in_st_coord.setMaximumSize(QtCore.QSize(100, 16777215))
        self.y_in_st_coord.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Times New Roman\";")
        self.y_in_st_coord.setObjectName("y_in_st_coord")
        self.horizontalLayout_7.addWidget(self.y_in_st_coord)
        self.st_coord = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.st_coord.setMinimumSize(QtCore.QSize(500, 0))
        self.st_coord.setStyleSheet("background-color: rgb(201, 246, 255);\n"
"font: 75 italic 12pt \"Times New Roman\";")
        self.st_coord.setAlignment(QtCore.Qt.AlignCenter)
        self.st_coord.setObjectName("st_coord")
        self.horizontalLayout_7.addWidget(self.st_coord)
        self.to_begin = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.to_begin.setMinimumSize(QtCore.QSize(160, 40))
        self.to_begin.setMaximumSize(QtCore.QSize(160, 16777215))
        self.to_begin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 12pt \"Times New Roman\";")
        self.to_begin.setObjectName("to_begin")
        self.horizontalLayout_7.addWidget(self.to_begin)
        self.back = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.back.setMinimumSize(QtCore.QSize(160, 40))
        self.back.setMaximumSize(QtCore.QSize(160, 16777215))
        self.back.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 italic 12pt \"Times New Roman\";")
        self.back.setObjectName("back")
        self.horizontalLayout_7.addWidget(self.back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1396, 26))
        self.menubar.setStyleSheet("background-color: rgb(169, 255, 224);")
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.author = QtWidgets.QAction(MainWindow)
        self.author.setObjectName("author")
        self.task = QtWidgets.QAction(MainWindow)
        self.task.setObjectName("task")
        self.func = QtWidgets.QAction(MainWindow)
        self.func.setObjectName("func")
        self.menu.addAction(self.author)
        self.menu.addAction(self.task)
        self.menu.addAction(self.func)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лабораторная работа 2"))
        self.x_mash.setText(_translate("MainWindow", "X"))
        self.y_mash.setText(_translate("MainWindow", "Y"))
        self.do_mash.setText(_translate("MainWindow", "Масштабировать"))
        self.x_per.setText(_translate("MainWindow", "X"))
        self.y_per.setText(_translate("MainWindow", "Y"))
        self.do_per.setText(_translate("MainWindow", "Перенести"))
        self.degr.setText(_translate("MainWindow", "Градусы "))
        self.pov.setText(_translate("MainWindow", "Повернуть"))
        self.make_new_st_coord.setText(_translate("MainWindow", "Задать начальные \n"
"координаты"))
        self.x_st_coord.setText(_translate("MainWindow", "X:"))
        self.y_st_coord.setText(_translate("MainWindow", "Y:"))
        self.st_coord.setText(_translate("MainWindow", "Текущие начальные координаты: (0, 0)"))
        self.to_begin.setText(_translate("MainWindow", "В начало"))
        self.back.setText(_translate("MainWindow", "Назад"))
        self.menu.setTitle(_translate("MainWindow", "Справка"))
        self.author.setText(_translate("MainWindow", "Автор"))
        self.task.setText(_translate("MainWindow", "Условие"))
        self.func.setText(_translate("MainWindow", "Функционал"))