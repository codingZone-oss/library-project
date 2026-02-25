from time import sleep
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QGraphicsDropShadowEffect, QTableView, QToolButton, QLineEdit, QPushButton, QSpinBox, QComboBox
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIntValidator, QRegularExpressionValidator
from classs_warning_frame import Alert, Successefull
from sql_parts import AddBook
from class_conextion import cursor
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt, QRegularExpression
from sql_parts import SqlParts
from PySide6.QtGui import QIcon
from datetime import date



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
        self.head_lyt = QHBoxLayout(self.head_wgt)
        self.head_wgt.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.head_wgt.setObjectName("head")   
        self.head_wgt.setStyleSheet(" #head {background-color: rgb(7, 30, 71);; border-radius: 10px; height: 50px; }")

        self.left_wgt1 = QWidget()
        self.left_lyt1 = QVBoxLayout(self.left_wgt1) 
        self.left_wgt1.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.left_wgt1.setObjectName("right")   
        self.left_wgt1.setStyleSheet(" #right {background-color: rgb(7, 30, 71);; border-radius: 10px; height: 50px; }")

        self.left_lyt1.addWidget(self.labels("Book Title"), alignment=Qt.AlignTop)
        self.txt_title = self.texts("Insert the Book Title")
        self.left_lyt1.addWidget(self.txt_title, alignment=Qt.AlignTop)


        self.center_wgt = QWidget()
        self.center_lyt = QVBoxLayout(self.center_wgt) 
        self.center_wgt.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.center_wgt.setObjectName("center")   
        self.center_wgt.setStyleSheet(" #center {background-color: rgb(7, 30, 71);; border-radius: 10px; height: 50px; }")

        self.center_lyt.addWidget(self.labels("Publisher"), alignment=Qt.AlignTop)
        self.txt_publisher = self.texts("Insert the Book Publisher")
        self.center_lyt.addWidget(self.txt_publisher, alignment=Qt.AlignTop)


        self.right_wgt = QWidget()
        self.right_lyt = QVBoxLayout(self.right_wgt) 
        self.right_wgt.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_wgt.setObjectName("right")   
        self.right_wgt.setStyleSheet(" #right {background-color: rgb(7, 30, 71);; border-radius: 10px; height: 50px; }")

        self.combo_category = QComboBox()
        self.combo_category.addItems(["Action and Adventure", "Alternate History", "Anthology", "Art and Photography", "Autobiography", "Biography", "Business and Economics", "Classic", "Comic Book", "Coming-of-age", "Contemporary", "Cookbooks", "Crime", "Diary", "Dictionary", "Drama", "Dystopian", "Education", "Encyclopedia", "Essays", "Fairy Tale", "Families and Relationships", "Fantasy", "Fitness", "Folklore", "Graphic Novel", "Guide", "Health and Wellness", "Historical Fiction", "History", "Home and Garden", "Horror", "How-to", "Humour and Satire", "Literary Fiction", "Memoir", "Mystery", "Mythology", "New Adult", "Parentship", "Paranormal", "Philosophy", "Picture Book", "Poetry", "Politics", "Psychological Thriller", "Psychology", "Religion and Spirituality", "Romance", "Science", "Science Fiction", "Self-Help", "Short Story", "Suspense", "Textbook", "Thriller", "Travel", "True Crime", "Western", "Women's Fiction", "Young Adult"])
        self.combo_category.setFixedHeight(30)
        self.combo_category.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.combo_category.setObjectName("combo_category")   
        self.combo_category.setStyleSheet(" #combo_category {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")
        shadow = QGraphicsDropShadowEffect(self.combo_category)
        shadow.setBlurRadius(1)
        shadow.setOffset(1)
        shadow.setColor(QColor(255, 255, 255))
        self.combo_category.setGraphicsEffect(shadow)

        self.right_lyt.addWidget(self.labels("Book Category"), alignment=Qt.AlignTop)
        self.right_lyt.addWidget(self.combo_category, alignment=Qt.AlignTop)

        self.head_lyt.addWidget(self.left_wgt1)
        self.head_lyt.addWidget(self.center_wgt)
        self.head_lyt.addWidget(self.right_wgt)

        self.head_lyt.setStretch(0, 1)
        self.head_lyt.setStretch(1, 1)
        self.head_lyt.setStretch(2, 1)

        
        # adding midle_wgt to main_wgt1

        self.midle_wgt = QWidget()
        self.midle_lyt = QHBoxLayout(self.midle_wgt)
        self.midle_wgt.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.midle_wgt.setObjectName("midle")   
        self.midle_wgt.setStyleSheet(" #midle {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")

        # adding midle_wgt to main_wgt1


        self.center_wgt2 = QWidget()
        self.center_lyt2 = QVBoxLayout(self.center_wgt2)
        self.center_wgt2.setObjectName("center")  
        self.center_wgt2.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.center_wgt2.setStyleSheet(" #center {background-color: rgb(7, 30, 71);; border-radius: 10px; height: 50px; }")

        self.center_lyt2.addWidget(self.labels("Price"), alignment=Qt.AlignTop)
        self.txt_price = self.texts("Insert the Book Price", real=True, limit=999999.99)
        self.center_lyt2.addWidget(self.txt_price, alignment=Qt.AlignTop)

        self.midle_lyt.addWidget(self.center_wgt2)


        self.left_wgt1 = QWidget()
        self.left_lyt1 = QVBoxLayout(self.left_wgt1)
        self.left_wgt1.setObjectName("left_wgt1")  
        self.left_wgt1.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.left_wgt1.setStyleSheet(" #left_wgt1 {background-color: rgb(7, 30, 71);; border-radius: 10px; height: 50px; }")

        self.left_lyt1.addWidget(self.labels("Year of Publication"), alignment=Qt.AlignTop)
        self.spn_publication_year = self.spin_number(date1=True, bigin=1500, end=date.today().year)
        self.left_lyt1.addWidget(self.spn_publication_year, alignment=Qt.AlignTop)

        self.midle_lyt.addWidget(self.left_wgt1)


        self.right_wgt3 = QWidget()
        self.right_lyt3 = QVBoxLayout(self.right_wgt3)
        self.right_wgt3.setObjectName("right")  
        self.right_wgt3.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_wgt3.setStyleSheet(" #right {background-color: rgb(7, 30, 71);; border-radius: 10px; height: 50px; }")

        self.spin_stock = self.spin_number(stock=True, bigin=0, end=10000)
        self.right_lyt3.addWidget(self.labels("Aumont of Stock"), alignment=Qt.AlignTop)
        self.right_lyt3.addWidget(self.spin_stock, alignment=Qt.AlignTop)

        # self.right_lyt3.addStretch()
        self.midle_lyt.addWidget(self.right_wgt3)


        self.midle_lyt.setStretch(0, 1)
        self.midle_lyt.setStretch(1, 1)
        self.midle_lyt.setStretch(2, 1)

        # adding midle_wgt2 to main_wgt

        self.midle_wgt2 = QWidget()
        self.midle_lyt2 = QHBoxLayout(self.midle_wgt2)
        self.midle_wgt2.setObjectName("midle2")   
        self.midle_wgt2.setStyleSheet(" #midle2 {background-color: rgb(7, 30, 71);; border-radius: 10px; height: 50px; }")

        # adding author_wgt to midle_wgt2

        self.author_wgt = QWidget()
        self.author_lyt = QVBoxLayout(self.author_wgt)
        self.author_wgt.setObjectName("author_wgt")  
        self.author_wgt.setFixedHeight(70)
        # self.author_wgt.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.author_wgt.setStyleSheet(" #author_wgt {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")

        self.author_lyt.addWidget(self.labels("Author"), alignment=Qt.AlignTop)
        self.txt_author = self.texts("Insert the Book Author")
        self.author_lyt.addWidget(self.txt_author, alignment=Qt.AlignTop)

        self.midle_lyt2.addWidget(self.author_wgt)

        # adding center_wgt5 to midle_wgt2

        self.center_wgt5 = QWidget()
        self.center_lyt5 = QVBoxLayout(self.center_wgt5)
        self.center_wgt5.setObjectName("center_wgt5")  
        self.center_wgt5.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.center_wgt5.setStyleSheet(" #center_wgt5 {background-color: rgb(7, 30, 71);; border-radius: 10px; height: 50px; }")

        self.center_lyt5.addWidget(self.labels("Nationality"), alignment=Qt.AlignTop)
        self.txt_nationality = self.texts("Insert the Book Nationality")
        self.center_lyt5.addWidget(self.txt_nationality, alignment=Qt.AlignTop)

        self.midle_lyt2.addWidget(self.center_wgt5)

        # adding bottom_wgt6 to midle_wgt2

        self.right_wgt6 = QWidget()
        self.right_lyt6 = QVBoxLayout(self.right_wgt6)
        self.right_wgt6.setObjectName("bottom_wgt6")  
        self.right_wgt6.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_wgt6.setStyleSheet(" #bottom_wgt6 {background-color: rgb(7, 30, 71);; border-radius: 10px; height: 50px; }")

        self.right_lyt6.addWidget(self.labels("ISBN"), alignment=Qt.AlignTop)
        self.txt_isnb = self.texts("xxxx-xxxx-xxx-xx")
        self.right_lyt6.addWidget(self.txt_isnb, alignment=Qt.AlignTop)

        self.midle_lyt2.addWidget(self.right_wgt6)


        # adding button_wgt2 to main_wgt

        self.botton_wgt2 = QWidget()
        self.button_lyt = QHBoxLayout(self.botton_wgt2)
        self.botton_wgt2.setObjectName("button")   
        self.botton_wgt2.setStyleSheet(" #button {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")


        # adding left_wgt4 to button_wgt2

        self.left_wgt4 = QWidget()
        self.left_lyt4 = QVBoxLayout(self.left_wgt4)
        self.left_wgt4.setObjectName("left_wgt4")  
        self.left_wgt4.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.left_wgt4.setStyleSheet(" #left_wgt4 {background-color: rgb(7, 30, 71);; border-radius: 10px; height: 50px; }")

        self.left_lyt4.addWidget(self.labels("Description"), alignment=Qt.AlignTop)
        self.txt_description = self.texts("Describe the Book")
        self.left_lyt4.addWidget(self.txt_description, alignment=Qt.AlignTop)

        self.button_lyt.addWidget(self.left_wgt4)


        # self.button_lyt.addStretch()

        self.btn_add = self.send_buttons("Add")
        self.btn_add.clicked.connect(self.addig_books)

        self.btn_clean = self.send_buttons("Clean")
        self.btn_clean.clicked.connect(self.clean_filds)

        self.button_lyt.addWidget(self.btn_clean, alignment=Qt.AlignRight)
        self.button_lyt.addWidget(self.btn_add, alignment=Qt.AlignRight)
        self.button_lyt.addWidget(self.send_buttons("Update"), alignment=Qt.AlignRight)
        self.button_lyt.addWidget(self.send_buttons("Delete"), alignment=Qt.AlignRight)


        # adding bottom_wgt to main_wgt1

        self.bottom_wgt = QWidget()
        self.bottom_lyt = QVBoxLayout(self.bottom_wgt)
        self.bottom_wgt.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.bottom_wgt.setObjectName("bottom")
        self.bottom_wgt.setStyleSheet(" #bottom {background-color: rgb(7, 30, 71);; border-radius: 10px; height: 50px; }")
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
        self.model.setHorizontalHeaderLabels(["ID", "Title", "Year of Publication", "Author", "Price", "Aumont of Stock", "ISBN", "Publisher", "Category", "Nationality"])
        self.book_table.setModel(self.model)
        self.book_table.setSelectionBehavior(QTableView.SelectRows)
        self.book_table.setSelectionMode(QTableView.SingleSelection)
        self.book_table.clicked.connect(self.row_clicked)

        self.model.removeRows(0, self.model.rowCount())

        # adding all the QWidget on the main_layout1

        self.main_layout1.addWidget(self.head_wgt)
        self.main_layout1.addWidget(self.midle_wgt)
        self.main_layout1.addWidget(self.midle_wgt2)
        self.main_layout1.addWidget(self.botton_wgt2)        
        self.main_layout1.addWidget(self.bottom_wgt)
        self.main_layout1.setStretch(0, 1)   
        self.main_layout1.setStretch(1, 1) 
        self.main_layout1.setStretch(2, 1)           
        self.main_layout1.setStretch(3, 1)           
        self.main_layout1.setStretch(4, 5)

        # adding the three widget to lyt_add_books

        # self.lyt_add_books.addWidget(self.informative_Label("Adding Books"))
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
        cursor.execute(' SELECT id, titulo, ano_publicacao, autor, preco, estoque, ISBN, editora, categoria, nacionalidade FROM livros WHERE titulo LIKE %s', (f"%{search_text}%",) )

        self.model.removeRows(0, self.model.rowCount())

        for row_data in cursor.fetchall():
            row_items = []
            for value in row_data:
                item = QStandardItem(str(value))
                item.setEditable(False)
                row_items.append(item)

            self.model.appendRow(row_items)

    def row_clicked(self, index) -> None:

        self.row = index.row()
        self.txt_title.setText(self.model.item(self.row, 1).text())
        self.spn_publication_year.setValue(int(self.model.item(self.row, 2).text()))
        self.txt_author.setText(self.model.item(self.row, 3).text())
        self.txt_price.setText(self.model.item(self.row, 4).text())
        self.spin_stock.setValue(int(self.model.item(self.row, 5).text()))
        self.txt_isnb.setText(self.model.item(self.row, 6).text())
        self.txt_publisher.setText(self.model.item(self.row, 7).text())
        self.combo_category.setCurrentText(self.model.item(self.row, 8).text())
        self.txt_nationality.setText(self.model.item(self.row, 9).text())

    def labels(self, text) -> None:
            lbl = QLabel()
            lbl.setText(text)
            lbl.setContentsMargins(30, 0, 0, 0)
            lbl.setStyleSheet(" QLabel { color: white; font-size: 16px; font-weight: bold; padding-top: 10px; }")
            return lbl
    
    def spin_number(self, bigin:int, end:int, date1:bool= False, stock:bool= False) -> None:
        self.spin = QSpinBox()
        
        if date1 == True:
            self.spin.setRange(bigin, end)
            self.spin.setValue(date.today().year)
            self.spin.setSuffix("  Year")

        if stock == True:
            self.spin.setRange(bigin, end)
            self.spin.setValue(0)
            self.spin.setSuffix("  Stock")
        
        self.spin.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.spin.setFixedHeight(30)
        self.spin.setStyleSheet(" QSpinBox {background-color: rgb(7, 30, 71); color: white; font-size: 13px; padding: 0px 20px;}") 
        shadow = QGraphicsDropShadowEffect(self.spin)
        shadow.setBlurRadius(1)
        shadow.setOffset(1)
        shadow.setColor(QColor(255, 255, 255))
        self.spin.setGraphicsEffect(shadow)

        return self.spin
    
    def texts(self, text, value= True, integer=False, real=False, limit:any=None) -> None:
        txt = QLineEdit()

        if value == False:
            txt.setFixedWidth(350)

        if integer == True:
            txt.setValidator(QIntValidator(0, limit))

        if real == True:
            validator = QRegularExpressionValidator(QRegularExpression(r"^\d+(\.\d{0,2})?$"))
            txt.setValidator(validator)
            
        txt.setFixedHeight(30)
        txt.setPlaceholderText(text)
        txt.setTextMargins(20, 0, 0, 0)    
        txt.setContentsMargins(30, 0, 40, 0)
        txt.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
        txt.setStyleSheet(" QLineEdit {background-color: rgb(7, 30, 71); color: white; border-radius: 10px;}") 
        shadow = QGraphicsDropShadowEffect(txt)
        shadow.setBlurRadius(1)
        shadow.setOffset(1)
        shadow.setColor(QColor(255, 255, 255))
        txt.setGraphicsEffect(shadow)
        return txt


    def addig_books(self) -> None:
        add = AddBook()
        while not self.txt_title.text() or not self.txt_price.text() or self.spin_stock.value() == 0 or not self.txt_description.text() or not self.txt_nationality.text() or not self.txt_publisher.text() or not self.txt_isnb.text() or not self.txt_author.text():
            self.warning = Alert("Fill All Fields")
            sleep(0.6)
            self.warning.show()
            return

        self.title = self.txt_title.text()
        self.ano = self.spn_publication_year.value()
        self.autor = self.txt_author.text()
        self.price = self.txt_price.text()
        self.stock = self.spin_stock.value()
        self.isbn = self.txt_isnb.text()
        self.editora = self.txt_publisher.text()
        self.categoria = self.combo_category.currentText()
        self.nacionalidade = self.txt_nationality.text()
        self.descricao = self.txt_description.text()


        add.insert(self.title, self.ano, self.autor, self.price, self.stock, self.isbn, self.editora, self.categoria, self.nacionalidade, self.descricao)
        self.success = Successefull("ADDED WITH SUCCESS")
        sleep(0.6)
        self.clean_filds()
        self.success.show()

    def send_buttons(self, text) -> None:
        self.btn1 = QPushButton(text)
        self.btn1.setCursor(Qt.PointingHandCursor)
        self.btn1.setShortcut("Return")
        self.btn1.setFixedSize(100, 30)
        return self.btn1
    
    def clean_filds(self) -> None:
        self.txt_title.clear()
        self.txt_price.clear()
        self.spin_stock.setValue(0)
        self.spn_publication_year.setValue(date.today().year)
        self.combo_category.setCurrentIndex(0)
        self.txt_publisher.clear()
        self.txt_nationality.clear()
        self.txt_isnb.clear()
        self.txt_description.clear()
        self.txt_author.clear()