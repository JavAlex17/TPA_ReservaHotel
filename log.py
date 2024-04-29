import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from pagRecepcionista import Reservas

class Login(QDialog):
    def __init__(self, main_win=None):
        super().__init__()
        self.main_win = main_win
        
        self.setWindowTitle("Acceso Recepcionista")
        self.setStyleSheet("background-color: #fefeff;")
        self.setMinimumSize(590, 560)
    
        
        #Agregar una Font personalizada
        font_local = "assets/fonts/PPNeueMachina-PlainRegular.otf"
        font_id = QFontDatabase.addApplicationFont(font_local)
        font = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        
        #Lista de Recepcionistas
        self.ListaRecepcionista = [{"Recepcionista1":"12345"},{"Recepcionista":"6789"}]
        
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(10, 30, 10, 10)
        
        #Imagen
        image_label = QLabel(self)
        pixmap = QPixmap("images/logo.png").scaledToWidth(150)  # Ruta de la imagen
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)
        
        # Título
        layout_titulo = QVBoxLayout()
        
        tituloLogin = QLabel("Acceso Recepcionistas")
        tituloLogin.setStyleSheet("color: #686961;")
        tituloLogin.setFont(QFont(font, 20, QFont.Weight.Bold))
        tituloLogin.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        layout_titulo.addWidget(tituloLogin)
        
        tituloWidget = QWidget()
        tituloWidget.setLayout(layout_titulo)
        tituloWidget.setFixedHeight(80)
        
        layout.addWidget(tituloWidget)
        
        
        
        #Input del Usuario
        layoutUsuario = QHBoxLayout()
        layoutUsuario.setContentsMargins(100, 0, 100, 0)
        usuarioLabel = QLabel("Usuario: ")
        usuarioLabel.setStyleSheet("color: #686961;")
        usuarioLabel.setFont(QFont(font, 14))
        layoutUsuario.addWidget(usuarioLabel)
        
        self.usuarioInput = QLineEdit()
        self.usuarioInput.setStyleSheet("background-color: #D9D9D9 ;color: #686961;")
        self.usuarioInput.setFont(QFont(font, 12))
        self.usuarioInput.setFixedWidth(200)
        self.usuarioInput.setFixedHeight(26)
        layoutUsuario.addWidget(self.usuarioInput)
        
        layout.addLayout(layoutUsuario)
        
        #Input contraseña
        layoutPass = QHBoxLayout()
        layoutPass.setContentsMargins(100, 0, 100, 0)
        passLabel = QLabel("Contraseña: ")
        passLabel.setStyleSheet("color: #686961;")
        passLabel.setFont(QFont(font,14))
        layoutPass.addWidget(passLabel)
        
        self.passInput = QLineEdit()
        self.passInput.setStyleSheet("background-color: #D9D9D9 ;color: #686961;")
        self.passInput.setFont(QFont(font,12))
        self.passInput.setFixedWidth(200)
        self.passInput.setFixedHeight(26)
        layoutPass.addWidget(self.passInput)
        
        layout.addLayout(layoutPass)
        
        layoutboton = QHBoxLayout()
        layoutboton.setContentsMargins(200, 50, 200, 0)
        
        botonAtras = QPushButton("Volver")
        botonAtras.setStyleSheet("background-color: #D9D9D9; color: #686961;")
        botonAtras.setFont(QFont(font, 13))
        botonAtras.clicked.connect(self.volverMain)
        layoutboton.addWidget(botonAtras, alignment=Qt.AlignmentFlag.AlignLeft)
        
        botonLogin = QPushButton("Login")
        botonLogin.setStyleSheet("background-color: #BAB78D; color: #FEFEFF;")
        botonLogin.setFont(QFont(font, 13))
        
        botonLogin.clicked.connect(self.iniciarSesion)
                
        layoutboton.addWidget(botonLogin, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(layoutboton)
        
    def iniciarSesion(self):
        usuario = self.usuarioInput.text()
        password = self.passInput.text()
        i = 0
        
        while i < len(self.ListaRecepcionista):      
            i += 1
            for recepcionista in self.ListaRecepcionista:
                if usuario in recepcionista and recepcionista[usuario] == password:
                    self.close()
                    ingresarReservas = Reservas()
                    ingresarReservas.exec()
                    return 
            if i == len(self.ListaRecepcionista):
                print("Error en las credenciales")
                    
                          
    def volverMain(self):
        self.close()
        if self.main_win:
            self.main_win.show()
            
            
