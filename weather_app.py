import sys
import requests

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from googletrans import Translator

lat = "50.06143"
lon = "19.93658"

def get_weather():
    # api_key = "a873d523875cab9a1f04d55526e2d604"
    # url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    # response = requests.get(url)
    # data = response.json()
    # return data
    return {
        "weather": [
            {
                "description": "clear sky"
            }
        ],
        "main": {
            "temp": 20,
            "feels_like": 21,
            "pressure": 1000,
            "humidity": 50
        },
        "wind": {
            "speed": 10
        }
    }

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

        layout = QHBoxLayout()
        self.central_widget.setLayout(layout)

        image_label = QLabel()
        pixmap = QPixmap("cloudy.png")
        scaled_pixmap = pixmap.scaledToWidth(200)
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(image_label, 1)

        weather_layout = QVBoxLayout()
        layout.addLayout(weather_layout, 2)

        weather = get_weather()
        
        temp = weather["main"]["temp"]
        temp_info = QLabel(f"{temp}ºC")
        temp_info.setObjectName("temperature-info")
        temp_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(temp_info)

        feels_like_temp = weather["main"]["feels_like"]
        feels_like_temp_info = QLabel(f"Odczuwalnie: {feels_like_temp}ºC")
        feels_like_temp_info.setObjectName("other-info")
        feels_like_temp_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(feels_like_temp_info)

        translator = Translator()
        message = weather["weather"][0]["description"]
        translated_message = translator.translate(message, dest="pl").text
        message_info = QLabel(f"Spodziewaj się: {translated_message.lower()}!")
        message_info.setObjectName("other-info")
        message_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(message_info)

        pressure = weather["main"]["pressure"]
        pressure_info = QLabel(f"Ciśnienie:\t{pressure} hPa")
        pressure_info.setObjectName("other-info")
        pressure_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(pressure_info)

        humidity = weather["main"]["humidity"]
        humidity_info = QLabel(f"Wilgotność:\t{humidity}%")
        humidity_info.setObjectName("other-info")
        humidity_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(humidity_info)

        wind_speed = weather["wind"]["speed"]
        wind_speed_info = QLabel(f"Prędkość:\t{wind_speed}km/h")
        wind_speed_info.setObjectName("other-info")
        wind_speed_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
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
