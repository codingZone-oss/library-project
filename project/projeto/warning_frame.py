from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
import sys



class Alert(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Warning Frame")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(450, 200)

        self.main_layout = QWidget()
        self.setCentralWidget(self.main_layout)

        self.layout = QVBoxLayout()
        self.main_layout.setLayout(self.layout)
        self.main_layout.setStyleSheet("background-color: #f9d60e;")
        self.setStyleSheet("border-radius: 10px;")

        self.warning_label = QLabel("This is a warning message!")
        self.warning_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.warning_label)
        self.warning_label.setStyleSheet("font-size: 16px; font-weight: bold; color: white;")

        self.ok_button = QPushButton("OK")
        self.ok_button.setFixedWidth(80)
        self.ok_button.clicked.connect(self.close)
        self.layout.addWidget(self.ok_button, alignment=Qt.AlignCenter)
        self.ok_button.setCursor(Qt.PointingHandCursor)
        self.ok_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: black;
                padding: 8px 16px;
                border: none;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """)


# app = QApplication(sys.argv)
# worning = Alert()
# worning.show()
# app.exec_()