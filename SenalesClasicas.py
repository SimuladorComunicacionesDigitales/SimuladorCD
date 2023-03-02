"""
Esta clase contiene la ventana de resultados para las Señales Clásicas.
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


class SenalesClasicas(QMainWindow):
    def __init__(self, widget, frameSizeWidth, frameSizeHeight, fSample, nTotalSimb,sizeHeight):
        """
        Método constructor donde se definen los elementos de la GUI.

        :param widget: QStackedWidget del simulador.
        :param frameSizeWidth: Ancho del Frame que contiene las gráficas.
        :param frameSizeHeight: Largo del Frame que contiene las gráficas.
        :param fSample: Frecuencia de muestreo.
        :param nTotalSimb: Número total de símbolos que compone la señal.
        :param sizeHeight: Alto de la Pantalla
        """
        super(SenalesClasicas, self).__init__()
        loadUi("UIs\SenalesClasicas.ui", self)

        self.SimularButton.setStatusTip('Los resultados pueden tomar tiempo')
        self.setMouseTracking(True)
        
        self.fSample = fSample
        self.nTotalSimb = nTotalSimb
        self.widget = widget
        self.sizeHeight = sizeHeight


        self.widget.insertWidget(1, self)

        self.SimbyBasesFrame.setMinimumSize(frameSizeWidth, frameSizeHeight)
        self.frame_77.setMinimumSize(frameSizeWidth, frameSizeHeight)
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

                                            QScrollBar:horizontal{
                                            background-color: rgb(204, 205, 206);
                                            width: 15px;
                                            }

                                            QScrollBar::handle:horizontal{
                                            background-color: rgb(255, 177, 64);
                                            width: 15px;
                                            }

                                            QScrollBar::handle:horizontal:hover{
                                            background-color: rgb(255, 202, 128);
                                            }

                                            QScrollBar::add-line:horizontal {
                                                 background: rgb(255, 177, 64);
                                            }

                                            QScrollBar::sub-line:horizontal {
                                                 background: rgb(255, 177, 64);
                                            }

                                            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                                                 background: none;
                                            }
                                            """)

        self.sbTsimb.valueChanged.connect(self.spinBoxInt)
        self.hsTsimb.valueChanged.connect(self.sliderFloat)
        self.leAmplitud.setText("1")

        self.leFsimb.setReadOnly(True)
        self.leFsimb.setText("10")

        self.hsFreq1.setEnabled(False)
        self.hsFreq1.setStyleSheet("""
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
        self.hsFreq2.setEnabled(False)
        self.hsFreq2.setStyleSheet("""
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
        self.sbFreq1.setEnabled(False)
        self.sbFreq1.setStyleSheet("""QSpinBox{
                                                    background-color: rgb(217, 217, 217);
                                                    qproperty-alignment: AlignCenter;
                                                }       
                                            """)
        self.sbFreq2.setEnabled(False)
        self.sbFreq2.setStyleSheet("""QSpinBox{
                                                            background-color: rgb(217, 217, 217);
                                                            qproperty-alignment: AlignCenter;
                                                        }       
                                                    """)

        self.cbTipoSenal.currentTextChanged.connect(self.hideData)

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

        self.O12_2.setScaledContents(True)
        self.O13_2.setScaledContents(True)
        self.O14_2.setScaledContents(True)
        self.O15_2.setScaledContents(True)
        self.O16_2.setScaledContents(True)
        self.O17_2.setScaledContents(True)
        self.O18_2.setScaledContents(True)
        self.O19_2.setScaledContents(True)
        self.O110_2.setScaledContents(True)
        self.O111_2.setScaledContents(True)
        self.O112_2.setScaledContents(True)
        self.O113_2.setScaledContents(True)
        self.O114_2.setScaledContents(True)
        self.O115_2.setScaledContents(True)
        self.O116_2.setScaledContents(True)

        self.O23_2.setScaledContents(True)
        self.O24_2.setScaledContents(True)
        self.O25_2.setScaledContents(True)
        self.O26_2.setScaledContents(True)
        self.O27_2.setScaledContents(True)
        self.O28_2.setScaledContents(True)
        self.O29_2.setScaledContents(True)
        self.O210_2.setScaledContents(True)
        self.O211_2.setScaledContents(True)
        self.O212_2.setScaledContents(True)
        self.O213_2.setScaledContents(True)
        self.O214_2.setScaledContents(True)
        self.O215_2.setScaledContents(True)
        self.O216_2.setScaledContents(True)

        self.O34_2.setScaledContents(True)
        self.O35_2.setScaledContents(True)
        self.O36_2.setScaledContents(True)
        self.O37_2.setScaledContents(True)
        self.O38_2.setScaledContents(True)
        self.O39_2.setScaledContents(True)
        self.O310_2.setScaledContents(True)
        self.O311_2.setScaledContents(True)
        self.O312_2.setScaledContents(True)
        self.O313_2.setScaledContents(True)
        self.O314_2.setScaledContents(True)
        self.O315_2.setScaledContents(True)
        self.O316_2.setScaledContents(True)

        self.O45_2.setScaledContents(True)
        self.O46_2.setScaledContents(True)
        self.O47_2.setScaledContents(True)
        self.O48_2.setScaledContents(True)
        self.O49_2.setScaledContents(True)
        self.O410_2.setScaledContents(True)
        self.O411_2.setScaledContents(True)
        self.O412_2.setScaledContents(True)
        self.O413_2.setScaledContents(True)
        self.O414_2.setScaledContents(True)
        self.O415_2.setScaledContents(True)
        self.O416_2.setScaledContents(True)

        self.O56_2.setScaledContents(True)
        self.O57_2.setScaledContents(True)
        self.O58_2.setScaledContents(True)
        self.O59_2.setScaledContents(True)
        self.O510_2.setScaledContents(True)
        self.O511_2.setScaledContents(True)
        self.O512_2.setScaledContents(True)
        self.O513_2.setScaledContents(True)
        self.O514_2.setScaledContents(True)
        self.O515_2.setScaledContents(True)
        self.O516_2.setScaledContents(True)

        self.O67_2.setScaledContents(True)
        self.O68_2.setScaledContents(True)
        self.O69_2.setScaledContents(True)
        self.O610_2.setScaledContents(True)
        self.O611_2.setScaledContents(True)
        self.O612_2.setScaledContents(True)
        self.O613_2.setScaledContents(True)
        self.O614_2.setScaledContents(True)
        self.O615_2.setScaledContents(True)
        self.O616_2.setScaledContents(True)

        self.O78_2.setScaledContents(True)
        self.O79_2.setScaledContents(True)
        self.O710_2.setScaledContents(True)
        self.O711_2.setScaledContents(True)
        self.O712_2.setScaledContents(True)
        self.O713_2.setScaledContents(True)
        self.O714_2.setScaledContents(True)
        self.O715_2.setScaledContents(True)
        self.O716_2.setScaledContents(True)

        self.O89_2.setScaledContents(True)
        self.O810_2.setScaledContents(True)
        self.O811_2.setScaledContents(True)
        self.O812_2.setScaledContents(True)
        self.O813_2.setScaledContents(True)
        self.O814_2.setScaledContents(True)
        self.O815_2.setScaledContents(True)
        self.O816_2.setScaledContents(True)

        self.O910_2.setScaledContents(True)
        self.O911_2.setScaledContents(True)
        self.O912_2.setScaledContents(True)
        self.O913_2.setScaledContents(True)
        self.O914_2.setScaledContents(True)
        self.O915_2.setScaledContents(True)
        self.O916_2.setScaledContents(True)

        self.O1011_2.setScaledContents(True)
        self.O1012_2.setScaledContents(True)
        self.O1013_2.setScaledContents(True)
        self.O1014_2.setScaledContents(True)
        self.O1015_2.setScaledContents(True)
        self.O1016_2.setScaledContents(True)

        self.O1112_2.setScaledContents(True)
        self.O1113_2.setScaledContents(True)
        self.O1114_2.setScaledContents(True)
        self.O1115_2.setScaledContents(True)
        self.O1116_2.setScaledContents(True)

        self.O1213_2.setScaledContents(True)
        self.O1214_2.setScaledContents(True)
        self.O1215_2.setScaledContents(True)
        self.O1216_2.setScaledContents(True)

        self.O1314_2.setScaledContents(True)
        self.O1315_2.setScaledContents(True)
        self.O1316_2.setScaledContents(True)

        self.O1415_2.setScaledContents(True)
        self.O1416_2.setScaledContents(True)

        self.O1516_2.setScaledContents(True)

        self.O12_3.setScaledContents(True)
        self.O13_3.setScaledContents(True)
        self.O14_3.setScaledContents(True)
        self.O15_3.setScaledContents(True)
        self.O16_3.setScaledContents(True)
        self.O17_3.setScaledContents(True)
        self.O18_3.setScaledContents(True)
        self.O19_3.setScaledContents(True)
        self.O110_3.setScaledContents(True)
        self.O111_3.setScaledContents(True)
        self.O112_3.setScaledContents(True)
        self.O113_3.setScaledContents(True)
        self.O114_3.setScaledContents(True)
        self.O115_3.setScaledContents(True)
        self.O116_3.setScaledContents(True)

        self.O23_3.setScaledContents(True)
        self.O24_3.setScaledContents(True)
        self.O25_3.setScaledContents(True)
        self.O26_3.setScaledContents(True)
        self.O27_3.setScaledContents(True)
        self.O28_3.setScaledContents(True)
        self.O29_3.setScaledContents(True)
        self.O210_3.setScaledContents(True)
        self.O211_3.setScaledContents(True)
        self.O212_3.setScaledContents(True)
        self.O213_3.setScaledContents(True)
        self.O214_3.setScaledContents(True)
        self.O215_3.setScaledContents(True)
        self.O216_3.setScaledContents(True)

        self.O34_3.setScaledContents(True)
        self.O35_3.setScaledContents(True)
        self.O36_3.setScaledContents(True)
        self.O37_3.setScaledContents(True)
        self.O38_3.setScaledContents(True)
        self.O39_3.setScaledContents(True)
        self.O310_3.setScaledContents(True)
        self.O311_3.setScaledContents(True)
        self.O312_3.setScaledContents(True)
        self.O313_3.setScaledContents(True)
        self.O314_3.setScaledContents(True)
        self.O315_3.setScaledContents(True)
        self.O316_3.setScaledContents(True)

        self.O45_3.setScaledContents(True)
        self.O46_3.setScaledContents(True)
        self.O47_3.setScaledContents(True)
        self.O48_3.setScaledContents(True)
        self.O49_3.setScaledContents(True)
        self.O410_3.setScaledContents(True)
        self.O411_3.setScaledContents(True)
        self.O412_3.setScaledContents(True)
        self.O413_3.setScaledContents(True)
        self.O414_3.setScaledContents(True)
        self.O415_3.setScaledContents(True)
        self.O416_3.setScaledContents(True)

        self.O56_3.setScaledContents(True)
        self.O57_3.setScaledContents(True)
        self.O58_3.setScaledContents(True)
        self.O59_3.setScaledContents(True)
        self.O510_3.setScaledContents(True)
        self.O511_3.setScaledContents(True)
        self.O512_3.setScaledContents(True)
        self.O513_3.setScaledContents(True)
        self.O514_3.setScaledContents(True)
        self.O515_3.setScaledContents(True)
        self.O516_3.setScaledContents(True)

        self.O67_3.setScaledContents(True)
        self.O68_3.setScaledContents(True)
        self.O69_3.setScaledContents(True)
        self.O610_3.setScaledContents(True)
        self.O611_3.setScaledContents(True)
        self.O612_3.setScaledContents(True)
        self.O613_3.setScaledContents(True)
        self.O614_3.setScaledContents(True)
        self.O615_3.setScaledContents(True)
        self.O616_3.setScaledContents(True)

        self.O78_3.setScaledContents(True)
        self.O79_3.setScaledContents(True)
        self.O710_3.setScaledContents(True)
        self.O711_3.setScaledContents(True)
        self.O712_3.setScaledContents(True)
        self.O713_3.setScaledContents(True)
        self.O714_3.setScaledContents(True)
        self.O715_3.setScaledContents(True)
        self.O716_3.setScaledContents(True)

        self.O89_3.setScaledContents(True)
        self.O810_3.setScaledContents(True)
        self.O811_3.setScaledContents(True)
        self.O812_3.setScaledContents(True)
        self.O813_3.setScaledContents(True)
        self.O814_3.setScaledContents(True)
        self.O815_3.setScaledContents(True)
        self.O816_3.setScaledContents(True)

        self.O910_3.setScaledContents(True)
        self.O911_3.setScaledContents(True)
        self.O912_3.setScaledContents(True)
        self.O913_3.setScaledContents(True)
        self.O914_3.setScaledContents(True)
        self.O915_3.setScaledContents(True)
        self.O916_3.setScaledContents(True)

        self.O1011_3.setScaledContents(True)
        self.O1012_3.setScaledContents(True)
        self.O1013_3.setScaledContents(True)
        self.O1014_3.setScaledContents(True)
        self.O1015_3.setScaledContents(True)
        self.O1016_3.setScaledContents(True)

        self.O1112_3.setScaledContents(True)
        self.O1113_3.setScaledContents(True)
        self.O1114_3.setScaledContents(True)
        self.O1115_3.setScaledContents(True)
        self.O1116_3.setScaledContents(True)

        self.O1213_3.setScaledContents(True)
        self.O1214_3.setScaledContents(True)
        self.O1215_3.setScaledContents(True)
        self.O1216_3.setScaledContents(True)

        self.O1314_3.setScaledContents(True)
        self.O1315_3.setScaledContents(True)
        self.O1316_3.setScaledContents(True)

        self.O1415_3.setScaledContents(True)
        self.O1416_3.setScaledContents(True)

        self.O1516_3.setScaledContents(True)

        self.O12_4.setScaledContents(True)
        self.O13_4.setScaledContents(True)
        self.O14_4.setScaledContents(True)
        self.O15_4.setScaledContents(True)
        self.O16_4.setScaledContents(True)
        self.O17_4.setScaledContents(True)
        self.O18_4.setScaledContents(True)
        self.O19_4.setScaledContents(True)
        self.O110_4.setScaledContents(True)
        self.O111_4.setScaledContents(True)
        self.O112_4.setScaledContents(True)
        self.O113_4.setScaledContents(True)
        self.O114_4.setScaledContents(True)
        self.O115_4.setScaledContents(True)
        self.O116_4.setScaledContents(True)

        self.O23_4.setScaledContents(True)
        self.O24_4.setScaledContents(True)
        self.O25_4.setScaledContents(True)
        self.O26_4.setScaledContents(True)
        self.O27_4.setScaledContents(True)
        self.O28_4.setScaledContents(True)
        self.O29_4.setScaledContents(True)
        self.O210_4.setScaledContents(True)
        self.O211_4.setScaledContents(True)
        self.O212_4.setScaledContents(True)
        self.O213_4.setScaledContents(True)
        self.O214_4.setScaledContents(True)
        self.O215_4.setScaledContents(True)
        self.O216_4.setScaledContents(True)

        self.O34_4.setScaledContents(True)
        self.O35_4.setScaledContents(True)
        self.O36_4.setScaledContents(True)
        self.O37_4.setScaledContents(True)
        self.O38_4.setScaledContents(True)
        self.O39_4.setScaledContents(True)
        self.O310_4.setScaledContents(True)
        self.O311_4.setScaledContents(True)
        self.O312_4.setScaledContents(True)
        self.O313_4.setScaledContents(True)
        self.O314_4.setScaledContents(True)
        self.O315_4.setScaledContents(True)
        self.O316_4.setScaledContents(True)

        self.O45_4.setScaledContents(True)
        self.O46_4.setScaledContents(True)
        self.O47_4.setScaledContents(True)
        self.O48_4.setScaledContents(True)
        self.O49_4.setScaledContents(True)
        self.O410_4.setScaledContents(True)
        self.O411_4.setScaledContents(True)
        self.O412_4.setScaledContents(True)
        self.O413_4.setScaledContents(True)
        self.O414_4.setScaledContents(True)
        self.O415_4.setScaledContents(True)
        self.O416_4.setScaledContents(True)

        self.O56_4.setScaledContents(True)
        self.O57_4.setScaledContents(True)
        self.O58_4.setScaledContents(True)
        self.O59_4.setScaledContents(True)
        self.O510_4.setScaledContents(True)
        self.O511_4.setScaledContents(True)
        self.O512_4.setScaledContents(True)
        self.O513_4.setScaledContents(True)
        self.O514_4.setScaledContents(True)
        self.O515_4.setScaledContents(True)
        self.O516_4.setScaledContents(True)

        self.O67_4.setScaledContents(True)
        self.O68_4.setScaledContents(True)
        self.O69_4.setScaledContents(True)
        self.O610_4.setScaledContents(True)
        self.O611_4.setScaledContents(True)
        self.O612_4.setScaledContents(True)
        self.O613_4.setScaledContents(True)
        self.O614_4.setScaledContents(True)
        self.O615_4.setScaledContents(True)
        self.O616_4.setScaledContents(True)

        self.O78_4.setScaledContents(True)
        self.O79_4.setScaledContents(True)
        self.O710_4.setScaledContents(True)
        self.O711_4.setScaledContents(True)
        self.O712_4.setScaledContents(True)
        self.O713_4.setScaledContents(True)
        self.O714_4.setScaledContents(True)
        self.O715_4.setScaledContents(True)
        self.O716_4.setScaledContents(True)

        self.O89_4.setScaledContents(True)
        self.O810_4.setScaledContents(True)
        self.O811_4.setScaledContents(True)
        self.O812_4.setScaledContents(True)
        self.O813_4.setScaledContents(True)
        self.O814_4.setScaledContents(True)
        self.O815_4.setScaledContents(True)
        self.O816_4.setScaledContents(True)

        self.O910_4.setScaledContents(True)
        self.O911_4.setScaledContents(True)
        self.O912_4.setScaledContents(True)
        self.O913_4.setScaledContents(True)
        self.O914_4.setScaledContents(True)
        self.O915_4.setScaledContents(True)
        self.O916_4.setScaledContents(True)

        self.O1011_4.setScaledContents(True)
        self.O1012_4.setScaledContents(True)
        self.O1013_4.setScaledContents(True)
        self.O1014_4.setScaledContents(True)
        self.O1015_4.setScaledContents(True)
        self.O1016_4.setScaledContents(True)

        self.O1112_4.setScaledContents(True)
        self.O1113_4.setScaledContents(True)
        self.O1114_4.setScaledContents(True)
        self.O1115_4.setScaledContents(True)
        self.O1116_4.setScaledContents(True)

        self.O1213_4.setScaledContents(True)
        self.O1214_4.setScaledContents(True)
        self.O1215_4.setScaledContents(True)
        self.O1216_4.setScaledContents(True)

        self.O1314_4.setScaledContents(True)
        self.O1315_4.setScaledContents(True)
        self.O1316_4.setScaledContents(True)

        self.O1415_4.setScaledContents(True)
        self.O1416_4.setScaledContents(True)

        self.O1516_4.setScaledContents(True)

        self.N1.setScaledContents(True)
        self.N2.setScaledContents(True)
        self.N3.setScaledContents(True)
        self.N4.setScaledContents(True)
        self.N5.setScaledContents(True)
        self.N6.setScaledContents(True)
        self.N7.setScaledContents(True)
        self.N8.setScaledContents(True)
        self.N9.setScaledContents(True)
        self.N10.setScaledContents(True)
        self.N11.setScaledContents(True)
        self.N12.setScaledContents(True)
        self.N13.setScaledContents(True)
        self.N14.setScaledContents(True)
        self.N15.setScaledContents(True)
        self.N16.setScaledContents(True)

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

        # Bits
        self.figure_bitsGraph = plt.figure()
        self.canvas_bitsGraph = FigureCanvas(self.figure_bitsGraph)
        self.toolbar_bitsGraph = NavigationToolbar(self.canvas_bitsGraph, self)

        self.verticalLayout_bitsGraph.addWidget(self.toolbar_bitsGraph)
        self.verticalLayout_bitsGraph.addWidget(self.canvas_bitsGraph)

        self.toolbar_bitsGraph.setMaximumHeight(int(frameSizeHeight * 0.06))

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

        # Botones
        # Simular
        self.SimularButton.clicked.connect(self.simular)
        # Núm Ciclos en Sinusoides
        self.NumCiclosButton.clicked.connect(self.numCiclosSinusoides_Window)
        # Atrás
        self.BackButton.clicked.connect(self.goToMenu)

    def goToMenu(self):
        """
        Navegar al menú incial
        """
        plt.close('all')
        self.widget.setCurrentIndex(0)

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
        msg.setText("Ingresó un valor inválido para la amplitud.")
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
        self.hsTsimb.setValue(int(value * 10))

        fSimb = 1 / value

        if fSimb.is_integer():
            self.leFsimb.setText(str(int(fSimb)))

        else:
            self.leFsimb.setText(format(fSimb, "10.3f"))

    def sliderFloat(self, value):
        """
        Este método actualiza el valor del SpinBox del Tiempo de Simbolo (float) con el Slider del Tiempo de Simbolo (int).
        """
        self.sbTsimb.setValue(value / 10)

    def hideData(self, tipo):
        """
        Esta función habilita o deshabilita los distintos datos a ingresar según la señal seleccionada.

        :param tipo: Opción de Señal seleccionada con el ComboBox
        """
        if tipo == "8-PSK" or tipo == "16QAM" or tipo == "QPSK":
            self.leAmplitud.setEnabled(False)
            self.leAmplitud.setStyleSheet("QLineEdit{\n"
                                          "    background-color: rgb(217, 217, 217);\n"
                                          "    border: 2px solid black;\n"
                                          "}")
            self.leAmplitud.setText('1')
        else:
            self.leAmplitud.setEnabled(True)
            self.leAmplitud.setStyleSheet("QLineEdit{\n"
                                          "    background-color: white;\n"
                                          "    border: 2px solid black;\n"
                                          "}")

        if tipo == "OOK" or tipo == "PRK" or tipo == "FSK" or tipo == "8-PSK" or tipo == "16QAM" or tipo == "QPSK":
            self.hsFreq1.setEnabled(True)
            self.hsFreq1.setStyleSheet("""
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
            self.sbFreq1.setEnabled(True)
            self.sbFreq1.setStyleSheet("""QSpinBox{
                                                            background-color: white;
                                                            qproperty-alignment: AlignCenter;
                                                        }       
                                                    """)
        else:
            self.hsFreq1.setEnabled(False)
            self.hsFreq1.setStyleSheet("""
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
            self.sbFreq1.setEnabled(False)
            self.sbFreq1.setStyleSheet("""QSpinBox{
                                                            background-color: rgb(217, 217, 217);
                                                            qproperty-alignment: AlignCenter;
                                                        }       
                                                    """)

        if tipo == "FSK":
            self.hsFreq2.setEnabled(True)
            self.hsFreq2.setStyleSheet("""
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
            self.sbFreq2.setEnabled(True)
            self.sbFreq2.setStyleSheet("""QSpinBox{
                                                            background-color: white;
                                                            qproperty-alignment: AlignCenter;
                                                        }       
                                                    """)
        else:
            self.hsFreq2.setEnabled(False)
            self.hsFreq2.setStyleSheet("""
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
            self.sbFreq2.setEnabled(False)
            self.sbFreq2.setStyleSheet("""QSpinBox{
                                                            background-color: rgb(217, 217, 217);
                                                            qproperty-alignment: AlignCenter;
                                                        }       
                                                    """)

    def limpiarIndicadores(self):
        """
        Esta función limpia todos los indicadores antes de enseñar nuevos resultados
        """
        self.O13_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O14_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O15_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O16_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O17_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O18_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O19_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O110_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O111_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O112_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O113_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O114_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O115_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O116_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O23_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O24_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O25_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O26_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O27_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O28_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O29_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O210_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O211_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O212_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O213_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O214_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O215_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O216_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O34_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O35_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O36_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O37_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O38_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O39_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O310_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O311_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O312_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O313_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O314_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O315_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O316_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O45_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O46_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O47_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O48_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O49_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O410_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O411_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O412_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O413_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O414_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O415_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O416_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O56_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O57_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O58_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O59_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O510_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O511_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O512_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O513_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O514_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O515_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O516_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O67_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O68_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O69_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O610_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O611_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O612_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O613_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O614_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O615_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O616_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O78_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O79_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O710_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O711_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O712_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O713_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O714_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O715_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O716_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O89_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O810_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O811_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O812_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O813_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O814_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O815_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O816_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O910_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O911_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O912_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O913_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O914_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O915_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O916_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1011_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1012_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1013_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1014_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1015_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1016_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1112_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1113_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1114_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1115_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1116_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1213_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1214_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1215_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1216_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1314_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1315_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1316_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1415_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1416_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1516_2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O13_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O14_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O15_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O16_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O17_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O18_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O19_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O110_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O111_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O112_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O113_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O114_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O115_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O116_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O23_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O24_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O25_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O26_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O27_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O28_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O29_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O210_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O211_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O212_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O213_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O214_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O215_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O216_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O34_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O35_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O36_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O37_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O38_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O39_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O310_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O311_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O312_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O313_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O314_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O315_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O316_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O45_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O46_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O47_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O48_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O49_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O410_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O411_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O412_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O413_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O414_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O415_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O416_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O56_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O57_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O58_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O59_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O510_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O511_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O512_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O513_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O514_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O515_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O516_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O67_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O68_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O69_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O610_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O611_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O612_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O613_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O614_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O615_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O616_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O78_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O79_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O710_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O711_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O712_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O713_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O714_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O715_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O716_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O89_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O810_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O811_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O812_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O813_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O814_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O815_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O816_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O910_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O911_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O912_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O913_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O914_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O915_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O916_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1011_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1012_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1013_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1014_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1015_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1016_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1112_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1113_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1114_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1115_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1116_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1213_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1214_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1215_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1216_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1314_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1315_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1316_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1415_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1416_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1516_3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O13_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O14_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O15_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O16_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O17_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O18_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O19_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O110_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O111_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O112_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O113_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O114_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O115_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O116_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O23_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O24_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O25_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O26_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O27_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O28_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O29_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O210_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O211_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O212_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O213_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O214_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O215_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O216_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O34_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O35_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O36_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O37_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O38_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O39_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O310_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O311_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O312_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O313_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O314_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O315_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O316_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O45_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O46_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O47_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O48_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O49_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O410_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O411_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O412_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O413_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O414_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O415_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O416_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O56_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O57_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O58_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O59_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O510_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O511_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O512_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O513_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O514_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O515_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O516_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O67_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O68_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O69_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O610_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O611_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O612_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O613_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O614_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O615_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O616_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O78_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O79_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O710_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O711_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O712_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O713_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O714_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O715_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O716_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O89_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O810_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O811_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O812_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O813_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O814_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O815_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O816_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O910_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O911_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O912_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O913_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O914_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O915_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O916_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1011_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1012_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1013_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1014_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1015_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1016_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1112_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1113_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1114_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1115_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1116_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1213_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1214_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1215_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1216_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1314_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1315_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1316_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1415_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.O1416_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.O1516_4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.N3.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.N4.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.N5.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.N6.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.N7.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.N8.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.N9.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.N10.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.N11.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.N12.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.N13.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.N14.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.N15.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
        self.N16.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

        self.E3.setText("")
        self.E4.setText("")
        self.E5.setText("")
        self.E6.setText("")
        self.E7.setText("")
        self.E8.setText("")
        self.E9.setText("")
        self.E10.setText("")
        self.E11.setText("")
        self.E12.setText("")
        self.E13.setText("")
        self.E14.setText("")
        self.E15.setText("")
        self.E16.setText("")

        self.leXS3.setText("")
        self.leYS3.setText("")
        self.leXS4.setText("")
        self.leYS4.setText("")
        self.leXS5.setText("")
        self.leYS5.setText("")
        self.leXS6.setText("")
        self.leYS6.setText("")
        self.leXS7.setText("")
        self.leYS7.setText("")
        self.leXS8.setText("")
        self.leYS8.setText("")
        self.leXS9.setText("")
        self.leYS9.setText("")
        self.leXS10.setText("")
        self.leYS10.setText("")
        self.leXS11.setText("")
        self.leYS11.setText("")
        self.leXS12.setText("")
        self.leYS12.setText("")
        self.leXS13.setText("")
        self.leYS13.setText("")
        self.leXS14.setText("")
        self.leYS14.setText("")
        self.leXS15.setText("")
        self.leYS15.setText("")
        self.leXS16.setText("")
        self.leYS16.setText("")

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

    def graficarSimb(self, simbs, tSimb, t, nroSimb):
        """
        Función que realiza la gráfica de los símbolos en la GUI.

        :param simbs: Vector con los símbolos de la señal
        :param tSimb: Tiempo de símbolo
        :param t:  Vector tiempo.
        :param nroSimb: Número de símbolos en la señal.
        """
        self.figure_simbGraph.clear()

        if nroSimb == 2:
            s1, s2, s3, s4 = simbs

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
            self.axs1.set_title("Simbolo 1", fontsize=self.sizeHeight*0.015, weight='bold')
            self.axs1.set_ylabel('Amplitud')
            self.axs1.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs1.grid()

            s1Graf = np.concatenate((zeroes, s1, zeroes))

            if esCoseno(s2, self.fSample):
                s2Graf = s2
                tGraf = t
            else:
                tGraf = np.linspace(-0.001 * tSimb, tSimb * 1.001, s1Graf.size)

            self.axs2 = self.figure_simbGraph.add_subplot(212)
            self.axs2.plot(tGraf, s2Graf, 'r', linewidth=3)
            self.axs2.set_title("Simbolo 2", fontsize=self.sizeHeight*0.015, weight='bold')
            self.axs2.set_xlabel('Tiempo [seg]', fontsize=self.sizeHeight*0.01)
            self.axs2.set_ylabel('Amplitud')
            self.axs2.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs2.grid()

        elif nroSimb == 4:
            s1, s2, s3, s4 = simbs

            yMax = np.amax(np.array([np.amax(abs(s1)), np.amax(abs(s2)), np.amax(abs(s3)), np.amax(abs(s4))]))

            self.axs1 = self.figure_simbGraph.add_subplot(221)
            self.axs1.plot(t, s1, 'r', linewidth=1.5)
            self.axs1.set_title("Simbolo 1", fontsize=self.sizeHeight*0.015, weight='bold')
            self.axs1.set_ylabel('Amplitud')
            self.axs1.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs1.grid()

            self.axs2 = self.figure_simbGraph.add_subplot(222)
            self.axs2.plot(t, s2, 'r', linewidth=1.5)
            self.axs2.set_title("Simbolo 2", fontsize=self.sizeHeight*0.015, weight='bold')
            self.axs2.set_ylabel('Amplitud')
            self.axs2.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs2.grid()

            self.axs3 = self.figure_simbGraph.add_subplot(223)
            self.axs3.plot(t, s3, 'r', linewidth=1.5)
            self.axs3.set_title("Simbolo 3", fontsize=self.sizeHeight*0.015, weight='bold')
            self.axs3.set_xlabel('Tiempo [seg]', fontsize=self.sizeHeight*0.01)
            self.axs3.set_ylabel('Amplitud')
            self.axs3.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs3.grid()

            self.axs4 = self.figure_simbGraph.add_subplot(224)
            self.axs4.plot(t, s4, 'r', linewidth=1.5)
            self.axs4.set_title("Simbolo 4", fontsize=self.sizeHeight*0.015, weight='bold')
            self.axs4.set_xlabel('Tiempo [seg]', fontsize=self.sizeHeight*0.01)
            self.axs4.set_ylabel('Amplitud')
            self.axs4.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs4.grid()

        elif nroSimb == 8:
            s1, s2, s3, s4, s5, s6, s7, s8 = simbs

            yMax = np.amax(abs(s1))

            self.axs1 = self.figure_simbGraph.add_subplot(241)
            self.axs1.plot(t, s1, 'r')
            self.axs1.set_title('Símbolo 1', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs1.set_ylabel('Amplitud')
            self.axs1.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs1.grid()

            self.axs2 = self.figure_simbGraph.add_subplot(242)
            self.axs2.plot(t, s2, 'r')
            self.axs2.set_title('Símbolo 2', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs2.set_ylabel('Amplitud')
            self.axs2.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs2.grid()

            self.axs3 = self.figure_simbGraph.add_subplot(243)
            self.axs3.plot(t, s3, 'r')
            self.axs3.set_title('Símbolo 3', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs3.set_ylabel('Amplitud')
            self.axs3.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs3.grid()

            self.axs4 = self.figure_simbGraph.add_subplot(244)
            self.axs4.plot(t, s4, 'r')
            self.axs4.set_title('Símbolo 4', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs4.set_ylabel('Amplitud')
            self.axs4.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs4.grid()

            self.axs5 = self.figure_simbGraph.add_subplot(245)
            self.axs5.plot(t, s5, 'r')
            self.axs5.set_title('Símbolo 5', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs5.set_xlabel('Tiempo [s]', fontsize=self.sizeHeight*0.01)
            self.axs5.set_ylabel('Amplitud')
            self.axs5.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs5.grid()

            self.axs6 = self.figure_simbGraph.add_subplot(246)
            self.axs6.plot(t, s6, 'r')
            self.axs6.set_title('Símbolo 6', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs6.set_xlabel('Tiempo [s]', fontsize=self.sizeHeight*0.01)
            self.axs6.set_ylabel('Amplitud')
            self.axs6.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs6.grid()

            self.axs7 = self.figure_simbGraph.add_subplot(247)
            self.axs7.plot(t, s7, 'r')
            self.axs7.set_title('Símbolo 7', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs7.set_xlabel('Tiempo [s]', fontsize=self.sizeHeight*0.01)
            self.axs7.set_ylabel('Amplitud')
            self.axs7.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs7.grid()

            self.axs8 = self.figure_simbGraph.add_subplot(248)
            self.axs8.plot(t, s8, 'r')
            self.axs8.set_title('Símbolo 8', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs8.set_xlabel('Tiempo [s]', fontsize=self.sizeHeight*0.01)
            self.axs8.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs8.set_ylabel('Amplitud')
            self.axs8.grid()

        else:
            s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16 = simbs
            yMax = np.amax(abs(s11))

            self.axs1 = self.figure_simbGraph.add_subplot(441)
            self.axs1.plot(t, s1, 'r')
            self.axs1.set_title('Símbolo 1', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs1.set_ylabel('Amplitud')
            self.axs1.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs1.grid()

            self.axs2 = self.figure_simbGraph.add_subplot(442)
            self.axs2.plot(t, s2, 'r')
            self.axs2.set_title('Símbolo 2', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs2.set_ylabel('Amplitud')
            self.axs2.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs2.grid()

            self.axs3 = self.figure_simbGraph.add_subplot(443)
            self.axs3.plot(t, s3, 'r')
            self.axs3.set_title('Símbolo 3', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs3.set_ylabel('Amplitud')
            self.axs3.grid()
            self.axs3.set_ylim([-yMax * 1.2, yMax * 1.2])

            self.axs4 = self.figure_simbGraph.add_subplot(444)
            self.axs4.plot(t, s4, 'r')
            self.axs4.set_title('Símbolo 4', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs4.set_ylabel('Amplitud')
            self.axs4.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs4.grid()

            self.axs5 = self.figure_simbGraph.add_subplot(445)
            self.axs5.plot(t, s5, 'r')
            self.axs5.set_title('Símbolo 5', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs5.set_ylabel('Amplitud')
            self.axs5.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs5.grid()

            self.axs6 = self.figure_simbGraph.add_subplot(446)
            self.axs6.plot(t, s6, 'r')
            self.axs6.set_title('Símbolo 6', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs6.set_ylabel('Amplitud')
            self.axs6.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs6.grid()

            self.axs7 = self.figure_simbGraph.add_subplot(447)
            self.axs7.plot(t, s7, 'r')
            self.axs7.set_title('Símbolo 7', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs7.set_ylabel('Amplitud')
            self.axs7.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs7.grid()

            self.axs8 = self.figure_simbGraph.add_subplot(448)
            self.axs8.plot(t, s8, 'r')
            self.axs8.set_title('Símbolo 8', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs8.set_ylabel('Amplitud')
            self.axs8.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs8.grid()

            self.axs9 = self.figure_simbGraph.add_subplot(449)
            self.axs9.plot(t, s9, 'r')
            self.axs9.set_title('Símbolo 9', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs9.set_ylabel('Amplitud')
            self.axs9.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs9.grid()

            self.axs10 = self.figure_simbGraph.add_subplot(4, 4, 10)
            self.axs10.plot(t, s10, 'r')
            self.axs10.set_title('Símbolo 10', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs10.set_ylabel('Amplitud')
            self.axs10.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs10.grid()

            self.axs11 = self.figure_simbGraph.add_subplot(4, 4, 11)
            self.axs11.plot(t, s11, 'r')
            self.axs11.set_title('Símbolo 11', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs11.set_ylabel('Amplitud')
            self.axs11.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs11.grid()

            self.axs12 = self.figure_simbGraph.add_subplot(4, 4, 12)
            self.axs12.plot(t, s12, 'r')
            self.axs12.set_title('Símbolo 12', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs12.set_ylabel('Amplitud')
            self.axs12.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs12.grid()

            self.axs13 = self.figure_simbGraph.add_subplot(4, 4, 13)
            self.axs13.plot(t, s13, 'r')
            self.axs13.set_title('Símbolo 13', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs13.set_xlabel('Tiempo [s]', fontsize=self.sizeHeight*0.01)
            self.axs13.set_ylabel('Amplitud')
            self.axs13.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs13.grid()

            self.axs14 = self.figure_simbGraph.add_subplot(4, 4, 14)
            self.axs14.plot(t, s14, 'r')
            self.axs14.set_title('Símbolo 14', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs14.set_xlabel('Tiempo [s]', fontsize=self.sizeHeight*0.01)
            self.axs14.set_ylabel('Amplitud')
            self.axs14.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs14.grid()

            self.axs15 = self.figure_simbGraph.add_subplot(4, 4, 15)
            self.axs15.plot(t, s15, 'r')
            self.axs15.set_title('Símbolo 15', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs15.set_xlabel('Tiempo [s]', fontsize=self.sizeHeight*0.01)
            self.axs15.set_ylabel('Amplitud')
            self.axs15.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs15.grid()

            self.axs16 = self.figure_simbGraph.add_subplot(4, 4, 16)
            self.axs16.plot(t, s16, 'r')
            self.axs16.set_title('Símbolo 16', fontsize=self.sizeHeight*0.011, weight='bold')
            self.axs16.set_xlabel('Tiempo [s]', fontsize=self.sizeHeight*0.01)
            self.axs16.set_ylabel('Amplitud')
            self.axs16.set_ylim([-yMax * 1.2, yMax * 1.2])
            self.axs16.grid()

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
        self.axs1.set_title("Base 1", fontsize=self.sizeHeight*0.015, weight='bold')
        self.axs1.set_ylabel('Amplitud')
        self.axs1.set_ylim([-yMax * 1.2, yMax * 1.2])
        self.axs1.grid()
        xmin, xmax = self.axs1.get_xlim()
        ymin, ymax = self.axs1.get_ylim()
        maX = np.amax(abs(s1Graf))

        self.axs1.annotate(f'Amplitud: {format(maX, "<10.4f")}', (xmin * 0.9, ymin * 0.9), weight='bold')

        s1Graf = np.concatenate((zeroes, s1, zeroes))

        if esCoseno(s2, self.fSample):
            s2Graf = s2
            tGraf = t
        else:
            tGraf = np.linspace(-0.001 * tSimb, tSimb * 1.001, s1Graf.size)

        self.axs2 = self.figure_basesGraph.add_subplot(212)
        self.axs2.plot(tGraf, s2Graf, 'r', linewidth=3)
        self.axs2.set_title("Base 2", fontsize=self.sizeHeight*0.015, weight='bold')
        self.axs2.set_xlabel('Tiempo [seg]', fontsize=self.sizeHeight*0.01)
        self.axs2.set_ylabel('Amplitud')
        self.axs2.set_ylim([-yMax * 1.2, yMax * 1.2])
        self.axs2.grid()

        maX = np.amax(abs(s2Graf))
        if maX != 0:
            xmin, xmax = self.axs2.get_xlim()
            ymin, ymax = self.axs2.get_ylim()
            self.axs2.annotate(f'Amplitud: {format(maX, "<10.4f")}', (xmin * 0.9, ymin * 0.9), weight='bold')

        self.canvas_basesGraph.draw()

    def graficarBitsAleatorios(self, nroSimb, t2, senal, bits, tSimb):
        """
        Función que realiza la gráfica de los bits aleatorios en la GUI.

        :param nroSimb: Número de símbolos en la señal.
        :param t2: Vector tiempo de la señal.
        :param senal: Arreglo con la señal.
        :param bits: Arreglo con los bits de la señal.
        :param tSimb: Tiempo de Símbolo.
        """
        self.figure_bitsGraph.clear()

        # Bits Aleatorios
        senal = senal[0:int(50 * tSimb * self.fSample)]
        t2 = t2[0:int(50 * tSimb * self.fSample)]
        j = tSimb / 2

        self.axs1 = self.figure_bitsGraph.add_subplot(211)
        self.axs1.set_title('Bits Aleatorios', fontsize=self.sizeHeight*0.015, weight='bold')
        self.axs1.set_xlim([0, 5 * tSimb])
        self.axs1.axes.xaxis.set_visible(False)
        self.axs1.axes.yaxis.set_visible(False)

        if nroSimb == 2:
            for i in range(50):
                if bits[i] == 1:
                    x = j
                    y = 0
                    self.axs1.scatter(x, y, s=500, c="r")
                    self.axs1.text(x, y, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                else:
                    x = j
                    y = 0
                    self.axs1.scatter(x, y, s=500, c="b")
                    self.axs1.text(x, y, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )

                j = j + tSimb

        elif nroSimb == 4:
            for i in range(50):
                if bits[i] == 0:
                    x = j
                    y1 = 1
                    y2 = 0

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 1:
                    x = j
                    y1 = 1
                    y2 = 0

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 2:
                    x = j
                    y1 = 1
                    y2 = 0

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )

                else:
                    x = j
                    y1 = 1
                    y2 = 0

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )

                j = j + tSimb

            self.axs1.set_ylim([-4, 4])

        elif nroSimb == 8:
            for i in range(50):
                if bits[i] == 0:
                    x = j
                    y1 = 1
                    y2 = 0
                    y3 = -1

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.scatter(x, y3, s=500, c='b')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 1:
                    x = j
                    y1 = 1
                    y2 = 0
                    y3 = -1

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.scatter(x, y3, s=500, c='r')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 2:
                    x = j
                    y1 = 1
                    y2 = 0
                    y3 = -1

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.scatter(x, y3, s=500, c='b')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 3:
                    x = j
                    y1 = 1
                    y2 = 0
                    y3 = -1

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.scatter(x, y3, s=500, c='r')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 4:
                    x = j
                    y1 = 1
                    y2 = 0
                    y3 = -1

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.scatter(x, y3, s=500, c='b')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 5:
                    x = j
                    y1 = 1
                    y2 = 0
                    y3 = -1

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.scatter(x, y3, s=500, c='r')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 6:
                    x = j
                    y1 = 1
                    y2 = 0
                    y3 = -1

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.scatter(x, y3, s=500, c='b')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                else:
                    x = j
                    y1 = 1
                    y2 = 0
                    y3 = -1

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.scatter(x, y3, s=500, c='r')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                j = j + tSimb

            self.axs1.set_ylim([-4, 4])

        else:
            for i in range(50):
                if bits[i] == 0:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.scatter(x, y3, s=500, c='b')
                    self.axs1.scatter(x, y4, s=500, c='b')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 1:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.scatter(x, y3, s=500, c='b')
                    self.axs1.scatter(x, y4, s=500, c='r')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 2:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.scatter(x, y3, s=500, c='r')
                    self.axs1.scatter(x, y4, s=500, c='b')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 3:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.scatter(x, y3, s=500, c='r')
                    self.axs1.scatter(x, y4, s=500, c='r')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 4:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.scatter(x, y3, s=500, c='b')
                    self.axs1.scatter(x, y4, s=500, c='b')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 5:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.scatter(x, y3, s=500, c='b')
                    self.axs1.scatter(x, y4, s=500, c='r')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 6:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.scatter(x, y3, s=500, c='r')
                    self.axs1.scatter(x, y4, s=500, c='b')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 7:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='b')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.scatter(x, y3, s=500, c='r')
                    self.axs1.scatter(x, y4, s=500, c='r')
                    self.axs1.text(x, y1, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 8:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.scatter(x, y3, s=500, c='b')
                    self.axs1.scatter(x, y4, s=500, c='b')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 9:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.scatter(x, y3, s=500, c='b')
                    self.axs1.scatter(x, y4, s=500, c='r')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 10:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.scatter(x, y3, s=500, c='r')
                    self.axs1.scatter(x, y4, s=500, c='b')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 11:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='b')
                    self.axs1.scatter(x, y3, s=500, c='r')
                    self.axs1.scatter(x, y4, s=500, c='r')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 12:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.scatter(x, y3, s=500, c='b')
                    self.axs1.scatter(x, y4, s=500, c='b')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 13:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.scatter(x, y3, s=500, c='b')
                    self.axs1.scatter(x, y4, s=500, c='r')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                elif bits[i] == 14:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.scatter(x, y3, s=500, c='r')
                    self.axs1.scatter(x, y4, s=500, c='b')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '0',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                else:
                    x = j
                    y1 = 2
                    y2 = 1
                    y3 = 0
                    y4 = -1

                    self.axs1.scatter(x, y1, s=500, c='r')
                    self.axs1.scatter(x, y2, s=500, c='r')
                    self.axs1.scatter(x, y3, s=500, c='r')
                    self.axs1.scatter(x, y4, s=500, c='r')
                    self.axs1.text(x, y1, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y2, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y3, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                    self.axs1.text(x, y4, '1',
                                   horizontalalignment='center',
                                   verticalalignment='center',
                                   c='w'
                                   )
                j = j + tSimb

            self.axs1.set_ylim([-3, 4])

        # Gráfica del la senal
        self.axs2 = self.figure_bitsGraph.add_subplot(212)
        if nroSimb != 2:
            self.axs2.plot(t2, senal, 'r')
        else:
            self.axs2.plot(t2, senal, 'r', linewidth=3)
        self.axs2.set_title('Señal', fontsize=self.sizeHeight*0.015, weight='bold')
        self.axs2.set_ylabel('Amplitud')
        self.axs2.set_xlabel('tiempo (s)', fontsize=self.sizeHeight*0.01)
        self.axs2.set_xlim([0, 5 * tSimb])
        self.axs2.grid()

        self.canvas_bitsGraph.draw()

    def graficarConstAntes(self, simbs, U1, U2, tSimb, nroSimb):
        """
        Función que realiza la gráfica de la constelación antes del canal en la GUI.

        :param simbs: Vector con los símbolos de la señal.
        :param U1: Base U1
        :param U2: Base U2
        :param tSimb: Tiempo de símbolo
        :param nroSimb: Número de símbolos en la señal.
        """
        self.figure_constACGraph.clear()

        if nroSimb == 2:
            s1, s2, s3, s4 = simbs

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

        elif nroSimb == 4:
            s1, s2, s3, s4 = simbs

            x1 = tSimb * np.mean(np.multiply(s1, U1))
            y1 = tSimb * np.mean(np.multiply(s1, U2))
            x2 = tSimb * np.mean(np.multiply(s2, U1))
            y2 = tSimb * np.mean(np.multiply(s2, U2))
            x3 = tSimb * np.mean(np.multiply(s3, U1))
            y3 = tSimb * np.mean(np.multiply(s3, U2))
            x4 = tSimb * np.mean(np.multiply(s4, U1))
            y4 = tSimb * np.mean(np.multiply(s4, U2))

            coord = (x1, y1, x2, y2, x3, y3, x4, y4)

            ejeX = np.array([x1, x2, x3, x4])
            ejeY = np.array([y1, y2, y3, y4])

            xMax = np.amax(abs(ejeX))
            yMax = np.amax(abs(ejeY))

            size = [300, 300, 300, 300]
            z = [0, 0, 0, 0]

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

            self.ax.text(x3, y3, 'S3',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )

            self.ax.text(x4, y4, 'S4',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )

        elif nroSimb == 8:
            s1, s2, s3, s4, s5, s6, s7, s8 = simbs

            x1 = tSimb * np.mean(np.multiply(s1, U1))
            y1 = tSimb * np.mean(np.multiply(s1, U2))
            x2 = tSimb * np.mean(np.multiply(s2, U1))
            y2 = tSimb * np.mean(np.multiply(s2, U2))
            x3 = tSimb * np.mean(np.multiply(s3, U1))
            y3 = tSimb * np.mean(np.multiply(s3, U2))
            x4 = tSimb * np.mean(np.multiply(s4, U1))
            y4 = tSimb * np.mean(np.multiply(s4, U2))
            x5 = tSimb * np.mean(np.multiply(s5, U1))
            y5 = tSimb * np.mean(np.multiply(s5, U2))
            x6 = tSimb * np.mean(np.multiply(s6, U1))
            y6 = tSimb * np.mean(np.multiply(s6, U2))
            x7 = tSimb * np.mean(np.multiply(s7, U1))
            y7 = tSimb * np.mean(np.multiply(s7, U2))
            x8 = tSimb * np.mean(np.multiply(s8, U1))
            y8 = tSimb * np.mean(np.multiply(s8, U2))

            coord = (x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8)

            ejeX = np.array([x1, x2, x3, x4, x5, x6, x7, x8])
            ejeY = np.array([y1, y2, y3, y4, y5, y6, y7, y8])

            xMax = np.amax(abs(ejeX))
            yMax = np.amax(abs(ejeY))

            size = [300, 300, 300, 300, 300, 300, 300, 300]
            z = [0, 0, 0, 0, 0, 0, 0, 0]

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

            self.ax.text(x3, y3, 'S3',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )

            self.ax.text(x4, y4, 'S4',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x5, y5, 'S5',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x6, y6, 'S6',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x7, y7, 'S7',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x8, y8, 'S8',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )

        else:
            s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16 = simbs

            x1 = tSimb * np.mean(np.multiply(s1, U1))
            y1 = tSimb * np.mean(np.multiply(s1, U2))
            x2 = tSimb * np.mean(np.multiply(s2, U1))
            y2 = tSimb * np.mean(np.multiply(s2, U2))
            x3 = tSimb * np.mean(np.multiply(s3, U1))
            y3 = tSimb * np.mean(np.multiply(s3, U2))
            x4 = tSimb * np.mean(np.multiply(s4, U1))
            y4 = tSimb * np.mean(np.multiply(s4, U2))
            x5 = tSimb * np.mean(np.multiply(s5, U1))
            y5 = tSimb * np.mean(np.multiply(s5, U2))
            x6 = tSimb * np.mean(np.multiply(s6, U1))
            y6 = tSimb * np.mean(np.multiply(s6, U2))
            x7 = tSimb * np.mean(np.multiply(s7, U1))
            y7 = tSimb * np.mean(np.multiply(s7, U2))
            x8 = tSimb * np.mean(np.multiply(s8, U1))
            y8 = tSimb * np.mean(np.multiply(s8, U2))
            x9 = tSimb * np.mean(np.multiply(s9, U1))
            y9 = tSimb * np.mean(np.multiply(s9, U2))
            x10 = tSimb * np.mean(np.multiply(s10, U1))
            y10 = tSimb * np.mean(np.multiply(s10, U2))
            x11 = tSimb * np.mean(np.multiply(s11, U1))
            y11 = tSimb * np.mean(np.multiply(s11, U2))
            x12 = tSimb * np.mean(np.multiply(s12, U1))
            y12 = tSimb * np.mean(np.multiply(s12, U2))
            x13 = tSimb * np.mean(np.multiply(s13, U1))
            y13 = tSimb * np.mean(np.multiply(s13, U2))
            x14 = tSimb * np.mean(np.multiply(s14, U1))
            y14 = tSimb * np.mean(np.multiply(s14, U2))
            x15 = tSimb * np.mean(np.multiply(s15, U1))
            y15 = tSimb * np.mean(np.multiply(s15, U2))
            x16 = tSimb * np.mean(np.multiply(s16, U1))
            y16 = tSimb * np.mean(np.multiply(s16, U2))

            coord = (
            x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12, x13,
            y13, x14, y14, x15, y15, x16, y16)

            ejeX = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16])
            ejeY = np.array([y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16])

            xMax = np.amax(abs(ejeX))
            yMax = np.amax(abs(ejeY))

            size = [300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300, 300]
            z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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

            self.ax.text(x3, y3, 'S3',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )

            self.ax.text(x4, y4, 'S4',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x5, y5, 'S5',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x6, y6, 'S6',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x7, y7, 'S7',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x8, y8, 'S8',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x9, y9, 'S9',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x10, y10, 'S10',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x11, y11, 'S11',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x12, y12, 'S12',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x13, y13, 'S13',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x14, y14, 'S14',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x15, y15, 'S15',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )
            self.ax.text(x16, y16, 'S16',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )

        self.canvas_constACGraph.draw()

        return coord

    def graficarConstDespues(self, senal, U1, U2, tSimb, coord, nMuestrasSimb, nroSimb):
        """
        Función que realiza la gráfica de la constelación después del canal en la GUI.

        :param senal: Arreglo con la señal con ruido.
        :param U1: Base U1
        :param U2: Base U2
        :param tSimb: Tiempo de símbolo
        :param coord: Vector con las coordenadas de los símbolos
        :param nMuestrasSimb: Número de muestras en cada símbolo
        :param nroSimb: Número de Símbolos en la señal
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

        if nroSimb == 2:
            x1, y1, x2, y2 = coord

            coordX = np.array([x1, x2])
            coordY = np.array([y1, y2])

        elif nroSimb == 4:
            x1, y1, x2, y2, x3, y3, x4, y4 = coord

            coordX = np.array([x1, x2, x3, x4])
            coordY = np.array([y1, y2, y3, y4])

        elif nroSimb == 8:
            x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8 = coord

            coordX = np.array([x1, x2, x3, x4, x5, x6, x7, x8])
            coordY = np.array([y1, y2, y3, y4, y5, y6, y7, y8])

        else:
            x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12, x13, y13, x14, y14, x15, y15, x16, y16 = coord

            coordX = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16])
            coordY = np.array([y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16])

        ejeX = np.concatenate((detU1, coordX))
        ejeY = np.concatenate((detU2, coordY))

        # size = np.concatenate((np.full((1, detU1.size), 5), np.full((1, coordX.size), 300)), axis=1)
        # z = np.concatenate((np.full((1, detU1.size), 0.5), np.full((1, coordX.size), 0)), axis=1)

        size = np.concatenate((np.full((1, 10000), 5), np.full((1, nroSimb), 300)), axis=1)
        z = np.concatenate((np.full((1, 10000), 0.5), np.full((1, nroSimb), 0)), axis=1)

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

        if nroSimb > 2:
            self.ax.text(x3, y3, 'S3',
                         horizontalalignment='center',
                         verticalalignment='center',
                         c='w'
                         )

            if nroSimb > 3:
                self.ax.text(x4, y4, 'S4',
                             horizontalalignment='center',
                             verticalalignment='center',
                             c='w'
                             )

                if nroSimb > 4:
                    self.ax.text(x5, y5, 'S5',
                                 horizontalalignment='center',
                                 verticalalignment='center',
                                 c='w'
                                 )

                    self.ax.text(x6, y6, 'S6',
                                 horizontalalignment='center',
                                 verticalalignment='center',
                                 c='w'
                                 )

                    self.ax.text(x7, y7, 'S7',
                                 horizontalalignment='center',
                                 verticalalignment='center',
                                 c='w'
                                 )

                    self.ax.text(x8, y8, 'S8',
                                 horizontalalignment='center',
                                 verticalalignment='center',
                                 c='w'
                                 )

                    if nroSimb > 8:
                        self.ax.text(x9, y9, 'S9',
                                     horizontalalignment='center',
                                     verticalalignment='center',
                                     c='w'
                                     )
                        self.ax.text(x10, y10, 'S10',
                                     horizontalalignment='center',
                                     verticalalignment='center',
                                     c='w'
                                     )
                        self.ax.text(x11, y11, 'S11',
                                     horizontalalignment='center',
                                     verticalalignment='center',
                                     c='w'
                                     )
                        self.ax.text(x12, y12, 'S12',
                                     horizontalalignment='center',
                                     verticalalignment='center',
                                     c='w'
                                     )
                        self.ax.text(x13, y13, 'S13',
                                     horizontalalignment='center',
                                     verticalalignment='center',
                                     c='w'
                                     )
                        self.ax.text(x14, y14, 'S14',
                                     horizontalalignment='center',
                                     verticalalignment='center',
                                     c='w'
                                     )
                        self.ax.text(x15, y15, 'S15',
                                     horizontalalignment='center',
                                     verticalalignment='center',
                                     c='w'
                                     )
                        self.ax.text(x16, y16, 'S16',
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
        :param t2: Vector tiempo.
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

        if senalBBPB!=2:
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

    def graficarSenalFreq(self, senal, t2, fSimb, frecuencias, senalBBPB, anchoBanda):
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
        numFreq = len(frecuencias)  # Numero de frecuencias en la señal. Solo 1 o 2 frecuencias.

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

    def graficarProbError(self, E, X, Y, etaGraf, peGraf):
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
        self.axs1.annotate(f'Punto Pe: ({format(X, "<6.4f")}, {format(Y, "<6.4f")})', (10, 10 ), xycoords='axes pixels',weight='bold')

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
            self.limpiarIndicadores()

            self.SimularButton.setStatusTip('')
            self.statusbar.clearMessage()
            self.statusbar.showMessage('¡Resultados listos!',5000)

            # Tipo Senal
            tipoSenal = self.cbTipoSenal.currentText()

            # Datos de la señal
            tSimb = self.sbTsimb.value()
            fSimb = 1 / tSimb
            nMuestrasSimb = int(self.fSample * tSimb)
            t = np.linspace(0, tSimb, nMuestrasSimb)

            # Nivel de Ruido
            if self.cbNivelRuido.currentText() == "Bajo":
                nivelRuido = 1
            elif self.cbNivelRuido.currentText() == "Medio":
                nivelRuido = 2
            elif self.cbNivelRuido.currentText() == "Alto":
                nivelRuido = 3

            if tipoSenal == "NRZ unipolar":
                nroSimb = 2
                amplitud = float(self.leAmplitud.text())
                s1 = simbolos(t, nMuestrasSimb, tSimb, 1, 0, 0, amplitud, 0, 0, self.fSample)
                s2 = simbolos(t, nMuestrasSimb, tSimb, 0, 0, 0, 0, 0, 0, self.fSample)
                s3 = 0
                s4 = 0

                U1, U2 = gramSchmidt(s1, s2, 0, 0, nMuestrasSimb, self.fSample)
                senal, t2, bits = senalAleatoria(s1, s2, s3, s4, tSimb, nMuestrasSimb, nroSimb, self.nTotalSimb)

                simbolos_senal = (s1, s2, 0, 0)
                tipoOndas = (1, 0, 0, 0)
                frecuencias = (0, 0, 0, 0)

            elif tipoSenal == "RZ unipolar":
                nroSimb = 2
                amplitud = float(self.leAmplitud.text())
                s1 = simbolos(t, nMuestrasSimb, tSimb, 2, 0, 0, amplitud, 0, 0, self.fSample)
                s2 = simbolos(t, nMuestrasSimb, tSimb, 0, 0, 0, 0, 0, 0, self.fSample)
                s3 = 0
                s4 = 0

                U1, U2 = gramSchmidt(s1, s2, 0, 0, nMuestrasSimb, self.fSample)
                senal, t2, bits = senalAleatoria(s1, s2, s3, s4, tSimb, nMuestrasSimb, nroSimb, self.nTotalSimb)

                simbolos_senal = (s1, s2, 0, 0)
                tipoOndas = (2, 0, 0, 0)
                frecuencias = (0, 0, 0, 0)

            elif tipoSenal == "NRZ polar":
                nroSimb = 2
                amplitud = float(self.leAmplitud.text())
                s1 = simbolos(t, nMuestrasSimb, tSimb, 1, 0, 0, amplitud, 0, 0, self.fSample)
                s2 = simbolos(t, nMuestrasSimb, tSimb, 1, 0, 0, -amplitud, 0, 0, self.fSample)
                s3 = 0
                s4 = 0

                U1, U2 = gramSchmidt(s1, s2, 0, 0, nMuestrasSimb, self.fSample)
                senal, t2, bits = senalAleatoria(s1, s2, s3, s4, tSimb, nMuestrasSimb, nroSimb, self.nTotalSimb)

                simbolos_senal = (s1, s2, 0, 0)
                tipoOndas = (1, 1, 0, 0)
                frecuencias = (0, 0, 0, 0)

            elif tipoSenal == "RZ polar":
                amplitud = float(self.leAmplitud.text())
                nroSimb = 2
                s1 = simbolos(t, nMuestrasSimb, tSimb, 2, 0, 0, amplitud, 0, 0, self.fSample)
                s2 = simbolos(t, nMuestrasSimb, tSimb, 2, 0, 0, -amplitud, 0, 0, self.fSample)
                s3 = 0
                s4 = 0

                U1, U2 = gramSchmidt(s1, s2, 0, 0, nMuestrasSimb, self.fSample)
                senal, t2, bits = senalAleatoria(s1, s2, s3, s4, tSimb, nMuestrasSimb, nroSimb, self.nTotalSimb)

                simbolos_senal = (s1, s2, 0, 0)
                tipoOndas = (2, 2, 0, 0)
                frecuencias = (0, 0, 0, 0)

            elif tipoSenal == "Manchester":
                amplitud = float(self.leAmplitud.text())
                nroSimb = 2
                s1 = simbolos(t, nMuestrasSimb, tSimb, 3, 0, 0, amplitud, 0, 0, self.fSample)
                s2 = simbolos(t, nMuestrasSimb, tSimb, 3, 0, 0, -amplitud, 0, 0, self.fSample)
                s3 = 0
                s4 = 0

                U1, U2 = gramSchmidt(s1, s2, 0, 0, nMuestrasSimb, self.fSample)
                senal, t2, bits = senalAleatoria(s1, s2, s3, s4, tSimb, nMuestrasSimb, nroSimb, self.nTotalSimb)

                simbolos_senal = (s1, s2, 0, 0)
                tipoOndas = (3, 3, 0, 0)
                frecuencias = (0, 0, 0, 0)

            elif tipoSenal == "OOK":
                amplitud = float(self.leAmplitud.text())
                frecuencia = self.hsFreq1.value()
                nroSimb = 2
                s1 = simbolos(t, nMuestrasSimb, tSimb, 4, frecuencia, 0, amplitud, 0, 0, self.fSample)
                s2 = simbolos(t, nMuestrasSimb, tSimb, 0, 0, 0, 0, 0, 0, self.fSample)
                s3 = 0
                s4 = 0

                U1, U2 = gramSchmidt(s1, s2, 0, 0, nMuestrasSimb, self.fSample)
                senal, t2, bits = senalAleatoria(s1, s2, s3, s4, tSimb, nMuestrasSimb, nroSimb, self.nTotalSimb)

                simbolos_senal = (s1, s2, 0, 0)
                tipoOndas = (4, 0, 0, 0)
                frecuencias = (frecuencia, 0, 0, 0)

            elif tipoSenal == "PRK":
                amplitud = float(self.leAmplitud.text())
                frecuencia = self.hsFreq1.value()
                nroSimb = 2
                s1 = simbolos(t, nMuestrasSimb, tSimb, 4, frecuencia, 0, amplitud, 0, 0, self.fSample)
                s2 = simbolos(t, nMuestrasSimb, tSimb, 4, frecuencia, 0, -amplitud, 0, 0, self.fSample)
                s3 = 0
                s4 = 0

                U1, U2 = gramSchmidt(s1, s2, 0, 0, nMuestrasSimb, self.fSample)
                senal, t2, bits = senalAleatoria(s1, s2, s3, s4, tSimb, nMuestrasSimb, nroSimb, self.nTotalSimb)

                simbolos_senal = (s1, s2, 0, 0)
                tipoOndas = (4, 4, 0, 0)
                frecuencias = (frecuencia, 0, 0, 0)

            elif tipoSenal == "FSK":
                amplitud = float(self.leAmplitud.text())
                frecuencia1 = self.hsFreq1.value()
                frecuencia2 = self.hsFreq2.value()
                nroSimb = 2
                s1 = simbolos(t, nMuestrasSimb, tSimb, 4, frecuencia1, 0, amplitud, 0, 0, self.fSample)
                s2 = simbolos(t, nMuestrasSimb, tSimb, 4, frecuencia2, 0, amplitud, 0, 0, self.fSample)
                s3 = 0
                s4 = 0

                U1, U2 = gramSchmidt(s1, s2, 0, 0, nMuestrasSimb, self.fSample)
                senal, t2, bits = senalAleatoria(s1, s2, s3, s4, tSimb, nMuestrasSimb, nroSimb, self.nTotalSimb)

                simbolos_senal = (s1, s2, 0, 0)
                tipoOndas = (4, 4, 0, 0)
                frecuencias = (frecuencia1, frecuencia2, 0, 0)

                simbsIguales = self.chequearSimbsIguales(s1, s2)

                if simbsIguales:
                    self.mensaje_errorSimbsIguales()

            elif tipoSenal == "QPSK":
                nroSimb = 4
                frecuencia = self.hsFreq1.value()

                U1 = bases(t, nMuestrasSimb, tSimb, 4, frecuencia, 0, 0, 0, self.fSample)
                U2 = bases(t, nMuestrasSimb, tSimb, 4, frecuencia, -(math.pi / 2), 0, 0, self.fSample)

                s1 = ((-1) * U1) + ((-1) * U2)
                s2 = ((1) * U1) + ((1) * U2)
                s3 = ((1) * U1) + ((-1) * U2)
                s4 = ((-1) * U1) + ((1) * U2)

                senal, t2, bits = senalAleatoria(s1, s2, s3, s4, tSimb, nMuestrasSimb, nroSimb, self.nTotalSimb)

                simbolos_senal = (s1, s2, s3, s4)
                tipoOndas = (4, 4, 4, 4)
                frecuencias = (frecuencia, 0, 0, 0)

            elif tipoSenal == "8-PSK":
                nroSimb = 8
                frecuencia = self.hsFreq1.value()

                U1 = bases(t, nMuestrasSimb, tSimb, 4, frecuencia, 0, 0, 0, self.fSample)
                U2 = bases(t, nMuestrasSimb, tSimb, 4, frecuencia, -(math.pi / 2), 0, 0, self.fSample)

                s8 = (math.cos(math.pi / 8) * U1) + ((math.sin(math.pi / 8) * U2))
                s1 = (math.cos(3 * math.pi / 8) * U1) + ((math.sin(3 * math.pi / 8) * U2))
                s2 = (math.cos(5 * math.pi / 8) * U1) + ((math.sin(5 * math.pi / 8) * U2))
                s3 = (math.cos(7 * math.pi / 8) * U1) + ((math.sin(7 * math.pi / 8) * U2))
                s4 = (math.cos(9 * math.pi / 8) * U1) + ((math.sin(9 * math.pi / 8) * U2))
                s5 = (math.cos(11 * math.pi / 8) * U1) + ((math.sin(11 * math.pi / 8) * U2))
                s6 = (math.cos(13 * math.pi / 8) * U1) + ((math.sin(13 * math.pi / 8) * U2))
                s7 = (math.cos(15 * math.pi / 8) * U1) + ((math.sin(15 * math.pi / 8) * U2))

                simbolos_senal = (s1, s2, s3, s4, s5, s6, s7, s8)
                tipoOndas = (4, 4, 4, 4)
                frecuencias = (frecuencia, 0, 0, 0)

                senal, t2, bits = senalAleatoriaMasSimbolos(simbolos_senal, tSimb, nMuestrasSimb, nroSimb, self.nTotalSimb)

            else:
                nroSimb = 16
                frecuencia = self.hsFreq1.value()

                U1 = bases(t, nMuestrasSimb, tSimb, 4, frecuencia, 0, 0, 0, self.fSample)
                U2 = bases(t, nMuestrasSimb, tSimb, 4, frecuencia, -(math.pi / 2), 0, 0, self.fSample)

                s1 = (1) * U1 + (1) * U2
                s2 = (1) * U1 + (-1) * U2
                s3 = (1) * U1 + (3) * U2
                s4 = (1) * U1 + (-3) * U2
                s5 = (-1) * U1 + (1) * U2
                s6 = (-1) * U1 + (-1) * U2
                s7 = (-1) * U1 + (3) * U2
                s8 = (-1) * U1 + (-3) * U2
                s9 = (3) * U1 + (1) * U2
                s10 = (3) * U1 + (-1) * U2
                s11 = (3) * U1 + (3) * U2
                s12 = (3) * U1 + (-3) * U2
                s13 = (-3) * U1 + (1) * U2
                s14 = (-3) * U1 + (-1) * U2
                s15 = (-3) * U1 + (3) * U2
                s16 = (-3) * U1 + (-3) * U2

                simbolos_senal = (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16)
                tipoOndas = (4, 4, 4, 4)
                frecuencias = (frecuencia, 0, 0, 0)

                senal, t2, bits = senalAleatoriaMasSimbolos(simbolos_senal, tSimb, nMuestrasSimb, nroSimb, self.nTotalSimb)

            self.graficarSimb(simbolos_senal, tSimb, t, nroSimb)
            self.graficarBases(U1, U2, tSimb, t)
            self.graficarBitsAleatorios(nroSimb, t2, senal, bits, tSimb)

            coord = self.graficarConstAntes(simbolos_senal, U1, U2, tSimb, nroSimb)

            potenciaSenal = np.mean(np.multiply(senal, senal))
            E = potenciaSenal * tSimb

            X, Y, etaGraf, peGraf, dmin, nDmin = obtenerEta(coord, nroSimb, E, self.nTotalSimb, nivelRuido)
            senalRuido = senal + (math.sqrt(0.5 * self.fSample * X)) * np.random.normal(0, 1, senal.size)

            detU1, detU2 = self.graficarConstDespues(senalRuido, U1, U2, tSimb, coord, nMuestrasSimb, nroSimb)

            if tipoSenal == "8-PSK" or tipoSenal == "16QAM":
                senalDet, rec = deteccionDistanciaMasSimbolos(coord, simbolos_senal, nroSimb, detU1, detU2, self.nTotalSimb,
                                                              nMuestrasSimb)

            else:
                senalDet, rec = deteccionDistancia(coord, s1, s2, s3, s4, nroSimb, detU1, detU2, self.nTotalSimb,
                                                   nMuestrasSimb)

            pe, primerError, cont = calcularPe(self.nTotalSimb, rec, bits)

            senalBBPB = senalBandabasePasabanda(s1, s2, s3, s4, nroSimb, self.fSample, nMuestrasSimb)

            self.graficarSenalTiempo(senal, senalRuido, senalDet, tSimb, primerError, t2, senalBBPB)

            anchoBanda = calcularAnchoBanda(tipoOndas, fSimb, nroSimb, freqs = frecuencias, tipoSenalBBPB = senalBBPB)

            self.graficarSenalFreq(senal, t2, fSimb, frecuencias, senalBBPB, anchoBanda)

            self.graficarProbError(E, X, Y, etaGraf, peGraf)

            ortogonalidad, polaridad, proporcionalidad, energia, numCiclos = resultadosNumericos(simbolos_senal,
                                                                                                 nroSimb, nMuestrasSimb,
                                                                                                 self.fSample, fSimb,
                                                                                                 tipoOndas, frecuencias)
            if nroSimb == 2:
                x1, y1, x2, y2 = coord

                o_s1s2 = ortogonalidad
                p_s1s2 = polaridad
                pp_s1s2 = proporcionalidad

                E1, E2 = energia
                numCiclosEnterosS1, numCiclosEnterosS2 = numCiclos

                if o_s1s2:
                    self.O12_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O12_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if p_s1s2:
                    self.O12_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O12_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if pp_s1s2:
                    self.O12_4.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O12_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if tipoSenal == 'FSK':
                    if numCiclosEnterosS1:
                        self.N1.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    else:
                        self.N1.setPixmap(QtGui.QPixmap("UIs/x.png"))

                    if numCiclosEnterosS2:
                        self.N2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    else:
                        self.N2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                elif tipoSenal == 'OOK':
                    if numCiclosEnterosS1:
                        self.N1.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    else:
                        self.N1.setPixmap(QtGui.QPixmap("UIs/x.png"))

                    self.N2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

                elif tipoSenal == 'PRK':
                    if numCiclosEnterosS1:
                        self.N1.setPixmap(QtGui.QPixmap("UIs/check.png"))
                        self.N2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    else:
                        self.N1.setPixmap(QtGui.QPixmap("UIs/x.png"))
                        self.N2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                else:
                    self.N1.setPixmap(QtGui.QPixmap("UIs/Empty.png"))
                    self.N2.setPixmap(QtGui.QPixmap("UIs/Empty.png"))

            elif nroSimb == 4:
                x1, y1, x2, y2, x3, y3, x4, y4 = coord

                o_s1s2, o_s1s3, o_s1s4, o_s2s3, o_s2s4, o_s3s4, = ortogonalidad
                p_s1s2, p_s1s3, p_s1s4, p_s2s3, p_s2s4, p_s3s4, = polaridad
                pp_s1s2, pp_s1s3, pp_s1s4, pp_s2s3, pp_s2s4, pp_s3s4, = proporcionalidad

                E1, E2, E3, E4 = energia
                numCiclosEnterosS1, numCiclosEnterosS2, numCiclosEnterosS3, numCiclosEnterosS4 = numCiclos

                if o_s1s2:
                    self.O12_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O12_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if o_s1s3:
                    self.O13_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O13_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if o_s1s4:
                    self.O14_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O14_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if o_s2s3:
                    self.O23_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O23_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if o_s2s4:
                    self.O24_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O24_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if o_s3s4:
                    self.O34_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O34_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if p_s1s2:
                    self.O12_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O12_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if p_s1s3:
                    self.O13_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O13_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if p_s1s4:
                    self.O14_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O14_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if p_s2s3:
                    self.O23_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O23_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if p_s2s4:
                    self.O24_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O24_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if p_s3s4:
                    self.O34_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O34_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if pp_s1s2:
                    self.O12_4.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O12_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if pp_s1s3:
                    self.O13_4.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O13_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if pp_s1s4:
                    self.O14_4.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O14_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if pp_s2s3:
                    self.O23_4.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O23_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if pp_s2s4:
                    self.O24_4.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O24_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if pp_s3s4:
                    self.O34_4.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.O34_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if numCiclosEnterosS1:
                    self.N1.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N4.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.N1.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if E3.is_integer():
                    self.E3.setText(str(int(E3)))
                else:
                    self.E3.setText(format(E3, "7.3f"))

                if E4.is_integer():
                    self.E4.setText(str(int(E4)))
                else:
                    self.E4.setText(format(E4, "7.3f"))

                if x3.is_integer():
                    self.leXS3.setText(str(int(x3)))
                else:
                    self.leXS3.setText(format(x3, "7.2f"))

                if y3.is_integer():
                    self.leYS3.setText(str(int(y3)))
                else:
                    self.leYS3.setText(format(y3, "7.2f"))

                if x4.is_integer():
                    self.leXS4.setText(str(int(x4)))
                else:
                    self.leXS4.setText(format(x4, "7.2f"))

                if y4.is_integer():
                    self.leYS4.setText(str(int(y3)))
                else:
                    self.leYS4.setText(format(y3, "7.2f"))

            elif nroSimb == 8:
                x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8 = coord

                E1, E2, E3, E4, E5, E6, E7, E8 = energia

                if numCiclos:
                    self.N1.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N4.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N5.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N6.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N7.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N8.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.N1.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N5.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N6.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N7.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N8.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O12_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O13_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O14_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O15_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O16_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O17_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O18_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O23_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O24_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O25_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O26_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O27_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O28_2.setPixmap(QtGui.QPixmap("UIs/check.png"))

                self.O34_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O35_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O36_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O37_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O38_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O45_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O46_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O47_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O48_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O56_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O57_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O58_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O67_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O68_2.setPixmap(QtGui.QPixmap("UIs/check.png"))

                self.O78_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O12_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O13_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O14_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O15_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O16_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O17_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O18_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O23_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O24_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O25_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O26_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O27_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O28_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O34_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O35_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O36_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O37_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O38_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O45_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O46_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O47_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O48_3.setPixmap(QtGui.QPixmap("UIs/check.png"))

                self.O56_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O57_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O58_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O67_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O68_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O78_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O12_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O13_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O14_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O15_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O16_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O17_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O18_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O23_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O24_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O25_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O26_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O27_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O28_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O34_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O35_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O36_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O37_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O38_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O45_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O46_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O47_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O48_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O56_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O57_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O58_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O67_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O68_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O78_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if E3.is_integer():
                    self.E3.setText(str(int(E3)))
                else:
                    self.E3.setText(format(E3, "7.3f"))

                if E4.is_integer():
                    self.E4.setText(str(int(E4)))
                else:
                    self.E4.setText(format(E4, "7.3f"))

                if E5.is_integer():
                    self.E5.setText(str(int(E5)))
                else:
                    self.E5.setText(format(E5, "7.3f"))

                if E6.is_integer():
                    self.E6.setText(str(int(E6)))
                else:
                    self.E6.setText(format(E6, "7.3f"))

                if E7.is_integer():
                    self.E7.setText(str(int(E7)))
                else:
                    self.E7.setText(format(E7, "7.3f"))

                if E8.is_integer():
                    self.E8.setText(str(int(E8)))
                else:
                    self.E8.setText(format(E8, "7.3f"))

                # Coordenadas

                if x3.is_integer():
                    self.leXS3.setText(str(int(x3)))
                else:
                    self.leXS3.setText(format(x3, "7.2f"))

                if y3.is_integer():
                    self.leYS3.setText(str(int(y3)))
                else:
                    self.leYS3.setText(format(y3, "7.2f"))

                if x4.is_integer():
                    self.leXS4.setText(str(int(x4)))
                else:
                    self.leXS4.setText(format(x4, "7.2f"))

                if y4.is_integer():
                    self.leYS4.setText(str(int(y3)))
                else:
                    self.leYS4.setText(format(y3, "7.2f"))

                if x5.is_integer():
                    self.leXS5.setText(str(int(x5)))
                else:
                    self.leXS5.setText(format(x5, "7.2f"))

                if y5.is_integer():
                    self.leYS5.setText(str(int(y5)))
                else:
                    self.leYS5.setText(format(y5, "7.2f"))

                if x6.is_integer():
                    self.leXS6.setText(str(int(x6)))
                else:
                    self.leXS6.setText(format(x6, "7.2f"))

                if y6.is_integer():
                    self.leYS6.setText(str(int(y6)))
                else:
                    self.leYS6.setText(format(y6, "7.2f"))

                if x7.is_integer():
                    self.leXS7.setText(str(int(x7)))
                else:
                    self.leXS7.setText(format(x7, "7.2f"))

                if y7.is_integer():
                    self.leYS7.setText(str(int(y7)))
                else:
                    self.leYS7.setText(format(y7, "7.2f"))

                if x8.is_integer():
                    self.leXS8.setText(str(int(x8)))
                else:
                    self.leXS8.setText(format(x8, "7.2f"))

                if y8.is_integer():
                    self.leYS8.setText(str(int(y8)))
                else:
                    self.leYS8.setText(format(y8, "7.2f"))


            else:
                x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12, x13, y13, x14, y14, x15, y15, x16, y16 = coord

                E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E12, E13, E14, E15, E16 = energia

                self.O12_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O13_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O14_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O15_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O16_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O17_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O18_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O19_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O110_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O111_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O112_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O113_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O114_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O115_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O116_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O23_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O24_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O25_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O26_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O27_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O28_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O29_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O210_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O211_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O212_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O213_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O214_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O215_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O216_2.setPixmap(QtGui.QPixmap("UIs/check.png"))

                self.O34_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O35_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O36_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O37_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O38_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O39_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O310_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O311_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O312_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O313_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O314_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O315_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O316_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O45_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O46_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O47_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O48_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O49_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O410_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O411_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O412_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O413_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O414_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O415_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O416_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O56_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O57_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O58_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O59_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O510_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O511_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O512_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O513_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O514_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O515_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O516_2.setPixmap(QtGui.QPixmap("UIs/check.png"))

                self.O67_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O68_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O69_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O610_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O611_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O612_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O613_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O614_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O615_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O616_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O78_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O79_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O710_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O711_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O712_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O713_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O714_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O715_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O716_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O89_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O810_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O811_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O812_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O813_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O814_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O815_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O816_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O910_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O911_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O912_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O913_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O914_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O915_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O916_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1011_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1012_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1013_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1014_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1015_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1016_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1112_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O1113_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1114_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1115_2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O1116_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1213_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1214_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1215_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1216_2.setPixmap(QtGui.QPixmap("UIs/check.png"))

                self.O1314_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1315_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1316_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1415_2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1416_2.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1516_2.setPixmap(QtGui.QPixmap("UIs/check.png"))

                self.O12_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O13_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O14_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O15_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O16_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O17_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O18_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O19_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O110_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O111_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O112_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O113_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O114_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O115_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O116_3.setPixmap(QtGui.QPixmap("UIs/check.png"))

                self.O23_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O24_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O25_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O26_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O27_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O28_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O29_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O210_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O211_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O212_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O213_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O214_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O215_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O216_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O34_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O35_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O36_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O37_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O38_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O39_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O310_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O311_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O312_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O313_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O314_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O315_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O316_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O45_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O46_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O47_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O48_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O49_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O410_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O411_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O412_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O413_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O414_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O415_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O416_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O56_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O57_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O58_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O59_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O510_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O511_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O512_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O513_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O514_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O515_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O516_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O67_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O68_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O69_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O610_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O611_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O612_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O613_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O614_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O615_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O616_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O78_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O79_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O710_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O711_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O712_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O713_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O714_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O715_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O716_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O89_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O810_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O811_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O812_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O813_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O814_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O815_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O816_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O910_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O911_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O912_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O913_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O914_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O915_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O916_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1011_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1012_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1013_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O1014_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1015_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1016_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1112_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1113_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1114_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1115_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1116_3.setPixmap(QtGui.QPixmap("UIs/check.png"))

                self.O1213_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1214_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1215_3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O1216_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1314_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1315_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1316_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1415_3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1416_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1516_3.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O12_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O13_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O14_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O15_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O16_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O17_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O18_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O19_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O110_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O111_4.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O112_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O113_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O114_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O115_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O116_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O23_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O24_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O25_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O26_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O27_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O28_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O29_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O210_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O211_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O212_4.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O213_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O214_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O215_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O216_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O34_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O35_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O36_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O37_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O38_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O39_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O310_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O311_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O312_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O313_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O314_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O315_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O316_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O45_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O46_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O47_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O48_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O49_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O410_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O411_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O412_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O413_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O414_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O415_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O416_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O56_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O57_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O58_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O59_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O510_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O511_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O512_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O513_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O514_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O515_4.setPixmap(QtGui.QPixmap("UIs/check.png"))
                self.O516_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O67_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O68_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O69_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O610_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O611_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O612_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O613_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O614_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O615_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O616_4.setPixmap(QtGui.QPixmap("UIs/check.png"))

                self.O78_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O79_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O710_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O711_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O712_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O713_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O714_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O715_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O716_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O89_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O810_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O811_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O812_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O813_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O814_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O815_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O816_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O910_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O911_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O912_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O913_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O914_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O915_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O916_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1011_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1012_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1013_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1014_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1015_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1016_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1112_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1113_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1114_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1115_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1116_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1213_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1214_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1215_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1216_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1314_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1315_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1316_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1415_4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                self.O1416_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                self.O1516_4.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if numCiclos:
                    self.N1.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N2.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N3.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N4.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N5.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N6.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N7.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N8.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N9.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N10.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N11.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N12.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N13.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N14.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N15.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    self.N16.setPixmap(QtGui.QPixmap("UIs/check.png"))
                else:
                    self.N1.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N2.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N3.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N4.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N5.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N6.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N7.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N8.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N9.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N10.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N11.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N12.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N13.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N14.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N15.setPixmap(QtGui.QPixmap("UIs/x.png"))
                    self.N16.setPixmap(QtGui.QPixmap("UIs/x.png"))

                if E3.is_integer():
                    self.E3.setText(str(int(E3)))
                else:
                    self.E3.setText(format(E3, "7.3f"))

                if E4.is_integer():
                    self.E4.setText(str(int(E4)))
                else:
                    self.E4.setText(format(E4, "7.3f"))

                if E5.is_integer():
                    self.E5.setText(str(int(E5)))
                else:
                    self.E5.setText(format(E5, "7.3f"))

                if E6.is_integer():
                    self.E6.setText(str(int(E6)))
                else:
                    self.E6.setText(format(E6, "7.3f"))

                if E7.is_integer():
                    self.E7.setText(str(int(E7)))
                else:
                    self.E7.setText(format(E7, "7.3f"))

                if E8.is_integer():
                    self.E8.setText(str(int(E8)))
                else:
                    self.E8.setText(format(E8, "7.3f"))

                if E9.is_integer():
                    self.E9.setText(str(int(E9)))
                else:
                    self.E9.setText(format(E9, "7.3f"))

                if E10.is_integer():
                    self.E10.setText(str(int(E10)))
                else:
                    self.E10.setText(format(E10, "7.3f"))

                if E11.is_integer():
                    self.E11.setText(str(int(E11)))
                else:
                    self.E11.setText(format(E11, "7.3f"))

                if E12.is_integer():
                    self.E12.setText(str(int(E12)))
                else:
                    self.E12.setText(format(E12, "7.3f"))

                if E13.is_integer():
                    self.E13.setText(str(int(E13)))
                else:
                    self.E13.setText(format(E13, "7.3f"))

                if E14.is_integer():
                    self.E14.setText(str(int(E14)))
                else:
                    self.E14.setText(format(E14, "7.3f"))

                if E15.is_integer():
                    self.E15.setText(str(int(E15)))
                else:
                    self.E15.setText(format(E15, "7.3f"))

                if E16.is_integer():
                    self.E16.setText(str(int(E16)))
                else:
                    self.E16.setText(format(E16, "7.3f"))

                if x3.is_integer():
                    self.leXS3.setText(str(int(x3)))
                else:
                    self.leXS3.setText(format(x3, "7.2f"))

                if y3.is_integer():
                    self.leYS3.setText(str(int(y3)))
                else:
                    self.leYS3.setText(format(y3, "7.2f"))

                if x4.is_integer():
                    self.leXS4.setText(str(int(x4)))
                else:
                    self.leXS4.setText(format(x4, "7.2f"))

                if y4.is_integer():
                    self.leYS4.setText(str(int(y4)))
                else:
                    self.leYS4.setText(format(y4, "7.2f"))

                if x5.is_integer():
                    self.leXS5.setText(str(int(x5)))
                else:
                    self.leXS5.setText(format(x5, "7.2f"))

                if y5.is_integer():
                    self.leYS5.setText(str(int(y5)))
                else:
                    self.leYS5.setText(format(y5, "7.2f"))

                if x6.is_integer():
                    self.leXS6.setText(str(int(x6)))
                else:
                    self.leXS6.setText(format(x6, "7.2f"))

                if y6.is_integer():
                    self.leYS6.setText(str(int(y6)))
                else:
                    self.leYS6.setText(format(y6, "7.2f"))

                if x7.is_integer():
                    self.leXS7.setText(str(int(x7)))
                else:
                    self.leXS7.setText(format(x7, "7.2f"))

                if y7.is_integer():
                    self.leYS7.setText(str(int(y7)))
                else:
                    self.leYS7.setText(format(y7, "7.2f"))

                if x8.is_integer():
                    self.leXS8.setText(str(int(x8)))
                else:
                    self.leXS8.setText(format(x8, "7.2f"))

                if y8.is_integer():
                    self.leYS8.setText(str(int(y8)))
                else:
                    self.leYS8.setText(format(y8, "7.2f"))

                if x9.is_integer():
                    self.leXS9.setText(str(int(x9)))
                else:
                    self.leXS9.setText(format(x9, "7.2f"))

                if y9.is_integer():
                    self.leYS9.setText(str(int(y9)))
                else:
                    self.leYS9.setText(format(y9, "7.2f"))

                if x10.is_integer():
                    self.leXS10.setText(str(int(x10)))
                else:
                    self.leXS10.setText(format(x10, "7.2f"))

                if y10.is_integer():
                    self.leYS10.setText(str(int(y10)))
                else:
                    self.leYS10.setText(format(y10, "7.2f"))

                if x11.is_integer():
                    self.leXS11.setText(str(int(x11)))
                else:
                    self.leXS11.setText(format(x11, "7.2f"))

                if y11.is_integer():
                    self.leYS11.setText(str(int(y11)))
                else:
                    self.leYS11.setText(format(y11, "7.2f"))

                if x12.is_integer():
                    self.leXS12.setText(str(int(x12)))
                else:
                    self.leXS12.setText(format(x12, "7.2f"))

                if y12.is_integer():
                    self.leYS12.setText(str(int(y12)))
                else:
                    self.leYS12.setText(format(y12, "7.2f"))

                if x13.is_integer():
                    self.leXS13.setText(str(int(x13)))
                else:
                    self.leXS13.setText(format(x13, "7.2f"))

                if y13.is_integer():
                    self.leYS13.setText(str(int(y13)))
                else:
                    self.leYS13.setText(format(y13, "7.2f"))

                if x14.is_integer():
                    self.leXS14.setText(str(int(x14)))
                else:
                    self.leXS14.setText(format(x14, "7.2f"))

                if y14.is_integer():
                    self.leYS14.setText(str(int(y14)))
                else:
                    self.leYS14.setText(format(y14, "7.2f"))

                if x15.is_integer():
                    self.leXS15.setText(str(int(x15)))
                else:
                    self.leXS15.setText(format(x15, "7.2f"))

                if y15.is_integer():
                    self.leYS15.setText(str(int(y15)))
                else:
                    self.leYS15.setText(format(y15, "7.2f"))

                if x16.is_integer():
                    self.leXS16.setText(str(int(x16)))
                else:
                    self.leXS16.setText(format(x16, "7.2f"))

                if y16.is_integer():
                    self.leYS16.setText(str(int(y16)))
                else:
                    self.leYS16.setText(format(y16, "7.2f"))

            if E1.is_integer():
                self.E1.setText(str(int(E1)))
            else:
                self.E1.setText(format(E1, "7.3f"))

            if E2.is_integer():
                self.E2.setText(str(int(E2)))
            else:
                self.E2.setText(format(E2, "7.3f"))

            # Dmin
            if dmin.is_integer():
                self.leDmin.setText(str(int(dmin)))
            else:
                self.leDmin.setText(format(dmin, "10.3f"))

            # Coordenadas S1
            if x1.is_integer():
                self.leXS1.setText(str(int(x1)))
            else:
                self.leXS1.setText(format(x1, "7.2f"))

            if y1.is_integer():
                self.leYS1.setText(str(int(y1)))
            else:
                self.leYS1.setText(format(y1, "7.2f"))

            # Coordenadas S2
            if x2.is_integer():
                self.leXS2.setText(str(int(x2)))
            else:
                self.leXS2.setText(format(x2, "7.2f"))

            if y2.is_integer():
                self.leYS2.setText(str(int(y2)))
            else:
                self.leYS2.setText(format(y2, "7.2f"))


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