import json
import locale
import os
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Reservas(QDialog):
    volver_main_signal = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reservas")
        self.setStyleSheet("background-color: #fefeff;")
        self.setMinimumSize(590, 560)

        # Agregar una Font personalizada
        font_local = "assets/fonts/PPNeueMachina-PlainRegular.otf"
        font_id = QFontDatabase.addApplicationFont(font_local)
        font = QFontDatabase.applicationFontFamilies(font_id)[0]

        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Contenedor horizontal para título y logo
        title_logo_layout = QGridLayout()
        title_logo_layout.setContentsMargins(10, 0, 10, 0)
        
        # Botón para volver a Main
        self.volver_main_button = QPushButton()
        self.volver_main_button.setIcon(QIcon("images/back.png"))
        self.volver_main_button.setIconSize(QSize(24, 24))
        self.volver_main_button.setFixedSize(40, 40)  # Ajusta el tamaño
        self.volver_main_button.clicked.connect(self.volver_main)
        
        title_logo_layout.addWidget(self.volver_main_button, 0, 0)


        # Espaciador para empujar el título al centro (1/3 del ancho total)
        left_spacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        title_logo_layout.addItem(left_spacer, 0, 0)

        # Título
        tituloR = QLabel("Reservas")
        tituloR.setStyleSheet("color: #686961;")
        tituloR.setFont(QFont(font, 23))
        tituloR.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom)
        title_logo_layout.addWidget(tituloR, 0, 1)

        # Logo a la derecha
        self.logo = QLabel(self)
        pixmap_logo = QPixmap("images/logo.png").scaledToWidth(70)
        self.logo.setPixmap(pixmap_logo)
        self.logo.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignTop)
        title_logo_layout.addWidget(self.logo, 0, 2)

        # Definir las proporciones de las columnas
        title_logo_layout.setColumnStretch(0, 1)  # Espaciador izquierdo
        title_logo_layout.setColumnStretch(1, 2)  # Título
        title_logo_layout.setColumnStretch(2, 1)  # Logo

        title_logo_widget = QWidget()
        title_logo_widget.setLayout(title_logo_layout)
        title_logo_widget.setFixedHeight(85)

        main_layout.addWidget(title_logo_widget)
        main_layout.addSpacing(20)
    
        # Lista de reservas
        self.reservas_list = QListWidget()
        self.reservas_list.setMinimumWidth(450)
        self.reservas_list.setMinimumHeight(400)
        main_layout.addWidget(self.reservas_list, alignment=Qt.AlignmentFlag.AlignCenter)
        
        
        # Botones
        self.add_button = QPushButton("Agregar Reserva")
        self.add_button.setStyleSheet("background-color: #D9D9D9; color: #686961;")
        self.add_button.setFont(QFont(font, 13))

        self.edit_button = QPushButton("Editar Reserva")
        self.edit_button.setStyleSheet("background-color: #D9D9D9; color: #686961;")
        self.edit_button.setFont(QFont(font, 13))

        self.delete_button = QPushButton("Eliminar Reserva")
        self.delete_button.setStyleSheet("background-color: #D9D9D9; color: #686961;")
        self.delete_button.setFont(QFont(font, 13))

        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(20, 10, 20, 10)
        buttons_layout.addWidget(self.add_button)
        buttons_layout.addWidget(self.edit_button)
        buttons_layout.addWidget(self.delete_button)

        main_layout.addLayout(buttons_layout)
        
        
        # Ruta del archivo JSON
        self.json_file = "disponibilidad_habitaciones.json"
        self.data = self.load_data_from_file()
        self.reservas = self.data.get('reservas', [])
        self.habitaciones = self.data.get('habitaciones', [])
        self.load_data()

        # Conectar botones
        self.add_button.clicked.connect(self.add_reserva)
        self.edit_button.clicked.connect(self.edit_reserva)
        self.delete_button.clicked.connect(self.delete_reserva)
        
        
        
    def load_data_from_file(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        return {"habitaciones": [], "reservas": []}


    def save_data_to_file(self):
        self.data['reservas'] = self.reservas
        with open(self.json_file, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)


    
    def load_data(self):
        self.reservas_list.clear()
        
        # Agregar una Font personalizada
        font_local = "assets/fonts/PPNeueMachina-PlainRegular.otf"
        font_id = QFontDatabase.addApplicationFont(font_local)
        font = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        custom_font = QFont(font, 14)
        
        for reserva in self.reservas:
            item_text =  (f"Reserva #{reserva['id_reserva']} - Estatus: {reserva['status']}\n"
                          f"Nombre cliente: {reserva['nombre_cliente']}\n"
                          f"Habitación: {reserva['habitacion']}\n"
                          f"Restaurante: {reserva['servicio_restaurante']}\n"
                          f"Excursión: {reserva['excursion']}\n"
                          f"Fecha inicio: {reserva['fecha_inicio']}\n"
                          f"Fecha salida: {reserva['fecha_salida']}\n"
                          f"Precio: {reserva['precio']}\n"
                          f"Método de pago: {reserva['metodo_pago']}\n"
                          f"Número de teléfono: {reserva['telefono']}")

            
            list_item = QListWidgetItem(item_text)
            list_item.setFont(custom_font)  # Aplicar la fuente personalizada
            list_item.setForeground(QColor("#686961"))  # Color del texto (en este caso, un gris oscuro)
            # Ajustar altura del item para separar líneas
            list_item.setSizeHint(QSize(list_item.sizeHint().width(), 200)) 
            
            list_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
        
            self.reservas_list.addItem(list_item)

            # Agregar divisor entre elementos
            if reserva != self.reservas[-1]:
                divider = QListWidgetItem()
                divider.setSizeHint(QSize(divider.sizeHint().width(), 5))  # Altura del divisor
                divider.setBackground(QColor("#CCCCCC"))  # Color del divisor
                self.reservas_list.addItem(divider)

    def add_reserva(self):
        new_id = f"{len(self.reservas) + 1:03}"
        nueva_reserva = {
            "id_reserva": new_id,
            "nombre_cliente": "",
            "habitacion": "Habitación Ejecutiva Individual",
            "servicio_restaurante": "No",
            "excursion": "Ninguna",
            "fecha_inicio": "",
            "fecha_salida": "",
            "precio": "",
            "metodo_pago": "Efectivo",
            "telefono": "",
            "status": "En espera"
        }
        dialog = EditReservaDialog(nueva_reserva)
        if dialog.exec():
            nueva_reserva = dialog.get_reserva()
            nueva_reserva["id_reserva"] = new_id
            self.reservas.append(nueva_reserva)
            self.update_habitacion_disponibilidad(nueva_reserva["habitacion"], nueva_reserva["status"])
            self.save_data_to_file()
            self.load_data()

    def edit_reserva(self):
        selected_row = self.reservas_list.currentRow()
        if selected_row >= 0:
            reserva = self.reservas[selected_row]
            old_status = reserva["status"]
            old_habitacion = reserva["habitacion"]  # Habitación anterior
        
            dialog = EditReservaDialog(reserva)
            if dialog.exec():
                nueva_reserva = dialog.get_reserva()
                nueva_reserva["id_reserva"] = reserva["id_reserva"]  # Mantener 'id_reserva' original
                self.reservas[selected_row] = nueva_reserva
            
               # Actualizar disponibilidad de la habitación anterior
                if old_habitacion != nueva_reserva["habitacion"]:
                    self.update_habitacion_disponibilidad(old_habitacion, "Check-out", old_status)
                    self.update_habitacion_disponibilidad(nueva_reserva["habitacion"], nueva_reserva["status"])

                else:
                    self.update_habitacion_disponibilidad(nueva_reserva["habitacion"], nueva_reserva["status"], old_status)
                
                self.save_data_to_file()
                self.load_data()

    def delete_reserva(self):
        selected_row = self.reservas_list.currentRow()
        if selected_row >= 0:
            confirmation = QMessageBox.question(
                self, 'Eliminar Reserva',
                '¿Estás seguro de que deseas eliminar esta reserva?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if confirmation == QMessageBox.StandardButton.Yes:
                reserva = self.reservas.pop(selected_row)
                if reserva["status"] in ["En espera", "Check-in"]:
                   self.update_habitacion_disponibilidad(reserva["habitacion"], "Check-out", reserva["status"])
                self.save_data_to_file()
                self.load_data()

    def update_habitacion_disponibilidad(self, habitacion_nombre, nuevo_status, old_status=None):
        for habitacion in self.habitaciones:
            if habitacion["nombre"] == habitacion_nombre:
                if old_status in ["En espera", "Check-in"]:
                   habitacion["disponibilidad"] += 1
                if nuevo_status in ["En espera", "Check-in"]:
                   habitacion["disponibilidad"] -= 1
                break

            
    def volver_main(self):
        self.close()
        # Emitir la señal para volver a la ventana principal
        self.volver_main_signal.emit()



class EditReservaDialog(QDialog):
    def __init__(self, reserva, parent=None):
        super().__init__(parent)
        
        # Configurar el locale para formateo de moneda
        locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8')
    

        self.setWindowTitle("Editar Reserva")
        self.setModal(True)

        layout = QFormLayout(self)

        self.nombre_cliente = QLineEdit(reserva['nombre_cliente'])
        
        self.habitacion = QComboBox()
        self.habitacion.addItems(["Ejecutiva Individual", "Ejecutiva Doble", "Familiar", "PentHouse Volcanes", "PentHouse Pacífico"])
        self.habitacion.setCurrentText(reserva['habitacion'])
        
        self.servicio_restaurante = QComboBox()
        self.servicio_restaurante.addItems(["Ninguno"] + ["Plan Básico", "Plan Intermedio", "Plan Completo", "Plan Avanzado", "Plan Premium"])
        self.servicio_restaurante.setCurrentText(reserva['servicio_restaurante'])
        self.servicio_restaurante.setCurrentText("Ninguno" if reserva['servicio_restaurante'] == 0 else reserva['servicio_restaurante'])
        
        self.excursion = QComboBox()
        self.excursion.addItems(["Ninguna"] + ["Excursión Light", "Excursión Plus", "Excursión Heavy"])
        self.excursion.setCurrentText("Ninguna" if reserva['excursion'] == 0 else reserva['excursion'])
        
        self.fecha_inicio = QDateEdit()
        self.fecha_inicio.setStyleSheet("color: #686961;")
        self.fecha_inicio.setCalendarPopup(True)
        if reserva["fecha_inicio"]:
            self.fecha_inicio.setDate(QDate.fromString(reserva["fecha_inicio"], "dd-MM-yyyy"))
        else:
            self.fecha_inicio.setDate(QDate.currentDate())

        self.fecha_salida = QDateEdit()
        self.fecha_salida.setStyleSheet("color: #686961;")
        self.fecha_salida.setCalendarPopup(True)
        if reserva["fecha_salida"]:
            self.fecha_salida.setDate(QDate.fromString(reserva["fecha_salida"], "dd-MM-yyyy"))
        else:
            self.fecha_salida.setDate(QDate.currentDate())

        
        self.precio = QLabel(reserva['precio'])
        
        self.metodo_pago = QComboBox()
        self.metodo_pago.addItems(["Tarjeta de Crédito", "Tarjeta de Débito", "Efectivo"])
        self.metodo_pago.setCurrentText(reserva['metodo_pago'])
        
        self.telefono = QLineEdit(reserva['telefono'])
        self.status = QComboBox()
        
        self.status.addItems(["En espera", "Check-in", "Check-out"])
        self.status.setCurrentText(reserva['status'])

        layout.addRow("Nombre cliente:", self.nombre_cliente)
        layout.addRow("Habitación:", self.habitacion)
        layout.addRow("Restaurante:", self.servicio_restaurante)
        layout.addRow("Excursión:", self.excursion)
        layout.addRow("Fecha inicio:", self.fecha_inicio)
        layout.addRow("Fecha salida:", self.fecha_salida)
        layout.addRow("Precio:", self.precio)
        layout.addRow("Método de pago:", self.metodo_pago)
        layout.addRow("Número teléfono:", self.telefono)
        layout.addRow("Status:", self.status)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, Qt.Orientation.Horizontal, self)
        buttons.accepted.connect(self.calcular_precio)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

        self.setLayout(layout)

    def get_reserva(self):
        return {
            "nombre_cliente": self.nombre_cliente.text(),
            "habitacion": self.habitacion.currentText(),
            "servicio_restaurante": self.servicio_restaurante.currentText() if self.servicio_restaurante.currentText() != "Ninguno" else 0,
            "excursion": self.excursion.currentText() if self.excursion.currentText() != "Ninguna" else 0,
            "fecha_inicio": self.fecha_inicio.date().toString("dd-MM-yyyy"),
            "fecha_salida": self.fecha_salida.date().toString("dd-MM-yyyy"),
            "precio": self.precio.text(),
            "metodo_pago": self.metodo_pago.currentText(),
            "telefono": self.telefono.text(),
            "status": self.status.currentText(),
        }

    def calcular_precio(self):
        # Obtener el precio base de la habitación seleccionada
        habitacion_precios = {
            "Ejecutiva Individual": 50000,
            "Ejecutiva Doble": 80000,
            "Familiar": 150000,
            "PentHouse Volcanes": 1080000,
            "PentHouse Pacífico": 1080000,
        }
        habitacion_seleccionada = self.habitacion.currentText()
        precio_total = habitacion_precios.get(habitacion_seleccionada, 0)

        # Agregar el costo del servicio de restaurante si está seleccionado
        if self.servicio_restaurante.currentText() != "Ninguno":
            servicio_restaurante_precios = {
                "Plan Básico": 10000,
                "Plan Intermedio": 25000,
                "Plan Completo": 45000,
                "Plan Avanzado": 60000,
                "Plan Premium": 100000,
            }
            servicio_restaurante_seleccionado = self.servicio_restaurante.currentText()
            precio_total += servicio_restaurante_precios.get(servicio_restaurante_seleccionado, 0)

        # Agregar el costo de la excursión seleccionada (si aplica)
        if self.excursion.currentText() != "Ninguna":
            excursion_precios = {
                "Excursión Light": 5000,
                "Excursión Plus": 25000,
                "Excursión Heavy": 50000,
            }
            excursion_seleccionada = self.excursion.currentText()
            precio_total += excursion_precios.get(excursion_seleccionada, 0)

        # Formatear el precio como moneda
        precio_formateado = "${:,.0f}".format(precio_total)

        # Mostrar el precio calculado
        self.precio.setText(precio_formateado)
        