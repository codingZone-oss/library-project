from time import sleep
from PySide6.QtWidgets import  QWidget, QVBoxLayout, QHBoxLayout, QMainWindow, QLabel, QGraphicsDropShadowEffect, QSizePolicy, QLineEdit, QPushButton, QToolButton, QMessageBox, QTableView
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator, QIcon, QColor, QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QRegularExpression
from sql_part import Readers
from classs_warning_frame import Alert


class Reader(QMainWindow):

    def __init__(self):
        super().__init__()
        pass

    def readers_page(self) -> QWidget:

    # creating a readers page

        self.wgt_readers = QWidget()
        self.lyt_readers = QVBoxLayout(self.wgt_readers)
        self.wgt_readers.setObjectName("readers")
        self.wgt_readers.setStyleSheet(" #readers {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")

    # adding self.top_wgt on lyt_readers

        self.top_wgt = QWidget()
        self.top_lyt = QHBoxLayout(self.top_wgt)
        self.top_wgt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.top_wgt.setObjectName("top")
        self.top_wgt.setStyleSheet(" #top {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")

        # adding widgets on top_wgt

        self.left_wgt2 = QWidget()
        self.left_lyt2 = QVBoxLayout(self.left_wgt2)
        self.left_wgt2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.left_wgt2.setObjectName("left")
        self.left_wgt2.setStyleSheet(" #left {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px;}")

            # adding some widgets on left_lyt2

        self.txt_name = self.texts("Insert the Name")
        self.left_lyt2.addWidget(self.labels("Reader`s Name"), alignment=Qt.AlignTop)
        self.left_lyt2.addWidget(self.txt_name, alignment=Qt.AlignTop)

        self.midle_wgt2 = QWidget()
        self.midle_lyt2 = QVBoxLayout(self.midle_wgt2)
        self.midle_wgt2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.midle_wgt2.setObjectName("midle")
        self.midle_wgt2.setStyleSheet(" #midle {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px;}")

            # adding some widgets on midle_lyt2

        self.midle_lyt2.addWidget(self.labels("E-mail"), alignment=Qt.AlignTop)
        self.txt_email = self.texts("Insert the Email")
        self.midle_lyt2.addWidget(self.txt_email, alignment=Qt.AlignTop)

        self.right_wgt2 = QWidget()
        self.right_lyt2 = QVBoxLayout(self.right_wgt2)
        self.right_wgt2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_wgt2.setObjectName("right")
        self.right_wgt2.setStyleSheet(" #right {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px;}")

            # adding some widgets on right_wgt2

        self.right_lyt2.addWidget(self.labels("Phone Number"), alignment=Qt.AlignTop)
        self.txt_phone = self.texts("Insert the Phone Number", integer=True, limit=100000000)
        self.right_lyt2.addWidget(self.txt_phone, alignment=Qt.AlignTop)

    # adding the 3 widget on top_lyt

        self.top_lyt.addWidget(self.left_wgt2)
        self.top_lyt.addWidget(self.midle_wgt2)
        self.top_lyt.addWidget(self.right_wgt2)



    # adding sub_top_wgt on lyt_readers

        self.sub_top_wgt = QWidget()
        self.sub_top_lyt = QHBoxLayout(self.sub_top_wgt)
        self.sub_top_wgt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sub_top_wgt.setObjectName("sub_top")
        self.sub_top_wgt.setStyleSheet(" #sub_top {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")

        # adding widgets on sub_top_wgt

        self.left_wgt21 = QWidget()
        self.left_lyt21 = QVBoxLayout(self.left_wgt21)
        self.left_wgt21.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.left_wgt21.setObjectName("left21")
        self.left_wgt21.setStyleSheet(" #left21 {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px;}")

            # adding widgets on left_lyt21

        self.left_lyt21.addWidget(self.labels("Nacionality"), alignment=Qt.AlignTop)
        self.txt_nacionality = self.texts("Insert the Nacionality")
        self.left_lyt21.addWidget(self.txt_nacionality, alignment=Qt.AlignTop)

        self.midle_wgt21 = QWidget()
        self.midle_lyt21 = QVBoxLayout(self.midle_wgt21)
        self.midle_wgt21.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.midle_wgt21.setObjectName("midle1")
        self.midle_wgt21.setStyleSheet(" #midle1 {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px;}")

            # adding widgets on midle_lyt21

        self.midle_lyt21.addWidget(self.labels("Location"), alignment=Qt.AlignTop)
        self.txt_city = self.texts("Insert the City Name")
        self.midle_lyt21.addWidget(self.txt_city, alignment=Qt.AlignTop)

        self.right_wgt21 = QWidget()
        self.right_lyt21 = QVBoxLayout(self.right_wgt21)
        self.right_wgt21.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_wgt21.setObjectName("right1")
        self.right_wgt21.setStyleSheet(" #right1 {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px;}")

            # adding widgets on right_lyt21

        self.right_lyt21.addWidget(self.labels("Identity Card Number"), alignment=Qt.AlignTop)
        self.txt_identity = self.texts("Insert the Identity Card Number")
        self.right_lyt21.addWidget(self.txt_identity, alignment=Qt.AlignTop)
        

    # adding the 3 widget on top_lyt

        self.sub_top_lyt.addWidget(self.left_wgt21)
        self.sub_top_lyt.addWidget(self.midle_wgt21)
        self.sub_top_lyt.addWidget(self.right_wgt21)



    # adding body on lyt_readers

        self.body_wgt = QWidget()
        self.body_lyt = QHBoxLayout(self.body_wgt)
        self.body_wgt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.body_wgt.setObjectName("body")
        self.body_wgt.setStyleSheet(" #body {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")

        # adding widgets on body_wgt

        self.left_wgt3 = QWidget()
        self.left_lyt3 = QVBoxLayout(self.left_wgt3)
        self.left_wgt3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.left_wgt3.setObjectName("left2")
        self.left_wgt3.setStyleSheet(" #left2 {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px;}")

            # adding some widgets on left_lyt3

        self.left_lyt3.addWidget(self.labels("Library Card Ticket"),alignment=Qt.AlignTop)
        self.txt_ticket = self.texts("xxxx xxxx xxx xxx xx", integer=True, limit=1000000000)
        self.left_lyt3.addWidget(self.txt_ticket, alignment=Qt.AlignTop)


        self.right_wgt3 = QWidget()
        self.right_lyt3 = QVBoxLayout(self.right_wgt3)
        self.right_wgt3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_wgt3.setObjectName("right")
        self.right_wgt3.setStyleSheet(" #right {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px;}")

                # top_right_wgt3
        self.top_right_wgt3 = QWidget()
        self.top_right_lyt3 = QHBoxLayout(self.top_right_wgt3)
        self.top_right_wgt3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.top_right_wgt3.setObjectName("top_right2")
        self.top_right_wgt3.setStyleSheet(" #top_right2 {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px;}")

            # adding some widgets on top_right_lyt3

        self.top_right_lyt3.addWidget(self.buttons("Clear", "Click to clear all Filds"))
        self.top_right_lyt3.addWidget(self.buttons("Add", "Click to add a new reader"))
        self.top_right_lyt3.addWidget(self.buttons("Update", "Click to update the reader data"))
        self.top_right_lyt3.addWidget(self.buttons("Delete", "Click to delete a reader"))

                # bottom_right_wgt3

        self.bottom_right_wgt3 = QWidget()
        self.bottom_right_lyt3 = QHBoxLayout(self.bottom_right_wgt3)
        self.bottom_right_wgt3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.bottom_right_wgt3.setObjectName("bottom_right2")
        self.bottom_right_wgt3.setStyleSheet(" #bottom_right2 {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px;}")

        # adding the top_right_wgt3 and bottom_right_wgt3 on right_lyt3

        self.right_lyt3.addWidget(self.top_right_wgt3)
        self.right_lyt3.addWidget(self.bottom_right_wgt3)

        # adding the 2 widget on body_lyt

        self.body_lyt.addWidget(self.left_wgt3)
        self.body_lyt.addWidget(self.right_wgt3)


    # adding bottom on lyt_readers

        self.bottom_wgt = QWidget()
        self.bottom_lyt = QVBoxLayout(self.bottom_wgt)
        self.bottom_wgt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.bottom_wgt.setObjectName("bottom")
        self.bottom_wgt.setStyleSheet(" #bottom {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")

        # adding widgets on bottom_lyt

        self.txt_search = self.texts("Search Readers", value=False)
        self.bottom_lyt.addWidget(self.txt_search, alignment=Qt.AlignLeft)


        self.search_icon = QToolButton(self.txt_search)
        self.search_icon.setIcon(QIcon("icons/procurar.png"))
        self.search_icon.setStyleSheet(" border:none;")
        self.search_icon.setCursor(Qt.ArrowCursor)

        self.txt_search.setLayoutDirection(Qt.LeftToRight)
        self.search_icon.move(self.txt_search.width() - 65, (self.txt_search.height() - 15) // 2)
        self.txt_search.textChanged.connect(self.search)

        # adding a table on bottom_lyt

        self.table = QTableView()
        self.bottom_lyt.addWidget(self.table)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table.setStyleSheet(" QTableView { background-color: rgb(7, 30, 71); color: #ffffff; font-size: 13px;}")

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["id", "Name", "E-mail", "Phone", "Nacionality", "City", "Number Identity", "Library Card Ticket"])
        self.table.setModel(self.model)
        
        self.table.setSelectionBehavior(QTableView.SelectRows)
        self.table.setSelectionMode(QTableView.SingleSelection)
        self.table.clicked.connect(self.row_clicked)

        
    # adding the 5 main_widget on lyt_readers

        self.lyt_readers.addWidget(self.informative_Label("Adding Readers"))
        self.lyt_readers.addWidget(self.top_wgt)
        self.lyt_readers.addWidget(self.sub_top_wgt)
        self.lyt_readers.addWidget(self.body_wgt)
        self.lyt_readers.addWidget(self.bottom_wgt)

        return self.wgt_readers

    def search(self)-> None:
        self.text = self.txt_search.text().strip()
        if self.text == "":
            self.model.removeRows(0, self.model.rowCount())
        else:
            self.cursor = Readers().select_readers(self.text)
            if self.cursor == False:
                self.alert = Alert("\n       ERROR EXECUTEING QUERY", Bool=True); sleep(0.6);self.alert.show()
            else:
                if not self.cursor:pass
                else:
                    for row_data in self.cursor:
                        row_items = []
                    for value in row_data:
                        print(value)
                        item = QStandardItem(str(value))
                        item.setEditable(False)
                        row_items.append(item)

                    self.model.appendRow(row_items)

    def row_clicked(self) -> None:
        pass


    def informative_Label(self, text) -> None:
        lbl = QLabel()
        lbl.setText(text)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setFixedHeight(40)
        lbl.setStyleSheet(" QLabel { background-color:  rgb(7, 30, 71); color: white; font-size: 15px; border-radius: 5px; } ")
        self.shadow(lbl)
        return lbl
    
    def buttons(self, text, tooltip) -> QPushButton:
        self.button = QPushButton(text)
        self.button.setCursor(Qt.PointingHandCursor)
        self.button.setShortcut("Return")
        self.button.setFixedSize(100, 30)
        self.button.setToolTip(tooltip)
        return self.button
         
        
    def texts(self, text, value= True, integer=False, real=False, limit:any=None) -> QLineEdit:
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
    
    def labels(self, text) -> QLabel:
            lbl = QLabel()
            lbl.setText(text)
            lbl.setContentsMargins(30, 0, 0, 0)
            lbl.setStyleSheet(" QLabel { color: white; font-size: 16px; font-weight: bold; padding-top: 10px; }")
            return lbl
    
    def shadow(self, widget):
            shadow = QGraphicsDropShadowEffect(widget)
            shadow.setBlurRadius(12)
            shadow.setOffset(1, 0)
            shadow.setColor(QColor(0, 0, 0, 80))
            return widget.setGraphicsEffect(shadow)