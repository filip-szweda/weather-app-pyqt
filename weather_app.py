import sys
import requests

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QDialog, QLineEdit, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from googletrans import Translator

api_key = "a873d523875cab9a1f04d55526e2d604"

is_sunny = True

lon = "19.93658"
lat = "50.06143"

background_color, foreground_color, selection_color, text_field_color = "#0A0D11", "#6272A4", "#44475A", "#F8F8F2"

base_window_style, menu_style, text_field_style, temp_info_style, other_info_style, about_program_style, close_button_style, save_button_style, inner_widget_style, color_picker_style = "", "", "", "", "", "", "", "", "", ""

def setup_styles():
    global base_window_style, menu_style, text_field_style, temp_info_style, other_info_style, about_program_style, close_button_style, save_button_style, inner_widget_style, color_picker_style
    base_window_style=f"background-color: {background_color};"
    menu_style="QMenuBar {background-color: " + foreground_color + "; color: #FFFFFF; font-size: 24px;} QMenuBar::item::selected {background-color: " + selection_color + "; } QMenu {background-color: " + foreground_color + "; color: #FFFFFF; font-size: 24px;} QMenu::item::selected { background-color: " + selection_color + ";}"
    text_field_style=f"background-color: {text_field_color}; border: 1px {text_field_color};"
    color_picker_style=f"background-color: {text_field_color}; border: 1px {text_field_color}; font-size: 24px;"
    temp_info_style="color: #FFFFFF; font-size: 96px;"
    other_info_style="color: #FFFFFF; font-size: 24px; border: 1px;"
    about_program_style="color: #FFFFFF; font-size: 20px;"
    close_button_style="color: #FFFFFF; background-color: #FF5555; border: 1px #FF5555; font-size: 24px;"
    save_button_style="background-color: #50FA7B; border: 1px #50FA7B; font-size: 24px;"
    inner_widget_style=f"background-color: {selection_color}; padding: 10px;"

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    global is_sunny
    if response.status_code == 200:
        data = response.json()
        message = data["weather"][0]["description"]
        is_sunny = "rain" in message or "cloud" in message
        return data
    is_sunny = True
    return {
        "weather": [
            {
                "description": "N/A"
            }
        ],
        "main": {
            "temp": "N/A",
            "feels_like": "N/A",
            "pressure": "N/A",
            "humidity": "N/A"
        },
        "wind": {
            "speed": "N/A"
        }
    }

