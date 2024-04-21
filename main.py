import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *

class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin,self).__init__()
        uic.loadUi('ventanamain.ui',self)
        self.setWindowTitle('Reserva Hotel')
        self.botonentrar.clicked.connect(self.abrirVentanaHabitaciones)
        
    def abrirVentanaHabitaciones(self):
        uic.loadUi('habitaciones.ui',self)
        self.setWindowTitle('Habitaciones')
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaMain = MainWin()
    ventanaMain.show()
    sys.exit(app.exec())
        
        