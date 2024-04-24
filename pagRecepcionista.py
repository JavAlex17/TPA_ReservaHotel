import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Reservas(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Reservas")
        self.setStyleSheet("background-color: #fefeff;")
        self.setMinimumSize(590, 560)
    
        
        #Agregar una Font personalizada
        font_local = "assets/fonts/PPNeueMachina-PlainRegular.otf"
        font_id = QFontDatabase.addApplicationFont(font_local)
        font = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(10, 30, 10, 10)
        
        # Título
        layout_titulo = QVBoxLayout()
        
        tituloR = QLabel("Reservas")
        tituloR.setStyleSheet("color: #686961;")
        tituloR.setFont(QFont(font, 20, QFont.Weight.Bold))
        tituloR.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        layout_titulo.addWidget(tituloR)
        
        tituloWidget = QWidget()
        tituloWidget.setLayout(layout_titulo)
        tituloWidget.setFixedHeight(200)
        
        layout.addWidget(tituloWidget)
        