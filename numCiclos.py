"""
Esta clase es la ventana 'Numero de Ciclos en Sinusoides' del simulador.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import math


class Ui_CalcuFreqWindow(object):
    def setupUi(self, CalcuFreqWindow):
        """
        Método constructor de todos los paramétros de la GUI.
        """

        CalcuFreqWindow.setObjectName("Verificar número de ciclos enteros")
        CalcuFreqWindow.resize(757, 545)
        self.centralwidget = QtWidgets.QWidget(CalcuFreqWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background: rgb(0, 23, 71);\n"
"font-family: Microsoft Sans Serif;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(1, 179, 191);\n"
"font-size: 40px;\n"
"border-radius: 20px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(77, 242, 243);\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgb(0, 23, 71)\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 20px;\n"
"color: black;\n"
"}\n"
"\n"
"QSlider\n"
"{\n"
"   background-color: transparent;\n"
"   padding: 2px;\n"
"\n"
"}\n"
"\n"
"QSlider::groove:horizontal\n"
"{\n"
"    subcontrol-origin: content;\n"
"    background-color: transparent;\n"
"    height: 17px;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal\n"
"{\n"
"   background-color: rgb(255, 177, 64);\n"
"   width: 16px;\n"
"   border-radius: 7px;\n"
"\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal\n"
"{\n"
"   background-color: white;\n"
"   margin: 4px;\n"
"   border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"QSlider::add-page:horizontal\n"
"{\n"
"   background-color: white;\n"
"   margin: 4px;\n"
"   border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"QSpinBox{\n"
"background-color: white;\n"
"qproperty-alignment: AlignCenter;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"background-color: white;\n"
"qproperty-alignment: AlignCenter;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"qproperty-alignment: AlignCenter;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 25px;\n"
"border-top: 3px solid white;\n"
"border-bottom: 3px solid white;\n"
"color: white;\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 300))
        self.widget.setStyleSheet("QWidget{\n"
"background-color: rgb(98, 146, 158)\n"
"}")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalSlider_tSimb = QtWidgets.QSlider(self.widget)
        self.horizontalSlider_tSimb.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_tSimb.setObjectName("horizontalSlider_tSimb")
        self.gridLayout.addWidget(self.horizontalSlider_tSimb, 2, 1, 1, 1)
        self.label_FreqSimbolo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_FreqSimbolo.setFont(font)
        self.label_FreqSimbolo.setStyleSheet("QLabel{\n"
"color: white\n"
"}")
        self.label_FreqSimbolo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FreqSimbolo.setObjectName("label_FreqSimbolo")
        self.gridLayout.addWidget(self.label_FreqSimbolo, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.doubleSpinBox_tSimb = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_tSimb.setObjectName("doubleSpinBox_tSimb")
        self.gridLayout.addWidget(self.doubleSpinBox_tSimb, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 50))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 2, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.widget)
        self.horizontalSlider.setMinimum(10)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setStyleSheet("QWidget{\n"
"background-color: white\n"
"}")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(98, 146, 158)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMaximumSize(QtCore.QSize(100, 100))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("UIs/check.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setMaximumSize(QtCore.QSize(100, 100))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("UIs/x.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout.addWidget(self.line_6)
        CalcuFreqWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CalcuFreqWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 24))
        self.menubar.setObjectName("menubar")
        CalcuFreqWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CalcuFreqWindow)
        self.statusbar.setObjectName("statusbar")
        CalcuFreqWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CalcuFreqWindow)
        self.horizontalSlider.valueChanged['int'].connect(self.spinBox.setValue)
        self.spinBox.valueChanged['int'].connect(self.horizontalSlider.setValue)
        QtCore.QMetaObject.connectSlotsByName(CalcuFreqWindow)

        self.doubleSpinBox_tSimb.setRange(0.1, 2)
        self.doubleSpinBox_tSimb.setSingleStep(0.1)
        self.doubleSpinBox_tSimb.setDecimals(1)

        self.horizontalSlider_tSimb.setRange(1, 20)
        self.horizontalSlider_tSimb.setSingleStep(1)

        self.doubleSpinBox_tSimb.valueChanged.connect(self.spinBoxInt)
        self.horizontalSlider_tSimb.valueChanged.connect(self.sliderFloat)

        self.horizontalSlider.valueChanged.connect(self.actualizarValor)

        self.horizontalSlider_tSimb.valueChanged.connect(self.actualizarValor)

    def spinBoxInt(self, value):
            """
            Este método actualiza el valor del slider del Tiempo de Simbolo (int) con el SpinBox del Tiempo de Simbolo (float).
            Adicionalmente actualiza el label con la Frecuencia de Simbolo.
            """

            self.horizontalSlider_tSimb.setValue(int(value * 10))
            fSimb = 1/value
            if fSimb.is_integer():
                    self.label_FreqSimbolo.setText(str(int(fSimb)))
            else:
                self.label_FreqSimbolo.setText(str(format(1 / value, "<7.3f")))

    def sliderFloat(self, value):
            """
            Este método actualiza el valor del SpinBox del Tiempo de Simbolo (float) con el Slider del Tiempo de Simbolo (int).
            """
            self.doubleSpinBox_tSimb.setValue(value / 10)

    def actualizarValor(self):
            """
            Este método calcula si la combinación entre Tiempo de Simbolo y Frecuencia de Portadora resulta en un simbolo de ciclos enteros.
            Utiliza el resto de la división entre la Frecuencia de Simbolo y la Frecuencia de Portadora.
            """

            freqPortadora = int(self.spinBox.value())
            freqSimbolo = 1 / (self.doubleSpinBox_tSimb.value())

            x = freqPortadora
            y = round(freqSimbolo, 16)
            y2 = round(freqSimbolo * 4, 16)
            div = x / y
            div2 = x / y2

            if math.isclose(0.769230769231, freqSimbolo):
                    resto1 = math.fmod(freqPortadora, round(freqSimbolo, 10))
                    resto2 = math.fmod(freqPortadora, round(4 * freqSimbolo, 10))

                    if math.isclose(resto1, 0, abs_tol=0.01):
                            self.label_6.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    else:
                            self.label_6.setPixmap(QtGui.QPixmap("UIs/x.png"))

                    if math.isclose(resto2, 0, abs_tol=0.01):
                            self.label_7.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    else:
                            self.label_7.setPixmap(QtGui.QPixmap("UIs/x.png"))

            else:

                    if div.is_integer():
                            self.label_6.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    else:
                            self.label_6.setPixmap(QtGui.QPixmap("UIs/x.png"))

                    if div2.is_integer():
                            self.label_7.setPixmap(QtGui.QPixmap("UIs/check.png"))
                    else:
                            self.label_7.setPixmap(QtGui.QPixmap("UIs/x.png"))

    def retranslateUi(self, CalcuFreqWindow):
        _translate = QtCore.QCoreApplication.translate
        CalcuFreqWindow.setWindowTitle(_translate("CalcuFreqWindow", "Verificar número de ciclos en portadoras"))
        self.label.setText(_translate("CalcuFreqWindow", "NÚMERO ENTERO DE CICLOS EN UN SÍMBOLO SINUSOIDE"))
        self.label_3.setText(_translate("CalcuFreqWindow", "Tiempo de Símbolo:"))
        self.label_FreqSimbolo.setText(_translate("CalcuFreqWindow", "10"))
        self.label_2.setText(_translate("CalcuFreqWindow", "Frecuencia de portadora:"))
        self.label_4.setText(_translate("CalcuFreqWindow", "Frecuencia de Símbolo:"))
        self.label_8.setText(_translate("CalcuFreqWindow", "Número entero de ciclos en símbolo de duración variable:"))
        self.label_5.setText(_translate("CalcuFreqWindow", "Número entero de ciclos en símbolo de duración completa:"))