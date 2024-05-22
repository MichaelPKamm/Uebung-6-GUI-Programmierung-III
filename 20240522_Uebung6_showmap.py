from PyQt5.QtWidgets import*
from PyQt5.uic import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import urllib.parse

class fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('2060_Geoprogrammierung/20240522_Uebung6_showmap.ui', self)

        self.Karte.clicked.connect(self.funktion)
    
    def funktion(self):
        addresse = f"{self.Breite.text()},{self.Laenge.text()}"
        query = urllib.parse.quote(addresse)
        link = f"https://www.google.ch/maps/place/{query}"
        QDesktopServices.openUrl(QUrl(link))
        

app = QApplication ([])

window = fenster()
window.show()

app.exec()