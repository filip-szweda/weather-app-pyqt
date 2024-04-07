import sys
import requests

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from googletrans import Translator

lat = "50.06143"
lon = "19.93658"

base_window_style="background-color: #0A0D11;"
menu_style="background-color: #6272A4; color: #ffffff; font-size: 24px;"
text_box_style="background-color: #F8F8F2; border: 1px #F8F8F2;"
temp_info_style="color: #ffffff; font-size: 96px;"
other_info_style="color: #ffffff; font-size: 24px;"
close_button_style="color: #ffffff; background-color: #FF5555; border: 1px #FF5555;"
save_button_style="background-color: #50FA7B; border: 1px #50FA7B;"

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
        self.setStyleSheet(base_window_style)

        self.create_menu_bar()
        self.create_ui()
        print(lat)

    def create_menu_bar(self):
        menubar = self.menuBar()
        menubar.setStyleSheet(menu_style)

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

    def create_ui(self):
        pass

    def on_latitude_clicked(self):
        latitude_window = ChangeLatitudeWindow()
        latitude_window.show()
        self.windows.append(latitude_window)
        self.close()

    def on_longitude_clicked(self):
        longitude_window = ChangeLongitudeWindow()
        longitude_window.show()
        self.windows.append(longitude_window)
        self.close()

    def on_about_program_clicked(self):
        about_program_window = AboutProgramWindow()
        about_program_window.show()
        self.windows.append(about_program_window)
        self.close()

    def on_city_clicked(self):
        city_window = ChangeCityWindow()
        city_window.show()
        self.windows.append(city_window)
        self.close()

    def on_theme_clicked(self):
        theme_window = ChangeThemeWindow()
        theme_window.show()
        self.windows.append(theme_window)
        self.close()

    def on_weather_clicked(self):
        weather_window = ShowWeatherWindow()
        weather_window.show()
        self.windows.append(weather_window)
        self.close()

class ShowWeatherWindow(BaseWindow):
    def create_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QHBoxLayout()
        self.central_widget.setLayout(layout)

        image_label = QLabel()
        pixmap = QPixmap("cloudy.png")
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(image_label, 1)

        weather_layout = QVBoxLayout()
        layout.addLayout(weather_layout, 2)

        weather = get_weather()
        
        temp = weather["main"]["temp"]
        temp_info = QLabel(f"{temp}ºC")
        temp_info.setStyleSheet(temp_info_style)
        temp_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(temp_info)

        feels_like_temp = weather["main"]["feels_like"]
        feels_like_temp_info = QLabel(f"Odczuwalnie: {feels_like_temp}ºC")
        feels_like_temp_info.setStyleSheet(other_info_style)
        feels_like_temp_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(feels_like_temp_info)

        translator = Translator()
        message = weather["weather"][0]["description"]
        translated_message = translator.translate(message, dest="pl").text
        message_info = QLabel(f"Spodziewaj się: {translated_message.lower()}!")
        message_info.setStyleSheet(other_info_style)
        message_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(message_info)

        pressure = weather["main"]["pressure"]
        pressure_info = QLabel(f"Ciśnienie:\t{pressure} hPa")
        pressure_info.setStyleSheet(other_info_style)
        pressure_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(pressure_info)

        humidity = weather["main"]["humidity"]
        humidity_info = QLabel(f"Wilgotność:\t{humidity}%")
        humidity_info.setStyleSheet(other_info_style)
        humidity_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(humidity_info)

        wind_speed = weather["wind"]["speed"]
        wind_speed_info = QLabel(f"Prędkość:\t{wind_speed}km/h")
        wind_speed_info.setStyleSheet(other_info_style)
        wind_speed_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(wind_speed_info)

class ChangeLatitudeWindow(BaseWindow):
    def create_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(100, 100, 100, 100)

        inner_widget = QWidget()
        inner_layout = QVBoxLayout()
        inner_widget.setLayout(inner_layout)
        inner_widget.setStyleSheet("background-color: #44475A; padding: 10px;")

        close_layout = QHBoxLayout()
        close_layout.addStretch()
        close_button = QPushButton("X")
        close_button.clicked.connect(self.on_weather_clicked)
        close_button.setStyleSheet(close_button_style)
        close_layout.addWidget(close_button)
        inner_layout.addLayout(close_layout)

        latitude_label = QLabel(f"Podaj długość geograficzną:")
        latitude_label.setStyleSheet(other_info_style)
        inner_layout.addWidget(latitude_label)

        self.number_entry = QLineEdit()
        self.number_entry.setPlaceholderText("<długość geograficzna>")
        self.number_entry.setStyleSheet(text_box_style)
        inner_layout.addWidget(self.number_entry)

        save_button = QPushButton("Zatwierdź")
        save_button.clicked.connect(self.save_number)
        save_button.setStyleSheet(save_button_style)
        inner_layout.addWidget(save_button)

        main_layout.addWidget(inner_widget)

        main_widget.setLayout(main_layout)

    def save_number(self):
        global lat
        lat = self.number_entry.text()
        self.on_weather_clicked()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShowWeatherWindow()
    window.show()
    sys.exit(app.exec())
