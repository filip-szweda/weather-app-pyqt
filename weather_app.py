import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QFont, QFontDatabase

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prognoza Pogody")
        self.setFixedSize(1280, 720)
        self.setObjectName("main-window")

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.create_menu_bar()

        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        label = QLabel("Welcome to My Application")
        label.setObjectName("logo")
        layout.addWidget(label)

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

        coordinates_menu.addAction("Długość Geo.")
        coordinates_menu.addAction("Szerokość Geo.")

        settings_menu.addAction("Motyw")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        with open("styles.css", "r") as file:
            app.setStyleSheet(file.read())
    except FileNotFoundError:
        print("Nie można odnaleźć pliku styles.css")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
