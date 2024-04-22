import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from hab import VentanaHabitaciones

class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin,self).__init__()
        self.setWindowTitle('Hotel CTCh')
        self.setStyleSheet("background-color: #fefeff;")
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setMinimumSize(600, 500)
        self.initUI()
        
    def initUI(self):  # sourcery skip: extract-duplicate-method
        layout = QVBoxLayout(self.central_widget)
        
        #Imagen
        image_label = QLabel(self)
        pixmap = QPixmap("images/logo.png").scaledToWidth(200)  # Ruta de la imagen
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)
        
        #Titulo de bienvenida
        welcome_label = QLabel("¡Bienvenido al Hotel CTCh!")
        welcome_label.setStyleSheet("color: #686961; font-style: italic; font-weight: bold")
        welcome_label.setFont(QFont("Segoe UI", 27))
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(welcome_label)
        
        #Subtitulo estilo html
        sub_label = QLabel(
            "<span style='color: #686961; font-size: 13pt; line-height: 1.2;'>"
            "Un espacio de descanso y relajación, con multiples  <br>"
            "instalaciones y actividades enfocadas en la reconección con la naturaleza <br>"
            " con todo el lujo y a comodidad de un hotel 5 estrellas."
            "</span>")
        sub_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub_label.setWordWrap(True)
        layout.addWidget(sub_label)
        
        
        #Boton de entrar
        botonEntrar = QPushButton("Entrar")
        botonEntrar.setStyleSheet("background-color: #BAB78D; color: #686961;")
        botonEntrar.setFont(QFont("Segoe UI", 15))
        botonEntrar.setFixedSize(140,40)  # Ancho máximo del botón
        layout.addWidget(botonEntrar, alignment=Qt.AlignmentFlag.AlignCenter)  # Centrar el botón en el layout

        #botonEntrar.clicked.connect(VentanaHabitaciones.abrirVentanaHabitaciones)
        botonEntrar.clicked.connect(self.abrirVentanaHabitaciones)
        
    def abrirVentanaHabitaciones(self):
        self.close()
        ventana_habitaciones = VentanaHabitaciones()
        ventana_habitaciones.exec()
        
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaMain = MainWin()
    ventanaMain.show()
    sys.exit(app.exec())