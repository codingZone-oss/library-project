from PySide6.QtWidgets import  QWidget, QVBoxLayout, QLabel, QGraphicsDropShadowEffect, QSizePolicy, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class Reader:

    def __init__(self):
        pass

    def readers_page(self) -> QWidget:

        # creating a readers page

        self.wgt_readers = QWidget()
        self.lyt_readers = QVBoxLayout(self.wgt_readers)
        self.wgt_readers.setObjectName("readers")
        self.wgt_readers.setStyleSheet(" #readers {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")

        # adding top_wgt on lyt_readers

        self.top_wgt = QWidget()
        self.top_lyt = QHBoxLayout(self.top_wgt)
        self.top_wgt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.top_wgt.setObjectName("top")
        self.top_wgt.setStyleSheet(" #top {background-color: red; border-radius: 10px; height: 50px; }")


        # adding sub_top_wgt on lyt_readers

        self.sub_top_wgt = QWidget()
        self.sub_top_lyt = QHBoxLayout(self.sub_top_wgt)
        self.sub_top_wgt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sub_top_wgt.setObjectName("sub_top")
        self.sub_top_wgt.setStyleSheet(" #sub_top {background-color: blue; border-radius: 10px; height: 50px; }")

        # adding body on lyt_readers

        self.body_wgt = QWidget()
        self.body_lyt = QHBoxLayout(self.body_wgt)
        self.body_wgt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.body_wgt.setObjectName("body")
        self.body_wgt.setStyleSheet(" #body {background-color: orange; border-radius: 10px; height: 50px; }")

        # adding bottom on lyt_readers

        self.bottom_wgt = QWidget()
        self.bottom_lyt = QHBoxLayout(self.bottom_wgt)
        self.bottom_wgt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.bottom_wgt.setObjectName("bottom")
        self.bottom_wgt.setStyleSheet(" #bottom {background-color: pink; border-radius: 10px; height: 50px; }")



        self.lyt_readers.addWidget(self.top_wgt)
        self.lyt_readers.addWidget(self.sub_top_wgt)
        self.lyt_readers.addWidget(self.body_wgt)
        self.lyt_readers.addWidget(self.bottom_wgt)


        #  so friend i´m about to teste just one more thing right here, just to teste the quicly it is

        return self.wgt_readers


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