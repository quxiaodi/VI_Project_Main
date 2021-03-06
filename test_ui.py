# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 529)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DatatableView = QtWidgets.QTableView(self.centralwidget)
        self.DatatableView.setGeometry(QtCore.QRect(0, 190, 351, 271))
        self.DatatableView.setObjectName("DatatableView")
        self.MessagelistView = QtWidgets.QListView(self.centralwidget)
        self.MessagelistView.setGeometry(QtCore.QRect(0, 0, 351, 191))
        self.MessagelistView.setObjectName("MessagelistView")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 460, 911, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(350, 0, 561, 461))
        self.graphicsView.setObjectName("graphicsView")
        self.open_DBC = QtWidgets.QPushButton(self.centralwidget)
        self.open_DBC.setGeometry(QtCore.QRect(310, 20, 31, 21))
        self.open_DBC.setStyleSheet("QPushButton{border-image: url(./Image/file.png);}\n"
"")
        self.open_DBC.setText("")
        self.open_DBC.setObjectName("open_DBC")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(7, 20, 81, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 20, 211, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget1)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.layoutWidget1)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_2.addWidget(self.plainTextEdit_2)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.layoutWidget1)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.verticalLayout_2.addWidget(self.plainTextEdit_3)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.layoutWidget1)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.verticalLayout_2.addWidget(self.plainTextEdit_4)
        self.open_CAR = QtWidgets.QPushButton(self.centralwidget)
        self.open_CAR.setGeometry(QtCore.QRect(310, 50, 31, 21))
        self.open_CAR.setStyleSheet("QPushButton{border-image: url(./Image/file.png);}\n"
"\n"
"")
        self.open_CAR.setText("")
        self.open_CAR.setObjectName("open_CAR")
        self.open_DRIVER = QtWidgets.QPushButton(self.centralwidget)
        self.open_DRIVER.setGeometry(QtCore.QRect(310, 80, 31, 21))
        self.open_DRIVER.setStyleSheet("QPushButton{border-image: url(./Image/file.png);}\n"
"")
        self.open_DRIVER.setText("")
        self.open_DRIVER.setObjectName("open_DRIVER")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 110, 31, 21))
        self.pushButton.setStyleSheet("QPushButton{border-image: url(./Image/Set_name.png);}\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 160, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 913, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiontest = QtWidgets.QAction(MainWindow)
        self.actiontest.setObjectName("actiontest")
        self.actiontest2 = QtWidgets.QAction(MainWindow)
        self.actiontest2.setObjectName("actiontest2")
        self.menu_PlotData = QtWidgets.QAction(MainWindow)
        self.menu_PlotData.setObjectName("menu_PlotData")
        self.menu_InputData = QtWidgets.QAction(MainWindow)
        self.menu_InputData.setObjectName("menu_InputData")
        self.menu_CalData = QtWidgets.QAction(MainWindow)
        self.menu_CalData.setObjectName("menu_CalData")
        self.menu_Exit = QtWidgets.QAction(MainWindow)
        self.menu_Exit.setObjectName("menu_Exit")
        self.menu_Guildlines = QtWidgets.QAction(MainWindow)
        self.menu_Guildlines.setObjectName("menu_Guildlines")
        self.menu_ContactUs = QtWidgets.QAction(MainWindow)
        self.menu_ContactUs.setObjectName("menu_ContactUs")
        self.menu.addAction(self.menu_InputData)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_Exit)
        self.menu_3.addAction(self.menu_PlotData)
        self.menu_2.addAction(self.menu_CalData)
        self.menu_4.addAction(self.menu_Guildlines)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.menu_ContactUs)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DBC Index"))
        self.label_2.setText(_translate("MainWindow", "CAR Index"))
        self.label_3.setText(_translate("MainWindow", "DRIVER Index"))
        self.label_4.setText(_translate("MainWindow", "Save Name"))
        self.plainTextEdit_4.setPlainText(_translate("MainWindow", "AS24_test_Result"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.menu.setTitle(_translate("MainWindow", "文件 (File)"))
        self.menu_3.setTitle(_translate("MainWindow", "绘图 (Ploting)"))
        self.menu_2.setTitle(_translate("MainWindow", "计算 (Calculation)"))
        self.menu_4.setTitle(_translate("MainWindow", "帮助 (Help)"))
        self.actiontest.setText(_translate("MainWindow", "test"))
        self.actiontest2.setText(_translate("MainWindow", "test2"))
        self.menu_PlotData.setText(_translate("MainWindow", "绘制轨迹曲线 Ploting Data"))
        self.menu_InputData.setText(_translate("MainWindow", "导入测试数据 Input Test Data"))
        self.menu_CalData.setText(_translate("MainWindow", "求解 Solution"))
        self.menu_Exit.setText(_translate("MainWindow", "退出"))
        self.menu_Guildlines.setText(_translate("MainWindow", "操作指南 Guildlines"))
        self.menu_ContactUs.setText(_translate("MainWindow", "联系作者 Contact Us!"))


