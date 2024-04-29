import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from hab import VentanaHabitaciones
from log import Login

class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin,self).__init__()
        self.setWindowTitle('Hotel CTCh')
        self.setStyleSheet("background-color: #fefeff;")
        
        #Agregar una Font personalizada
        font_local = "assets/fonts/PPNeueMachina-PlainRegular.otf"
        font_id = QFontDatabase.addApplicationFont(font_local)
        font = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setMinimumSize(590, 560)
        self.initUI(font)
        
    def initUI(self, font):
        layout = QVBoxLayout(self.central_widget)
        layout.setContentsMargins(10, 25, 20, 20)
        
        #Imagen
        image_label = QLabel(self)
        pixmap = QPixmap("images/logo.png").scaledToWidth(180)  # Ruta de la imagen
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)
        
        #Titulo de bienvenida
        welcome_label = QLabel("¡Bienvenido al Hotel CTCh!")
        welcome_label.setStyleSheet("color: #686961; font-weight: bold; line-height 1.15")
        welcome_label.setFont(QFont(font, 25))
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(welcome_label)
        
        #Subtitulo estilo html
        sub_label = QLabel(
            "<div style='color: #686961; line-height: 1.25;'>"
            "Un espacio de descanso y relajación, <br>"
            "con multiples instalaciones y<br>"
            "actividades enfocadas en la<br>"
            "reconexión con la naturaleza con<br>"
            "todo el lujo y la comodidad de un<br>"
            "hotel 5 estrellas."
            "</div>")
        sub_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub_label.setFont(QFont(font, 16))
        sub_label.setWordWrap(True)
        layout.addWidget(sub_label)
        
        
        #Boton de entrar
        botonEntrar = QPushButton("Entrar")
        botonEntrar.setStyleSheet("background-color: #BAB78D; color: #FEFEFF;")
        botonEntrar.setFont(QFont(font, 15))
        botonEntrar.setFixedSize(140,40)  # Ancho máximo del botón
        layout.addWidget(botonEntrar, alignment=Qt.AlignmentFlag.AlignCenter)  # Centrar el botón en el layout

        botonEntrar.clicked.connect(self.abrirVentanaHabitaciones)
        
        #Texto para acceso recepcionista
        texto_acceso = QLabel("Acceso Recepcionista")
        texto_acceso.setStyleSheet("color: #686961; text-decoration: underline;")
        texto_acceso.setFont(QFont(font, 12))
        texto_acceso.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        layout.addWidget(texto_acceso)
        
        #Lambda event: es para ignorar el evento de moussePressEvent, pero que igualmente se llame a la funcion
        texto_acceso.mousePressEvent = lambda event: self.abrirAccesoRecepcionista()
        
        
    def abrirVentanaHabitaciones(self):
        self.close()
        ventana_habitaciones = VentanaHabitaciones()
        ventana_habitaciones.show()
        
    def abrirAccesoRecepcionista(self):
        self.close()
        loginRecepcionista = Login(main_win=self)
        loginRecepcionista.exec()
        
        
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaMain = MainWin()
    ventanaMain.show()
    sys.exit(app.exec())