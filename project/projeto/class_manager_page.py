from PySide6.QtWidgets import  QWidget, QHBoxLayout, QLabel, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class Manager1:

    def __init__(self):
        pass

    def manager_page(self) -> QWidget:


        # creating a maneger page

        self.wgt_manager = QWidget()
        self.lyt_manager = QHBoxLayout(self.wgt_manager)
        self.wgt_manager.setObjectName("manager")
        self.wgt_manager.setStyleSheet(" #manager {background-color: red; border-radius: 10px; height: 50px; }")

        self.lyt_manager.addWidget(self.informative_Label("Manager Page"))

        return self.wgt_manager


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