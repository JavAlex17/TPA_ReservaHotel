from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class MenuDesplegable(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #fefeff; border: 1px solid #BAB78D;")
        self.setFixedWidth(200)
        
         #Agregar una Font personalizada
        font_local = "assets/fonts/PPNeueMachina-PlainRegular.otf"
        font_id = QFontDatabase.addApplicationFont(font_local)
        font = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        layout = QVBoxLayout(self)
        opciones = ["Habitaciones", "Restaurante", "Opción 3", "Opción 4"]
        for opcion in opciones:
            boton = QPushButton(opcion, self)
            boton.setStyleSheet("background-color: #BAB78D; color: #FEFEFF;")
            boton.setFont(QFont(font, 12))  # Usar una fuente genérica o cambiar según sea necesario
            boton.setFixedHeight(50)
            layout.addWidget(boton)
        
        self.hide()
    
    def toggle(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.raise_()
            