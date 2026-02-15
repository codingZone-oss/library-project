from PySide6.QtWidgets import  QWidget, QHBoxLayout, QLabel, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class Reader:

    def __init__(self):
        pass

    def readers_page(self) -> QWidget:

        # creating a readers page

        self.wgt_add_readers = QWidget()
        self.lyt_add_readers = QHBoxLayout(self.wgt_add_readers)
        self.wgt_add_readers.setObjectName("readers")
        self.wgt_add_readers.setStyleSheet(" #readers {background-color: red; border-radius: 10px; height: 50px; }")

        self.lyt_add_readers.addWidget(self.informative_Label("Adding Readers"))

        return self.wgt_add_readers
        #_________________________________



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