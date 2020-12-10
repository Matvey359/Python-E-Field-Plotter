import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib import cm, colors
import numpy as np
import math

from ui_plot import Ui_MainWindow
from ui_functions import *

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

## ==> WINDOW MOVE
		def moveWindow(event):

			if event.buttons() == Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.dragPos)
				self.dragPos = event.globalPos()
				event.accept()

		self.ui.frame_9.mouseMoveEvent = moveWindow

## ==> SETTING UP SPIN BOXES
		self.ui.Charge1_2.setSuffix(" px")
		#self.ui.Charge1_2.setValue(25)
		self.ui.Charge1_2.valueChanged.connect(self.variables)
		self.ui.Charge1_3.setSuffix(" px")
		#self.ui.Charge1_3.setValue(25)
		self.ui.Charge1_3.valueChanged.connect(self.variables)
		self.ui.Charge1_6.setSuffix(" px")
		#self.ui.Charge1_6.setValue(52)
		self.ui.Charge1_6.valueChanged.connect(self.variables)
		self.ui.Charge1_7.setSuffix(" px")
		#self.ui.Charge1_7.setValue(52)
		self.ui.Charge1_7.valueChanged.connect(self.variables)

		self.ui.Charge1.setSuffix(" q")
		#self.ui.Charge1.setValue(1000)
		self.ui.Charge1.valueChanged.connect(self.variables)
		self.ui.Charge2.setSuffix(" q")
		#self.ui.Charge2.setValue(-1000)
		self.ui.Charge2.valueChanged.connect(self.variables)

## ==> SETTING UP BUTTON
		self.ui.pushButton.clicked.connect(self.plot)

## ==> SETTING UP TITLE BAR
		UIFunctions.uiDefininitions(self)

## ==> WINDOW SHOW
		self.show()

## ==> CONTINUATION OF WINDOW MOVE
	def mousePressEvent(self, event):
		self.dragPos = event.globalPos()

## ==> GET VALUES FROM SPIN BOXES
	def variables(self):
		self.q1 = self.ui.Charge1.value()
		self.q2 = self.ui.Charge2.value()
		self.q1CordX = self.ui.Charge1_2.value()
		self.q1CordY = self.ui.Charge1_3.value()

		self.q2CordX = self.ui.Charge1_7.value()
		self.q2CordY = self.ui.Charge1_6.value()

## ==> PLOTTING
	def plot(self):

## ==> DEBUG
		print(self.q1)
		print(self.q2)
		print(self.q1CordX)
		print(self.q1CordY)
		print(self.q2CordX)
		print(self.q2CordY)

## ==> CREATING COLOR MAP
		cdict = {'red':   [[0.0, 1.0, 1.0],
							[0.25, 1.0, 1.0],
							[0.5, 0.0, 0.0],
							[1.0, 0.0, 0.0]],
				'green': [[0.0, 0.0, 0.0],
							[0.0, 0.0, 0.0],
							[0.0, 0.0, 0.0],
							[1.0, 0.01, 0.01]],
				'blue':  [[0.0, 0.0, 0.0],
							[0.5, 0.0, 0.0],
							[0.75, 1.0, 1.0],
							[1.0, 1.0, 1.0]]}

		newcmp = colors.LinearSegmentedColormap('testCmap', segmentdata=cdict, N=256)

## ==> SETTING UP CANVAS
		width = 100
		height = 100

		np.random.seed(19680801)

		self.data = np.random.randn(width, height)

## ==> MATH AND PHYSICS MAGIC :)
		for x in range(width):
			for y in range(height):
				a1 = math.fabs(x - self.q1CordX)
				b1 = math.fabs(y - self.q1CordY)
				r1 = math.sqrt(a1**2 + b1**2)
	
				a2 = math.fabs(x - self.q2CordX)
				b2 = math.fabs(y - self.q2CordY)
				r2 = math.sqrt(a2**2 + b2**2)

				if r1 == 0:
					fiQ1 = 0
				else:
					fiQ1 = self.q1 / r1
	
				if r2 == 0:
					fiQ2 = 0
				else:
					fiQ2 = self.q2 / r2
	
				fi = (fiQ1 + fiQ2)
	
				#if y <= 200 or y >= 800:
				#	data[[x], [y]] = 0
	
				self.data[[x], [y]] = fi
	
			#if x <= 250 or x >= 750:
			#	data[[x], [y]] = 0

## ==> SHOW RESULT

		plt.imshow(self.data, cmap=newcmp, interpolation='bicubic')
		plt.colorbar()
		plt.scatter(self.q1CordY, self.q1CordX, s=150, c='blue', marker='o')
		plt.scatter(self.q1CordY, self.q1CordX, s=75, c='white', marker='_')
		plt.scatter(self.q2CordY, self.q2CordX, s=150, c='red', marker='o')
		plt.scatter(self.q2CordY, self.q2CordX, s=75, c='white', marker='+')
		plt.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())