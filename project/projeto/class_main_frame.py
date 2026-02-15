from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QToolButton, QSizePolicy, QGraphicsDropShadowEffect,  QStackedWidget
from class_book_page import Book
from class_libraian_page import Libraian
from class_manager_page import Manager1
from class_readers_page import Reader
from class_settings import Settings
from classs_warning_frame import  Successefull
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor
from PySide6.QtGui import QIcon
from class_home_page import Home
from time import sleep
import sys

class MainFrame(QMainWindow):
    def __init__(self, controller) -> None:
        super().__init__()

        # self.controller = controller

        # Home
        self.setWindowState(Qt.WindowMaximized)
        self.setObjectName("id")
        self.setWindowTitle("Class Main")
        self.setStyleSheet(" #id {background-color: white; } ")

        # sub Home
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.setMaximumWidth(1920)
        self.setMinimumWidth(1324)
        self.setMaximumHeight(1080)
        self.setMinimumHeight(600)
        self.setObjectName("class")
        # self.setStyleSheet(" #class {background-color: black; } ")
        self.setStyleSheet(" #class {background-color: rgb(7, 30, 71); } ")

        #_________________________________



        # sub sub Home

        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        #_________________________________



        # adding a left layout painel on main layout

        self.left_painel_widget = QWidget()
        self.left_painel_layout = QVBoxLayout(self.left_painel_widget)
        self.left_painel_widget.setMaximumWidth(200)
        self.left_painel_widget.setMinimumWidth(200)
        self.left_painel_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.left_painel_widget.setObjectName("painel_widget")
        self.left_painel_widget.setStyleSheet(" #painel_widget {background-color: rgb(7, 30, 71); width: 700px; border-top-right-radius: 5px; border-bottom-right-radius: 5px;}")
        self.shadow(self.left_painel_widget)


        # adding a top painel on left layout

        self.header_widget = QWidget()
        self.header_layout = QHBoxLayout(self.header_widget)
        self.header_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.header_widget.setObjectName("header")
        self.header_widget.setStyleSheet(" #header {background-color: rgb(7, 30, 71);}")


        # adding label icon on the left side to scroll pux up the menu

        self.menu_label = QToolButton()
        self.menu_label.setIcon(QIcon("icons/menu_24px.png"))
        self.menu_label.setCursor(Qt.PointingHandCursor)
        self.menu_label.setToolTip("Click to Expand Menu")
        self.menu_label.setFixedSize(40, 30)
        self.header_layout.addWidget(self.menu_label, alignment=Qt.AlignLeft)
        self.menu_label.clicked.connect(self.label_menu)


        # adding a bottom painel on left layout

        self.bottom_widget = QWidget()
        self.bottom_layout = QVBoxLayout(self.bottom_widget)
        self.bottom_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.bottom_widget.setObjectName("header")
        self.bottom_widget.setStyleSheet(" #header {background-color:  rgb(7, 30, 71);}")

        self.left_painel_layout.addWidget(self.header_widget, alignment=Qt.AlignTop)
        self.left_painel_layout.addWidget(self.bottom_widget, alignment=Qt.AlignTop)

        self.left_painel_layout.setStretch(0, 1)  # Top side
        self.left_painel_layout.setStretch(1, 8)  # bottom side

        # __________________________________________________ 



        # adding a main right layout painel on main layout

        self.main_right_wgt = QWidget()
        self.main_right_lyt = QVBoxLayout(self.main_right_wgt)
        self.main_right_wgt.setObjectName("right_wgt")
        # self.main_right_wgt.setStyleSheet(" #right_wgt {background-color: pink; width: 70px; border-radius: 10px}")
        self.main_right_wgt.setStyleSheet(" #right_wgt {background-color: rgb(7, 30, 71); width: 70px; border-radius: 10px}")


        # adding a top layout sub painel on right layout

        self.top_widget = QWidget()
        self.top_layout = QHBoxLayout(self.top_widget)
        self.top_widget.setFixedHeight(50)
        self.top_widget.setObjectName("top")
        self.top_widget.setStyleSheet(" #top {background-color: rgb(7, 30, 71); border-radius: 10px; }")
        self.shadow(self.top_widget)

        # adding a label title to the top layout 

        self.title_label = QLabel()
        self.title_label.setText("Libary System")
        self.top_layout.addWidget(self.title_label, alignment=Qt.AlignRight)
        self.title_label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)
        self.title_label.setStyleSheet("""QLabel{ background-color:  rgb(7, 30, 71); color: white; font-weight: bold; font-size: 24px; padding-bottom: 10px;}""")
        self.title_label.setFixedHeight(40)
        self.title_label.setContentsMargins(450, 0, 0, 0)
        

        # adding a label icon to log out on the top layout

        self.logout_label = QToolButton()
        self.logout_label.setIcon(QIcon("imagens/sair.png"))
        self.logout_label.setCursor(Qt.PointingHandCursor)
        self.logout_label.setToolTip("Log Out")
        self.top_layout.addWidget(self.logout_label, alignment=Qt.AlignRight)
        self.logout_label.setFixedSize(40, 30)
        self.logout_label.clicked.connect(self.logout)

        # adding a QStackedWidget on the main_right_wgt

        self.right_painel_stackedwidget = QStackedWidget()
        self.right_painel_stackedwidget.setObjectName("stackwidget")
        self.right_painel_stackedwidget.setStyleSheet(" #stackwidget {background-color: rgb(7, 30, 71); width: 70px; border-radius: 10px}")

        self.setup_pages()
        self.setup_menu()
        self.setup_connect()
        self.main_right_lyt.addWidget(self.top_widget)
        self.main_right_lyt.addWidget(self.right_painel_stackedwidget)


        #_________________________________
        

        # adding both layouts to the main layout | adicionando ambos os layouts ao layout principal
        self.main_layout.addWidget(self.left_painel_widget)
        self.main_layout.addWidget(self.main_right_wgt)       
        self.main_layout.setStretch(0, 1)  # Top side
        self.main_layout.setStretch(1, 5)  # Top side
     
    def setup_menu(self) -> None:

        self.btn_home = self.building_buttons('Home', "icons/home_32px.png")
        self.btn_book = self.building_buttons('Add Books', "icons/add_book.png")
        self.btn_reader = self.building_buttons("Add Reades", "icons/leitura.png")
        self.btn_librarian = self.building_buttons("Add librarian", "icons/bibliotecario.png")        
        self.btn_manager = self.building_buttons("Manager", "icons/gerente.png")        
        self.btn_settings = self.building_buttons("Settings", "icons/configuracoes.png")        

        self.bottom_layout.addWidget(self.btn_home)
        self.bottom_layout.addWidget(self.btn_book)
        self.bottom_layout.addWidget(self.btn_reader)
        self.bottom_layout.addWidget(self.btn_librarian)
        self.bottom_layout.addWidget(self.btn_manager)
        self.bottom_layout.addWidget(self.btn_settings)

    def setup_pages(self) -> None:

        # adding all widget into right_painel_stackedwidget

        self.wgt_home = Home()
        self.wgt_add_books = Book()
        self.wgt_add_readers = Reader()
        self.wgt_add_librarian = Libraian()
        self.wgt_manager = Manager1()
        self.wgt_settings = Settings()

        self.right_painel_stackedwidget.addWidget(self.wgt_home.home_page())
        self.right_painel_stackedwidget.addWidget(self.wgt_add_books.book_page())
        self.right_painel_stackedwidget.addWidget(self.wgt_add_readers.readers_page())
        self.right_painel_stackedwidget.addWidget(self.wgt_add_librarian.libraian_page())
        self.right_painel_stackedwidget.addWidget(self.wgt_manager.manager_page())
        self.right_painel_stackedwidget.addWidget(self.wgt_settings.settings_page())


    def setup_connect(self) -> None:
        self.btn_home.clicked.connect(self.show_home)
        self.btn_book.clicked.connect(self.show_books)
        self.btn_reader.clicked.connect(self.show_readers)
        self.btn_librarian.clicked.connect(self.show_librarian)
        self.btn_manager.clicked.connect(self.show_manager)
        self.btn_settings.clicked.connect(self.show_settings)

    def shadow(self, widget):
        shadow = QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(12)
        shadow.setOffset(1, 0)
        shadow.setColor(QColor(0, 0, 0, 80))
        return widget.setGraphicsEffect(shadow)


    def show_home(self) -> None:
        self.right_painel_stackedwidget.setCurrentIndex(0)

    def show_books(self) -> None:
        self.right_painel_stackedwidget.setCurrentIndex(1)
    
    def show_readers(self) -> None:
        self.right_painel_stackedwidget.setCurrentIndex(2)

    def show_librarian(self) -> None:
        self.right_painel_stackedwidget.setCurrentIndex(3)

    def show_manager(self) -> None:
        self.right_painel_stackedwidget.setCurrentIndex(4)

    def show_settings(self) -> None:
        self.right_painel_stackedwidget.setCurrentIndex(5)

    def logout(self) -> None: # this methods close the login frame and also open the main window frame
        sleep(1)
        self.success = Successefull("Leaving System...")
        self.success.show()
        self.timer = QTimer()
        self.timer.singleShot(4000, self.controller.show_login)
       
    
    def label_menu(self):
        if self.left_painel_widget.width() > 70:
            self.timer = QTimer()
            self.timer.singleShot(-1000, self.width)
        else:
            self.timer2 = QTimer()
            self.timer.singleShot(-1000, self.width2)

    def width(self):
        self.left_painel_widget.setMaximumWidth(68)
        self.left_painel_widget.setMinimumWidth(68)
        self.btn.setMinimumHeight(40)

    def width2(self):
        self.left_painel_widget.setMaximumWidth(200)
        self.left_painel_widget.setMinimumWidth(150)

    def building_buttons(self, text, icon):
        self.btn = QPushButton(f"       {text}")
        self.btn.setIcon(QIcon(icon))
        self.btn.setCursor(Qt.PointingHandCursor)
        self.btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.btn.setMinimumHeight(50)
        self.btn.setCheckable(True)
        self.btn.setFlat(True)
        self.btn.setStyleSheet(" QPushButton { background-color: rgb(7, 30, 71); text-align: left; } ")
        return self.btn
    

app = QApplication(sys.argv)
window = MainFrame(None)
window.show()
app.exec()