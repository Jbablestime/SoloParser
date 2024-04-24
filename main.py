import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QDialog, QHBoxLayout
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt, QUrl

import requests

class DataWindow(QDialog):
    def __init__(self, data):
        super().__init__()

        self.setWindowTitle("Fetched Data for /" + data["name"])
        self.setGeometry(200, 200, 400, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        for endpoint, value in data.items():
            endpoint_label = QLabel(f"<b>{endpoint}</b>: {value}")
            endpoint_label.setStyleSheet("color: white;")
            self.layout.addWidget(endpoint_label)

            line = QLabel("<hr>")
            line.setStyleSheet("color: #101010;")
            self.layout.addWidget(line)

        self.setStyleSheet(
            """
            QDialog {
                background-color: #1a1a1a;
            }
            """
        )

class SoloToApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("solo.to API Parser")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.username_label = QLabel("Enter solo.to username:")
        self.username_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.username_label.setFont(QFont("Arial", 12))
        self.username_label.setStyleSheet("color: white;")
        self.layout.addWidget(self.username_label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet(
            """
            QLineEdit {
                background-color: #333333;
                color: white;
                border: 1px solid #555555;
                padding: 8px;
                border-radius: 5px;
            }
            """
        )
        self.layout.addWidget(self.username_input)

        self.button = QPushButton("Fetch Data")
        self.button.setStyleSheet(
            """
            QPushButton {
                background-color: #1e90ff;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1e75db;
            }
            """
        )
        self.button.clicked.connect(self.fetch_data)
        self.layout.addWidget(self.button)

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setStyleSheet("color: white;")
        self.layout.addWidget(self.result_label)

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #1a1a1a;
            }
            """
        )

    def fetch_data(self):
        username = self.username_input.text()
        solo_to_api_url = f'https://api.solo.to/{username}'

        headers = {
            'User-Agent': 'Jb/1.0.0'
        }
        
        try:
            response = requests.get(solo_to_api_url, headers=headers)
            data = response.json()

            if 'error' in data:
                self.result_label.setText("Enter a valid username.")
            else:
                self.open_data_window(data)

        except requests.exceptions.RequestException:
            self.result_label.setText("Please enter a valid username.")

    def open_data_window(self, data):
        self.data_window = DataWindow(data)
        self.data_window.exec()


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = SoloToApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
