"""
Esta clase es la ventana de documentación del simulador.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess


class Ui_TabWidget(object):
    def setupUi(self, TabWidget, availableWidth,availableHeight):
        """
        Método constructor de todos los paramétros de la GUI.

        """
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(1301, 858)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        TabWidget.setFont(font)
        TabWidget.setStyleSheet("QWidget{\n"
"    background-color: rgb(176, 200, 207);\n"
"    font-family: Microsoft Sans Serif;\n"
"}\n"
"\n"
"QTabBar{\n"
"    background:rgb(129, 166, 177);\n"
"    color: black;\n"
"    font-size: 20px\n"
"}\n"
"\n"
"QTabBar:tab{\n"
"    background: rgb(129, 166, 177);\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"    background-color: rgb(176, 200, 207);\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: none;\n"
"    border-radius: 25px\n"
"}\n"
"\n"
"\n"
"")
        TabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        TabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        TabWidget.setDocumentMode(True)
        self.Inicio = QtWidgets.QWidget()
        self.Inicio.setObjectName("Inicio")
        self.gridLayout = QtWidgets.QGridLayout(self.Inicio)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.Inicio)
        self.scrollArea.setStyleSheet("QLabel{\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 22px;\n"
"color: black;\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1256, 1563))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.QLabelSimulador = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.QLabelSimulador.setMinimumSize(QtCore.QSize(600, 100))
        self.QLabelSimulador.setStyleSheet("QLabel{\n"
"qproperty-alignment: AlignCenter;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 50px;\n"
"font-weight: bold;\n"
"border-top: 3px solid black;\n"
"border-bottom: 3px solid black;\n"
"color: black;\n"
"}\n"
"")
        self.QLabelSimulador.setObjectName("QLabelSimulador")
        self.verticalLayout_2.addWidget(self.QLabelSimulador)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.frame3_Inicio = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame3_Inicio.setMinimumSize(QtCore.QSize(400, 200))
        self.frame3_Inicio.setStyleSheet("QFrame    { border: 10 px solid black }\n"
"")
        self.frame3_Inicio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3_Inicio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3_Inicio.setObjectName("frame3_Inicio")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame3_Inicio)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame3_Inicio)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 150))
        self.pushButton.setMaximumSize(QtCore.QSize(10, 16777215))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(244, 15, 2);\n"
"color: rgb(255,255,255);\n"
"font-size: 40px;\n"
"border-radius: 20px;\n"
"text-align: center;\n"
"border: 3px solid black\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(252, 134, 130);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 3, 1, 1)
        self.textBrowser_Boton = QtWidgets.QTextBrowser(self.frame3_Inicio)
        self.textBrowser_Boton.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textBrowser_Boton.setStyleSheet("QTextEdit { border: none }\n"
"")
        self.textBrowser_Boton.setObjectName("textBrowser_Boton")
        self.gridLayout_2.addWidget(self.textBrowser_Boton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame3_Inicio)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.frame1_Inicio = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame1_Inicio.setMinimumSize(QtCore.QSize(400, 600))
        self.frame1_Inicio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1_Inicio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1_Inicio.setObjectName("frame1_Inicio")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame1_Inicio)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame1_Inicio)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("QLabel{\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 22px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_diagramaBloque = QtWidgets.QLabel(self.frame1_Inicio)
        self.label_diagramaBloque.setMinimumSize(QtCore.QSize(200, 200))
        self.label_diagramaBloque.setMaximumSize(QtCore.QSize(5000, 16777215))
        self.label_diagramaBloque.setText("")
        self.label_diagramaBloque.setPixmap(QtGui.QPixmap("UIs\DiagramaBloque.png"))
        self.label_diagramaBloque.setScaledContents(True)
        self.label_diagramaBloque.setAlignment(QtCore.Qt.AlignCenter)
        self.label_diagramaBloque.setIndent(-1)
        self.label_diagramaBloque.setObjectName("label_diagramaBloque")
        self.verticalLayout_3.addWidget(self.label_diagramaBloque, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame1_Inicio)
        self.textBrowser_Inicio = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_Inicio.setMinimumSize(QtCore.QSize(400, 600))
        self.textBrowser_Inicio.setStyleSheet("QTextEdit { \n"
"border: none ;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 25px;\n"
"}\n"
"")
        self.textBrowser_Inicio.setObjectName("textBrowser_Inicio")
        self.verticalLayout_2.addWidget(self.textBrowser_Inicio)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.Inicio)
        self.line_12.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout.addWidget(self.line_12, 1, 0, 1, 1)
        TabWidget.addTab(self.Inicio, "")
        self.DatoAIngresar = QtWidgets.QWidget()
        self.DatoAIngresar.setObjectName("DatoAIngresar")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.DatoAIngresar)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ClasicasNoConvencionales_TAB = QtWidgets.QTabWidget(self.DatoAIngresar)
        self.ClasicasNoConvencionales_TAB.setStyleSheet("QTabBar{\n"
"    background:rgb(129, 166, 177);\n"
"    color: black;\n"
"    font-size: 20px\n"
"}\n"
"\n"
"QTabBar:tab{\n"
"    background: rgb(129, 166, 177);\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"    background-color: rgb(176, 200, 207);\n"
"}\n"
"\n"
"QTabWidget{\n"
"    border: none;\n"
"    border-radius: 25px\n"
"}\n"
"")
        self.ClasicasNoConvencionales_TAB.setObjectName("ClasicasNoConvencionales_TAB")
        self.SenalesClasicas = QtWidgets.QWidget()
        self.SenalesClasicas.setObjectName("SenalesClasicas")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.SenalesClasicas)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.SenalesClasicas)
        self.scrollArea_2.setStyleSheet("QFrame { border: none }\n"
"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1234, 1692))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelSenalesClasicas = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.labelSenalesClasicas.setStyleSheet("QLabel{\n"
"qproperty-alignment: AlignCenter;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 50px;\n"
"font-weight: bold;\n"
"border-top: 3px solid black;\n"
"border-bottom: 3px solid black;\n"
"color: black;\n"
"}\n"
"")
        self.labelSenalesClasicas.setObjectName("labelSenalesClasicas")
        self.verticalLayout_6.addWidget(self.labelSenalesClasicas)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_3.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_6.addWidget(self.line_3)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setMinimumSize(QtCore.QSize(600, 0))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_SClasicas = QtWidgets.QLabel(self.frame)
        self.label_SClasicas.setText("")
        self.label_SClasicas.setPixmap(QtGui.QPixmap("UIs\DatosSC.png"))
        self.label_SClasicas.setScaledContents(True)
        self.label_SClasicas.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SClasicas.setObjectName("label_SClasicas")
        self.horizontalLayout.addWidget(self.label_SClasicas, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_6.addWidget(self.frame)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_4.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_6.addWidget(self.line_4)
        self.textBrowser_SClasicas = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser_SClasicas.setMinimumSize(QtCore.QSize(0, 800))
        self.textBrowser_SClasicas.setStyleSheet("QTextEdit { border: none }\n"
"")
        self.textBrowser_SClasicas.setObjectName("textBrowser_SClasicas")
        self.verticalLayout_6.addWidget(self.textBrowser_SClasicas)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.addWidget(self.scrollArea_2)
        self.line_7 = QtWidgets.QFrame(self.SenalesClasicas)
        self.line_7.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_5.addWidget(self.line_7)
        self.ClasicasNoConvencionales_TAB.addTab(self.SenalesClasicas, "")
        self.SenalesNoConvencionales = QtWidgets.QWidget()
        self.SenalesNoConvencionales.setObjectName("SenalesNoConvencionales")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.SenalesNoConvencionales)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.SenalesNoConvencionales)
        self.scrollArea_3.setStyleSheet("QFrame { border: none }\n"
"")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 544, 1505))
        self.scrollAreaWidgetContents_3.setStyleSheet("QFrame { \n"
"border: none }\n"
"")
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelSNCTitulo = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelSNCTitulo.setStyleSheet("QLabel{\n"
"qproperty-alignment: AlignCenter;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 50px;\n"
"font-weight: bold;\n"
"border-top: 3px solid black;\n"
"border-bottom: 3px solid black;\n"
"color: black;\n"
"}\n"
"")
        self.labelSNCTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSNCTitulo.setObjectName("labelSNCTitulo")
        self.verticalLayout_7.addWidget(self.labelSNCTitulo)
        self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_5.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_7.addWidget(self.line_5)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelSNCSimb = QtWidgets.QLabel(self.frame_2)
        self.labelSNCSimb.setMinimumSize(QtCore.QSize(500, 0))
        self.labelSNCSimb.setText("")
        self.labelSNCSimb.setPixmap(QtGui.QPixmap("UIs\DatosSNCSimb.png"))
        self.labelSNCSimb.setScaledContents(True)
        self.labelSNCSimb.setObjectName("labelSNCSimb")
        self.verticalLayout_8.addWidget(self.labelSNCSimb, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_7.addWidget(self.frame_2)
        self.line_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_6.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_7.addWidget(self.line_6)
        self.textBrowserSNCSimb = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowserSNCSimb.setObjectName("textBrowserSNCSimb")
        self.verticalLayout_7.addWidget(self.textBrowserSNCSimb)
        self.line_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_8.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_7.addWidget(self.line_8)
        self.labelSNCBasesTitulo = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.labelSNCBasesTitulo.setStyleSheet("QLabel{\n"
"qproperty-alignment: AlignCenter;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 50px;\n"
"border-top: 3px solid black;\n"
"font-weight: bold;\n"
"border-bottom: 3px solid black;\n"
"color: black;\n"
"}\n"
"")
        self.labelSNCBasesTitulo.setObjectName("labelSNCBasesTitulo")
        self.verticalLayout_7.addWidget(self.labelSNCBasesTitulo)
        self.line_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_10.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_7.addWidget(self.line_10)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 500))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.labelSNCBases = QtWidgets.QLabel(self.frame_3)
        self.labelSNCBases.setMinimumSize(QtCore.QSize(200, 0))
        self.labelSNCBases.setText("")
        self.labelSNCBases.setPixmap(QtGui.QPixmap("UIs\DatosSNCBases.png"))
        self.labelSNCBases.setScaledContents(True)
        self.labelSNCBases.setObjectName("labelSNCBases")
        self.verticalLayout_9.addWidget(self.labelSNCBases, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.line_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_9.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_7.addWidget(self.line_9)
        self.textBrowserSNCBases = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_3)
        self.textBrowserSNCBases.setObjectName("textBrowserSNCBases")
        self.verticalLayout_7.addWidget(self.textBrowserSNCBases)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollArea_3)
        self.line_11 = QtWidgets.QFrame(self.SenalesNoConvencionales)
        self.line_11.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout.addWidget(self.line_11)
        self.ClasicasNoConvencionales_TAB.addTab(self.SenalesNoConvencionales, "")
        self.verticalLayout_4.addWidget(self.ClasicasNoConvencionales_TAB)
        TabWidget.addTab(self.DatoAIngresar, "")
        self.Resultados = QtWidgets.QWidget()
        self.Resultados.setObjectName("Resultados")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Resultados)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.Resultados)
        self.scrollArea_4.setStyleSheet("QFrame { \n"
"border: none }")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1258, 3743))
        self.scrollAreaWidgetContents_4.setStyleSheet("QFrame { \n"
"border: none }")
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.labelResTitulo = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.labelResTitulo.setStyleSheet("QLabel{\n"
"qproperty-alignment: AlignCenter;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 50px;\n"
"font-weight: bold;\n"
"border-top: 3px solid black;\n"
"border-bottom: 3px solid black;\n"
"color: black;\n"
"}\n"
"")
        self.labelResTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResTitulo.setObjectName("labelResTitulo")
        self.verticalLayout_12.addWidget(self.labelResTitulo)
        self.frame_BotonResultados = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_BotonResultados.setMinimumSize(QtCore.QSize(400, 200))
        self.frame_BotonResultados.setStyleSheet("QFrame    { border: 10 px solid black }\n"
"")
        self.frame_BotonResultados.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_BotonResultados.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_BotonResultados.setObjectName("frame_BotonResultados")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_BotonResultados)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_BotonResultados)
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 150))
        self.pushButton_2.setMaximumSize(QtCore.QSize(10, 16777215))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(244, 15, 2);\n"
"color: rgb(255,255,255);\n"
"font-size: 40px;\n"
"border-radius: 20px;\n"
"text-align: center;\n"
"border: 3px solid black\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(252, 134, 130);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 3, 1, 1)
        self.textBrowser_Boton_2 = QtWidgets.QTextBrowser(self.frame_BotonResultados)
        self.textBrowser_Boton_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.textBrowser_Boton_2.setStyleSheet("QTextEdit { border: none }\n"
"")
        self.textBrowser_Boton_2.setObjectName("textBrowser_Boton_2")
        self.gridLayout_3.addWidget(self.textBrowser_Boton_2, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 1, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 2, 1, 1, 1)
        self.verticalLayout_12.addWidget(self.frame_BotonResultados)
        self.labelResSimbsTitulo = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.labelResSimbsTitulo.setStyleSheet("QLabel{\n"
"qproperty-alignment: AlignCenter;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 50px;\n"
"font-weight: bold;\n"
"border-top: 3px solid black;\n"
"border-bottom: 3px solid black;\n"
"color: black;\n"
"}\n"
"")
        self.labelResSimbsTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResSimbsTitulo.setObjectName("labelResSimbsTitulo")
        self.verticalLayout_12.addWidget(self.labelResSimbsTitulo)
        self.frame_ImgSimbs = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_ImgSimbs.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_ImgSimbs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ImgSimbs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ImgSimbs.setObjectName("frame_ImgSimbs")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_ImgSimbs)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.labelResSimbs = QtWidgets.QLabel(self.frame_ImgSimbs)
        self.labelResSimbs.setMinimumSize(QtCore.QSize(500, 0))
        self.labelResSimbs.setText("")
        self.labelResSimbs.setPixmap(QtGui.QPixmap("UIs\ResSimbs.png"))
        self.labelResSimbs.setScaledContents(True)
        self.labelResSimbs.setObjectName("labelResSimbs")
        self.verticalLayout_11.addWidget(self.labelResSimbs, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_12.addWidget(self.frame_ImgSimbs)
        self.textBrowserResSimbs = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_4)
        self.textBrowserResSimbs.setStyleSheet("")
        self.textBrowserResSimbs.setObjectName("textBrowserResSimbs")
        self.verticalLayout_12.addWidget(self.textBrowserResSimbs)
        self.labelResBitsTitulo = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.labelResBitsTitulo.setStyleSheet("QLabel{\n"
"qproperty-alignment: AlignCenter;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 50px;\n"
"font-weight: bold;\n"
"border-top: 3px solid black;\n"
"border-bottom: 3px solid black;\n"
"color: black;\n"
"}\n"
"")
        self.labelResBitsTitulo.setObjectName("labelResBitsTitulo")
        self.verticalLayout_12.addWidget(self.labelResBitsTitulo)
        self.frame_ImgBits = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_ImgBits.setMinimumSize(QtCore.QSize(500, 500))
        self.frame_ImgBits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ImgBits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ImgBits.setObjectName("frame_ImgBits")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_ImgBits)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.labelResBits = QtWidgets.QLabel(self.frame_ImgBits)
        self.labelResBits.setText("")
        self.labelResBits.setPixmap(QtGui.QPixmap("UIs\ResBits.png"))
        self.labelResBits.setScaledContents(True)
        self.labelResBits.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResBits.setObjectName("labelResBits")
        self.verticalLayout_13.addWidget(self.labelResBits, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_12.addWidget(self.frame_ImgBits)
        self.textBrowserResBits = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_4)
        self.textBrowserResBits.setObjectName("textBrowserResBits")
        self.verticalLayout_12.addWidget(self.textBrowserResBits)
        self.labelResConsTitulo = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.labelResConsTitulo.setStyleSheet("QLabel{\n"
"qproperty-alignment: AlignCenter;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 50px;\n"
"font-weight: bold;\n"
"border-top: 3px solid black;\n"
"border-bottom: 3px solid black;\n"
"color: black;\n"
"}\n"
"")
        self.labelResConsTitulo.setObjectName("labelResConsTitulo")
        self.verticalLayout_12.addWidget(self.labelResConsTitulo)
        self.frame_ImgCons = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_ImgCons.setMinimumSize(QtCore.QSize(500, 500))
        self.frame_ImgCons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ImgCons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ImgCons.setObjectName("frame_ImgCons")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_ImgCons)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.labelResCons = QtWidgets.QLabel(self.frame_ImgCons)
        self.labelResCons.setText("")
        self.labelResCons.setPixmap(QtGui.QPixmap("UIs\ResConstelacion.png"))
        self.labelResCons.setScaledContents(True)
        self.labelResCons.setObjectName("labelResCons")
        self.verticalLayout_14.addWidget(self.labelResCons, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_12.addWidget(self.frame_ImgCons)
        self.textBrowserResCons = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_4)
        self.textBrowserResCons.setObjectName("textBrowserResCons")
        self.verticalLayout_12.addWidget(self.textBrowserResCons)
        self.labelResSenalTitulo = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.labelResSenalTitulo.setStyleSheet("QLabel{\n"
"qproperty-alignment: AlignCenter;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 50px;\n"
"font-weight: bold;\n"
"border-top: 3px solid black;\n"
"border-bottom: 3px solid black;\n"
"color: black;\n"
"}\n"
"")
        self.labelResSenalTitulo.setObjectName("labelResSenalTitulo")
        self.verticalLayout_12.addWidget(self.labelResSenalTitulo)
        self.frame_ImgSenal = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_ImgSenal.setMinimumSize(QtCore.QSize(500, 500))
        self.frame_ImgSenal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ImgSenal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ImgSenal.setObjectName("frame_ImgSenal")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_ImgSenal)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.labelResSenal = QtWidgets.QLabel(self.frame_ImgSenal)
        self.labelResSenal.setText("")
        self.labelResSenal.setPixmap(QtGui.QPixmap("UIs\ResSenal.png"))
        self.labelResSenal.setScaledContents(True)
        self.labelResSenal.setObjectName("labelResSenal")
        self.verticalLayout_15.addWidget(self.labelResSenal, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_12.addWidget(self.frame_ImgSenal)
        self.textBrowserResSenal = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_4)
        self.textBrowserResSenal.setObjectName("textBrowserResSenal")
        self.verticalLayout_12.addWidget(self.textBrowserResSenal)
        self.labelResPeTitulo = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.labelResPeTitulo.setStyleSheet("QLabel{\n"
"qproperty-alignment: AlignCenter;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 50px;\n"
"font-weight: bold;\n"
"border-top: 3px solid black;\n"
"border-bottom: 3px solid black;\n"
"color: black;\n"
"}\n"
"")
        self.labelResPeTitulo.setObjectName("labelResPeTitulo")
        self.verticalLayout_12.addWidget(self.labelResPeTitulo)
        self.frame_ImgPe = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_ImgPe.setMinimumSize(QtCore.QSize(500, 500))
        self.frame_ImgPe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ImgPe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ImgPe.setObjectName("frame_ImgPe")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_ImgPe)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.labelResPe = QtWidgets.QLabel(self.frame_ImgPe)
        self.labelResPe.setText("")
        self.labelResPe.setPixmap(QtGui.QPixmap("UIs\ResPe.png"))
        self.labelResPe.setScaledContents(True)
        self.labelResPe.setObjectName("labelResPe")
        self.verticalLayout_16.addWidget(self.labelResPe, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_12.addWidget(self.frame_ImgPe)
        self.textBrowserResPe = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_4)
        self.textBrowserResPe.setObjectName("textBrowserResPe")
        self.verticalLayout_12.addWidget(self.textBrowserResPe)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_10.addWidget(self.scrollArea_4)
        self.line_13 = QtWidgets.QFrame(self.Resultados)
        self.line_13.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout_10.addWidget(self.line_13)
        TabWidget.addTab(self.Resultados, "")
        self.NumCiclos = QtWidgets.QWidget()
        self.NumCiclos.setObjectName("NumCiclos")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.NumCiclos)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.NumCiclos)
        self.scrollArea_5.setStyleSheet("QFrame { border: none }\n"
"")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 1279, 793))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.labelNumCiclosTitulo = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.labelNumCiclosTitulo.setStyleSheet("QLabel{\n"
"qproperty-alignment: AlignCenter;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 50px;\n"
"font-weight: bold;\n"
"border-top: 3px solid black;\n"
"border-bottom: 3px solid black;\n"
"color: black;\n"
"}\n"
"")
        self.labelNumCiclosTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNumCiclosTitulo.setObjectName("labelNumCiclosTitulo")
        self.verticalLayout_19.addWidget(self.labelNumCiclosTitulo)
        self.frame_ImgNumCiclos = QtWidgets.QFrame(self.scrollAreaWidgetContents_5)
        self.frame_ImgNumCiclos.setMinimumSize(QtCore.QSize(500, 500))
        self.frame_ImgNumCiclos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ImgNumCiclos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ImgNumCiclos.setObjectName("frame_ImgNumCiclos")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_ImgNumCiclos)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.labelNumCiclos = QtWidgets.QLabel(self.frame_ImgNumCiclos)
        self.labelNumCiclos.setText("")
        self.labelNumCiclos.setPixmap(QtGui.QPixmap("UIs\VentanaCiclos.png"))
        self.labelNumCiclos.setScaledContents(True)
        self.labelNumCiclos.setObjectName("labelNumCiclos")
        self.verticalLayout_18.addWidget(self.labelNumCiclos, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_19.addWidget(self.frame_ImgNumCiclos)
        self.textBrowserNumCiclos = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_5)
        self.textBrowserNumCiclos.setObjectName("textBrowserNumCiclos")
        self.verticalLayout_19.addWidget(self.textBrowserNumCiclos)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_17.addWidget(self.scrollArea_5)
        self.line_14 = QtWidgets.QFrame(self.NumCiclos)
        self.line_14.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_17.addWidget(self.line_14)
        TabWidget.addTab(self.NumCiclos, "")
        self.Zoom = QtWidgets.QWidget()
        self.Zoom.setObjectName("Zoom")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.Zoom)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.Zoom)
        self.scrollArea_6.setStyleSheet("QFrame { border: none }\n"
"")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, -1715, 1258, 2508))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.labelZoomTitulo = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.labelZoomTitulo.setStyleSheet("QLabel{\n"
"qproperty-alignment: AlignCenter;\n"
"font-family: Microsoft Sans Serif;\n"
"font-size: 50px;\n"
"font-weight: bold;\n"
"border-top: 3px solid black;\n"
"border-bottom: 3px solid black;\n"
"color: black;\n"
"}\n"
"")
        self.labelZoomTitulo.setObjectName("labelZoomTitulo")
        self.verticalLayout_21.addWidget(self.labelZoomTitulo)
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_6)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.verticalLayout_21.addWidget(self.textBrowser_1)
        self.frame_ImgToolBar = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_ImgToolBar.setMinimumSize(QtCore.QSize(100, 700))
        self.frame_ImgToolBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ImgToolBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ImgToolBar.setObjectName("frame_ImgToolBar")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_ImgToolBar)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.labelToolBar = QtWidgets.QLabel(self.frame_ImgToolBar)
        self.labelToolBar.setText("")
        self.labelToolBar.setPixmap(QtGui.QPixmap("UIs\ToolBarSims.png"))
        self.labelToolBar.setScaledContents(True)
        self.labelToolBar.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelToolBar.setObjectName("labelToolBar")
        self.verticalLayout_22.addWidget(self.labelToolBar)
        self.verticalLayout_21.addWidget(self.frame_ImgToolBar, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line_16 = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.line_16.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.verticalLayout_21.addWidget(self.line_16)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_6)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_21.addWidget(self.textBrowser_2)
        self.frame_Move = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_Move.setMinimumSize(QtCore.QSize(500, 500))
        self.frame_Move.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Move.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Move.setObjectName("frame_Move")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_Move)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowserMove_1 = QtWidgets.QTextBrowser(self.frame_Move)
        self.textBrowserMove_1.setObjectName("textBrowserMove_1")
        self.horizontalLayout_2.addWidget(self.textBrowserMove_1)
        self.labelMove = QtWidgets.QLabel(self.frame_Move)
        self.labelMove.setText("")
        self.labelMove.setPixmap(QtGui.QPixmap("UIs\Arrow.png"))
        self.labelMove.setScaledContents(True)
        self.labelMove.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMove.setObjectName("labelMove")
        self.horizontalLayout_2.addWidget(self.labelMove)
        self.textBrowserMove_2 = QtWidgets.QTextBrowser(self.frame_Move)
        self.textBrowserMove_2.setObjectName("textBrowserMove_2")
        self.horizontalLayout_2.addWidget(self.textBrowserMove_2)
        self.verticalLayout_21.addWidget(self.frame_Move)
        self.frame_Zoom = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_Zoom.setMinimumSize(QtCore.QSize(500, 500))
        self.frame_Zoom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Zoom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Zoom.setObjectName("frame_Zoom")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_Zoom)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowserZoom_1 = QtWidgets.QTextBrowser(self.frame_Zoom)
        self.textBrowserZoom_1.setObjectName("textBrowserZoom_1")
        self.horizontalLayout_3.addWidget(self.textBrowserZoom_1)
        self.labelZoom = QtWidgets.QLabel(self.frame_Zoom)
        self.labelZoom.setText("")
        self.labelZoom.setPixmap(QtGui.QPixmap("UIs\Lupa.png"))
        self.labelZoom.setScaledContents(True)
        self.labelZoom.setAlignment(QtCore.Qt.AlignCenter)
        self.labelZoom.setObjectName("labelZoom")
        self.horizontalLayout_3.addWidget(self.labelZoom)
        self.textBrowserZoom_2 = QtWidgets.QTextBrowser(self.frame_Zoom)
        self.textBrowserZoom_2.setObjectName("textBrowserZoom_2")
        self.horizontalLayout_3.addWidget(self.textBrowserZoom_2)
        self.verticalLayout_21.addWidget(self.frame_Zoom)
        self.frame_Edit = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_Edit.setMinimumSize(QtCore.QSize(500, 500))
        self.frame_Edit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Edit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Edit.setObjectName("frame_Edit")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_Edit)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowserEdit_1 = QtWidgets.QTextBrowser(self.frame_Edit)
        self.textBrowserEdit_1.setObjectName("textBrowserEdit_1")
        self.horizontalLayout_4.addWidget(self.textBrowserEdit_1)
        self.labelEdit = QtWidgets.QLabel(self.frame_Edit)
        self.labelEdit.setText("")
        self.labelEdit.setPixmap(QtGui.QPixmap("UIs\Opc.png"))
        self.labelEdit.setScaledContents(True)
        self.labelEdit.setObjectName("labelEdit")
        self.horizontalLayout_4.addWidget(self.labelEdit)
        self.textBrowserEdit_2 = QtWidgets.QTextBrowser(self.frame_Edit)
        self.textBrowserEdit_2.setObjectName("textBrowserEdit_2")
        self.horizontalLayout_4.addWidget(self.textBrowserEdit_2)
        self.verticalLayout_21.addWidget(self.frame_Edit)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.verticalLayout_20.addWidget(self.scrollArea_6)
        self.line_15 = QtWidgets.QFrame(self.Zoom)
        self.line_15.setStyleSheet("QFrame{\n"
"border: 2px solid black\n"
"}")
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.verticalLayout_20.addWidget(self.line_15)
        TabWidget.addTab(self.Zoom, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        self.ClasicasNoConvencionales_TAB.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

        #Botones
        self.pushButton.clicked.connect(self.documentacion)
        self.pushButton_2.clicked.connect(self.documentacion)

        # Dimensiones Tab Inicio
        self.QLabelSimulador.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.1))
        self.frame1_Inicio.setMinimumSize(int(availableWidth * 0.2), int(availableHeight * 0.4))
        self.label_diagramaBloque.setMinimumSize(int(availableWidth * 0.2), int(availableHeight * 0.1))
        self.label_diagramaBloque.setMaximumSize(int(availableWidth * 0.8), int(availableHeight * 0.9))
        self.frame3_Inicio.setMinimumSize(int(availableWidth * 0.3), int(availableHeight * 0.2))
        self.pushButton.setMinimumSize(int(availableWidth * 0.15), int(availableHeight * 0.15))
        self.textBrowser_Boton.setMinimumSize(int(availableWidth * 0.3), int(availableHeight * 0.3))
        self.textBrowser_Inicio.setMinimumSize(int(availableWidth * 0.9), int(availableHeight * 0.7))

        # Dimensiones Tab Ingresar Datos SeñalesClasicas
        self.labelSenalesClasicas.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.1))
        self.frame.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.6))
        self.label_SClasicas.setMinimumSize(int(availableWidth * 0.1), int(availableHeight * 0.5))
        self.label_SClasicas.setMaximumSize(int(availableWidth * 0.6), int(availableHeight * 0.5))
        self.textBrowser_SClasicas.setMinimumSize(int(availableWidth * 0.95), int(availableHeight * 1.3))
        # self.textBrowser_SClasicas.setMaximumSize(int(availableWidth*0.95), int(availableHeight*0.75))

        # Tab Ingresar Datos SeñalesNC
        self.labelSNCTitulo.setMinimumSize(int(availableWidth * 0.2), int(availableHeight * 0.1))
        self.labelSNCBasesTitulo.setMinimumSize(int(availableWidth * 0.2), int(availableHeight * 0.1))
        self.frame_2.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.6))
        self.labelSNCSimb.setMinimumSize(int(availableWidth * 0.1), int(availableHeight * 0.5))
        self.labelSNCSimb.setMaximumSize(int(availableWidth * 0.6), int(availableHeight * 0.5))
        self.frame_3.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.6))
        self.labelSNCBases.setMinimumSize(int(availableWidth * 0.1), int(availableHeight * 0.5))
        self.labelSNCBases.setMaximumSize(int(availableWidth * 0.6), int(availableHeight * 0.5))
        self.textBrowserSNCSimb.setMinimumSize(int(availableWidth * 0.85), int(availableHeight * 1.6))
        self.textBrowserSNCBases.setMinimumSize(int(availableWidth * 0.85), int(availableHeight * 0.4))

        # Dimensiones Tab Resultados
        self.frame_BotonResultados.setMinimumSize(int(availableWidth * 0.3), int(availableHeight * 0.2))
        self.pushButton_2.setMinimumSize(int(availableWidth * 0.15), int(availableHeight * 0.15))
        self.textBrowser_Boton_2.setMinimumSize(int(availableWidth * 0.3), int(availableHeight * 0.3))

        self.labelResSimbsTitulo.setMinimumSize(int(availableWidth * 0.2), int(availableHeight * 0.1))
        self.labelResTitulo.setMinimumSize(int(availableWidth * 0.2), int(availableHeight * 0.1))
        self.frame_ImgSimbs.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.6))
        self.labelResSimbs.setMinimumSize(int(availableWidth * 0.1), int(availableHeight * 0.5))
        self.labelResSimbs.setMaximumSize(int(availableWidth * 0.6), int(availableHeight * 0.5))
        self.textBrowserResSimbs.setMinimumSize(int(availableWidth * 0.85), int(availableHeight * 0.7))

        self.labelResBitsTitulo.setMinimumSize(int(availableWidth * 0.2), int(availableHeight * 0.1))
        self.frame_ImgBits.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.6))
        self.labelResBits.setMinimumSize(int(availableWidth * 0.1), int(availableHeight * 0.5))
        self.labelResBits.setMaximumSize(int(availableWidth * 0.6), int(availableHeight * 0.5))
        self.textBrowserResBits.setMinimumSize(int(availableWidth * 0.85), int(availableHeight * 0.2))

        self.labelResConsTitulo.setMinimumSize(int(availableWidth * 0.2), int(availableHeight * 0.1))
        self.frame_ImgCons.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.6))
        self.labelResCons.setMinimumSize(int(availableWidth * 0.1), int(availableHeight * 0.5))
        self.labelResCons.setMaximumSize(int(availableWidth * 0.6), int(availableHeight * 0.5))
        self.textBrowserResCons.setMinimumSize(int(availableWidth * 0.85), int(availableHeight * 0.9))

        self.labelResSenalTitulo.setMinimumSize(int(availableWidth * 0.2), int(availableHeight * 0.1))
        self.frame_ImgSenal.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.6))
        self.labelResSenal.setMinimumSize(int(availableWidth * 0.1), int(availableHeight * 0.5))
        self.labelResSenal.setMaximumSize(int(availableWidth * 0.6), int(availableHeight * 0.5))
        self.textBrowserResSenal.setMinimumSize(int(availableWidth * 0.85), int(availableHeight * 1.4))

        self.labelResPeTitulo.setMinimumSize(int(availableWidth * 0.2), int(availableHeight * 0.1))
        self.frame_ImgPe.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.6))
        self.labelResPe.setMinimumSize(int(availableWidth * 0.1), int(availableHeight * 0.5))
        self.labelResPe.setMaximumSize(int(availableWidth * 0.6), int(availableHeight * 0.5))
        self.textBrowserResPe.setMinimumSize(int(availableWidth * 0.85), int(availableHeight * 0.8))

        # Dimensiones Tab Num Ciclos
        self.labelNumCiclosTitulo.setMinimumSize(int(availableWidth * 0.2), int(availableHeight * 0.1))
        self.frame_ImgNumCiclos.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.6))
        self.labelNumCiclos.setMinimumSize(int(availableWidth * 0.1), int(availableHeight * 0.5))
        self.labelNumCiclos.setMaximumSize(int(availableWidth * 0.6), int(availableHeight * 0.5))
        self.textBrowserNumCiclos.setMinimumSize(int(availableWidth * 0.85), int(availableHeight * 0.25))

        # Dimensiones Tab Zoom
        self.labelZoomTitulo.setMinimumSize(int(availableWidth * 0.2), int(availableHeight * 0.1))
        self.frame_ImgToolBar.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.2))
        self.labelToolBar.setMinimumSize(int(availableWidth * 0.1), int(availableHeight * 0.1))
        self.textBrowser_1.setMinimumSize(int(availableWidth * 0.85), int(availableHeight * 0.1))
        self.textBrowser_2.setMinimumSize(int(availableWidth * 0.85), int(availableHeight * 0.1))

        self.frame_Move.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.15))
        self.labelMove.setMinimumSize(int(availableWidth * 0.12), int(availableHeight * 0.1))
        self.textBrowserMove_1.setMinimumSize(int(availableWidth * 0.085), int(availableHeight * 0.1))
        self.textBrowserMove_2.setMinimumSize(int(availableWidth * 0.85), int(availableHeight * 0.1))

        self.frame_Zoom.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.15))
        self.labelZoom.setMinimumSize(int(availableWidth * 0.12), int(availableHeight * 0.1))
        self.textBrowserZoom_1.setMinimumSize(int(availableWidth * 0.085), int(availableHeight * 0.1))
        self.textBrowserZoom_2.setMinimumSize(int(availableWidth * 0.85), int(availableHeight * 0.1))

        self.frame_Edit.setMinimumSize(int(availableWidth * 0.6), int(availableHeight * 0.15))
        self.labelEdit.setMinimumSize(int(availableWidth * 0.12), int(availableHeight * 0.1))
        self.textBrowserEdit_1.setMinimumSize(int(availableWidth * 0.085), int(availableHeight * 0.1))
        self.textBrowserEdit_2.setMinimumSize(int(availableWidth * 0.85), int(availableHeight * 0.1))

    def documentacion(self):
        """
        Abrir PDF de documentación
        """
        subprocess.Popen('Documentación_Simulador.pdf', shell=True)


    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        TabWidget.setWhatsThis(_translate("TabWidget", "<html><head/><body><p>aaaaaaaaaaaaaa</p></body></html>"))

        TabWidget.setWindowTitle("Documentacion")
        TabWidget.setWindowState(QtCore.Qt.WindowMaximized)

        self.QLabelSimulador.setText(_translate("TabWidget", "SIMULADOR DE COMUNICACIONES DIGITALES"))
        self.pushButton.setText(_translate("TabWidget", "PDF"))
        self.textBrowser_Boton.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:600; text-decoration: underline;\">DOCUMENTACIÓN COMPLETA</span></p></body></html>"))
        self.label_2.setText(_translate("TabWidget", "Los resultados de este simulador se basan en el siguiente diagrama de bloque de un sistema de comunicaciones digital:"))
        self.textBrowser_Inicio.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:25px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Los bloques representan:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">1) Codificador de Línea // Modulador: </span><span style=\" font-size:12pt;\">Se genera la señal digital. El simulador posee dos opciones:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    </span><span style=\" font-size:12pt; font-weight:600;\">a. Señales Clásicas: </span><span style=\" font-size:12pt;\">señales estandarizadas con característias conocidas y aplicaciones prácticas.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    </span><span style=\" font-size:12pt; font-weight:600;\">b. Señales No Convencionales: </span><span style=\" font-size:12pt;\">señales cuyos símbolos que la conforman son definidas por el usuario.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    Las señals no convencionales pueden ser ingresadas de dos formas:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">        </span><span style=\" font-size:12pt; font-weight:600;\">- Símbolos:</span><span style=\" font-size:12pt;\"> se especifican directamente la forma de los símbolos.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">        </span><span style=\" font-size:12pt; font-weight:600;\">- Bases:</span><span style=\" font-size:12pt;\"> se especifican las bases de la señal para luego ingresar las coordenadas de cada símbolo en el diagrama de constelación.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">2) Canal AWGN: </span><span style=\" font-size:12pt;\">La señal generada es transmitida por un canal con ruido blanco aditivo gaussiano.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">3) Receptor Óptimo Gram-Schmidt: </span><span style=\" font-size:12pt;\">se utiliza un receptor basado en el proceso de ortogonalización Gram-Schmidt para recuperar la señal transmitida con la menor cantidad de errores posibles.</span></p></body></html>"))
        TabWidget.setTabText(TabWidget.indexOf(self.Inicio), _translate("TabWidget", "Inicio"))
        self.labelSenalesClasicas.setText(_translate("TabWidget", "SEÑALES CLÁSICAS"))
        self.textBrowser_SClasicas.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:8pt; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-size:12pt; font-weight:600;\">Tipo de Señal:</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><a name=\"docs-internal-guid-a9c4f637-7fff-08cf-657c-df5da0b5fffa\"></a><span style=\" font-size:12pt; color:#000000; background-color:transparent;\">E</span><span style=\" font-size:12pt; color:#000000; background-color:transparent;\">ste parámetro define el tipo de señal que se va a simular. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%; font-size:12pt; color:#000000; background-color:transparent;\"><br /></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:12pt; font-weight:696; color:#000000; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-weight:600;\">Amplitud (Volts):</span></li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-size:12pt; color:#000000; background-color:transparent;\">Este parámetro define la amplitud de los símbolos en la señal. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:12pt; font-weight:696; color:#000000; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><a name=\"docs-internal-guid-1508d8ee-7fff-a695-4ac8-a6ed865f60c7\"></a>Frecuencia de portadora (Hertz)</li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-size:12pt; color:#000000; background-color:transparent;\">En las señales pasabanda, este parámetro define la frecuencia de modulación.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-size:12pt; color:#000000; background-color:transparent;\">En FSK, define la frecuencia del símbolo 1.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%; font-size:12pt; color:#000000;\"><br /></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:12pt; font-weight:696; color:#000000; background-color:transparent;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><a name=\"docs-internal-guid-e6c5ca71-7fff-ffe3-dc8c-ce5fe23137ec\"></a>Frecuencia 2 - FSK (Hertz)</li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-size:12pt; color:#000000; background-color:transparent;\">En FSK, este parámetro define la frecuencia de modulación del símbolo 2.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%; font-size:12pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; line-height:138%; background-color:transparent;\"><a name=\"docs-internal-guid-4bacdaae-7fff-c0ba-0746-9e009c6fb1b8\"></a><span style=\" font-size:12pt; font-style:italic; color:#000000;\">    </span><span style=\" font-size:12pt; font-style:italic; color:#000000;\">Para verificar que la combinación de frecuencia de portadora y tiempo de símbolo resulte en símbolos con un número entero de ciclos, puedes utilizar la ventana de Num. Ciclos En Sinusoides.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%; font-size:12pt; font-style:italic; color:#000000; background-color:transparent;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Tiempo de símbolo (segundos)</span><span style=\" font-size:8pt;\"> </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">// Frecuencia de símbolo (símbolos por segundo)</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Este parámetro define la duración de un símbolo en la señal. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">A su vez, define la </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">velocidad de la señal</span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">, ya que su inverso es la frecuencia de los símbolos. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Este valor representa el número de símbolos que se transmiten en un segundo.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Nivel de ruido</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Representa un nivel cualitativo de la potencia del ruido en el canal. Puede ser un nivel de ruido bajo, medio o alto.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Esto va a impactar directamente en la </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Probabilidad de Error </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">de la señal.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; line-height:138%; font-size:12pt; background-color:transparent;\"><br /></p></body></html>"))
        self.ClasicasNoConvencionales_TAB.setTabText(self.ClasicasNoConvencionales_TAB.indexOf(self.SenalesClasicas), _translate("TabWidget", "Señales Clásicas"))
        self.labelSNCTitulo.setText(_translate("TabWidget", "SNC - SÍMBOLOS"))
        self.textBrowserSNCSimb.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Tipo de símbolo</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Este parámetro define la forma del símbolo que se está ingresando. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600; text-decoration: underline;\">Recuerda:</span><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">No deben haber dos símbolos iguales</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">La señal no puede tener más de dos bases.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Por el proceso de ortogonalización Gram-Schmidt, el símbolo 1 no puede ser un pulso nulo.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Amplitud (Volts)</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Este parámetro define la amplitud del símbolo. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Frecuencia de portadora (Hertz)</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En los símbolos pasabanda, este parámetro define la frecuencia de modulación.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-style:italic;\">    - Para verificar que la combinación de frecuencia de portadora y tiempo de símbolo resulte en símbolos con un número entero de ciclos, puedes utilizar la ventana de </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600; font-style:italic;\">Num. Ciclos En Sinusoides.</span><span style=\" font-size:8pt; font-style:italic;\">  -</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Fase (Radianes)</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En el símbolo Coseno, este parámetro define la fase del mismo.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se puede ingresar el número π escribiendo “pi”. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Algunos ejemplos de</span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; color:#202124;\"> sintaxis correcta para la fase: “pi”; “-pi”; “pi/2”; “3pi/4”; “0.75 pi”; </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">“​2.356194”   </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Si se desea ingresar un seno, basta con ingresar en la fase “-pi/2”.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Inicio del símbolo</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En los símbolos de duración variable, este parámetro indica el instante de inicio del símbolo. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se puede elegir entre las opciones: 0; 0.25 TSimb; 0.5 TSimb; 0.75 TSimb</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Duración del símbolo</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En los símbolos de duración variable, este parámetro indica la duración del símbolo. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se indica como un porcentaje relativo a la duración completa del símbolo.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se puede elegir entre las opciones: 25%; 50%; 75%.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Tiempo de símbolo (segundos)</span><span style=\" font-size:8pt;\"> </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">// Frecuencia de símbolo (símbolos por segundo)</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Este parámetro define la duración de un símbolo en la señal. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">A su vez, define la </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">velocidad de la señal</span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">, ya que su inverso es la frecuencia de los símbolos. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">La frecuencia de los símbolos representa el número de símbolos que se transmiten en un segundo.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Nivel de ruido</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Representa un nivel cualitativo de la potencia del ruido en el canal. Puede ser un nivel de ruido bajo, medio o alto.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Esto va a impactar directamente en la </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Probabilidad de Error </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">de la señal.</span><span style=\" font-size:8pt;\"> </span></p></body></html>"))
        self.labelSNCBasesTitulo.setText(_translate("TabWidget", "SNC - BASES"))
        self.textBrowserSNCBases.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Tipo de base</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Este parámetro define la forma de la base que se está ingresando. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-style:italic;\">    Recuerda:</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Las bases </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">deben </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">ser ortogonales entre sí.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Coordenadas de símbolos</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Para cada símbolo, este parámetro define las coordenadas de ubicación en el Diagrama de Constelación.</span><span style=\" font-size:8pt;\"> </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-style:italic;\">    - Los demás parámetros son iguales que en la opción de señales no convencionales - símbolos.</span><span style=\" font-size:8pt; font-style:italic;\"> -</span></p></body></html>"))
        self.ClasicasNoConvencionales_TAB.setTabText(self.ClasicasNoConvencionales_TAB.indexOf(self.SenalesNoConvencionales), _translate("TabWidget", "Señales No Convencionales"))
        TabWidget.setTabText(TabWidget.indexOf(self.DatoAIngresar), _translate("TabWidget", "Datos a Ingresar"))
        self.labelResTitulo.setText(_translate("TabWidget", "RESULTADOS"))
        self.pushButton_2.setText(_translate("TabWidget", "PDF"))
        self.textBrowser_Boton_2.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:600;\">DESCRIPCIÓN COMPLETA DE LOS RESULTADOS</span></p></body></html>"))
        self.labelResSimbsTitulo.setText(_translate("TabWidget", "SÍMBOLOS Y BASES DE LA SEÑAL"))
        self.textBrowserResSimbs.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\"> </span><span style=\" font-size:10pt;\"> </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Símbolos</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En esta gráfica se observan los símbolos que conforman la señal en el dominio del tiempo.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En ella se puede visualizar la duración, amplitud y forma de cada símbolo.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\"> </span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Bases</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En esta gráfica se observan las bases utilizadas para representar la señal en el Diagrama de Constelación.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Las bases son ortogonales entre sí y de energía unitaria. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En la gráfica se enseña la amplitud máxima de cada base.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"> </span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Energía (Joules)</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se visualiza la energía de cada símbolo . </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; color:#212121;\">La energía de un símbolo puede ser calculada en el diagrama de constelación como </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600; color:#212121;\">la distancia del origen hasta la ubicación del símbolo, elevada al cuadrado</span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; color:#212121;\">.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Número de ciclos</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Para los símbolos sinusoides, se visualiza si existe un número entero de ciclos en la duración temporal del símbolo. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.labelResBitsTitulo.setText(_translate("TabWidget", "BITS ALEATORIOS VS SEÑAL"))
        self.textBrowserResBits.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En las señales clásicas, en esta gráfica se visualiza la comparación entre el flujo de bits aleatorios y su correspondiente codificación en una señal bandabase o pasabanda.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Para las señales binarias, se observa como a cada bit se le asignan distintas formas de onda.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Para las señales multinivel (QPSK, 8-PSK y 16QAM), se aprecia que el proceso se realiza para agrupaciones de bits y no con bits individuales. </span></p></body></html>"))
        self.labelResConsTitulo.setText(_translate("TabWidget", "CONSTELACIÓN"))
        self.textBrowserResCons.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Antes del canal</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En esta gráfica se visualiza el Diagrama de Constelación antes de que la señal sea contaminada con ruido.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-style:italic;\">Recuerda:</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">El Diagrama de Constelación es una representación visual de los símbolos en función de las bases obtenidas a través del proceso de ortogonalización Gram-Schmidt </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Después del canal</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En esta gráfica se visualiza el Diagrama de Constelación luego de que la señal sea contaminada con ruido.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">La posición de los símbolos detectados se mueve en el diagrama debido a la presencia del ruido.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Mientras el nivel de ruido es mayor los símbolos detectados están más alejados de su posición original.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se puede intuir una idea del nivel de ruido presente en el canal con está gráfica.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Ortogonalidad/Polaridad/Proporcionalidad</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se visualiza si se cumplen las relaciones de Ortogonalidad, Polaridad y Proporcionalidad entre los símbolos de la señal.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Las relaciones son verificadas mediante el cálculo del</span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\"> factor λ de correlación.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Distancia mínima</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se visualiza la distancia mínima entre dos símbolos en el Diagrama de Constelación.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Una distancia mínima grande puede significar menos errores al detectar la señal, por lo que este parámetro puede ser útil para comparar dos sistemas en relación a su fortaleza frente al ruido.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Coordenadas</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se visualiza el valor numérico de las coordenadas X Y de cada símbolo.</span><span style=\" font-size:10pt;\"> </span></p></body></html>"))
        self.labelResSenalTitulo.setText(_translate("TabWidget", "SEÑAL EN TIEMPO Y FRECUENCIA"))
        self.textBrowserResSenal.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Tiempo</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\"> </span><span style=\" font-size:10pt;\"> </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En esta gráfica se visualiza la señal generada en el dominio del tiempo.</span><span style=\" font-size:10pt;\"> </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"> </span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Esta gráfica presenta la variación de amplitud de la señal (voltaje) con respecto al tiempo.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">La información más relevante que se puede extraer de esta representación es la duración temporal de cada símbolo, que repercute directamente en el ancho de banda práctico de la señal, ya que </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">existe una relación inversa entre ambos parámetros. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600; font-style:italic;\">IMPORTANTE:</span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-style:italic;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-style:italic;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-style:italic;\">La gráfica se enseña a partir del primer símbolo errado. Se puede realizar la comparación entre la gráfica de la señal original con la señal detectada.</span><span style=\" font-size:10pt; font-style:italic;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-style:italic;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; font-style:italic;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-style:italic;\">La gráfica completa consta de 100 símbolos de la señal.</span><span style=\" font-size:10pt; font-style:italic;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Frecuencia</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En esta gráfica se visualiza la señal generada en el dominio de la frecuencia.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Esta gráfica presenta la distribución de la potencia de la señal a lo largo de todo el espectro de las frecuencias. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">La información más importante que se puede extraer de esta representación es el ancho de banda práctico de la señal y poder determinar si la misma es banda base o pasa banda.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Nota:</span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">El eje de la amplitud está normalizado a 1 por razones de facilidad al ajustar la visualización en la gráfica. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se pueden utilizar las dos gráficas (DEP 1 y DEP 2) para compararlas con distintos niveles de zoom.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Potencia de la señal (Wats)</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se visualiza la potencia de la señal. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Energía promedio (Joules)</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se visualiza la energía promedio.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600; color:#202124;\">η</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; color:#202124;\">Se visualiza el valor η del ruido simulado en la señal, proporcional a la potencia del ruido.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; color:#202124;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#202124;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600; color:#202124;\">Número de símbolos errados</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; color:#202124;\">Se visualiza el número de símbolos detectados de forma errónea a causa del ruido.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600; color:#202124;\"> </span><span style=\" font-size:10pt;\"> </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600; color:#202124;\"> </span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; color:#202124;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#202124;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600; color:#202124;\">Ancho de banda práctico</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; color:#202124;\">Se visualiza el ancho de banda práctico de la señal, definido por acumulación de potencia en el lóbulo principal (o lóbulos principales) de la DEP de la señal. </span></p></body></html>"))
        self.labelResPeTitulo.setText(_translate("TabWidget", "PROBABILIDAD DE ERROR"))
        self.textBrowserResPe.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Pe</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En esta gráfica se visualiza el comportamiento de la probabilidad de error de la señal. El eje Y representa probabilidades de error de forma logarítmica y el eje X representa </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">10Log(E/</span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600; color:#202124;\">η</span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">). Se presenta en la gráfica el punto donde se ubica la situación simulada.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"> </span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se presentan dos fórmulas para llegar a la probabilidad de error de una señal. Una aproximación mediante la cota superior de error y directamente a través de los símbolos errados.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"> </span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Cota superior de error</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se visualiza el cálculo de la probabilidad de error mediante cuatro parámetros de la señal:</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Número de distancias igual a la distancia mínima:</span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"> en el diagrama de constelación, se cuenta cuántas de las distancias entre símbolos son iguales a la distancia mínima.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Número de símbolos de la señal.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Distancia mínima entre símbolos en el diagrama de constelación.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600; color:#202124;\">η</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Símbolos errados</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se visualiza el cálculo de la probabilidad de error de forma directa, como el número de errores en el proceso de detección dividido entre el número total de símbolos transmitidos.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ○</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">La correspondencia aproximada entre ambos caminos para obtener la probabilidad de error, valida la cota superior de la probabilidad de error como un método para estimar la probabilidad de error de una señal a partir de sus características y del nivel de ruido en el canal.</span><span style=\" font-size:10pt;\"> </span></p></body></html>"))
        TabWidget.setTabText(TabWidget.indexOf(self.Resultados), _translate("TabWidget", "Resultados"))
        self.labelNumCiclosTitulo.setText(_translate("TabWidget", "Número de ciclos en sinusoides"))
        self.textBrowserNumCiclos.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En esta ventana se puede verificar si las distintas combinaciones de </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-style:italic;\">Frecuencia de Portadora</span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"> y </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-style:italic;\">Tiempo de Símbolo</span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"> resulta en </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">símbolos con número entero de ciclos.</span><span style=\" font-size:10pt; font-weight:600;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Se muestra el resultado para símbolos de duración completa o símbolos de duración variable.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Que los símbolos sinusoides posean un número entero de ciclos es una condición que se cumple en la práctica.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">    ●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt;\">      </span><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">En el simulador, hace que los resultados tengan mejor exactitud.</span><span style=\" font-size:10pt;\"> </span></p></body></html>"))
        TabWidget.setTabText(TabWidget.indexOf(self.NumCiclos), _translate("TabWidget", "Número de ciclos en sinusoides"))
        self.labelZoomTitulo.setText(_translate("TabWidget", "ZOOM Y MOVILIDAD EN GRÁFICAS"))
        self.textBrowser_1.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">Las gráficas poseen una barra de herramientas para modificar la visualización de la gráfica.</span><span style=\" font-size:8pt;\"> </span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt; font-weight:600;\">Las funciones más importantes:</span><span style=\" font-size:8pt; font-weight:600;\"> </span></p></body></html>"))
        self.textBrowserMove_1.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">- Con el ícono</span></p></body></html>"))
        self.textBrowserMove_2.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">se puede mover por la gráfica.</span></p></body></html>"))
        self.textBrowserZoom_1.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">- Con el ícono</span></p></body></html>"))
        self.textBrowserZoom_2.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">se puede hacer zoom.</span></p></body></html>"))
        self.textBrowserEdit_1.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">- Con el ícono</span></p></body></html>"))
        self.textBrowserEdit_2.setHtml(_translate("TabWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft Sans Serif\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft Sans Serif,sans-serif\'; font-size:12pt;\">se abre una ventana que permite, entre otras cosas, cambiar el color de cada gráfica y definir los límites de los eje X Y.</span></p></body></html>"))
        TabWidget.setTabText(TabWidget.indexOf(self.Zoom), _translate("TabWidget", "Zoom y movilidad en gráficas"))