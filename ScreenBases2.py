"""
Esta clase contiene la ventana de resultados para Señales No Convencionales - Bases - 2 Símbolos.
"""
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from Funciones_GUI import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import traceback

from numCiclos import Ui_CalcuFreqWindow

class ScreenBases2(QMainWindow):
    def __init__(self, widget,frameSizeWidth, frameSizeHeight, fSample, nTotalSimb, sizeHeight):
        """
        Método constructor donde se definen los elementos de la GUI.

        :param widget: QStackedWidget del simulador.
        :param frameSizeWidth: Ancho del Frame que contiene las gráficas.
        :param frameSizeHeight: Largo del Frame que contiene las gráficas.
        :param fSample: Frecuencia de muestreo.
        :param nTotalSimb: Número total de símbolos que compone la señal.
        :param sizeHeight: Alto de la Pantalla
        """
        super(ScreenBases2, self).__init__()
        loadUi("UIs\SenalesNC_Bases_2S.ui", self)
        self.widget = widget
        self.fSample = fSample
        self.nTotalSimb = nTotalSimb
        self.sizeHeight = sizeHeight

        self.SimularButton.setStatusTip('Los resultados pueden tomar tiempo')
        self.setMouseTracking(True)

        # Tamaño de las gráficas
        self.SimbyBasesFrame.setMinimumSize(frameSizeWidth, frameSizeHeight)
        self.ConstFrame.setMinimumSize(frameSizeWidth, frameSizeHeight)
        self.SenalFrame.setMinimumSize(frameSizeWidth, frameSizeHeight)
        self.PeFrame.setMinimumSize(frameSizeWidth, frameSizeHeight)

        self.setStyleSheet("""
                                            QScrollBar:vertical{
                                            background-color: rgb(204, 205, 206);
                                            width: 15px;
                                            }

                                            QScrollBar::handle:vertical{
                                            background-color: rgb(255, 177, 64);
                                            width: 15px;
                                            }

                                            QScrollBar::handle:vertical:hover{
                                            background-color: rgb(255, 202, 128);
                                            }

                                            QScrollBar::add-line:vertical {
                                                 background: rgb(255, 177, 64);
                                            }

                                            QScrollBar::sub-line:vertical {
                                                 background: rgb(255, 177, 64);
                                            }

                                            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                                 background: none;
                                            }
                                            """)

        # Simbolo por default U1 y U2
        self.cbSimb2.setCurrentIndex(4)
        self.cbSimb1.setCurrentIndex(3)

        self.sbTsimb.valueChanged.connect(self.spinBoxInt)
        self.hsTsimb.valueChanged.connect(self.sliderFloat)
        self.leFaseS1.setText("0")
        self.leFaseS2.setText("-pi/2")

        self.XS1.setText("1")
        self.YS1.setText("0")

        self.XS2.setText("0")
        self.YS2.setText("1")

        self.leFsimb.setReadOnly(True)
        self.leFsimb.setText("10")


        self.cbT1S1.setEnabled(False)
        self.cbT1S1.setStyleSheet("QComboBox{\n"
                                  "    background: rgb(217, 217, 217);\n"
                                  "    color: black;\n"
                                  "    border: 2px solid black;\n"
                                  "    font-size: 15px;\n"
                                  "}")
        self.cbT2S1.setEnabled(False)
        self.cbT2S1.setStyleSheet("QComboBox{\n"
                                  "    background: rgb(217, 217, 217);\n"
                                  "    color: black;\n"
                                  "    border: 2px solid black;\n"
                                  "    font-size: 15px;\n"
                                  "}")
        self.cbT1S2.setEnabled(False)
        self.cbT1S2.setStyleSheet("QComboBox{\n"
                                  "    background: rgb(217, 217, 217);\n"
                                  "    color: black;\n"
                                  "    border: 2px solid black;\n"
                                  "    font-size: 15px;\n"
                                  "}")
        self.cbT2S2.setEnabled(False)
        self.cbT2S2.setStyleSheet("QComboBox{\n"
                                  "    background: rgb(217, 217, 217);\n"
                                  "    color: black;\n"
                                  "    border: 2px solid black;\n"
                                  "    font-size: 15px;\n"
                                  "}")

        self.cbSimb1.currentTextChanged.connect(self.hideDataS1)
        self.cbSimb2.currentTextChanged.connect(self.hideDataS2)

        self.cbT1S1.setItemData(0, ["25%", "50%", "75%"])
        self.cbT1S1.setItemData(1, ["25%", "50%", "75%"])
        self.cbT1S1.setItemData(2, ["25%", "50%"])
        self.cbT1S1.setItemData(3, ["25%"])

        self.cbT1S2.setItemData(0, ["25%", "50%", "75%"])
        self.cbT1S2.setItemData(1, ["25%", "50%", "75%"])
        self.cbT1S2.setItemData(2, ["25%", "50%"])
        self.cbT1S2.setItemData(3, ["25%"])

        self.E1.setReadOnly(True)
        self.E2.setReadOnly(True)

        self.leDmin.setReadOnly(True)

        self.leXS1.setReadOnly(True)
        self.leYS1.setReadOnly(True)

        self.leXS2.setReadOnly(True)
        self.leYS2.setReadOnly(True)

        self.lePotencia.setReadOnly(True)
        self.leEnergia.setReadOnly(True)
        self.leEta.setReadOnly(True)
        self.leSimbErrados.setReadOnly(True)
        self.leBW.setReadOnly(True)

        self.leNDmin.setReadOnly(True)
        self.leNumSimb.setReadOnly(True)
        self.leDminPe.setReadOnly(True)
        self.leEtaPe.setReadOnly(True)
        self.lePeCota.setReadOnly(True)
        self.leSimbErradosPe.setReadOnly(True)
        self.leSimbTotalesPe.setReadOnly(True)
        self.lePeSimbErrados.setReadOnly(True)

        self.cbT1S1.activated.connect(self.tiemposInicioDuracionS1)
        self.cbT1S2.activated.connect(self.tiemposInicioDuracionS2)

        # Aca va en el Canvas
        # Símbolos
        self.figure_simbGraph = plt.figure(constrained_layout=True)
        self.canvas_simbGraph = FigureCanvas(self.figure_simbGraph)
        self.toolbar_simbGraph = NavigationToolbar(self.canvas_simbGraph, self)

        self.verticalLayout_simbGraph.addWidget(self.toolbar_simbGraph)
        self.verticalLayout_simbGraph.addWidget(self.canvas_simbGraph)

        self.toolbar_simbGraph.setMaximumHeight(int(frameSizeHeight * 0.06))

        # Bases
        self.figure_basesGraph = plt.figure(constrained_layout=True)
        self.canvas_basesGraph = FigureCanvas(self.figure_basesGraph)
        self.toolbar_basesGraph = NavigationToolbar(self.canvas_basesGraph, self)

        self.verticalLayout_basesGraph.addWidget(self.toolbar_basesGraph)
        self.verticalLayout_basesGraph.addWidget(self.canvas_basesGraph)

        self.toolbar_basesGraph.setMaximumHeight(int(frameSizeHeight * 0.06))

        # Constelación antes del canal
        self.figure_constACGraph = plt.figure(constrained_layout=True)
        self.canvas_constACGraph = FigureCanvas(self.figure_constACGraph)
        self.toolbar_constACGraph = NavigationToolbar(self.canvas_constACGraph, self)

        self.verticalLayout_constACGraph.addWidget(self.toolbar_constACGraph)
        self.verticalLayout_constACGraph.addWidget(self.canvas_constACGraph)

        self.toolbar_constACGraph.setMaximumHeight(int(frameSizeHeight * 0.06))

        # Constelación después del canal
        self.figure_constDCGraph = plt.figure(constrained_layout=True)
        self.canvas_constDCGraph = FigureCanvas(self.figure_constDCGraph)
        self.toolbar_constDCGraph = NavigationToolbar(self.canvas_constDCGraph, self)

        self.verticalLayout_constDCGraph.addWidget(self.toolbar_constDCGraph)
        self.verticalLayout_constDCGraph.addWidget(self.canvas_constDCGraph)

        self.toolbar_constDCGraph.setMaximumHeight(int(frameSizeHeight * 0.06))

        # Señal en tiempo
        self.figure_senalTiempoGraph = plt.figure(constrained_layout=True)
        self.canvas_senalTiempoGraph = FigureCanvas(self.figure_senalTiempoGraph)
        self.toolbar_senalTiempoGraph = NavigationToolbar(self.canvas_senalTiempoGraph, self)

        self.verticalLayout_senalTiempoGraph.addWidget(self.toolbar_senalTiempoGraph)
        self.verticalLayout_senalTiempoGraph.addWidget(self.canvas_senalTiempoGraph)

        self.toolbar_senalTiempoGraph.setMaximumHeight(int(frameSizeHeight * 0.06))

        # Señal en Frecuencia
        self.figure_senalFreqGraph = plt.figure(constrained_layout=True)
        self.canvas_senalFreqGraph = FigureCanvas(self.figure_senalFreqGraph)
        self.toolbar_senalFreqGraph = NavigationToolbar(self.canvas_senalFreqGraph, self)

        self.verticalLayout_senalFreqGraph.addWidget(self.toolbar_senalFreqGraph)
        self.verticalLayout_senalFreqGraph.addWidget(self.canvas_senalFreqGraph)

        self.toolbar_senalFreqGraph.setMaximumHeight(int(frameSizeHeight * 0.06))

        # Probabilidad de Error
        self.figure_PeGraph = plt.figure(constrained_layout=True)
        self.canvas_PeGraph = FigureCanvas(self.figure_PeGraph)
        self.toolbar_PeGraph = NavigationToolbar(self.canvas_PeGraph, self)

        self.verticalLayout_PeGraph.addWidget(self.toolbar_PeGraph)
        self.verticalLayout_PeGraph.addWidget(self.canvas_PeGraph)

        self.toolbar_PeGraph.setMaximumHeight(int(frameSizeHeight * 0.06))

        # Simular
        self.SimularButton.clicked.connect(self.simular)
        # Núm Ciclos en Sinusoides
        self.NumCiclosButton.clicked.connect(self.numCiclosSinusoides_Window)
        # # Atrás
        self.BackButton.clicked.connect(self.goToSNCWindow)

    def goToSNCWindow(self):
        """
        Navegar al menú de Señales No Convencionales
        """
        plt.close('all')
        self.widget.setCurrentIndex(2)

    def numCiclosSinusoides_Window(self):
        """
        Abrir ventana de Num. Ciclos en Sinusoides
        """
        self.NCWindow = QtWidgets.QMainWindow()
        self.ui = Ui_CalcuFreqWindow()
        self.ui.setupUi(self.NCWindow)
        self.NCWindow.show()

    def mensaje_error1(self,error):
        """
        Definición de PopUpWindow para notificar error.

        :param error: String con el error ocurrido.
        """
        msg = QMessageBox()
        msg.setWindowTitle("¡Error!")
        msg.setText("Ingresó un valor inválido para la amplitud o fase.")
        msg.setIcon(QMessageBox.Warning)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setDetailedText(error)
        x = msg.exec_()

    def mensaje_error2(self,error):
        """
        Definición de PopUpWindow para notificar error.

        :param error: String con el error ocurrido.
        """
        msg = QMessageBox()
        msg.setWindowTitle("¡Error!")
        msg.setText("Oh oh! Algo salió mal.")
        msg.setIcon(QMessageBox.Warning)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setDetailedText(error)
        x = msg.exec_()

    def mensaje_errorBases(self):
        """
        Definición de PopUpWindow para notificar que se ingresaron dos bases que no son ortogonales.
        """
        msg = QMessageBox()
        msg.setWindowTitle("¡Error!")
        msg.setText("Las bases ingresadas no son ortogonales. Los resultados pueden resultar erróneos")
        msg.setIcon(QMessageBox.Warning)
        msg.setDefaultButton(QMessageBox.Ok)
        x = msg.exec_()

    def mensaje_errorSimbsIguales(self):
        """
        Definición de PopUpWindow para notificar que se ingresaron dos símbolos iguales.
        """
        msg = QMessageBox()
        msg.setWindowTitle("¡Error!")
        msg.setText("Has ingresado dos símbolos iguales.")
        msg.setIcon(QMessageBox.Warning)
        msg.setDefaultButton(QMessageBox.Ok)
        x = msg.exec_()

    def spinBoxInt(self, value):
        """
        Este método actualiza el valor del slider del Tiempo de Simbolo (int) con el SpinBox del Tiempo de Simbolo (float).
        Adicionalmente actualiza el label con la Frecuencia de Simbolo.
        """
        self.hsTsimb.setValue(int(value*10))

        fSimb = 1/value

        if fSimb.is_integer():
            self.leFsimb.setText(str(int(fSimb)))

        else:
            self.leFsimb.setText(format(fSimb, "10.3f"))

    def sliderFloat(self, value):
        """
        Este método actualiza el valor del SpinBox del Tiempo de Simbolo (float) con el Slider del Tiempo de Simbolo (int).
        """
        self.sbTsimb.setValue(value/10)

    def tiemposInicioDuracionS1(self, index):
        """
        Para base U1. Esta función actualiza las opciones de Duración de los símbolos de duración variable según el instante de inicio.

        :param index:  Instante de inicio.
        """
        self.cbT2S1.clear()
        self.cbT2S1.addItems(self.cbT1S1.itemData(index))

    def tiemposInicioDuracionS2(self, index):
        """
        Para base U2. Esta función actualiza las opciones de Duración de los símbolos de duración variable según el instante de inicio.

        :param index:  Instante de inicio.
        """
        self.cbT2S2.clear()
        self.cbT2S2.addItems(self.cbT1S2.itemData(index))

    def hideDataS1(self, tipo):
        """
        Para base U1. Esta función habilita o deshabilita los distintos datos a ingresar según el símbolo seleccionado.

        :param tipo: Opción de Símbolo seleccionada con el ComboBox
        """
        if tipo == "Coseno" or tipo == "Coseno de duración variable":
            self.hsFreqS1.setEnabled(True)
            self.hsFreqS1.setStyleSheet("""
                                                QSlider{
                                                    background-color: transparent;
                                                    padding: 2px;
                                                }

                                                QSlider::groove:horizontal{
                                                    subcontrol-origin: content;
                                                    background-color: transparent;
                                                    height: 17px;
                                                }

                                                QSlider::handle:horizontal{
                                                    background-color: rgb(255, 177, 64);
                                                    width: 16px;
                                                    border-radius: 7px;
                                                }

                                                QSlider::sub-page:horizontal{
                                                    background-color: white;
                                                    margin: 4px;
                                                    border-radius: 5px;
                                                }

                                                QSlider::add-page:horizontal{
                                                    background-color: white;
                                                    margin: 4px;
                                                    border-radius: 5px; 
                                                }
                                                """)
            self.sbFreqS1.setEnabled(True)
            self.sbFreqS1.setStyleSheet("""QSpinBox{
                                                        background-color: white;
                                                        qproperty-alignment: AlignCenter;
                                                    }       
                                                """)
        else:
            self.hsFreqS1.setEnabled(False)
            self.hsFreqS1.setStyleSheet("""
                                                QSlider{
                                                    background-color: transparent;
                                                    padding: 2px;
                                                }

                                                QSlider::groove:horizontal{
                                                    subcontrol-origin: content;
                                                    background-color: transparent;
                                                    height: 17px;
                                                }

                                                QSlider::handle:horizontal{
                                                    background-color: rgb(255, 177, 64);
                                                    width: 16px;
                                                    border-radius: 7px;
                                                }

                                                QSlider::sub-page:horizontal{
                                                    background-color: rgb(217, 217, 217);
                                                    margin: 4px;
                                                    border-radius: 5px;
                                                }

                                                QSlider::add-page:horizontal{
                                                    background-color: rgb(217, 217, 217);
                                                    margin: 4px;
                                                    border-radius: 5px; 
                                                }
                                                """)
            self.sbFreqS1.setEnabled(False)
            self.sbFreqS1.setStyleSheet("""QSpinBox{
                                                        background-color: rgb(217, 217, 217);
                                                        qproperty-alignment: AlignCenter;
                                                    }       
                                                """)

        if tipo == "Coseno":
            self.leFaseS1.setEnabled(True)
            self.leFaseS1.setStyleSheet("QLineEdit{\n"
                                        "    background-color: white;\n"
                                        "    border: 2px solid black;\n"
                                        "}")
        else:
            self.leFaseS1.setEnabled(False)
            self.leFaseS1.setStyleSheet("QLineEdit{\n"
                                        "    background-color: rgb(217, 217, 217);\n"
                                        "    border: 2px solid black;\n"
                                        "}")

        if tipo == "Pulso de duración variable" or tipo == "Coseno de duración variable":
            self.cbT1S1.setEnabled(True)
            self.cbT1S1.setStyleSheet("QComboBox{\n"
                                      "    background: white;\n"
                                      "    color: black;\n"
                                      "    border: 2px solid black;\n"
                                      "    font-size: 15px;\n"    
                                      "}")
            self.cbT2S1.setEnabled(True)
            self.cbT2S1.setStyleSheet("QComboBox{\n"
                                      "    background: white;\n"
                                      "    color: black;\n"
                                      "    border: 2px solid black;\n"
                                      "    font-size: 15px;\n"    
                                      "}")
            self.leFaseS1.setText("0")
        else:
            self.cbT1S1.setEnabled(False)
            self.cbT1S1.setStyleSheet("QComboBox{\n"
                                      "    background: rgb(217, 217, 217);\n"
                                      "    color: black;\n"
                                      "    border: 2px solid black;\n"
                                      "    font-size: 15px;\n"    
                                      "}")
            self.cbT2S1.setEnabled(False)
            self.cbT2S1.setStyleSheet("QComboBox{\n"
                                      "    background: rgb(217, 217, 217);\n"
                                      "    color: black;\n"
                                      "    border: 2px solid black;\n"
                                      "    font-size: 15px;\n"    
                                      "}")

    def hideDataS2(self, tipo):
        """
        Para base U2. Esta función habilita o deshabilita los distintos datos a ingresar según el símbolo seleccionado.

        :param tipo: Opción de Símbolo seleccionada con el ComboBox
        """

        if tipo == "Coseno" or tipo == "Coseno de duración variable":
            self.hsFreqS2.setEnabled(True)
            self.hsFreqS2.setStyleSheet("""
                                                QSlider{
                                                    background-color: transparent;
                                                    padding: 2px;
                                                }

                                                QSlider::groove:horizontal{
                                                    subcontrol-origin: content;
                                                    background-color: transparent;
                                                    height: 17px;
                                                }

                                                QSlider::handle:horizontal{
                                                    background-color: rgb(255, 177, 64);
                                                    width: 16px;
                                                    border-radius: 7px;
                                                }

                                                QSlider::sub-page:horizontal{
                                                    background-color: white;
                                                    margin: 4px;
                                                    border-radius: 5px;
                                                }

                                                QSlider::add-page:horizontal{
                                                    background-color: white;
                                                    margin: 4px;
                                                    border-radius: 5px; 
                                                }
                                                """)
            self.sbFreqS2.setEnabled(True)
            self.sbFreqS2.setStyleSheet("""QSpinBox{
                                                        background-color: white;
                                                        qproperty-alignment: AlignCenter;
                                                    }       
                                                """)
        else:
            self.hsFreqS2.setEnabled(False)
            self.hsFreqS2.setStyleSheet("""
                                                QSlider{
                                                    background-color: transparent;
                                                    padding: 2px;
                                                }

                                                QSlider::groove:horizontal{
                                                    subcontrol-origin: content;
                                                    background-color: transparent;
                                                    height: 17px;
                                                }

                                                QSlider::handle:horizontal{
                                                    background-color: rgb(255, 177, 64);
                                                    width: 16px;
                                                    border-radius: 7px;
                                                }

                                                QSlider::sub-page:horizontal{
                                                    background-color: rgb(217, 217, 217);
                                                    margin: 4px;
                                                    border-radius: 5px;
                                                }

                                                QSlider::add-page:horizontal{
                                                    background-color: rgb(217, 217, 217);
                                                    margin: 4px;
                                                    border-radius: 5px; 
                                                }
                                                """)
            self.sbFreqS2.setEnabled(False)
            self.sbFreqS2.setStyleSheet("""QSpinBox{
                                                        background-color: rgb(217, 217, 217);
                                                        qproperty-alignment: AlignCenter;
                                                    }       
                                                """)

        if tipo == "Coseno":
            self.leFaseS2.setEnabled(True)
            self.leFaseS2.setStyleSheet("QLineEdit{\n"
                                        "    background-color: white;\n"
                                        "    border: 2px solid black;\n"
                                        "}")
        else:
            self.leFaseS2.setEnabled(False)
            self.leFaseS2.setStyleSheet("QLineEdit{\n"
                                        "    background-color: rgb(217, 217, 217);\n"
                                        "    border: 2px solid black;\n"
                                        "}")

        if tipo == "Pulso de duración variable" or tipo == "Coseno de duración variable":
            self.cbT1S2.setEnabled(True)
            self.cbT1S2.setStyleSheet("QComboBox{\n"
                                      "    background: white;\n"
                                      "    color: black;\n"
                                      "    border: 2px solid black;\n"
                                      "    font-size: 15px;\n"    
                                      "}")
            self.cbT2S2.setEnabled(True)
            self.cbT2S2.setStyleSheet("QComboBox{\n"
                                      "    background: white;\n"
                                      "    color: black;\n"
                                      "    border: 2px solid black;\n"
                                      "    font-size: 15px;\n"    
                                      "}")
            self.leFaseS2.setText("0")
        else:
            self.cbT1S2.setEnabled(False)
            self.cbT1S2.setStyleSheet("QComboBox{\n"
                                      "    background: rgb(217, 217, 217);\n"
                                      "    color: black;\n"
                                      "    border: 2px solid black;\n"
                                      "    font-size: 15px;\n"    
                                      "}")
            self.cbT2S2.setEnabled(False)
            self.cbT2S2.setStyleSheet("QComboBox{\n"
                                      "    background: rgb(217, 217, 217);\n"
                                      "    color: black;\n"
                                      "    border: 2px solid black;\n"
                                      "    font-size: 15px;\n"    
                                      "}")

    def tipoSenal(self, opcion):
        """
        Esta función devuelve un número del 0 al 6 para cada tipo de símbolo.

        :param opcion:  Símbolo escogido por el usuario
        """
        if opcion == 'Pulso nulo':
            return 0
        elif opcion == 'Pulso':
            return 1
        elif opcion == 'Medio pulso':
            return 2
        elif opcion == 'Manchester':
            return 3
        elif opcion == 'Coseno':
            return 4
        elif opcion == 'Pulso de duración variable':
            return 5
        elif opcion == 'Coseno de duración variable':
            return 6

    def inicioDuracion(self, inicio, duracion):
        """
        Esta función define numericamente los instantes de inicio y la duración de los símbolos de duración variable

        :param inicio: Opción escogida para inicio del símbolo por el usuario.
        :param duracion: Opción escogida para duración del símbolo por el usuario.
        """
        if inicio == "0":
            t1s1 = 0
        elif inicio == "0.25 tsimb":
            t1s1 = 1
        elif inicio == "0.5 tsimb":
            t1s1 = 2
        else:
            t1s1 = 3

        if duracion == "25%":
            t2s1 = t1s1 + 1
            tipoOnda = 5
        elif duracion == "50%":
            t2s1 = t1s1 + 2
            tipoOnda = 6
        else:
            t2s1 = t1s1 + 3
            tipoOnda = 7

        return (t1s1, t2s1, tipoOnda)

    def chequearSimbsIguales(self,s1,s2):
        """
        Función que devuelve True si dos símbolos son iguales o False si son diferentes.

        :param s1: Símbolo 1 para comparar.
        :param s2: Símbolo 2 para comparar.
        """
        if np.allclose(s1,s2):
            return True
        else:
            return False

    def graficarSimb(self, s1, s2, tSimb, t):
        """
        Función que realiza la gráfica de los símbolos en la GUI.

        :param s1: Símbolo 1
        :param s2: Símbolo 2
        :param tSimb: Tiempo de símbolo
        :param t: Vector tiempo
        """
        self.figure_simbGraph.clear()

        zeroes = np.zeros(1)
        s1Graf = np.concatenate((zeroes, s1, zeroes))
        s2Graf = np.concatenate((zeroes, s2, zeroes))

        tGraf = np.linspace(-0.001 * tSimb, tSimb * 1.001, s1Graf.size)

        yMax = np.amax(np.array([np.amax(abs(s1)), np.amax(abs(s2))]))

        if esCoseno(s1, self.fSample):
            s1Graf = s1
            tGraf = t
        else:
            tGraf = np.linspace(-0.001 * tSimb, tSimb * 1.001, s1Graf.size)

        self.axs1 = self.figure_simbGraph.add_subplot(211)
        self.axs1.plot(tGraf, s1Graf, 'r', linewidth=3)
        self.axs1.set_title("Símbolo 1", fontsize=self.sizeHeight*0.015, weight = "bold")
        self.axs1.set_ylabel('Amplitud')
        self.axs1.set_ylim([-yMax * 1.2, yMax * 1.2])
        self.axs1.grid()
        maX = np.amax(abs(s1Graf))
        self.axs1.annotate(f'Amplitud: {format(maX, "<10.4f")}', (10, 10 ), xycoords='axes pixels',weight='bold',fontsize=self.sizeHeight*0.01)

        s1Graf = np.concatenate((zeroes, s1, zeroes))

        if esCoseno(s2, self.fSample):
            s2Graf = s2
            tGraf = t
        else:
            tGraf = np.linspace(-0.001 * tSimb, tSimb * 1.001, s1Graf.size)

        self.axs2 = self.figure_simbGraph.add_subplot(212)
        self.axs2.plot(tGraf, s2Graf, 'r', linewidth=3)
        self.axs2.set_title("Símbolo 2", fontsize=self.sizeHeight*0.015, weight = "bold")
        self.axs2.set_xlabel('Tiempo [seg]', fontsize=self.sizeHeight*0.01)
        self.axs2.set_ylabel('Amplitud')
        self.axs2.set_ylim([-yMax * 1.2, yMax * 1.2])
        self.axs2.grid()
        maX = np.amax(abs(s2Graf))
        self.axs2.annotate(f'Amplitud: {format(maX, "<10.4f")}', (10, 10 ), xycoords='axes pixels',weight='bold',fontsize=self.sizeHeight*0.01)

        self.canvas_simbGraph.draw()

    def graficarBases(self, s1, s2, tSimb, t):
        """
        Función que realiza la gráfica de las bases en la GUI.

        :param s1: Base U1
        :param s2: Base U2
        :param tSimb: Tiempo de Símbolo
        :param t: Vector tiempo
        """

        self.figure_basesGraph.clear()

        zeroes = np.zeros(1)
        s1Graf = np.concatenate((zeroes, s1, zeroes))
        s2Graf = np.concatenate((zeroes, s2, zeroes))

        tGraf = np.linspace(-0.001 * tSimb, tSimb * 1.001, s1Graf.size)

        yMax = np.amax(np.array([np.amax(abs(s1)), np.amax(abs(s2))]))

        if esCoseno(s1, self.fSample):
            s1Graf = s1
            tGraf = t
        else:
            tGraf = np.linspace(-0.001 * tSimb, tSimb * 1.001, s1Graf.size)

        self.axs1 = self.figure_basesGraph.add_subplot(211)
        self.axs1.plot(tGraf, s1Graf, 'r', linewidth=3)
        self.axs1.set_title("Base 1", fontsize=self.sizeHeight*0.015, weight = "bold")
        self.axs1.set_ylabel('Amplitud')
        self.axs1.set_ylim([-yMax * 1.2, yMax * 1.2])
        self.axs1.grid()
        xmin, xmax = self.axs1.get_xlim()
        ymin, ymax = self.axs1.get_ylim()
        maX = np.amax(abs(s1Graf))

        self.axs1.annotate(f'Amplitud: {format(maX, "<10.4f")}', (xmin * 0.9, ymin * 0.9), weight='bold',fontsize=self.sizeHeight*0.01)


        s1Graf = np.concatenate((zeroes, s1, zeroes))

        if esCoseno(s2, self.fSample):
            s2Graf = s2
            tGraf = t
        else:
            tGraf = np.linspace(-0.001 * tSimb, tSimb * 1.001, s1Graf.size)

        self.axs2 = self.figure_basesGraph.add_subplot(212)
        self.axs2.plot(tGraf, s2Graf, 'r', linewidth=3)
        self.axs2.set_title("Base 2", fontsize=self.sizeHeight*0.015, weight = "bold")
        self.axs2.set_xlabel('Tiempo [seg]', fontsize=self.sizeHeight*0.01)
        self.axs2.set_ylabel('Amplitud')
        self.axs2.set_ylim([-yMax * 1.2, yMax * 1.2])
        self.axs2.grid()

        maX = np.amax(abs(s2Graf))
        if maX != 0:
            xmin, xmax = self.axs2.get_xlim()
            ymin, ymax = self.axs2.get_ylim()
            self.axs2.annotate(f'Amplitud: {format(maX, "<10.4f")}', (xmin * 0.9, ymin * 0.9), weight='bold',fontsize=self.sizeHeight*0.01)

        self.canvas_basesGraph.draw()

    def graficarConstAntes(self, s1, s2, U1, U2, tSimb):
        """
        Función que realiza la gráfica de la constelación antes del canal en la GUI.

        :param s1: Símbolo 1
        :param s2: Símbolo 2
        :param U1: Base U1
        :param U2: Base U2
        :param tSimb: Tiempo de símbolo
        :return: Devuelve las coordenadas de los símbolos.
        """
        self.figure_constACGraph.clear()

        x1 = tSimb * np.mean(np.multiply(s1, U1))
        y1 = tSimb * np.mean(np.multiply(s1, U2))
        x2 = tSimb * np.mean(np.multiply(s2, U1))
        y2 = tSimb * np.mean(np.multiply(s2, U2))
        coord = (x1, y1, x2, y2)
        coordX = np.array([x1, x2])
        coordY = np.array([y1, y2])

        ejeX = np.array([x1, x2])
        ejeY = np.array([y1, y2])

        xMax = np.amax(abs(coordX))
        yMax = np.amax(abs(coordY))

        size = [300, 300]
        z = [0, 0]

        self.ax = self.figure_constACGraph.add_subplot(111)
        self.ax.scatter(ejeX, ejeY, s=size, c=z, norm=plt.Normalize(vmin=0, vmax=1), cmap="inferno")
        self.ax.set_xlabel('U1')
        self.ax.set_ylabel('U2')
        self.ax.set_xlim([-xMax * 1.2, xMax * 1.2])
        self.ax.grid()

        if yMax != 0:
            self.ax.set_ylim([-yMax * 1.2, yMax * 1.2])

        ymin, ymax = self.ax.get_ylim()
        xmin, xmax = self.ax.get_xlim()

        self.ax.annotate("",
                         xy=(xmax, 0), xycoords='data',
                         xytext=(xmin, 0), textcoords='data',
                         arrowprops=dict(arrowstyle="->",
                                         connectionstyle="arc3"),
                         )
        self.ax.annotate("",
                         xy=(0, ymax), xycoords='data',
                         xytext=(0, ymin), textcoords='data',
                         arrowprops=dict(arrowstyle="->",
                                         connectionstyle="arc3"),
                         )

        self.ax.text(x1, y1, 'S1',
                     horizontalalignment='center',
                     verticalalignment='center',
                     c='w'
                     )
        self.ax.text(x2, y2, 'S2',
                     horizontalalignment='center',
                     verticalalignment='center',
                     c='w'
                     )

        self.canvas_constACGraph.draw()

        return coord

    def graficarConstDespues(self, senal, U1, U2, tSimb, coord, nMuestrasSimb):
        """
        Función que realiza la gráfica de la constelación después del canal en la GUI.

        :param senal: Arreglo con la señal con ruido.
        :param U1: Base U1
        :param U2: Base U2
        :param tSimb: Tiempo de símbolo
        :param coord: Vector con las coordenadas de los símbolos
        :param nMuestrasSimb: Número de muestras en cada símbolo
        :return: DetU1 y DetU2: vectores con las proyecciones de los símbolos con ruido sobre las bases.
        """
        self.figure_constDCGraph.clear()

        detU1 = np.empty(self.nTotalSimb)
        detU2 = np.empty(self.nTotalSimb)

        base2Cero = False
        if (U2 == np.zeros(U2.size)).all() == True:
            U2 = U2 + np.random.normal(0, 0.0000000001, U2.size)
            # U2 = U2
            base2Cero = True

        for i in range(self.nTotalSimb):
            detU1[i] = tSimb * np.mean(np.multiply(senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)], U1))
            detU2[i] = tSimb * np.mean(np.multiply(senal[nMuestrasSimb * i:nMuestrasSimb * (i + 1)], U2))

        xMax = np.amax(abs(detU1))
        yMax = np.amax(abs(detU2))

        x1, y1, x2, y2 = coord

        coordX = np.array([x1, x2])
        coordY = np.array([y1, y2])

        ejeX = np.concatenate((detU1, coordX))
        ejeY = np.concatenate((detU2, coordY))

        size = np.concatenate((np.full((1, detU1.size), 5), np.full((1, 2), 300)), axis=1)
        z = np.concatenate((np.full((1, detU1.size), 0.5), np.full((1, 2), 0)), axis=1)

        self.ax = self.figure_constDCGraph.add_subplot(111)
        self.ax.scatter(ejeX, ejeY, s=size, c=z, norm=plt.Normalize(vmin=0, vmax=1), cmap="inferno")
        self.ax.set_xlabel('U1')
        self.ax.set_ylabel('U2')
        self.ax.set_xlim([-xMax * 1.2, xMax * 1.2])
        self.ax.grid()

        if yMax != 0:
            if base2Cero == False:
                self.ax.set_ylim([-yMax * 1.2, yMax * 1.2])

        ymin, ymax = self.ax.get_ylim()
        xmin, xmax = self.ax.get_xlim()

        self.ax.annotate("",
                         xy=(xmax, 0), xycoords='data',
                         xytext=(xmin, 0), textcoords='data',
                         arrowprops=dict(arrowstyle="->",
                                         connectionstyle="arc3"),
                         )
        self.ax.annotate("",
                         xy=(0, ymax), xycoords='data',
                         xytext=(0, ymin), textcoords='data',
                         arrowprops=dict(arrowstyle="->",
                                         connectionstyle="arc3"),
                         )

        self.ax.text(x1, y1, 'S1',
                     horizontalalignment='center',
                     verticalalignment='center',
                     c='w'
                     )
        self.ax.text(x2, y2, 'S2',
                     horizontalalignment='center',
                     verticalalignment='center',
                     c='w'
                     )

        self.canvas_constDCGraph.draw()

        return (detU1, detU2)

    def graficarSenalTiempo(self, senal, senalRuido, senalDet, tSimb, primerError, t2, senalBBPB):
        """
        Función que realiza la gráfica de la señal en tiempo en la GUI.

        :param senal: Arreglo con la señal original.
        :param senalRuido: Arreglo con la señal + ruido.
        :param senalDet: Arreglo con la señal detectada con el detector óptimo.
        :param tSimb: Tiempo de símbolo.
        :param primerError: Posición en el que ocurre el primer error.
        :param t2: Vector tiempo
        :param senalBBPB: Flag que indica si la señal es pasabanda o bandabase.
        """
        self.figure_senalTiempoGraph.clear()

        if primerError > 50:
            senal = senal[int((primerError - 50) * tSimb * self.fSample):int((primerError + 50) * tSimb * self.fSample)]
            senalRuido = senalRuido[int((primerError - 50) * tSimb * self.fSample):int((primerError + 50) * tSimb * self.fSample)]
            senalDet = senalDet[int((primerError - 50) * tSimb * self.fSample):int((primerError + 50) * tSimb * self.fSample)]
            t2 = t2[int((primerError - 50) * tSimb * self.fSample):int((primerError + 50) * tSimb * self.fSample)]
        else:
            senal = senal[0:int(100 * tSimb * self.fSample)]
            senalDet = senalDet[0:int(100 * tSimb * self.fSample)]
            senalRuido = senalRuido[0:int(100 * tSimb * self.fSample)]
            t2 = t2[0:int(100 * tSimb * self.fSample)]

        if senalBBPB !=2:
            self.axs1 = self.figure_senalTiempoGraph.add_subplot(311)
            self.axs1.plot(t2, senal, 'r', linewidth=3)
            self.axs1.set_title('Señal', fontsize=self.sizeHeight*0.015, weight='bold')
            self.axs1.set_ylabel('Amplitud')
            # Se grafican los simbolos a partir del primer error
            self.axs1.set_xlim([tSimb * primerError, tSimb * (primerError + 15)])
            self.axs1.grid()

            self.axs2 = self.figure_senalTiempoGraph.add_subplot(312)
            self.axs2.plot(t2, senalRuido, 'r', linewidth=3)
            self.axs2.set_title('Señal + ruido', fontsize=self.sizeHeight*0.015, weight='bold')
            self.axs2.set_ylabel('Amplitud')
            self.axs2.set_xlim([tSimb * primerError, tSimb * (primerError + 15)])
            self.axs2.grid()

            self.axs3 = self.figure_senalTiempoGraph.add_subplot(313)
            self.axs3.plot(t2, senalDet, 'r', linewidth=3)
            self.axs3.set_title('Señal detectada', fontsize=self.sizeHeight*0.015, weight='bold')
            self.axs3.set_ylabel('Amplitud')
            self.axs3.set_xlim([tSimb * primerError, tSimb * (primerError + 15)])
            self.axs3.set_xlabel('S [segundos]', fontsize=self.sizeHeight*0.01)
            self.axs3.grid()
        else:
            self.axs1 = self.figure_senalTiempoGraph.add_subplot(311)
            self.axs1.plot(t2, senal, 'r')
            self.axs1.set_title('Señal', fontsize=self.sizeHeight*0.015, weight='bold')
            self.axs1.set_ylabel('Amplitud')
            # Se grafican los simbolos a partir del primer error
            self.axs1.set_xlim([tSimb * primerError, tSimb * (primerError + 8)])
            self.axs1.grid()

            self.axs2 = self.figure_senalTiempoGraph.add_subplot(312)
            self.axs2.plot(t2, senalRuido, 'r')
            self.axs2.set_title('Señal + ruido', fontsize=self.sizeHeight*0.015, weight='bold')
            self.axs2.set_ylabel('Amplitud')
            self.axs2.set_xlim([tSimb * primerError, tSimb * (primerError + 8)])
            self.axs2.grid()

            self.axs3 = self.figure_senalTiempoGraph.add_subplot(313)
            self.axs3.plot(t2, senalDet, 'r')
            self.axs3.set_title('Señal detectada', fontsize=self.sizeHeight*0.015, weight='bold')
            self.axs3.set_ylabel('Amplitud')
            self.axs3.set_xlim([tSimb * primerError, tSimb * (primerError + 8)])
            self.axs3.set_xlabel('S [segundos]', fontsize=self.sizeHeight*0.01)
            self.axs3.grid()

        self.canvas_senalTiempoGraph.draw()

    def graficarSenalFreq(self,senal, t2, fSimb, frecuencias, senalBBPB, anchoBanda):
        """
        Función que realiza la gráfica de la señal en frecuencia en la GUI.

        :param senal: Arreglo con la señal.
        :param t2: Vector tiempo.
        :param fSimb: Frecuencia de símbolo.
        :param frecuencias: Vector con las frecuencias de portadora de los símbolos.
        :param senalBBPB: Flag que indica si la señal es pasabanda o bandabase.
        :param anchoBanda: Valor del ancho de banda práctico de la señal.
        """
        self.figure_senalFreqGraph.clear()

        frecuencias = [*set(frecuencias)]  # quita los elementos repetidos
        for i in range(len(frecuencias)):
            if frecuencias[i] == 0:
                frecuencias.pop(i)
                break

        frecuencias.sort()
        numFreq = len(frecuencias) #Numero de frecuencias en la señal. Solo 1 o 2 frecuencias.

        n = t2.size
        transf = np.fft.fftshift(np.fft.fft(senal, n))
        DEP = transf * np.conj(transf) / n
        DEP = DEP.real
        DEP = (DEP) / np.amax(DEP)
        freq = np.linspace(-self.fSample / 2, self.fSample / 2, int(len(DEP)))


        delta, indexDelta = verificarDelta(DEP, senalBBPB, numFreq)

        if delta:
            sum = 0
            for i in range(500):
                sum = sum + DEP[indexDelta + i]
            prom = sum / 500

        DEP = DEP[int((n / 2) - ((200 * n) / 1500)):int((n / 2) + ((200 * n) / 1500))]
        freq = freq[int((n / 2) - ((200 * n) / 1500)):int((n / 2) + ((200 * n) / 1500))]

        if senalBBPB == 1:
            self.axs1 = self.figure_senalFreqGraph.add_subplot(211)
            self.axs1.plot(freq, DEP, linewidth=3)
            self.axs1.set_title('DEP Gráfica 1')
            self.axs1.set_ylabel('Amplitud')
            if delta:
                self.axs1.set_ylim([-0.001, prom * 10])
            self.axs1.set_xlim([-100, 100])
            self.axs1.grid()

            self.axs2 = self.figure_senalFreqGraph.add_subplot(212)
            self.axs2.plot(freq, DEP, linewidth=3)
            self.axs2.set_title('DEP Gráfica 2')
            self.axs2.set_xlabel('Frecuencia [Hz]', fontsize=self.sizeHeight*0.01)
            self.axs2.set_ylabel('Amplitud')
            if delta:
                self.axs2.set_ylim([-1e-04, prom])
            self.axs2.set_xlim([-anchoBanda * 4, anchoBanda * 4])
            self.axs2.grid()

        else:
            if numFreq == 1:
                self.axs1 = self.figure_senalFreqGraph.add_subplot(211)
                self.axs1.set_title('DEP Gráfica 1')
                self.axs1.plot(freq, DEP, linewidth=3)
                self.axs1.set_ylabel('Amplitud')
                self.axs1.set_xlim([-frecuencias[0] - 100, frecuencias[0] + 100])
                if delta:
                    self.axs1.set_ylim([-0.001, prom * 10])
                self.axs1.grid()

                self.axs2 = self.figure_senalFreqGraph.add_subplot(212)
                self.axs2.plot(freq, DEP, linewidth=3)
                self.axs2.set_title('DEP Gráfica 2')
                self.axs2.set_xlabel('Frecuencia [Hz]', fontsize=self.sizeHeight*0.01)
                self.axs2.set_ylabel('Amplitud')
                self.axs2.set_xlim([frecuencias[0] - (anchoBanda * 4), frecuencias[0] + (anchoBanda * 4)])
                if delta:
                    self.axs2.set_ylim([-1e-04, prom])
                self.axs2.grid()
            else:
                self.axs1 = self.figure_senalFreqGraph.add_subplot(211)
                self.axs1.set_title('DEP Gráfica 1')
                self.axs1.plot(freq, DEP, linewidth=3)
                self.axs1.set_ylabel('Amplitud')
                self.axs1.set_xlim([-frecuencias[1] - 100, frecuencias[1] + 100])
                if delta:
                    self.axs1.set_ylim([-0.001, prom * 10])
                self.axs1.grid()

                self.axs2 = self.figure_senalFreqGraph.add_subplot(212)
                self.axs2.plot(freq, DEP, linewidth=3)
                self.axs2.set_title('DEP Gráfica 2')
                self.axs2.set_xlabel('Frecuencia [Hz]', fontsize=self.sizeHeight*0.01)
                self.axs2.set_ylabel('Amplitud')
                self.axs2.set_xlim([frecuencias[0] - (anchoBanda * 4), frecuencias[0] + (anchoBanda * 4)])
                if delta:
                    self.axs2.set_ylim([-1e-04, prom])
                self.axs2.grid()

        self.canvas_senalFreqGraph.draw()

    def graficarProbError(self,E, X, Y, etaGraf, peGraf):
        """
        Función que realiza la gráfica de la señal en frecuencia en la GUI.

        :param E: Energía de la señal.
        :param X: Valor de Eta del punto de operación (eje X en la gráfica)
        :param Y: Valor de la Probabilidad de Error del punto de operación (eje Y en la gráfica)
        :param etaGraf: Vector con los valores de Eta para la gráfica.
        :param peGraf: Vector con los valores de Probabilidad de Error en la gráfica.
        """
        self.figure_PeGraph.clear()

        ejeX = 10 * np.log10(E / etaGraf)
        X = 10 * np.log10(E / X)
        ejeY = peGraf

        self.axs1 = self.figure_PeGraph.add_subplot(111)
        self.axs1.semilogy(ejeX, ejeY, X, Y, 'o')
        self.axs1.set_xlabel('10log(E/eta)')
        self.axs1.set_ylabel('Pe')
        self.axs1.annotate('Pe Obtenida', (X + 0.25, Y))
        self.axs1.annotate(f'Punto Pe: ({format(X, "<6.4f")}, {format(Y, "<6.4f")})', (10, 10 ), xycoords='axes pixels',weight='bold',fontsize=self.sizeHeight*0.01)

        self.axs1.grid()

        self.canvas_PeGraph.draw()

    def mousePressEvent(self, e):
        """
        Actualizar mensaje de espera.

        :param e: evento del mouse.
        """
        self.SimularButton.setStatusTip('Los resultados pueden tomar tiempo')

    def mouseDoubleClickEvent(self, e):
        """
        Actualizar mensaje de espera.

        :param e: evento del mouse.
        """
        self.SimularButton.setStatusTip('Los resultados pueden tomar tiempo')

    def simular(self):
        """
        Método que ejecuta todos los resultados de la simulación.
        """

        try:
            self.SimularButton.setStatusTip('')
            self.statusbar.clearMessage()
            self.statusbar.showMessage('Resultados listos!',5000)

            # Datos U1
            tipoOnda_Opcion1 = self.tipoSenal(self.cbSimb1.currentText())
            tipoOnda1 = tipoOnda_Opcion1

            if tipoOnda_Opcion1 ==4 or tipoOnda_Opcion1==6:
                frecuencia1 = self.hsFreqS1.value()
            else:
                frecuencia1 = 0

            fase1 = convertirFase(self.leFaseS1.text())

            if tipoOnda_Opcion1 == 5 or tipoOnda_Opcion1 == 6:
                t1s1, t2s1, tipoOnda1 = self.inicioDuracion(self.cbT1S1.currentText(), self.cbT2S1.currentText())
            else:
                t1s1, t2s1 = 0, 0

            # Datos U2
            tipoOnda_Opcion2 = self.tipoSenal(self.cbSimb2.currentText())
            tipoOnda2 = tipoOnda_Opcion2

            if tipoOnda_Opcion2 ==4 or tipoOnda_Opcion2==6:
                frecuencia2 = self.hsFreqS2.value()
            else:
                frecuencia2 = 0

            fase2 = convertirFase(self.leFaseS2.text())

            if tipoOnda_Opcion2 == 5 or tipoOnda_Opcion2 == 6:
                t1s2, t2s2, tipoOnda2 = self.inicioDuracion(self.cbT1S2.currentText(), self.cbT2S2.currentText())
            else:
                t1s2, t2s2 = 0, 0

            #Datos de los simbolos
            xS1 = float(self.XS1.text())
            yS1 = float(self.YS1.text())

            xS2 = float(self.XS2.text())
            yS2 = float(self.YS2.text())


            # Datos de la señal
            tSimb = self.sbTsimb.value()
            fSimb = 1/tSimb
            nMuestrasSimb = int(self.fSample * tSimb)
            t = np.linspace(0, tSimb, nMuestrasSimb)
            nroSimb = 2

            U1 = bases(t, nMuestrasSimb, tSimb, tipoOnda_Opcion1, frecuencia1, fase1, t1s1, t2s1, self.fSample)
            U2 = bases(t, nMuestrasSimb, tSimb, tipoOnda_Opcion2, frecuencia2, fase2, t1s2, t2s2, self.fSample)

            s1 = (xS1 * U1) + (yS1 * U2)
            s2 = (xS2 * U1) + (yS2 * U2)

            simbsIguales = self.chequearSimbsIguales(s1,s2)

            if simbsIguales:
                self.mensaje_errorSimbsIguales()

            # Nivel de Ruido
            if self.cbNivelRuido.currentText() == "Bajo":
                nivelRuido = 1
            elif self.cbNivelRuido.currentText() == "Medio":
                nivelRuido = 2
            else:
                nivelRuido = 3

            simbolos_senal = (s1, s2,0,0)
            tipoOndas = (tipoOnda1, tipoOnda2,0,0)
            frecuencias = (frecuencia1, frecuencia2,0,0)
            datos = (self.fSample, nMuestrasSimb, t, nroSimb, tSimb, nivelRuido, self.nTotalSimb)

            senal, t2, bits = senalAleatoria(s1,s2,0,0,tSimb,nMuestrasSimb,nroSimb, self.nTotalSimb)

            self.graficarSimb(s1, s2, tSimb, t)
            self.graficarBases(U1, U2, tSimb, t)

            coord = self.graficarConstAntes(s1, s2, U1, U2, tSimb)

            potenciaSenal = np.mean(np.multiply(senal, senal))
            E = potenciaSenal * tSimb

            X, Y, etaGraf, peGraf, dmin, nDmin = obtenerEta(coord, nroSimb, E, self.nTotalSimb, nivelRuido)
            senalRuido = senal + (math.sqrt(0.5 * self.fSample * X)) * np.random.normal(0, 1, senal.size)

            detU1, detU2 = self.graficarConstDespues(senalRuido, U1, U2, tSimb, coord, nMuestrasSimb)

            senalDet, rec = deteccionDistancia(coord, s1, s2, 0, 0, nroSimb, detU1, detU2, self.nTotalSimb, nMuestrasSimb)

            pe, primerError, cont = calcularPe(self.nTotalSimb, rec, bits)

            senalBBPB = senalBandabasePasabanda(s1,s2,0,0,nroSimb,self.fSample,nMuestrasSimb)

            self.graficarSenalTiempo(senal, senalRuido, senalDet,tSimb, primerError, t2, senalBBPB)

            anchoBanda = calcularAnchoBanda(tipoOndas,fSimb,nroSimb)

            self.graficarSenalFreq(senal, t2, fSimb, frecuencias, senalBBPB, anchoBanda)

            self.graficarProbError(E, X, Y, etaGraf, peGraf)

            ortogonalidad, polaridad, proporcionalidad, energia, numCiclos = resultadosNumericos(simbolos_senal,
                                                                                                 nroSimb, nMuestrasSimb,
                                                                                                 self.fSample, fSimb, (
                                                                                                 tipoOnda_Opcion1,
                                                                                                 tipoOnda_Opcion2, 0,
                                                                                                 0), frecuencias)

            o_s1s2 = ortogonalidad
            p_s1s2 = polaridad
            pp_s1s2 = proporcionalidad

            E1,E2 = energia
            numCiclosEnterosS1, numCiclosEnterosS2 = numCiclos

            #Ortogonalidad de las bases
            factorLambda = factorCorrelacion(1, 1, U1, U2, nMuestrasSimb, self.fSample)

            if math.isclose(factorLambda, 0, abs_tol=0.01):
                self.O12_4.setPixmap(QtGui.QPixmap("UIs/check.png"))

                # Coordenadas S1
                if xS1.is_integer():
                    self.leXS1.setText(str(int(xS1)))
                else:
                    self.leXS1.setText(format(xS1, "10.3f"))

                if yS1.is_integer():
                    self.leYS1.setText(str(int(yS1)))
                else:
                    self.leYS1.setText(format(yS1, "10.3f"))

                # Coordenadas S2
                if xS2.is_integer():
                    self.leXS2.setText(str(int(xS2)))
                else:
                    self.leXS2.setText(format(xS2, "10.3f"))

                if yS2.is_integer():
                    self.leYS2.setText(str(int(yS2)))
                else:
                    self.leYS2.setText(format(yS2, "10.3f"))
            else:
                x1, y1, x2, y2 = coord

                # Coordenadas S1
                if x1.is_integer():
                    self.leXS1.setText(str(int(x1)))
                else:
                    self.leXS1.setText(format(x1, "10.3f"))

                if y1.is_integer():
                    self.leYS1.setText(str(int(y1)))
                else:
                    self.leYS1.setText(format(y1, "10.3f"))

                # Coordenadas S2
                if x2.is_integer():
                    self.leXS2.setText(str(int(x2)))
                else:
                    self.leXS2.setText(format(x2, "10.3f"))

                if y2.is_integer():
                    self.leYS2.setText(str(int(y2)))
                else:
                    self.leYS2.setText(format(y2, "10.3f"))

                self.O12_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.mensaje_errorBases()

            if o_s1s2:
                self.O12.setPixmap(QtGui.QPixmap("UIs/check.png"))
            else:
                self.O12.setPixmap(QtGui.QPixmap("UIs/x.png"))

            if p_s1s2:
                self.O12_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
            else:
                self.O12_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

            if pp_s1s2:
                self.O12_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
            else:
                self.O12_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

            if E1.is_integer():
                self.E1.setText(str(int(E1)))
            else:
                self.E1.setText(format(E1,"10.3f"))

            if E2.is_integer():
                self.E2.setText(str(int(E2)))
            else:
                self.E2.setText(format(E2,"10.3f"))

            if tipoOnda_Opcion1 == 4 or tipoOnda_Opcion1 == 6:
                if numCiclosEnterosS1:
                    self.NumCiclosS1.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.NumCiclosS1.setPixmap(QtGui.QPixmap("UIs/x.png"))
            else:
                self.NumCiclosS1.setPixmap(QtGui.QPixmap("UIs/Empty.png"))


            if tipoOnda_Opcion2 == 4 or tipoOnda_Opcion2 == 6:
                if numCiclosEnterosS2:
                    self.NumCiclosS2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.NumCiclosS2.setPixmap(QtGui.QPixmap("UIs/x.png"))
            else:
                self.NumCiclosS2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

            #Dmin
            if dmin.is_integer():
                self.leDmin.setText(str(int(dmin)))
            else:
                self.leDmin.setText(format(dmin,"10.3f"))

            #Potencia de la señal
            if potenciaSenal.is_integer():
                self.lePotencia.setText(str(int(potenciaSenal)))
            else:
                self.lePotencia.setText(format(potenciaSenal, "10.3f"))

            #Energia de la señal
            if E.is_integer():
                self.leEnergia.setText(str(int(E)))
            else:
                self.leEnergia.setText(format(E, "10.3f"))

            #Eta
            if X.is_integer():
                self.leEta.setText(str(int(X)))
            else:
                self.leEta.setText(format(X, "10.3f"))


            #Num de simbolos errados

            self.leSimbErrados.setText(str(int(cont)))

            #Ancho de banda práctico
            if senalBBPB == 1:
                if anchoBanda.is_integer():
                    self.leBW.setText(str(int(anchoBanda)))
                else:
                    self.leBW.setText(format(anchoBanda, "10.3f"))
            else:
                anchoBanda = 2*anchoBanda
                if anchoBanda.is_integer():
                    self.leBW.setText(str(int(anchoBanda)))
                else:
                    self.leBW.setText(format(anchoBanda, "10.3f"))

            self.leNDmin.setText(str((nDmin)))

            self.leNumSimb.setText(str(nroSimb))

            #Dmin
            if dmin.is_integer():
                self.leDminPe.setText(str(int(dmin)))
            else:
                self.leDminPe.setText(format(dmin,"10.3f"))

            if X.is_integer():
                self.leEtaPe.setText(str(int(X)))
            else:
                self.leEtaPe.setText(format(X, "10.3f"))


            self.lePeCota.setText(format(Y, "10.4f"))

            self.leSimbErradosPe.setText(str(int(cont)))

            self.leSimbTotalesPe.setText(str(self.nTotalSimb))

            self.lePeSimbErrados.setText(format(pe, "10.4f"))

        except ValueError:
            traceback.print_exc()
            error = traceback.format_exc()
            self.mensaje_error1(error)

        except:
            traceback.print_exc()
            error = traceback.format_exc()
            self.mensaje_error2(error)