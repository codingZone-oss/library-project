from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QToolButton
from classs_warning_frame import Alert, Successefull
from PySide6.QtGui import QIcon
from class_conextion import cursor
from PySide6.QtCore import Qt, QTimer, QSize
from time import sleep

import sys

class MainFrame(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Home
        self.setWindowState(Qt.WindowMaximized)
        self.setObjectName("id")
        self.setWindowTitle("Class Main")
        self.setStyleSheet(" #id {background-color: white; } ")

        # sub Home
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.setObjectName("class")
        self.setStyleSheet(" #class {background-color: rgb(7, 30, 71);; } ")

        #_________________________________

        # sub sub Home
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        # adding a left layout painel on main layout

        self.left_painel_widget = QWidget()
        self.left_painel_layout = QVBoxLayout(self.left_painel_widget)
        self.left_painel_widget.setObjectName("painel_widget")
        self.left_painel_widget.setStyleSheet(" #painel_widget {background-color: rgb(7, 30, 71);; width: 700px; border-top-right-radius: 5px; border-bottom-right-radius: 5px;}")

        # adding icon label on the left side to scroll pux up the menu
        self.menu_label = QToolButton()
        self.menu_label.setIcon(QIcon("icons/menu_24px.png"))
        self.menu_label.setCursor(Qt.PointingHandCursor)
        self.menu_label.setToolTip("Click to Expand Menu")
        self.left_painel_layout.addWidget(self.menu_label, alignment=Qt.AlignTop)
        self.menu_label.setFixedSize(40, 30)
        self.menu_label.clicked.connect(self.label_menu)

        #_________________________________

        # adding a right layout painel on main layout
        self.right_painel_widget = QWidget()
        self.right_painel_layout = QVBoxLayout(self.right_painel_widget)
        self.right_painel_widget.setObjectName("painel_widget1")
        self.right_painel_widget.setStyleSheet(" #painel_widget1 {background-color: white; width: 70px;}")


        # adding a top layout sub painel on right layout
        self.top_widget = QWidget()
        self.top_layout = QHBoxLayout(self.top_widget)
        self.top_widget.setObjectName("top")
        self.top_widget.setStyleSheet(" #top {background-color: rgb(7, 30, 71); border-radius: 10px; }")
        self.right_painel_layout.addWidget(self.top_widget)
        self.top_widget.setFixedHeight(90)

        # adding a label title to the top layout 
        self.title_label = QLabel()
        self.title_label.setText("Labery System")
        self.top_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        self.title_label.setStyleSheet("""QLabel{ color: white; font-weight: bold; font-size: 30px; padding-bottom: 10px;}""")


        # adding a sub-top layout sub painel on right layout
        self.midel_widget = QWidget()
        self.midel_layout = QHBoxLayout(self.midel_widget)
        self.midel_widget.setObjectName("midel")
        self.midel_widget.setStyleSheet(" #midel {background-color: rgb(7, 30, 71); border-radius: 10px; hight: 50px; }")
        self.right_painel_layout.addWidget(self.midel_widget)
        self.midel_widget.setFixedHeight(120)
        self.midel_layout.setSpacing(50)


        # adding a the first label on the midel layout
        self.label_book = QLabel()
        self.label_book.setText(f"Added Books \n \n {self.select_books()[0]}")
        self.label_book.setAlignment(Qt.AlignCenter)
        self.midel_layout.addWidget(self.label_book)
        self.label_book.setFixedSize(350, 150)
        self.label_book.setStyleSheet(" QLabel { background-color: rgb(255, 192, 35); color: white; font-size: 20px; font-weight: bold; border-radius: 50px; }")
        self.label_book.setFixedHeight(100)

        # adding a the second label on the top layout
        self.label_worker = QLabel()
        self.label_worker.setText(f"Added Workers \n \n {self.select_workers()[0]}")
        self.label_worker.setAlignment(Qt.AlignCenter)
        self.midel_layout.addWidget(self.label_worker)
        self.label_worker.setFixedSize(350, 150)
        self.label_worker.setStyleSheet(" QLabel { background-color: rgb(5, 193, 116); color: white; font-size: 20px; font-weight: bold; border-radius: 50px;}")
        self.label_worker.setFixedHeight(100)

        # adding a the third label on the top layout
        self.label_reader = QLabel()
        self.label_reader.setText(f"Added Readers \n \n {self.select_readers()[0]}")
        self.label_reader.setAlignment(Qt.AlignCenter)
        self.midel_layout.addWidget(self.label_reader)
        self.label_reader.setFixedSize(350, 150)
        self.label_reader.setStyleSheet(" QLabel { background-color: rgb(19, 102, 232); color: white; font-size: 20px; font-weight: bold; border-radius: 50px;}")
        self.label_reader.setFixedHeight(100)



        # adding a bottom layout sub painel on right layout

        self.bottom_widget = QWidget()
        self.bottom_layout = QHBoxLayout(self.bottom_widget)
        self.bottom_widget.setObjectName("bottom")
        self.bottom_widget.setStyleSheet(" #bottom { background-color: rgb(7, 30, 71); border-color: black; border-style: solid; border-radius: 10px; }")
        self.right_painel_layout.addWidget(self.bottom_widget)

        self.right_painel_layout.setStretch(0, 1) 
        self.right_painel_layout.setStretch(1, 1) 
        self.right_painel_layout.setStretch(2, 4)

        #_________________________________


        # adding both layouts to the main layout | adicionando ambos os layouts ao layout principal
        self.main_layout.addWidget(self.left_painel_widget)
        self.main_layout.addWidget(self.right_painel_widget)
        self.main_layout.setStretch(0, 1)  # Top side
        self.main_layout.setStretch(1, 28)  # Top side

    def select_books(self):
        cursor.execute("SELECT COUNT(id) FROM livros")
        for line in cursor:
            values = line
        return values

    def select_workers(self):
        cursor.execute("SELECT COUNT(id) FROM worker")
        for line in cursor:
            values = line
        return values
    
    def select_readers(self):
        cursor.execute("SELECT COUNT(id) FROM clientes")
        for line in cursor:
            values = line
        return values
    
    def label_menu(self):
        self.timer = QTimer()
        self.timer.setInterval(-1000)
        self.timer.timeout.connect(self.width)
        self.timer.start()

    def width(self):
        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 5)

    def width2(self):
        self.main_layout.setStretch(0, 1)
        self.main_layout.setStretch(1, 28)


app = QApplication(sys.argv)
window = MainFrame()
window.show()
app.exec()

"""    
    def label_menu(self):
        if self.left_painel_widget.width() == 5:
            self.timer = QTimer()
            self.timer.setInterval(-1000)
            self.timer.timeout.connect(self.width)
            self.timer.start()
        else:
            self.timer2 = QTimer()
            self.timer2.setInterval(-1000)
            self.timer2.timeout.connect(self.width2)
            self.timer2.start()
"""

