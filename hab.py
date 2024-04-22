import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class VentanaHabitaciones(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Habitaciones")
        self.setStyleSheet("background-color: #fefeff;")
        self.setMinimumSize(600, 500)
        
        layout = QVBoxLayout(self)
        
        # Título
        title_label = QLabel("Habitaciones")
        title_label.setStyleSheet("color: #686961; font-style: italic")
        title_label.setFont(QFont("Arial", 30, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        #Listas habitaciones
        self.ListaImagenes = ["images/hab1.jpg", "images/hab2.jpg", "images/hab3.jpg", "images/hab4.jpg", "images/hab5.jpg"]
        self.ListaDisponibilidad = [10,10,10,1,1]
        self.ListaNombres = ["Habitación Ejecutiva Individual", "Habitación Ejecutiva Doble", "Habitación Familiar", "PentHouse Volcanes", "PentHouse Pacifico"]
        self.ListaPrecios = ["$50.000", "$80.000", "$150.000", "$1.080.000", "$1.080.000"]
        self.ListaCapacidad = ["2 (1 Recomendado)", "4 (2 Recomendado)", "8 (6 Recomendado)", "2 (Invitados temporales indefinidos)", "2 (Invitados temporales indefinidos)"]
        self.ListaDestacados = ["Ninguno.", "Ninguno.", "Habitación matrimonial y<br>habitación con camarotes dobles.", "Terraza al aire libre, habitación<br>principal y habitación de invitados.", "Terraza al aire libre, habitación<br>principal y habitación de invitados."]

        #Indice habitacion
        self.indice = 0
        
        #Layout horizontal para la imagen y los botones
        hbox = QHBoxLayout()
        
        #Boton retroceder
        self.boton_atras = QLabel(self)
        pixmap_atras = QPixmap("images/atras.png").scaledToWidth(45) 
        self.boton_atras.setPixmap(pixmap_atras)
        self.boton_atras.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #Lambda event: es para ignorar el evento de moussePressEvent, pero que igualmente se llame a la funcion atras
        self.boton_atras.mousePressEvent = lambda event: self.atras()
        hbox.addWidget(self.boton_atras)
        
        #Imagen habitaciones
        self.image_label = QLabel(self)
        pixmap = QPixmap(self.ListaImagenes[self.indice]).scaledToWidth(400)  # Ruta de la imagen
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hbox.addWidget(self.image_label)
        
        #Boton siguiente
        self.boton_sig = QLabel(self)
        pixmap_atras = QPixmap("images/siguiente.png").scaledToWidth(45) 
        self.boton_sig.setPixmap(pixmap_atras)
        self.boton_sig.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boton_sig.mousePressEvent = lambda event: self.siguiente()
        hbox.addWidget(self.boton_sig)
        
        layout.addLayout(hbox)

        
        # Información debajo de la imagen
        self.info_label = QLabel()
        self.actualizar_info()
        self.info_label.setStyleSheet("color: #686961;")
        self.info_label.setFont(QFont("Arial", 12))
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.info_label)
        
        
    #Funcion para actualizar la informacion
    #Informacion estilizada con html
    def actualizar_info(self):
        nombre_habitacion = f"<div style='color: #686961; font-size: 16pt; margin-left: 20px; font-style: italic; line-height: 1.2;'>{self.ListaNombres[self.indice]}</div>"
        capacidad_personas = f"<div style='margin-left: 50px; font-size: 12pt; line-height: 1.2;'>Capacidad de Personas: {self.ListaCapacidad[self.indice]}</div>"
        servicios_destacados = f"<div style='margin-left: 50px; font-size: 12pt; line-height: 1.2;'>Servicios destacados: {self.ListaDestacados[self.indice]}</div>"
        texto = "<div style='margin-left: 50px; font-size; line-height: 1.2;'>Todas las reservas incluyen desayuno continental para todos los pasajeros.</div>"
        info = f"{nombre_habitacion}{capacidad_personas}{servicios_destacados}{texto}"
        self.info_label.setText(info)
        
    #Funcion botones   
    def siguiente(self):
        self.indice += 1
        if self.indice >= len(self.ListaImagenes):
            self.indice = 0
        self.actualizar_img()
        self.actualizar_info()
        
    def atras(self):
        self.indice -= 1
        if self.indice < 0:
            self.indice = len(self.ListaImagenes) - 1
        self.actualizar_img()
        self.actualizar_info()
        
    #Funcion para actualizar la imagen  
    def actualizar_img(self):
        pixmap = QPixmap(self.ListaImagenes[self.indice]).scaledToWidth(400)
        self.image_label.setPixmap(pixmap)
        

