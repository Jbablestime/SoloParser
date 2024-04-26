"""
This script creates a simple GUI application using PyQt6 that fetches
data from the solo.to API
"""

import sys
from typing import Any, Dict

import requests
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

CSS_WHITE = "color: white;"


class DataWindow(QDialog):
    """
    Represents a dialog window displaying fetched data.
    """

    def __init__(self, data: Dict[str, Any]):
        """
        Initializes the dialog window with fetched data.

        Args:
            data: A dictionary containing fetched data.
        """
        super().__init__()

        self.setWindowTitle("Fetched Data for /" + data["name"])
        self.setGeometry(200, 200, 400, 200)

        self.layout: QVBoxLayout = QVBoxLayout()
        self.setLayout(self.layout)

        for endpoint, value in data.items():
            endpoint_label = QLabel(f"<b>{endpoint}</b>: {value}")
            endpoint_label.setStyleSheet(CSS_WHITE)
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
    """
    Represents the main application window for the solo.to API parser.
    """

    def __init__(self):
        """
        Initializes the main application window for the solo.to API Parser.
        """

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
        self.username_label.setStyleSheet(CSS_WHITE)
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

        self.data_window = None

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setStyleSheet(CSS_WHITE)
        self.layout.addWidget(self.result_label)

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #1a1a1a;
            }
            """
        )

    def fetch_data(self):
        """
        Fetches data from the solo.to API based on the entered username
        and displays the result.
        """
        username = self.username_input.text()
        solo_to_api_url = f"https://api.solo.to/{username}"

        headers = {"User-Agent": "Jb/1.0.0"}

        try:
            response = requests.get(solo_to_api_url, headers=headers, timeout=10)
            data = response.json()

            error_messages = ["error", "page reserved or blocked", "page not found"]
            if any(message in data.values() for message in error_messages):
                self.result_label.setText("Enter a valid username.")
            else:
                self.open_data_window(data)

        except requests.exceptions.RequestException:
            self.result_label.setText("Please enter a valid username.")

    def open_data_window(self, data: Dict[str, Any]):
        """
        Opens a dialog window to display fetched data.

        Args:
            data: A dictionary containing fetched data.
        """
        self.data_window = DataWindow(data)
        self.data_window.exec()


def main():
    """
    Initializes the application, sets the style, shows the main window,
    and starts the application event loop.
    """
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = SoloToApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
