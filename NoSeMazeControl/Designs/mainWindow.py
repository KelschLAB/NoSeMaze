# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/MainWindowEdited.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QtWidgets.QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1056, 847)
        self.centralwidget: QtWidgets.QWidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout: QtWidgets.QGridLayout = QtWidgets.QGridLayout(
            self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox: QtWidgets.QGroupBox = QtWidgets.QGroupBox(
            self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3: QtWidgets.QGridLayout = QtWidgets.QGridLayout(
            self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.startButton: QtWidgets.QPushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.startButton.setObjectName("startButton")
        self.gridLayout_3.addWidget(self.startButton, 0, 0, 1, 1)
        self.stopButton: QtWidgets.QPushButton = QtWidgets.QPushButton(
            self.groupBox)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_3.addWidget(self.stopButton, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2: QtWidgets.QGroupBox = QtWidgets.QGroupBox(
            self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2: QtWidgets.QGridLayout = QtWidgets.QGridLayout(
            self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.experimentDateLabel: QtWidgets.QLabel = QtWidgets.QLabel(
            self.groupBox_2)
        self.experimentDateLabel.setObjectName("experimentDateLabel")
        self.gridLayout_2.addWidget(self.experimentDateLabel, 2, 1, 1, 1)
        self.label_3: QtWidgets.QLabel = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.experimentNameLabel: QtWidgets.QLabel = QtWidgets.QLabel(
            self.groupBox_2)
        self.experimentNameLabel.setObjectName("experimentNameLabel")
        self.gridLayout_2.addWidget(self.experimentNameLabel, 0, 1, 1, 1)
        self.label: QtWidgets.QLabel = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2: QtWidgets.QLabel = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.savePathLabel: QtWidgets.QLabel = QtWidgets.QLabel(
            self.groupBox_2)
        self.savePathLabel.setObjectName("savePathLabel")
        self.gridLayout_2.addWidget(self.savePathLabel, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.trialView = QtWidgets.QTableView(self.centralwidget)
        font: QtGui.QFont = QtGui.QFont()
        font.setPointSize(9)
        self.trialView.setFont(font)
        self.trialView.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.trialView.setObjectName("trialView")
        self.gridLayout.addWidget(self.trialView, 1, 0, 1, 2)
        self.groupBox_3: QtWidgets.QGroupBox = QtWidgets.QGroupBox(
            self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setToolTip(
            "The data view shows the following information:\n1. Odor data.\n2. Licks data (right) or analog input connected to it.\n3. Licks data (left) or analog input connected to it.")
        self.gridLayout_4: QtWidgets.QGridLayout = QtWidgets.QGridLayout(
            self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.dataRView: PlotWidget = PlotWidget(self.groupBox_3)
        self.dataRView.setObjectName("dataRView")
        self.gridLayout_4.addWidget(self.dataRView, 2, 1, 1, 1)
        self.graphicsView: PlotWidget = PlotWidget(self.groupBox_3)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_4.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.dataLView: PlotWidget = PlotWidget(self.groupBox_3)
        self.dataLView.setObjectName("dataLView")
        self.gridLayout_4.addWidget(self.dataLView, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar: QtWidgets.QMenuBar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile: QtWidgets.QMenu = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHardware: QtWidgets.QMenu = QtWidgets.QMenu(self.menubar)
        self.menuHardware.setObjectName("menuHardware")
        self.menuAnimals: QtWidgets.QMenu = QtWidgets.QMenu(self.menubar)
        self.menuAnimals.setObjectName("menuAnimals")
        self.menuAnalysis: QtWidgets.QMenu = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuNotification: QtWidgets.QMenu = QtWidgets.QMenu(self.menubar)
        self.menuNotification.setObjectName("menuNotification")
        self.menuVideo: QtWidgets.QMenu = QtWidgets.QMenu(self.menubar)
        self.menuVideo.setObjectName("menuVideo")
        self.menuHelp: QtWidgets.QMenu = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar: QtWidgets.QStatusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHardware_Preferences: QtWidgets.QAction = QtWidgets.QAction(
            MainWindow)
        self.actionHardware_Preferences.setObjectName(
            "actionHardware_Preferences")
        self.actionAnimal_List: QtWidgets.QAction = QtWidgets.QAction(
            MainWindow)
        self.actionAnimal_List.setObjectName("actionAnimal_List")
        self.actionSave_Experiment: QtWidgets.QAction = QtWidgets.QAction(
            MainWindow)
        self.actionSave_Experiment.setObjectName("actionSave_Experiment")
        self.actionLoad_Experiment: QtWidgets.QAction = QtWidgets.QAction(
            MainWindow)
        self.actionLoad_Experiment.setObjectName("actionLoad_Experiment")
        self.actionPreferences: QtWidgets.QAction = QtWidgets.QAction(
            MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAnalyse_Experiment: QtWidgets.QAction = QtWidgets.QAction(
            MainWindow)
        self.actionAnalyse_Experiment.setObjectName("actionAnalyse_Experiment")
        self.actionMailing_List: QtWidgets.QAction = QtWidgets.QAction(
            MainWindow)
        self.actionMailing_List.setObjectName("actionMailing_List")
        self.actionMessage_Folder: QtWidgets.QAction = QtWidgets.QAction(
            MainWindow)
        self.actionMessage_Folder.setObjectName("actionMessage_Folder")
        self.actionVideo_Control: QtWidgets.QAction = QtWidgets.QAction(
            MainWindow)
        self.actionVideo_Control.setObjectName("actionVideo_Control")
        self.actionOpenUserGuide: QtWidgets.QAction = QtWidgets.QAction(
            MainWindow)
        self.actionOpenUserGuide.setObjectName("actionOpenUserGuide")
        self.actionAbout: QtWidgets.QAction = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionSave_Experiment)
        self.menuFile.addAction(self.actionLoad_Experiment)
        self.menuHardware.addAction(self.actionHardware_Preferences)
        self.menuAnimals.addAction(self.actionAnimal_List)
        self.menuAnalysis.addAction(self.actionAnalyse_Experiment)
        self.menuNotification.addAction(self.actionMailing_List)
        self.menuNotification.addAction(self.actionMessage_Folder)
        self.menuVideo.addAction(self.actionVideo_Control)
        self.menuHelp.addAction(self.actionOpenUserGuide)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHardware.menuAction())
        self.menubar.addAction(self.menuAnimals.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuNotification.menuAction())
        self.menubar.addAction(self.menuVideo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NoSeMaze Control"))
        self.groupBox.setTitle(_translate("MainWindow", "Control Panel"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Experiment Info"))
        self.experimentDateLabel.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "Date of Creation :"))
        self.experimentNameLabel.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Experiment Name :"))
        self.label_2.setText(_translate("MainWindow", "Save Path"))
        self.savePathLabel.setText(_translate("MainWindow", "..."))
        self.groupBox_3.setTitle(_translate("MainWindow", "Data View"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHardware.setTitle(_translate("MainWindow", "Hardware"))
        self.menuAnimals.setTitle(_translate("MainWindow", "Animals"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.menuNotification.setTitle(
            _translate("MainWindow", "Notification"))
        self.menuVideo.setTitle(_translate("MainWindow", "Video"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionHardware_Preferences.setText(
            _translate("MainWindow", "Hardware Preferences"))
        self.actionAnimal_List.setText(_translate("MainWindow", "Animal List"))
        self.actionSave_Experiment.setText(
            _translate("MainWindow", "Save Experiment"))
        self.actionLoad_Experiment.setText(
            _translate("MainWindow", "Load Experiment"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionAnalyse_Experiment.setText(
            _translate("MainWindow", "Analyse Experiment"))
        self.actionMailing_List.setText(
            _translate("MainWindow", "Mailing List"))
        self.actionMessage_Folder.setText(
            _translate("MainWindow", "Message Folder"))
        self.actionVideo_Control.setText(
            _translate("MainWindow", "Video Control"))
        self.actionOpenUserGuide.setText(
            _translate("MainWindow", "Open User Guide"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
