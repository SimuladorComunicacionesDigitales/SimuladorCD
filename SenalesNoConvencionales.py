from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow
from ScreenSimbolos2 import ScreenSimbolos2
from ScreenSimbolos3 import ScreenSimbolos3
from ScreenSimbolos4 import ScreenSimbolos4
from ScreenBases2 import ScreenBases2
from ScreenBases3 import ScreenBases3
from ScreenBases4 import ScreenBases4


class SenalesNoConvencionales(QMainWindow):
    def __init__(self, widget,frameSizeWidth, frameSizeHeight, fSample, nTotalSimb,sizeHeight):
        super(SenalesNoConvencionales, self).__init__()
        loadUi("UIs\SNC_MainWindow.ui", self)
        self.widget = widget
        self.widget.insertWidget(2, self)
        self.sizeHeight = sizeHeight

        self.frameSizeWidth = frameSizeWidth
        self.frameSizeHeight = frameSizeHeight
        self.fSample = fSample
        self.nTotalSimb = nTotalSimb

        self.cbNumSimb.currentTextChanged.connect(self.numeroSimbolos)
        self.SimbolosButton.clicked.connect(self.goToScreenSimbolos)
        self.BasesButton.clicked.connect(self.goToScreenBases)
        self.BackButton.clicked.connect(self.goToMainWindow)

    def goToMainWindow(self):
        self.widget.setCurrentIndex(0)

    def numeroSimbolos(self, nroSimb):
        nroSimb = int(nroSimb)
        self.whichScreenSimb(nroSimb)
        self.whichScreenBases(nroSimb)
        #return nroSimb

    def whichScreenSimb(self, nroSimb):
        if nroSimb == 2:
            screenSimb = ScreenSimbolos2(self.widget,self.frameSizeWidth, self.frameSizeHeight, self.fSample, self.nTotalSimb,self.sizeHeight)
        elif nroSimb == 3:
            screenSimb = ScreenSimbolos3(self.widget,self.frameSizeWidth, self.frameSizeHeight, self.fSample, self.nTotalSimb,self.sizeHeight)
        elif nroSimb == 4:
            screenSimb = ScreenSimbolos4(self.widget,self.frameSizeWidth, self.frameSizeHeight, self.fSample, self.nTotalSimb,self.sizeHeight)

        self.widget.insertWidget(3, screenSimb)
        return screenSimb

    def whichScreenBases(self, nroSimb):
        if nroSimb == 2:
            screenBases = ScreenBases2(self.widget,self.frameSizeWidth, self.frameSizeHeight, self.fSample, self.nTotalSimb,self.sizeHeight)
        elif nroSimb == 3:
            screenBases = ScreenBases3(self.widget,self.frameSizeWidth, self.frameSizeHeight, self.fSample, self.nTotalSimb,self.sizeHeight)
        elif nroSimb == 4:
            screenBases = ScreenBases4(self.widget,self.frameSizeWidth, self.frameSizeHeight, self.fSample, self.nTotalSimb,self.sizeHeight)

        self.widget.insertWidget(4, screenBases)
        return screenBases

    def goToScreenSimbolos(self):
        self.widget.setCurrentIndex(3)

    def goToScreenBases(self):
        self.widget.setCurrentIndex(4)
