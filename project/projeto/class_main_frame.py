from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QToolButton, QSizePolicy, QGraphicsDropShadowEffect,  QStackedWidget, QTableView
from PySide6.QtSql import QSqlTableModel
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtGui import QColor
from classs_warning_frame import Alert, Successefull
from PySide6.QtGui import QIcon
from class_conextion import cursor
from PySide6.QtCore import Qt, QTimer, QSize
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
        self.left_painel_layout.setStretch(1, 8)  # Top side

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

        # creating a home page

        self.wgt_home = QWidget()
        self.lyt_home1 = QVBoxLayout(self.wgt_home)
        self.wgt_home.setObjectName("home")
        self.wgt_home.setStyleSheet(" #home {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")


        # creating a center information Label
        
        self.informative_Label("Home Page")


        # creating a header widget 

        self.wgt_header = QWidget()
        self.lyt_header = QHBoxLayout(self.wgt_header)
        self.lyt_header.setSpacing(50)
        self.wgt_header.setObjectName("home")
        self.wgt_header.setStyleSheet(" #home {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")
        self.shadow(self.wgt_header)


        # adding a the first label on the midel layout
        self.label_book = QLabel()
        self.label_book.setText(f"Added Books \n \n {self.select_books()[0]}")
        self.label_book.setAlignment(Qt.AlignCenter)
        self.lyt_header.addWidget(self.label_book)
        self.label_book.setStyleSheet(" QLabel { background-color: rgb(255, 192, 35); color: white; font-size: 20px; font-weight: bold; border-radius: 40px; }")
        self.label_book.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)

        # adding a the second label on the top layout
        self.label_worker = QLabel()
        self.label_worker.setText(f"Added Workers \n \n {self.select_workers()[0]}")
        self.label_worker.setAlignment(Qt.AlignCenter)
        self.lyt_header.addWidget(self.label_worker)
        self.label_worker.setStyleSheet(" QLabel { background-color: rgb(5, 193, 116); color: white; font-size: 20px; font-weight: bold; border-radius: 40px;}")
        self.label_worker.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)

        # adding a the third label on the top layout
        self.label_reader = QLabel()
        self.label_reader.setText(f"Added Readers \n \n {self.select_readers()[0]}")
        self.label_reader.setAlignment(Qt.AlignCenter)
        self.lyt_header.addWidget(self.label_reader)
        self.label_reader.setStyleSheet(" QLabel { background-color: rgb(19, 102, 232); color: white; font-size: 20px; font-weight: bold; border-radius: 40px}")
        self.label_reader.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)


        # adding a bottom layout sub painel on right layout

        self.bottom_widget = QWidget()
        self.bottom_layout1 = QHBoxLayout(self.bottom_widget)
        self.bottom_widget.setObjectName("bottom")
        self.bottom_widget.setStyleSheet(" #bottom { background-color: rgb(7, 30, 71); border-color: black; border-style: solid; border-radius: 10px; }")
        self.shadow(self.bottom_widget)

        # adding a label to the bottom layout 

        self.bottom_label = QLabel()
        self.bottom_label.setText('What´s New ToDay')
        self.bottom_layout1.addWidget(self.bottom_label, alignment=Qt.AlignCenter)
        self.bottom_label.setAlignment(Qt.AlignCenter)
        self.bottom_label.setStyleSheet(" QLabel { background-color:  rgb(7, 30, 71); color: white; font-size: 50px; font-weight: bold;} ")
        self.bottom_label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)
        # self.bottom_label.setWordWrap(True)


        # adding a footer label to the bottom layout

        self.footer_label = QLabel()
        self.footer_label.setText('© 2026 Labery System. All rights reserved.')
        self.footer_label.setAlignment(Qt.AlignCenter)
        self.footer_label.setFixedHeight(20)
        self.footer_label.setStyleSheet(" QLabel { background-color:  rgb(7, 30, 71); color: white; font-size: 12px; border-radius: 5px; } ")


        # adding the four widget to lyt_home 

        self.lyt_home1.addWidget(self.informative_Label("Home Page"))
        self.lyt_home1.addWidget(self.wgt_header)
        self.lyt_home1.addWidget(self.bottom_widget)
        self.lyt_home1.addWidget(self.footer_label)

        self.lyt_home1.setStretch(0, 1) 
        self.lyt_home1.setStretch(1, 1) 
        self.lyt_home1.setStretch(2, 4)
        self.lyt_home1.setStretch(3, 1)

        #_________________________________



        # creating a book page

        self.wgt_add_books = QWidget()
        self.lyt_add_books = QVBoxLayout(self.wgt_add_books)
        self.wgt_add_books.setObjectName("books")
        self.wgt_add_books.setStyleSheet(" #books {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")


        # creating the head_book to add on wgt_add_books

        self.main_wgt1 = QWidget()
        self.main_layout1 = QVBoxLayout(self.main_wgt1)
        self.main_wgt1.setObjectName("main")
        self.main_wgt1.setStyleSheet(" #main {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")
        self.shadow(self.main_wgt1)


        # adding head_wgt to main_wgt1

        self.head_wgt = QWidget()
        self.head_lyt = QVBoxLayout(self.head_wgt)
        self.head_wgt.setObjectName("head")   
        self.head_wgt.setStyleSheet(" #head {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")
        # self.shadow(self.head_wgt)

        self.head_lyt.addStretch()
        self.head_lyt.addWidget(self.labels("Book Title"), alignment=Qt.AlignTop)
        self.txt_title = self.texts("Insert the Book Title")
        self.head_lyt.addWidget(self.txt_title, alignment=Qt.AlignTop)


        # adding midle_wgt to main_wgt1

        self.midle_wgt = QWidget()
        self.midle_lyt = QHBoxLayout(self.midle_wgt)
        self.midle_wgt.setFixedHeight(100)
        self.midle_wgt.setObjectName("midle")   
        self.midle_wgt.setStyleSheet(" #midle {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")
        # self.shadow(self.midle_wgt)

        self.midle_lyt.addWidget(self.labels("Year of Publication"), alignment=Qt.AlignTop)
        self.midle_lyt.addWidget(self.labels("Price"), alignment=Qt.AlignTop)
        self.midle_lyt.addWidget(self.labels("Aumont of Stock"), alignment=Qt.AlignTop)


        # adding midle_wgt2 to main_wgt1

        self.midle_wgt2 = QWidget()
        self.midle_lyt2 = QHBoxLayout(self.midle_wgt2)
        self.midle_wgt2.setObjectName("midle2")   
        self.midle_wgt2.setStyleSheet(" #midle2 {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")
        # self.shadow(self.midle_wgt2)

        self.txt_publication_year = self.texts("Insert the Book Publication Year", False)
        self.midle_lyt2.addWidget(self.txt_publication_year, alignment=Qt.AlignTop)

        self.txt_price = self.texts("Insert the Book Price", False)
        self.midle_lyt2.addWidget(self.txt_price, alignment=Qt.AlignTop)

        self.txt_stock = self.texts("Insert the Stock Aumont", False)
        self.midle_lyt2.addWidget(self.txt_stock, alignment=Qt.AlignTop)

        self.midle_lyt2.addStretch()

        # adding button_wgt2 to main_wgt1

        self.button_wgt = QWidget()
        self.button_lyt = QHBoxLayout(self.button_wgt)
        self.button_wgt.setObjectName("button")   
        self.button_wgt.setStyleSheet(" #button {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")
        # self.shadow(self.button_wgt)

        # adding buttons on bottom_lyt
        self.button_lyt.addStretch()

        self.btn_add = self.send_buttons("Add")
        self.button_lyt.addWidget(self.btn_add, alignment=Qt.AlignRight)
        self.btn_add.clicked.connect(self.add)

        self.button_lyt.addWidget(self.send_buttons("Update"), alignment=Qt.AlignRight)
        self.button_lyt.addWidget(self.send_buttons("Delete"), alignment=Qt.AlignRight)


        # adding bottom_wgt to main_wgt1

        self.bottom_wgt = QWidget()
        self.bottom_lyt = QVBoxLayout(self.bottom_wgt)
        self.bottom_wgt.setObjectName("bottom")
        self.bottom_wgt.setStyleSheet(" #bottom {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")
        self.shadow(self.bottom_wgt)

        self.search = self.texts("Search Books", False)
        self.bottom_lyt.addWidget(self.search, alignment=Qt.AlignTop)
        

        self.search_icon = QToolButton(self.search)
        self.search_icon.setIcon(QIcon("icons/procurar.png"))
        self.search_icon.setCursor(Qt.PointingHandCursor)
        self.search_icon.setStyleSheet("border: none;")

        self.search.setLayoutDirection(Qt.LeftToRight)
        self.search_icon.move(self.search.width() - 65, (self.search.height() - 15) // 2)
        self.search_icon.clicked.connect(self.search_books)


        # adding table to bottom_wgt

        self.book_table = QTableView()
        self.bottom_lyt.addWidget(self.book_table)
        self.book_table.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.book_table.setStyleSheet(""" QTableView { background-color: rgb(16, 40, 83); border-radius: 5px; gridline-color: transparent; color: #ffffff; font-size: 13px; } QTableView::item { padding: 6px; } """)



        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["ID", "Title", "Year of Publication", "Price", "Aumont of Stock"])
        self.book_table.setModel(self.model)
        self.book_table.setSelectionBehavior(QTableView.SelectRows)
        self.book_table.setSelectionMode(QTableView.SingleSelection)
        self.book_table.clicked.connect(self.row_clicked)

        self.model.removeRows(0, self.model.rowCount())

        # adding all the QWidget on the main_layout1

        self.main_layout1.addWidget(self.head_wgt)
        self.main_layout1.addWidget(self.midle_wgt)
        self.main_layout1.addWidget(self.midle_wgt2)
        self.main_layout1.addWidget(self.button_wgt)        
        self.main_layout1.addWidget(self.bottom_wgt)
        self.main_layout1.setStretch(0, 1)   
        self.main_layout1.setStretch(1, 1) 
        self.main_layout1.setStretch(2, 1)           
        self.main_layout1.setStretch(3, 1)           
        self.main_layout1.setStretch(4, 5)

        # adding the three widget to lyt_add_books

        self.lyt_add_books.addWidget(self.informative_Label("Adding Books"))
        self.lyt_add_books.addWidget(self.main_wgt1)


        #_________________________________



        # creating a readers page

        self.wgt_add_readers = QWidget()
        self.lyt_add_readers = QHBoxLayout(self.wgt_add_readers)
        self.lyt_add_readers.addWidget(QLabel("Addeding Readers Page", alignment=Qt.AlignTop))
        self.wgt_add_readers.setObjectName("readers")
        self.wgt_add_readers.setStyleSheet(" #readers {background-color: red; border-radius: 10px; height: 50px; }")


        #_________________________________



        # creating a librarian page

        self.wgt_add_librarian = QWidget()
        self.lyt_add_librarian = QHBoxLayout(self.wgt_add_librarian)
        self.lyt_add_librarian.addWidget(QLabel("Adding librarian Page", alignment=Qt.AlignTop))
        self.wgt_add_librarian.setObjectName("librarian")
        self.wgt_add_librarian.setStyleSheet(" #librarian {background-color: red; border-radius: 10px; height: 50px; }")


        #_________________________________



        # creating a maneger page

        self.wgt_manager = QWidget()
        self.lyt_manager = QHBoxLayout(self.wgt_manager)
        self.lyt_manager.addWidget(QLabel("Manager Page", alignment=Qt.AlignTop))
        self.wgt_manager.setObjectName("manager")
        self.wgt_manager.setStyleSheet(" #manager {background-color: red; border-radius: 10px; height: 50px; }")



        #_________________________________


        # creating a settings page

        self.wgt_settings = QWidget()
        self.lyt_settings = QHBoxLayout(self.wgt_settings)
        self.lyt_settings.addWidget(QLabel("Settings Page", alignment=Qt.AlignTop))
        self.wgt_settings.setObjectName("settings")
        self.wgt_settings.setStyleSheet(" #settings {background-color: red; border-radius: 10px; height: 50px; }")


        #_________________________________



        # adding all widget into right_painel_stackedwidget

        self.right_painel_stackedwidget.addWidget(self.wgt_home)
        self.right_painel_stackedwidget.addWidget(self.wgt_add_books)
        self.right_painel_stackedwidget.addWidget(self.wgt_add_readers)
        self.right_painel_stackedwidget.addWidget(self.wgt_add_librarian)
        self.right_painel_stackedwidget.addWidget(self.wgt_manager)
        self.right_painel_stackedwidget.addWidget(self.wgt_settings)


    def labels(self, text) -> None:
        lbl = QLabel()
        lbl.setText(text)
        lbl.setContentsMargins(30, 40, 0, 10)
        lbl.setStyleSheet(" QLabel { color: white; font-size: 16px; font-weight: bold; padding-top: 10px; }")
        return lbl
    
    def texts(self, text, value= True) -> None:
        if value == True:
            txt = QLineEdit()
            txt.setFixedHeight(30)
            txt.setContentsMargins(30, 0, 40, 0)
            txt.setTextMargins(20, 0, 0, 0)    
            txt.setPlaceholderText(text)
            txt.setStyleSheet(" QLineEdit {background-color: rgb(7, 30, 71); color: white; border-radius: 10px;}") 
            shadow = QGraphicsDropShadowEffect(txt)
            shadow.setBlurRadius(1)
            shadow.setOffset(1)
            shadow.setColor(QColor(255, 255, 255))
            txt.setGraphicsEffect(shadow)
            return txt
        else:
            txt = QLineEdit()
            txt.setFixedHeight(30)
            txt.setFixedWidth(350)
            txt.setContentsMargins(30, 0, 40, 0)
            txt.setTextMargins(20, 0, 0, 0)    
            txt.setPlaceholderText(text)
            txt.setStyleSheet(" QLineEdit {background-color: rgb(7, 30, 71); color: white; border-radius: 10px;}") 
            shadow = QGraphicsDropShadowEffect(txt)
            shadow.setBlurRadius(1)
            shadow.setOffset(1)
            shadow.setColor(QColor(255, 255, 255))
            txt.setGraphicsEffect(shadow)
            return txt


    def setup_connect(self) -> None:
        self.btn_home.clicked.connect(self.show_home)
        self.btn_book.clicked.connect(self.show_books)
        self.btn_reader.clicked.connect(self.show_readers)
        self.btn_librarian.clicked.connect(self.show_librarian)
        self.btn_manager.clicked.connect(self.show_manager)
        self.btn_settings.clicked.connect(self.show_settings)

    def informative_Label(self, text) -> None:
        lbl = QLabel()
        lbl.setText(text)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setFixedHeight(40)
        lbl.setStyleSheet(" QLabel { background-color:  rgb(7, 30, 71); color: white; font-size: 15px; border-radius: 5px; } ")
        self.shadow(lbl)
        return lbl

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
    
    def send_buttons(self, text) -> None:
        self.btn1 = QPushButton(text)
        self.btn1.setCursor(Qt.PointingHandCursor)
        self.btn1.setFixedSize(100, 30)
        return self.btn1

    def create_table(self):
        self.table = QTableView()
        self.table.setModel(self.model)

        self.table.setSelectionBehavior(QTableView.SelectRows)
        self.table.setSelectionMode(QTableView.SingleSelection)
        self.table.setEditTriggers(QTableView.NoEditTriggers)

        self.table.horizontalHeader().setStretchLastSection(True)

        self.table.setStyleSheet(" QTableView { border: none; background-color: #1e1e1e; } QHeaderView::section { background-color: #2d2d2d; border: none; padding: 6px; } ")

    def search_books(self) -> None:
        search_text = self.search.text()
        cursor.execute(' SELECT id, titulo, ano_publicacao, preco, estoque FROM livros WHERE titulo LIKE %s', (f"%{search_text}%",) )

        self.model.removeRows(0, self.model.rowCount())

        for row_data in cursor.fetchall():
            row_items = []
            for value in row_data:
                item = QStandardItem(str(value))
                item.setEditable(False)
                row_items.append(item)

            self.model.appendRow(row_items)

    def row_clicked(self, index) -> None:
        row = index.row()
        self.txt_title.setText(self.model.item(row, 1).text())
        self.txt_publication_year.setText(self.model.item(row, 2).text())
        self.txt_price.setText(self.model.item(row, 3).text())
        self.txt_stock.setText(self.model.item(row, 4).text())


    def add(self) -> None:
        from class_add_books import AddBook
        added = AddBook()
        ano = int(self.txt_publication_year)
        preco = int(self.txt_price)
        stock = int(self.txt_stock)
        added.insert(self.txt_title, ano, preco, stock)


app = QApplication(sys.argv)
window = MainFrame(None)
window.show()
app.exec()