import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt

class BaseWindow(QMainWindow):
    windows = []

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prognoza Pogody")
        self.setFixedSize(1280, 720)
        self.setObjectName("main-window")

        self.create_menu_bar()
        self.init_ui()

    def create_menu_bar(self):
        menubar = self.menuBar()
        menubar.setObjectName("menu")

        menubar.addMenu("Prognoza Pogody")
        
        localisation_menu = menubar.addMenu("Lokalizacja")
        localisation_menu.setObjectName("menu")

        settings_menu = menubar.addMenu("Ustawienia")
        settings_menu.setObjectName("menu")

        menubar.addAction("O Programie")

        coordinates_menu = localisation_menu.addMenu("Zmień Koordynaty")
        coordinates_menu.setObjectName("menu")

        localisation_menu.addAction("Zmień Miasto")

        length_action = coordinates_menu.addAction("Długość Geo.")
        length_action.triggered.connect(self.on_length_clicked)

        coordinates_menu.addAction("Szerokość Geo.")

        settings_menu.addAction("Motyw")

    def init_ui(self):
        pass

    def on_length_clicked(self):
        length_window = LengthWindow()
        length_window.show()
        self.windows.append(length_window)

class WeatherWindow(BaseWindow):
    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        weather_layout = QVBoxLayout()
        layout.addLayout(weather_layout)

        temperature_info = QLabel("12ºC")
        temperature_info.setObjectName("temperature-info")
        temperature_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        weather_layout.addWidget(temperature_info)

        felt_temperature_info = QLabel("Odczuwalnie: 11ºC")
        felt_temperature_info.setObjectName("other-info")
        felt_temperature_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        weather_layout.addWidget(felt_temperature_info)

        message_info = QLabel("Spodziewaj się dnia z częściowym zachmurzeniem i deszczem!")
        message_info.setObjectName("other-info")
        message_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        weather_layout.addWidget(message_info)

        pressure_info = QLabel("Ciśnienie:\t\t1014 hPa")
        pressure_info.setObjectName("other-info")
        pressure_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        weather_layout.addWidget(pressure_info)

        moisture_info = QLabel("Wilgotność:\t\t91%")
        moisture_info.setObjectName("other-info")
        moisture_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        weather_layout.addWidget(moisture_info)

        wind_speed_info = QLabel("Prędkość:\t\t8km/h")
        wind_speed_info.setObjectName("other-info")
        wind_speed_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        weather_layout.addWidget(wind_speed_info)

class LengthWindow(BaseWindow):
    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        length_layout = QVBoxLayout()
        layout.addLayout(length_layout)

        length_info = QLabel("Długość geograficzna: 50.06143")
        length_info.setObjectName("other-info")
        length_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        length_layout.addWidget(length_info)

        length_info = QLabel("Długość geograficzna: 19.93658")
        length_info.setObjectName("other-info")
        length_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        length_layout.addWidget(length_info)

        length_info = QLabel("Długość geograficzna: 50.06143")
        length_info.setObjectName("other-info")
        length_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        length_layout.addWidget(length_info)

        length_info = QLabel("Długość geograficzna: 19.93658")
        length_info.setObjectName("other-info")
        length_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        length_layout.addWidget(length_info)

        length_info = QLabel("Długość geograficzna: 50.06143")
        length_info.setObjectName("other-info")
        length_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        length_layout.addWidget(length_info)

        length_info = QLabel("Długość geograficzna: 19.93658")
        length_info.setObjectName("other-info")
        length_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        length_layout.addWidget(length_info)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        with open("styles.css", "r") as file:
            app.setStyleSheet(file.read())
    except FileNotFoundError:
        print("Nie można odnaleźć pliku styles.css")
    window = WeatherWindow()
    window.show()
    sys.exit(app.exec())
