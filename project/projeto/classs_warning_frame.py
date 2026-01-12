from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QLabel, QWidget, QPushButton, QVBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QTimer
from time import sleep
import sys

class Alert(QMainWindow):

    def __init__(self, Bool:bool=False, parent=None) -> None:
        super().__init__()

        # home
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(450, 200)
        self.setStyleSheet("background-color: #ff000000;") #color transparent

        # sob-home
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_widget.setObjectName("id")
        self.main_widget.setStyleSheet(" #id { background-color: #ff0000b0; border-radius: 50px;}")

        # sub-sub-home
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.top_widget = QWidget()
        self.top_layout = QHBoxLayout(self.top_widget)
        self.top_layout.setAlignment(Qt.AlignTop)
        self.top_widget.setStyleSheet(" QWidget { background-color: #ff0000b0; border-radius: 50px;}")

        self.label_title = QLabel()
        self.label_title.setText("User Name or Pass Word Incorrect")
        self.label_title.setObjectName("tester")
        self.label_title.setStyleSheet(" #tester { background-color: #ff0000b0; color: white; font-size: 19px; border-radius: 50px; font-weight: bold;}")
        self.top_layout.addWidget(self.label_title, alignment=Qt.AlignRight)

        self.check_label = QLabel()
        self.check_label.setObjectName("tes")
        self.check_label.setStyleSheet(" #tes { background-color: #ff0000b0;}")
        self.check_label.setPixmap(QIcon("imagens/crisis.png").pixmap(100, 100))
        self.top_layout.addWidget(self.check_label, alignment=Qt.AlignCenter)

        if Bool == True:
            self.bottom_widget = QWidget()
            self.bottom_layout = QHBoxLayout(self.bottom_widget)
            self.bottom_layout.setAlignment(Qt.AlignBottom)
            self.bottom_widget.setStyleSheet(""" QWidget { background-color: #ff0000b0; border-radius: 29px; }""")


            self.ok_button = QPushButton("OK")
            self.ok_button.setFixedWidth(80)
            self.ok_button.clicked.connect(self.close)
            self.ok_button.setCursor(Qt.PointingHandCursor)
            self.ok_button.setStyleSheet("""QPushButton {background-color: white; color: black; padding: 8px 16px; border: none; font-size: 14px; border-radius: 15px; box-shadow: #000000a3;} QPushButton:hover { background-color: #e0e0e0; color: white;}""")
            self.bottom_layout.addWidget(self.ok_button, alignment=Qt.AlignCenter)

            self.main_layout.addWidget(self.top_widget, alignment=Qt.AlignCenter)
            self.main_layout.addWidget(self.bottom_widget)
            self.main_layout.setStretch(0, 2)  # Top side
            self.main_layout.setStretch(1, 1)  # Bottom side

        else:
            self.main_layout.addWidget(self.top_widget, alignment=Qt.AlignCenter)

            self.timer = QTimer()
            self.timer.setInterval(3000)  # 2 seconds
            self.timer.timeout.connect(self.close)
            self.timer.start()


class Successefull(QMainWindow):

    def __init__(self, text1:str, var:bool=False, parent=None) -> None:
        super().__init__()

        # home
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(450, 200)
        self.setStyleSheet("background-color: #ff000000;") #color transparent

        # sob-home
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_widget.setObjectName("id")
        self.main_widget.setStyleSheet(" #id { background-color: green; border-radius: 60px;}")

        # sub-sub-home
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.top_widget = QWidget()
        self.top_layout = QHBoxLayout(self.top_widget)
        self.top_layout.setAlignment(Qt.AlignTop)
        self.top_widget.setStyleSheet(" QWidget { background-color: green; border-radius: 40px; }")
        self.top_widget.setFixedHeight(120)


        self.label_title = QLabel()
        self.label_title.setText("WellCome")
        self.label_title.setObjectName("tester")
        self.label_title.setStyleSheet(" #tester { background-color: green; color: white; font-size: 27px; border-radius: 50px; font-weight: bold;}")
        self.top_layout.addWidget(self.label_title, alignment=Qt.AlignRight)

        self.check_label = QLabel()
        self.check_label.setObjectName("tes")
        self.check_label.setStyleSheet(" #tes { background-color: green;}")
        self.check_label.setPixmap(QIcon("imagens/mark.png").pixmap(103, 102))
        self.top_layout.addWidget(self.check_label, alignment=Qt.AlignRight)

        self.top_layout.setStretch(0, 2)  # right side
        self.top_layout.setStretch(1, 1)  # left side

        self.midle_widget = QWidget()
        self.midle_layout = QHBoxLayout(self.midle_widget)
        self.midle_layout.setAlignment(Qt.AlignBottom)
        self.midle_widget.setFixedHeight(25)
        self.midle_widget.setStyleSheet(""" QWidget { background-color: green; border-radius: 10px; }""")

        self.midle_label = QLabel()
        self.midle_label.setText(text1)
        self.midle_label.setObjectName("tester")
        self.midle_label.setStyleSheet(" #tester { background-color: green; color: white; font-size: 12px; border-radius: 5px; font-weight: bold;}")
        self.midle_layout.addWidget(self.midle_label, alignment=Qt.AlignCenter)
        self.midle_label.setFixedHeight(15)

        if var == True:
            self.bottom_widget = QWidget()
            self.bottom_layout = QHBoxLayout(self.bottom_widget)
            self.bottom_layout.setAlignment(Qt.AlignBottom)
            self.bottom_widget.setStyleSheet(""" QWidget { background-color: green; border-radius: 20px; }""")
            self.bottom_widget.setFixedHeight(40)
            self.bottom_widget.setFixedWidth(200)
            #self.bottom_widget.setContentsMargins(80, 0, 0, 0)

            self.ok_button = QPushButton("OK")
            self.ok_button.setFixedWidth(75)
            self.ok_button.clicked.connect(self.close)
            self.ok_button.setCursor(Qt.PointingHandCursor)
            self.ok_button.setStyleSheet("""QPushButton {background-color: white; color: black; padding: 4px 16px; border: none; font-size: 16px; border-radius: 10px; box-shadow: black;} QPushButton:hover { background-color: #e0e0e0; color: green;}""")
            self.bottom_layout.addWidget(self.ok_button, alignment=Qt.AlignCenter)

            self.main_layout.addWidget(self.top_widget)
            self.main_layout.addWidget(self.midle_widget)
            self.main_layout.addWidget(self.bottom_widget, alignment=Qt.AlignCenter)
            self.main_layout.setStretch(0, 2)  # Top side
            self.main_layout.setStretch(1, 1)  # midle side
            self.main_layout.setStretch(2, 1)  # Bottom side
        else:
            self.main_layout.addWidget(self.top_widget)
            self.main_layout.addWidget(self.midle_widget)
            self.main_layout.setStretch(0, 1)  # Top side
            self.main_layout.setStretch(1, 2)

            self.timer = QTimer()
            self.timer.setInterval(3000)  # 2 seconds
            self.timer.timeout.connect(self.close)
            self.timer.start()

# app = QApplication(sys.argv)
# worning = Successefull("Admin: Fulano de Tal")
# worning.show()
# app.exec_()