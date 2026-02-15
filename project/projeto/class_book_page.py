from time import sleep
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QGraphicsDropShadowEffect, QTableView, QToolButton, QLineEdit, QPushButton
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIntValidator, QDoubleValidator
from classs_warning_frame import Alert, Successefull
from sql_parts import AddBook
from class_conextion import cursor
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from sql_parts import SqlParts
from PySide6.QtGui import QIcon



class Book:

    def __init__(self):
        pass

    def book_page(self) -> QWidget:

        self.sql = SqlParts("") 

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

        self.txt_publication_year = self.texts("Insert the Book Publication Year", value=False, integer=True, limit=1000)
        self.midle_lyt2.addWidget(self.txt_publication_year, alignment=Qt.AlignTop)

        self.txt_price = self.texts("Insert the Book Price", value=False, real=True, limit=999999.99)
        self.midle_lyt2.addWidget(self.txt_price, alignment=Qt.AlignTop)

        self.txt_stock = self.texts("Insert the Stock Aumont", value=False, integer=True, limit=10000)
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
        self.btn_add.clicked.connect(self.addig_books)
        

        self.button_lyt.addWidget(self.send_buttons("Update"), alignment=Qt.AlignRight)
        self.button_lyt.addWidget(self.send_buttons("Delete"), alignment=Qt.AlignRight)


        # adding bottom_wgt to main_wgt1

        self.bottom_wgt = QWidget()
        self.bottom_lyt = QVBoxLayout(self.bottom_wgt)
        self.bottom_wgt.setObjectName("bottom")
        self.bottom_wgt.setStyleSheet(" #bottom {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")
        self.shadow(self.bottom_wgt)

        self.search = self.texts("Search Books", value=False)
        self.bottom_lyt.addWidget(self.search, alignment=Qt.AlignTop)
        

        self.search_icon = QToolButton(self.search)
        self.search_icon.setIcon(QIcon("icons/procurar.png"))
        self.search_icon.setCursor(Qt.PointingHandCursor)
        self.search_icon.setStyleSheet("border: none;")
        self.search_icon.setShortcut("Return")

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

        return self.wgt_add_books

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


    def labels(self, text) -> None:
            lbl = QLabel()
            lbl.setText(text)
            lbl.setContentsMargins(30, 40, 0, 10)
            lbl.setStyleSheet(" QLabel { color: white; font-size: 16px; font-weight: bold; padding-top: 10px; }")

            return lbl
    
    def texts(self, text, value= True, integer=False, real=False, limit:any=None) -> None:
        txt = QLineEdit()

        if value == False:
            txt.setFixedWidth(350)

        if integer == True:
            txt.setValidator(QIntValidator(0, limit))

        if real == True:
            txt.setValidator(QDoubleValidator(0.0, limit, 2))
            
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


    def addig_books(self) -> None:
        add = AddBook()
        while not self.txt_title.text() or not self.txt_publication_year.text() or not self.txt_price.text() or not self.txt_stock.text():
            self.warning = Alert("Fill In All Fields")
            sleep(0.6)
            self.warning.show()
            return

        self.title = self.txt_title.text()
        self.ano = self.txt_publication_year.text()
        self.price = self.txt_price.text()
        self.stock = self.txt_stock.text()

        add.insert(self.title, self.ano, self.price, self.stock)
        self.success = Successefull("ADDED WITH SUCCESS")
        sleep(0.6)
        self.success.show()

    def send_buttons(self, text) -> None:
        self.btn1 = QPushButton(text)
        self.btn1.setCursor(Qt.PointingHandCursor)
        self.btn1.setShortcut("Return")
        self.btn1.setFixedSize(100, 30)
        return self.btn1