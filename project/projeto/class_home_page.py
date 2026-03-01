from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from sql_parts import SqlParts


class Home:

    def __init__(self):
       pass

    def home_page(self) -> QWidget:

        self.sql = SqlParts("") 

        # creating a home page

        self.wgt_home = QWidget()
        self.lyt_home1 = QVBoxLayout(self.wgt_home)
        self.wgt_home.setObjectName("home")
        self.wgt_home.setStyleSheet(" #home {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")


        # creating a center information Label
        
        # self.informative_Label("Home Page")


        # creating a header widget 

        self.wgt_header = QWidget()
        self.lyt_header = QHBoxLayout(self.wgt_header)
        self.lyt_header.setSpacing(50)
        self.wgt_header.setObjectName("home")
        self.wgt_header.setStyleSheet(" #home {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")
        self.shadow(self.wgt_header)


        # adding a the first label on the midel layout
        self.label_book = QLabel()
        self.label_book.setText(f"Added Books \n \n {self.sql.select_books()[0]}")
        self.label_book.setAlignment(Qt.AlignCenter)
        self.lyt_header.addWidget(self.label_book)
        self.label_book.setStyleSheet(" QLabel { background-color: rgb(255, 192, 35); color: white; font-size: 20px; font-weight: bold; border-radius: 40px; }")
        self.label_book.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)

        # adding a the second label on the top layout
        self.label_worker = QLabel()
        self.label_worker.setText(f"Added Workers \n \n {self.sql.select_workers()[0]}")
        self.label_worker.setAlignment(Qt.AlignCenter)
        self.lyt_header.addWidget(self.label_worker)
        self.label_worker.setStyleSheet(" QLabel { background-color: rgb(5, 193, 116); color: white; font-size: 20px; font-weight: bold; border-radius: 40px;}")
        self.label_worker.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred)

        # adding a the third label on the top layout
        self.label_reader = QLabel()
        self.label_reader.setText(f"Added Readers \n \n {self.sql.select_readers()[0]}")
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

        return self.wgt_home

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