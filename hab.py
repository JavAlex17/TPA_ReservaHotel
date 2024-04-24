import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *



class VentanaHabitaciones(QDialog):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Habitaciones")
        self.setStyleSheet("background-color: #fefeff;")
        self.setMinimumSize(590, 560)
    
        
        #Agregar una Font personalizada
        font_local = "assets/fonts/PPNeueMachina-PlainRegular.otf"
        font_id = QFontDatabase.addApplicationFont(font_local)
        font = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        layout = QVBoxLayout(self)
        
        
        #Agregar una appBar 
        appbar_layout = QGridLayout()
        appbar_layout.setContentsMargins(20, 10, 20, 10)
        
        #Agregar el boton de menu a la izquierda
        self.botonMenu = QLabel(self)
        pixmap_btnmenu = QPixmap("images/menuappbar.png").scaledToWidth(35)
        self.botonMenu.setPixmap(pixmap_btnmenu)
        self.botonMenu.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        #Lambda event: es para ignorar el evento de moussePressEvent, pero que igualmente se llame a la funcion
        #self.botonMenu.mousePressEvent = lambda event: self.abrirMenu()
    
        appbar_layout.addWidget(self.botonMenu,0,0)
        
        #Titulo de la appBar a la derecha
        tituloHotel = QLabel("Hotel CTCh")
        tituloHotel.setStyleSheet('color: #604B32;')
        tituloHotel.setFont(QFont(font, 19))
        tituloHotel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        appbar_layout.addWidget(tituloHotel,0,1)
        
        #Logo del hotel a la derecha de la appBar
        self.logo_appbar = QLabel(self)
        pixmap_logo = QPixmap("images/logoappbar.png").scaledToWidth(45)
        self.logo_appbar.setPixmap(pixmap_logo)
        self.logo_appbar.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        appbar_layout.addWidget(self.logo_appbar,0,2)
        #Lambda event: es para ignorar el evento de moussePressEvent, pero que igualmente se llame a la funcion
        self.logo_appbar.mousePressEvent = lambda event: self.volverMain()
        
        #appbar como widget para agregarle color
        appbarWidget = QWidget()
        appbarWidget.setLayout(appbar_layout)
        appbarWidget.setStyleSheet("background-color: #BAB78D;")
        appbarWidget.setFixedHeight(65)
        
        layout.addWidget(appbarWidget)
        
        layout_titulo = QVBoxLayout()
        # Título
        self.tituloHab = QLabel("Habitaciones")
        self.tituloHab.setStyleSheet("color: #686961;")
        self.tituloHab.setFont(QFont(font, 26, QFont.Weight.Bold))
        self.tituloHab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout_titulo.addWidget(self.tituloHab)
        
        tituloWidget = QWidget()
        tituloWidget.setLayout(layout_titulo)
        tituloWidget.setFixedHeight(60)
        
        layout.addWidget(tituloWidget)
        
        #Listas habitaciones
        self.ListaImagenes = ["images/hab1.png", "images/hab2.jpg", "images/hab3.jpg", "images/hab4.jpg", "images/hab5.jpg"]
        self.ListaDisponibilidad = [10,10,10,1,1]
        self.ListaNombres = ["Habitación Ejecutiva Individual", "Habitación Ejecutiva Doble", "Habitación Familiar", "PentHouse Volcanes", "PentHouse Pacífico"]
        self.ListaPrecios = ["$50.000", "$80.000", "$150.000", "$1.080.000", "$1.080.000"]
        self.ListaCapacidad = ["2 (1 Recomendado)", "4 (2 Recomendado)", "8 (6 Recomendado)", "2 (Invitados temporales indefinidos)", "2 (Invitados temporales indefinidos)"]
        self.ListaDestacados = ["Ninguno.", "Ninguno.", "Habitación matrimonial y<br>habitación con camarotes dobles.", "Terraza al aire libre, habitación<br>principal y habitación de invitados.", "Terraza al aire libre, habitación<br>principal y habitación de invitados."]

        #Indice habitacion
        self.indice = 0
        
        #Layout horizontal para la imagen y los botones
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 5)
        
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
        self.info_label.setFont(QFont(font, 12))
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.info_label)
        
        texto = QLabel(
            "<div style='margin-left: 45px; font-size: 10pt; line-height: 1.2;'>*Todas las reservas incluyen desayuno continental para todos los pasajeros.</div>")
        texto.setAlignment(Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(texto)
        
    #Funcion para actualizar la informacion
    #Informacion estilizada con html
    def actualizar_info(self):
        nombre_habitacion = f"<div style='color: #686961; font-size: 16pt; margin-left: 20px; font-style: italic; line-height: 1.8;'>{self.ListaNombres[self.indice]} - {self.ListaPrecios[self.indice]}</div>"
        disponibilidad = f"<div style='margin-left: 45px; font-size: 12pt; line-height: 1.2;'>Disponibilidad: {self.ListaDisponibilidad[self.indice]}</div>"
        capacidad_personas = f"<div style='margin-left: 45px; font-size: 12pt; line-height: 1.2;'>Capacidad de Personas: {self.ListaCapacidad[self.indice]}</div>"
        servicios_destacados = f"<div style='margin-left: 45px; font-size: 12pt; line-height: 1.2;'>Servicios destacados: {self.ListaDestacados[self.indice]}</div>"
        info = f"{nombre_habitacion}{disponibilidad}{capacidad_personas}{servicios_destacados}"
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
        
        
    def volverMain(self):
        pass
            
    
        

