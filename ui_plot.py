# -*- coding: utf-8 -*-

###################################################################################
## Form generated from reading UI file 'plotKvWxGF.ui'                           ##
##                                                                               ##
## Created by: Qt User Interface Compiler version 5.15.2                         ##
##                                                                               ##
## WARNING! All changes made in this file will be lost when recompiling UI file! ##
###################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(301, 371)
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet(u"background-color: rgba(44, 62, 80, 0);\n"
"color: white;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 0, 301, 371))
        self.frame_9.setStyleSheet(u"background-color: rgb(44, 62, 80);\n"
"border-radius: 20px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_9)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 310, 281, 51))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: #3498DB;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(41, 128, 185);\n"
"}\n"
"")
        self.frame = QFrame(self.frame_9)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 30, 281, 111))
        self.frame.setStyleSheet(u"background-color: rgb(52, 73, 94);\n"
"border-radius: 20px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(120, 60, 141, 31))
        self.frame_4.setStyleSheet(u"background-color: rgb(44, 62, 80);\n"
"border-radius:10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.Charge2 = QSpinBox(self.frame_4)
        self.Charge2.setObjectName(u"Charge2")
        self.Charge2.setGeometry(QRect(10, 0, 121, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.Charge2.setFont(font1)
        self.Charge2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Charge2.setMinimum(-1000)
        self.Charge2.setMaximum(1000)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(120, 20, 141, 31))
        self.frame_3.setStyleSheet(u"background-color: rgb(44, 62, 80);\n"
"border-radius:10px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.Charge1 = QSpinBox(self.frame_3)
        self.Charge1.setObjectName(u"Charge1")
        self.Charge1.setGeometry(QRect(10, 0, 121, 31))
        self.Charge1.setFont(font1)
        self.Charge1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Charge1.setMinimum(-1000)
        self.Charge1.setMaximum(1000)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 91, 31))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 91, 31))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.frame_9)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 150, 281, 151))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(52, 73, 94);\n"
"border-radius: 20px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QRect(20, 50, 31, 31))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(170, 10, 91, 31))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 10, 91, 31))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(70, 50, 81, 33))
        self.frame_5.setStyleSheet(u"color: rgb(231, 76, 60);\n"
"background-color: rgb(44, 62, 80);\n"
"border-radius:10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.Charge1_2 = QSpinBox(self.frame_5)
        self.Charge1_2.setObjectName(u"Charge1_2")
        self.Charge1_2.setGeometry(QRect(10, 0, 61, 31))
        self.Charge1_2.setFont(font1)
        self.Charge1_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Charge1_2.setMinimum(-1000)
        self.Charge1_2.setMaximum(1000)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 90, 31, 31))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(70, 90, 81, 33))
        self.frame_6.setStyleSheet(u"color: rgb(46, 204, 113);\n"
"background-color: rgb(44, 62, 80);\n"
"border-radius:10px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.Charge1_3 = QSpinBox(self.frame_6)
        self.Charge1_3.setObjectName(u"Charge1_3")
        self.Charge1_3.setGeometry(QRect(10, 0, 61, 31))
        self.Charge1_3.setFont(font1)
        self.Charge1_3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Charge1_3.setMinimum(-1000)
        self.Charge1_3.setMaximum(1000)
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(180, 90, 81, 33))
        self.frame_7.setStyleSheet(u"color: rgb(46, 204, 113);\n"
"background-color: rgb(44, 62, 80);\n"
"border-radius:10px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.Charge1_6 = QSpinBox(self.frame_7)
        self.Charge1_6.setObjectName(u"Charge1_6")
        self.Charge1_6.setGeometry(QRect(10, 0, 61, 31))
        self.Charge1_6.setFont(font1)
        self.Charge1_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Charge1_6.setMinimum(-1000)
        self.Charge1_6.setMaximum(1000)
        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(180, 50, 81, 33))
        self.frame_8.setStyleSheet(u"color: rgb(231, 76, 60);\n"
"background-color: rgb(44, 62, 80);\n"
"border-radius:10px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.Charge1_7 = QSpinBox(self.frame_8)
        self.Charge1_7.setObjectName(u"Charge1_7")
        self.Charge1_7.setGeometry(QRect(10, 0, 61, 31))
        self.Charge1_7.setFont(font1)
        self.Charge1_7.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Charge1_7.setMinimum(-1000)
        self.Charge1_7.setMaximum(1000)
        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 10, 14, 14))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"width:14px;\n"
"height:14px;\n"
"border-radius:7px;\n"
"background-color:#E74C3C;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(192, 57, 43);\n"
"}")
        self.pushButton_3 = QPushButton(self.frame_9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 10, 14, 14))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"width:14px;\n"
"height:14px;\n"
"border-radius:7px;\n"
"background-color:#F1C40F;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(243, 156, 18);\n"
"}")
        self.pushButton_4 = QPushButton(self.frame_9)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(50, 10, 14, 14))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Symbol")
        font2.setPointSize(18)
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setCursor(QCursor(Qt.ForbiddenCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"width:14px;\n"
"height:14px;\n"
"border-radius:7px;\n"
"	background-color: rgba(46, 204, 113, 150);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Charge plotter", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PLOT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CHARGE 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CHARGE 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CHARGE 2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CHARGE 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
    # retranslateUi

