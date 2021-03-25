import os
import sys

from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtCore import pyqtSignal, QThread, QTimer
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QAction, QVBoxLayout, QLabel, QBoxLayout

_scriptdir = os.path.dirname(os.path.realpath(__file__))

class MainDialog(*uic.loadUiType(os.path.join(_scriptdir, 'ui', 'main_dialog.ui'))):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        layout = QVBoxLayout()
        self.HiggsBozon.setGeometry(QtCore.QRect(100, 270, 126, 25))
        self.Photon.setGeometry(QtCore.QRect(100, 357, 126, 25))
        self.WZbozon.setGeometry(QtCore.QRect(250, 270, 126, 25))
        self.Gluon.setGeometry(QtCore.QRect(250, 357, 126, 25))
        self.HiggsBozon.setText('<a href="https://ru.wikipedia.org/wiki/Бозон_Хиггса"> Бозон Хиггса </a>')
        self.Photon.setText('<a href="https://ru.wikipedia.org/wiki/%D0%A4%D0%BE%D1%82%D0%BE%D0%BD"> Фотон </a>')
        self.WZbozon.setText('<a href="https://ru.wikipedia.org/wiki/W-_%D0%B8_Z-%D0%B1%D0%BE%D0%B7%D0%BE%D0%BD%D1%8B"> W и Z бозоны </a>')
        self.Gluon.setText('<a href="https://ru.wikipedia.org/wiki/%D0%93%D0%BB%D1%8E%D0%BE%D0%BD"> Глюон </a>')
        self.HiggsBozon.setOpenExternalLinks(True)
        self.Photon.setOpenExternalLinks(True)
        self.WZbozon.setOpenExternalLinks(True)
        self.Gluon.setOpenExternalLinks(True)
        layout.addWidget(self.HiggsBozon)
        layout.addWidget(self.WZbozon)
        layout.addWidget(self.Gluon)
        layout.addWidget(self.Photon)
        self.setLayout(layout)
        self.bindEvents()
        
    def bindEvents(self):
        self.closeButton.clicked.connect(self.close)


if __name__== '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainDialog()
    w.show()
    sys.exit(app.exec_())
