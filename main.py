"""
Script que ejecuta el simulador.
"""

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication
from matplotlib import pyplot as plt
from MainWindow import MainWindow
from SenalesClasicas import SenalesClasicas
from SenalesNoConvencionales import SenalesNoConvencionales

#Parametros globales de la simulación
fSample = 3000
nTotalSimb = 10000

#Se obtienen las dimensiones de la pantalla
app = QApplication(sys.argv)
screen = app.primaryScreen()
size = screen.size()
rect = screen.availableGeometry()
sizeHeight = rect.height()
frameSizeWidth = int(rect.width()*0.85)
frameSizeHeight = int(rect.height()*0.85)
availableWidth = rect.width()
availableHeight = rect.height()

#Se inicializan las ventanas
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow(widget,availableWidth, availableHeight)
senalesClasicas = SenalesClasicas(widget, frameSizeWidth, frameSizeHeight, fSample, nTotalSimb, sizeHeight)
senalesNC = SenalesNoConvencionales(widget,frameSizeWidth, frameSizeHeight, fSample, nTotalSimb, sizeHeight)
plt.close('all')

nroSimb = senalesNC.cbNumSimb.currentText()
senalesNC.numeroSimbolos(nroSimb)

widget.show()
widget.setWindowState(QtCore.Qt.WindowMaximized)
widget.setWindowTitle("Simulador de Señales Digitales")

try:
    sys.exit(app.exec_())
except:
    print("Exiting")