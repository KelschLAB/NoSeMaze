# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/SchedGenUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QtWidgets.QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1165, 841)
        self.centralwidget: QtWidgets.QWidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout: QtWidgets.QGridLayout = QtWidgets.QGridLayout(
            self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scheduleParamsScrollArea: QtWidgets.QScrollArea = QtWidgets.QScrollArea(
            self.centralwidget)
        sizePolicy: QtWidgets.QSizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scheduleParamsScrollArea.sizePolicy().hasHeightForWidth())
        self.scheduleParamsScrollArea.setSizePolicy(sizePolicy)
        self.scheduleParamsScrollArea.setMinimumSize(QtCore.QSize(598, 300))
        self.scheduleParamsScrollArea.setWidgetResizable(True)
        self.scheduleParamsScrollArea.setObjectName("scheduleParamsScrollArea")
        self.scheduleParamsContents: QtWidgets.QWidget = QtWidgets.QWidget()
        self.scheduleParamsContents.setGeometry(QtCore.QRect(0, 0, 598, 350))
        self.scheduleParamsContents.setObjectName("scheduleParamsContents")
        self.gridLayout_2: QtWidgets.QGridLayout = QtWidgets.QGridLayout(
            self.scheduleParamsContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scheduleParamsScrollArea.setWidget(self.scheduleParamsContents)
        self.gridLayout.addWidget(self.scheduleParamsScrollArea, 2, 0, 3, 1)
        self.valveMapScrollArea: QtWidgets.QScrollArea = QtWidgets.QScrollArea(
            self.centralwidget)
        sizePolicy: QtWidgets.QSizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.valveMapScrollArea.sizePolicy().hasHeightForWidth())
        self.valveMapScrollArea.setSizePolicy(sizePolicy)
        self.valveMapScrollArea.setMinimumSize(QtCore.QSize(400, 200))
        self.valveMapScrollArea.setWidgetResizable(True)
        self.valveMapScrollArea.setObjectName("valveMapScrollArea")
        self.valveMapContents: QtWidgets.QWidget = QtWidgets.QWidget()
        self.valveMapContents.setGeometry(QtCore.QRect(0, 0, 598, 200))
        self.valveMapContents.setObjectName("valveMapContents")
        self.verticalLayout: QtWidgets.QVBoxLayout = QtWidgets.QVBoxLayout(
            self.valveMapContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.valveMapScrollArea.setWidget(self.valveMapContents)
        self.gridLayout.addWidget(self.valveMapScrollArea, 0, 0, 1, 1)
        self.generateScheduleButton: QtWidgets.QPushButton = QtWidgets.QPushButton(
            self.centralwidget)
        self.generateScheduleButton.setObjectName("generateScheduleButton")
        self.gridLayout.addWidget(self.generateScheduleButton, 5, 0, 1, 1)
        self.scheduleTypesCombo: QtWidgets.QComboBox = QtWidgets.QComboBox(
            self.centralwidget)
        self.scheduleTypesCombo.setMinimumSize(QtCore.QSize(150, 0))
        self.scheduleTypesCombo.setObjectName("scheduleTypesCombo")
        self.gridLayout.addWidget(self.scheduleTypesCombo, 1, 0, 1, 1)
        self.scheduleView: QtWidgets.QTableView = QtWidgets.QTableView(
            self.centralwidget)
        self.scheduleView.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scheduleView.setAlternatingRowColors(True)
        self.scheduleView.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.scheduleView.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.scheduleView.setObjectName("scheduleView")
        self.scheduleView.horizontalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.scheduleView, 0, 1, 3, 1)
        self.pulseView: PlotWidget = PlotWidget(self.centralwidget)
        self.pulseView.setObjectName("pulseView")
        self.gridLayout.addWidget(self.pulseView, 3, 1, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar: QtWidgets.QMenuBar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1165, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile: QtWidgets.QMenu = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp: QtWidgets.QMenu = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar: QtWidgets.QStatusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave: QtWidgets.QAction = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.actionOpenUserGuide: QtWidgets.QAction = QtWidgets.QAction(
            MainWindow)
        self.actionOpenUserGuide.setObjectName("actionOpenUserGuide")
        self.actionAbout: QtWidgets.QAction = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionOpenUserGuide)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Schedule Generator"))
        self.generateScheduleButton.setText(
            _translate("MainWindow", "Generate"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpenUserGuide.setText(
            _translate("MainWindow", "Open User Guide"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
