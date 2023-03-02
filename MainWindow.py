"""
Esta clase es la ventana del menú inicial del simulador.
"""
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from matplotlib import pyplot as plt
from documentacion import Ui_TabWidget


class MainWindow(QMainWindow):
    def __init__(self, widget,availableWidth,availableHeight):
        """
        Se inicializan todos los paramétros de la ventana.

        :param widget: QStackedWidget del simulador.
        :param availableWidth: Ancho disponible de la pantalla.
        :param availableHeight: Largo disponible de la pantalla.
        """
        self.availableWidth, self.availableHeight = availableWidth,availableHeight
        super(MainWindow, self).__init__()
        loadUi("UIs\MainWindow_Simulador.ui", self)
        self.widget = widget

        self.widget.insertWidget(0, self)
        self.SClasicasButton.clicked.connect(self.goToScreenSenalesClasicas)
        self.SNoConvencionalesButton.clicked.connect(self.goToScreenSenalesNC)
        self.DocumentationButton.clicked.connect(self.documentacion_Window)
        plt.close('all')

    def goToScreenSenalesClasicas(self):
        """
        Navegar a la ventana de Señales Clásicas
        """
        self.widget.setCurrentIndex(1)

    def goToScreenSenalesNC(self):
        """
        Navegar a la ventana de Señales No Convencionales (SNC)
        """
        self.widget.setCurrentIndex(2)

    def documentacion_Window(self):
        """
        Se abre la ventana de la documentación
        """
        self.documentacionWindow = QtWidgets.QTabWidget()
        self.ui = Ui_TabWidget()
        self.ui.setupUi(self.documentacionWindow,self.availableWidth,self.availableHeight)
        self.documentacionWindow.show()