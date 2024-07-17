from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class VentanaContacto(QDialog):
    volver_habitaciones_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contacto")
        self.setStyleSheet("background-color: #fefeff;")
        self.setMinimumSize(590, 560)
        

        # Agregar una Font personalizada
        font_local = "assets/fonts/PPNeueMachina-PlainRegular.otf"
        font_id = QFontDatabase.addApplicationFont(font_local)
        font = QFontDatabase.applicationFontFamilies(font_id)[0]

        # Layout principal de la ventana
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 25, 20, 170)

        # Appbar
        appbar_layout = QGridLayout()
        appbar_layout.setContentsMargins(20, 10, 20, 10)

        # Botón de menú a la izquierda
        self.botonMenu = QLabel(self)
        pixmap_btnmenu = QPixmap("images/flecha.png").scaledToWidth(35)
        self.botonMenu.setPixmap(pixmap_btnmenu)
        self.botonMenu.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.botonMenu.mousePressEvent = lambda event: self.mostrar_habitaciones()  # Lambda para evento de clic
        appbar_layout.addWidget(self.botonMenu, 0, 0)

        # Título del hotel a la derecha
        tituloHotel = QLabel("Hotel CTCh")
        tituloHotel.setStyleSheet('color: #604B32;')
        tituloHotel.setFont(QFont(font, 19))
        tituloHotel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        appbar_layout.addWidget(tituloHotel, 0, 1)

        # Logo del hotel a la derecha de la appbar
        self.logo_appbar = QLabel(self)
        pixmap_logo = QPixmap("images/logoappbar.png").scaledToWidth(45)
        self.logo_appbar.setPixmap(pixmap_logo)
        self.logo_appbar.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        appbar_layout.addWidget(self.logo_appbar, 0, 2)

        # Widget de la appbar para agregarle color
        appbarWidget = QWidget()
        appbarWidget.setLayout(appbar_layout)
        appbarWidget.setStyleSheet("background-color: #BAB78D;")
        appbarWidget.setFixedHeight(65)

        layout.addWidget(appbarWidget)
        
        

        # Título "Contacto"
        self.tituloHab = QLabel("Contacto")
        self.tituloHab.setStyleSheet("color: #686961; margin: 20px;")
        self.tituloHab.setFont(QFont(font, 26, QFont.Weight.Bold))
        self.tituloHab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.tituloHab, alignment=Qt.AlignmentFlag.AlignTop)


    
        # Texto debajo de "Contacto"
        texto_contacto = QLabel(
            "<div style='color: #686961; line-height: 1.65;'>"
            "Nuestros clientes pueden realizar <br>"
            "sus reservas llamando al siguiente número,<br>"
            "donde personal capacitado responderá<br>"
            "todas sus inquietudes y agendará su estadía.<br>"
            "</div>")
        texto_contacto.setFont(QFont(font, 16))
        texto_contacto.setAlignment(Qt.AlignmentFlag.AlignCenter)

    
        layout.addWidget(texto_contacto)
        
        texto_numero = QLabel(
            "<div style='color: #686961; line-height: 1.5;'>"
            "Número: +569 XXXX XXXX<br>"
            "</div>")
        texto_numero.setFont(QFont(font, 18))
        texto_numero.setAlignment(Qt.AlignmentFlag.AlignCenter)

    
        layout.addWidget(texto_numero)

    def mostrar_habitaciones(self):
        self.close()
        self.volver_habitaciones_signal.emit()