class WeatherForecastWindow(QMainWindow):
    windows = []

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prognoza Pogody")
        self.setFixedSize(1280, 720)
        self.setStyleSheet(base_window_style)

        self.create_menu_bar()
        self.create_ui()

    def create_menu_bar(self):
        menubar = self.menuBar()
        menubar.setStyleSheet(menu_style)
        
        localisation_menu = menubar.addMenu("Lokalizacja")

        settings_menu = menubar.addMenu("Ustawienia")

        about_program_action = menubar.addAction("O Programie")
        about_program_action.triggered.connect(self.on_about_program_clicked)

        refresh_action = menubar.addAction("Odśwież")
        refresh_action.triggered.connect(self.on_refresh_clicked)

        coordinates_action = localisation_menu.addAction("Zmień Współrzędne")
        coordinates_action.triggered.connect(self.on_change_coordinates_clicked)

        theme_action = settings_menu.addAction("Zmień Motyw")
        theme_action.triggered.connect(self.on_change_theme_clicked)

    def create_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QHBoxLayout()
        self.central_widget.setLayout(layout)

        image_label = QLabel()
        pixmap = QPixmap("sunny.png" if is_sunny else "cloudy.png")
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(image_label, 1)

        weather_layout = QVBoxLayout()
        layout.addLayout(weather_layout, 2)

        weather = get_weather()

        temp = weather["main"]["temp"]
        self.temp_info = QLabel(f"{temp}ºC")
        self.temp_info.setStyleSheet(temp_info_style)
        self.temp_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(self.temp_info)

        feels_like_temp = weather["main"]["feels_like"]
        self.feels_like_temp_info = QLabel(f"Odczuwalnie: {feels_like_temp}ºC")
        self.feels_like_temp_info.setStyleSheet(other_info_style)
        self.feels_like_temp_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(self.feels_like_temp_info)

        translator = Translator()
        message = weather["weather"][0]["description"]
        translated_message = translator.translate(message, dest="pl").text.lower() if message != "N/A" else "N/A"
        self.message_info = QLabel(f"Spodziewaj się: {translated_message}!")
        self.message_info.setStyleSheet(other_info_style)
        self.message_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(self.message_info)

        pressure = weather["main"]["pressure"]
        self.pressure_info = QLabel(f"Ciśnienie:\t{pressure} hPa")
        self.pressure_info.setStyleSheet(other_info_style)
        self.pressure_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(self.pressure_info)

        humidity = weather["main"]["humidity"]
        self.humidity_info = QLabel(f"Wilgotność:\t{humidity}%")
        self.humidity_info.setStyleSheet(other_info_style)
        self.humidity_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(self.humidity_info)

        wind_speed = weather["wind"]["speed"]
        self.wind_speed_info = QLabel(f"Prędkość:\t{wind_speed}km/h")
        self.wind_speed_info.setStyleSheet(other_info_style)
        self.wind_speed_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(self.wind_speed_info)

        self.coordinates_info = QLabel(f"Obecne współrzędne geograficzne:\nDługość ({lon}), Szerokość ({lat})")
        self.coordinates_info.setStyleSheet(other_info_style)
        self.coordinates_info.setAlignment(Qt.AlignmentFlag.AlignLeft)
        weather_layout.addWidget(self.coordinates_info)

    def update_weather_in_ui(self, weather):
        temp = weather["main"]["temp"]
        feels_like_temp = weather["main"]["feels_like"]
        message = weather["weather"][0]["description"]
        pressure = weather["main"]["pressure"]
        humidity = weather["main"]["humidity"]
        wind_speed = weather["wind"]["speed"]

        self.temp_info.setText(f"{temp}ºC")
        self.feels_like_temp_info.setText(f"Odczuwalnie: {feels_like_temp}ºC")
        self.message_info.setText(f"Spodziewaj się: {message}!")
        self.pressure_info.setText(f"Ciśnienie:\t{pressure} hPa")
        self.humidity_info.setText(f"Wilgotność:\t{humidity}%")
        self.wind_speed_info.setText(f"Prędkość:\t{wind_speed}km/h")

    def update_coordinates_in_ui(self):
        self.coordinates_info.setText(f"Obecne współrzędne geograficzne:\nDługość ({lon}), Szerokość ({lat})")

    def on_refresh_clicked(self):
        weather = get_weather()
        self.update_weather_in_ui(weather)

    def on_about_program_clicked(self):
        dialog = QDialog(self)
        dialog.setStyleSheet(about_program_style)
        dialog.setWindowTitle("O Programie")
        dialog.setFixedSize(910, 355)

        layout = QVBoxLayout(dialog)
        label = QLabel("Aplikacja prognozy pogody pozwala na natychmiastowe uzyskanie aktualnych informacji o: temperaturze wraz z wartością odzuwalną, podsumowaniu pogody, ciśnieniu, wilgotności i prędkości wiatru. Wyświetlana jest ikona przedstawiająca obecną sytuację pogodową. Działanie programu wymaga ustawienia lokalizacji według miasta lub współrzędnych geograficznych.")
        label.setAlignment(Qt.AlignmentFlag.AlignJustify)
        label.setWordWrap(True)
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)

        dialog.exec()

    def on_change_coordinates_clicked(self):
        self.dialog = QDialog(self)
        self.dialog.setStyleSheet(inner_widget_style)
        self.dialog.setWindowTitle("Zmień Współrzędne")
        self.dialog.setFixedSize(910, 355)

        layout = QVBoxLayout(self.dialog)

        longitude_label = QLabel(f"Podaj długość geograficzną w formacie zmiennoprzecinkowym:")
        longitude_label.setStyleSheet(other_info_style)
        layout.addWidget(longitude_label)

        self.longitude_entry = QLineEdit()
        self.longitude_entry.setPlaceholderText("<długość geograficzna>")
        self.longitude_entry.setStyleSheet(text_field_style)
        layout.addWidget(self.longitude_entry)

        latitude_label = QLabel(f"Podaj szerokość geograficzną w formacie zmiennoprzecinkowym:")
        latitude_label.setStyleSheet(other_info_style)
        layout.addWidget(latitude_label)

        self.latitude_entry = QLineEdit()
        self.latitude_entry.setPlaceholderText("<szerokość geograficzna>")
        self.latitude_entry.setStyleSheet(text_field_style)
        layout.addWidget(self.latitude_entry)

        save_button = QPushButton("Zatwierdź")
        save_button.clicked.connect(self.save_coordinates)
        save_button.setStyleSheet(save_button_style)
        layout.addWidget(save_button)

        self.dialog.exec()

    def validate_coordinates(self, lon, lat):
        lon_valid = False
        lat_valid = False
        try:
            lon_float = float(lon)
            lon_valid = True
        except ValueError:
            pass
        try:
            lat_float = float(lat)
            lat_valid = True
        except ValueError:
            pass
        return lon_valid and lat_valid

    def save_coordinates(self):
        tmp_lon = self.longitude_entry.text()
        tmp_lat = self.latitude_entry.text()
        if self.validate_coordinates(tmp_lon, tmp_lat):
            global lon, lat
            lon = tmp_lon
            lat = tmp_lat
            self.update_coordinates_in_ui()
            self.on_refresh_clicked()
            self.dialog.close()
        else:
            error_dialog = QDialog(self)
            error_dialog.setWindowTitle("Błąd")
            error_dialog.setFixedSize(610, 100)
            error_dialog.setStyleSheet(inner_widget_style)
            layout = QVBoxLayout(error_dialog)
            error_label = QLabel("Niepoprawne współrzędne geograficzne!")
            error_label.setStyleSheet(other_info_style)
            error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(error_label)
            error_dialog.exec()

    def on_change_theme_clicked(self):
        self.dialog = QDialog(self)
        self.dialog.setStyleSheet(inner_widget_style)
        self.dialog.setWindowTitle("Zmień Motyw")
        self.dialog.setFixedSize(910, 355)

        layout = QVBoxLayout(self.dialog)

        dracula_theme_button = QPushButton("Motyw Dracula (Domyślny)")
        dracula_theme_button.clicked.connect(lambda: self.change_theme("Dracula"))
        dracula_theme_button.setStyleSheet(color_picker_style)
        layout.addWidget(dracula_theme_button)

        oxocarbon_theme_button = QPushButton("Motyw Seoul256")
        oxocarbon_theme_button.clicked.connect(lambda: self.change_theme("Seoul256"))
        oxocarbon_theme_button.setStyleSheet(color_picker_style)
        layout.addWidget(oxocarbon_theme_button)
        
        seoul256_theme_button = QPushButton("Motyw Gotham")
        seoul256_theme_button.clicked.connect(lambda: self.change_theme("Gotham"))
        seoul256_theme_button.setStyleSheet(color_picker_style)
        layout.addWidget(seoul256_theme_button)

        dogrun_theme_button = QPushButton("Motyw Nord")
        dogrun_theme_button.clicked.connect(lambda: self.change_theme("Nord"))
        dogrun_theme_button.setStyleSheet(color_picker_style)
        layout.addWidget(dogrun_theme_button)

        self.dialog.exec()

    def change_theme(self, theme):
        global background_color, foreground_color, selection_color, text_field_color
        if theme == "Dracula":
            background_color, foreground_color, selection_color, text_field_color = "#0A0D11", "#6272A4", "#44475A", "#F8F8F2"
        elif theme == "Seoul256":
            background_color, foreground_color, selection_color, text_field_color = "#4B4B4B", "#9A7372", "#565656", "#DFDEBD"
        elif theme == "Gotham":
            background_color, foreground_color, selection_color, text_field_color = "#091F2E", "#599CAB", "#2AA889", "#99D1CE"
        elif theme == "Nord":
            background_color, foreground_color, selection_color, text_field_color = "#81A1C1", "#D8DEE9", "#3C4455", "#434C5E"
        setup_styles()
        new_window = WeatherForecastWindow()
        new_window.show()
        self.windows.append(new_window)
        self.dialog.close()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    setup_styles()
    window = WeatherForecastWindow()
    window.show()
    sys.exit(app.exec())
