import sys
import platform
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from main import *

GLOBAL_STATE = 0

class UIFunctions(MainWindow):
	
	def uiDefininitions(self):
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		self.ui.pushButton_3.clicked.connect(lambda: self.showMinimized())

		self.ui.pushButton_2.clicked.connect(lambda: self.close())