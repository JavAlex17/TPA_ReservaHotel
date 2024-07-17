from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class VentanaAreas(QDialog):
    volver_habitaciones_signal = pyqtSignal()
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Áreas Comunes")
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
        pixmap_btnmenu = QPixmap("images/flecha.png").scaledToWidth(35)
        self.botonMenu.setPixmap(pixmap_btnmenu)
        self.botonMenu.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        #Lambda event: es para ignorar el evento de moussePressEvent, pero que igualmente se llame a la funcion
        self.botonMenu.mousePressEvent = lambda event: self.mostrar_habitaciones()
    
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

        
        #appbar como widget para agregarle color
        appbarWidget = QWidget()
        appbarWidget.setLayout(appbar_layout)
        appbarWidget.setStyleSheet("background-color: #BAB78D;")
        appbarWidget.setFixedHeight(65)
        
        layout.addWidget(appbarWidget)
        
        
        
        
        layout_titulo = QVBoxLayout()
        # Título
        self.tituloHab = QLabel("Áreas Comunes")
        self.tituloHab.setStyleSheet("color: #686961;")
        self.tituloHab.setFont(QFont(font, 26, QFont.Weight.Bold))
        self.tituloHab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout_titulo.addWidget(self.tituloHab)
        
        tituloWidget = QWidget()
        tituloWidget.setLayout(layout_titulo)
        tituloWidget.setFixedHeight(60)
        
        layout.addWidget(tituloWidget)
        
        #Listas Areas Comunes
        self.ListaImagenes = ["images/area1.jpg", "images/area2.jpg", "images/area3.jpg", "images/area4.png", "images/area5.jpg", "images/area6.jpg"]
        self.ListaNombres = ["Terrenos Bosque Nativo", "Áreas Recreativas", "Piscinas", "Tinas Calientes SPA", "Gimnasio", "Juegos Infantiles"]
        #self.ListaDescripcion = []
    
        
        #Indice areas
        self.indice = 0
        
        #Layout horizontal para la imagen y los botones
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 20)
        
        #Boton retroceder
        self.boton_atras = QLabel(self)
        pixmap_atras = QPixmap("images/atras.png").scaledToWidth(45) 
        self.boton_atras.setPixmap(pixmap_atras)
        self.boton_atras.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #Lambda event: es para ignorar el evento de moussePressEvent, pero que igualmente se llame a la funcion atras
        self.boton_atras.mousePressEvent = lambda event: self.atras()
        hbox.addWidget(self.boton_atras)
        
        #Imagen
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
        
   

        
        
    #Funcion para actualizar la informacion
    #Informacion estilizada con html
    def actualizar_info(self):
        nombre_plan = f"<div style='color: #686961; font-size: 16pt; margin-left: 20px; font-style: italic; line-height: 1.8;'>{self.ListaNombres[self.indice]}</div>"
        #descripcion = f"<div style='margin-left: 45px; font-size: 12pt; line-height: 1.2;'>Capacidad de Personas: {self.ListaDescripcion[self.indice]}</div>"
        info = f"{nombre_plan}"
        self.info_label.setText(info)
        self.info_label.setWordWrap(True)
        
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
        
    def mostrar_habitaciones(self):
        self.close()
        self.volver_habitaciones_signal.emit()
        