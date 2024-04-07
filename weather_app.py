import sys
import requests

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt

lat = "50.06143"
lon = "19.93658"

def get_weather():
    api_key = "a873d523875cab9a1f04d55526e2d604"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

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

        latitude_action = coordinates_menu.addAction("Długość Geo.")
        latitude_action.triggered.connect(self.on_latitude_clicked)

        coordinates_menu.addAction("Szerokość Geo.")

        settings_menu.addAction("Motyw")

    def init_ui(self):
        pass

    def on_latitude_clicked(self):
        latitude_window = LatitudeWindow()
        latitude_window.show()
        self.windows.append(latitude_window)

class WeatherWindow(BaseWindow):
    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        weather_layout = QVBoxLayout()
        layout.addLayout(weather_layout)

        weather = get_weather()
        
        temperature = weather["main"]["temp"]
        temperature_info = QLabel(f"{temperature}ºC")
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

class LatitudeWindow(BaseWindow):
    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        latitude_layout = QVBoxLayout()
        layout.addLayout(latitude_layout)

        latitude_info = QLabel("Długość geograficzna: 50.06143")
        latitude_info.setObjectName("other-info")
        latitude_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        latitude_layout.addWidget(latitude_info)

        latitude_info = QLabel("Długość geograficzna: 19.93658")
        latitude_info.setObjectName("other-info")
        latitude_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        latitude_layout.addWidget(latitude_info)

        latitude_info = QLabel("Długość geograficzna: 50.06143")
        latitude_info.setObjectName("other-info")
        latitude_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        latitude_layout.addWidget(latitude_info)

        latitude_info = QLabel("Długość geograficzna: 19.93658")
        latitude_info.setObjectName("other-info")
        latitude_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        latitude_layout.addWidget(latitude_info)

        latitude_info = QLabel("Długość geograficzna: 50.06143")
        latitude_info.setObjectName("other-info")
        latitude_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        latitude_layout.addWidget(latitude_info)

        latitude_info = QLabel("Długość geograficzna: 19.93658")
        latitude_info.setObjectName("other-info")
        latitude_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        latitude_layout.addWidget(latitude_info)


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
