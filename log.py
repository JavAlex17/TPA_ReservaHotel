import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Login(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Acceso Administración")
        self.setStyleSheet("background-color: #fefeff;")
        self.setMinimumSize(590, 560)
        
        #Agregar una Font personalizada
        font_local = "assets/fonts/PPNeueMachina-PlainRegular.otf"
        font_id = QFontDatabase.addApplicationFont(font_local)
        font = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        
