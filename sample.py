import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QPixmap, QFont
from PyQt6 import QtCore

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image and Text Display")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # First Column: Image Aligned to the Right
        image_label = QLabel()
        pixmap = QPixmap("cloudy.png")  # Assuming you have an image file
        scaled_pixmap = pixmap.scaledToWidth(200)  # Scale the image to be smaller
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        main_layout.addWidget(image_label)

        # Second Column: Text "abcd" Aligned to the Left
        text_label = QLabel("abcd")
        text_label.setFont(QFont("Arial", 16))  # Adjust font and size as needed
        text_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(text_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
