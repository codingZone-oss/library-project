from PySide6.QtWidgets import  QWidget, QVBoxLayout, QSizePolicy, QMainWindow, QHBoxLayout, QLabel, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class Libraian(QMainWindow):

    def __init__(self):
        super().__init__()
        pass

    def libraian_page(self) -> QWidget:


    # creating a librarian page


        self.wgt_add_librarian = QWidget()
        self.lyt_add_librarian = QVBoxLayout(self.wgt_add_librarian)
        self.wgt_add_librarian.setObjectName("readers")
        self.wgt_add_librarian.setStyleSheet(" #readers {background-color: rgb(7, 30, 71); border-radius: 10px; height: 50px; }")

    # adding self.top_wgt on lyt_add_librarian

        self.top_wgt = QWidget()
        self.top_lyt = QHBoxLayout(self.top_wgt)
        self.top_wgt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.top_wgt.setObjectName("top")
        self.top_wgt.setStyleSheet(" #top {background-color: red; border-radius: 10px; height: 50px; }")

        # adding widgets on top_wgt

        self.left_wgt2 = QWidget()
        self.left_lyt2 = QHBoxLayout(self.left_wgt2)
        self.left_wgt2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.left_wgt2.setObjectName("left")
        self.left_wgt2.setStyleSheet(" #left {background-color: yellow; border-radius: 10px; height: 50px;}")

        self.midle_wgt2 = QWidget()
        self.midle_lyt2 = QHBoxLayout(self.midle_wgt2)
        self.midle_wgt2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.midle_wgt2.setObjectName("midle")
        self.midle_wgt2.setStyleSheet(" #midle {background-color: green; border-radius: 10px; height: 50px;}")

        self.right_wgt2 = QWidget()
        self.right_lyt2 = QHBoxLayout(self.right_wgt2)
        self.right_wgt2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_wgt2.setObjectName("right")
        self.right_wgt2.setStyleSheet(" #right {background-color: blue; border-radius: 10px; height: 50px;}")

        # adding the 3 widget on top_lyt

        self.top_lyt.addWidget(self.left_wgt2)
        self.top_lyt.addWidget(self.midle_wgt2)
        self.top_lyt.addWidget(self.right_wgt2)



    # adding sub_top_wgt on lyt_add_librarian

        self.sub_top_wgt = QWidget()
        self.sub_top_lyt = QHBoxLayout(self.sub_top_wgt)
        self.sub_top_wgt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.sub_top_wgt.setObjectName("sub_top")
        self.sub_top_wgt.setStyleSheet(" #sub_top {background-color: blue; border-radius: 10px; height: 50px; }")

        # adding widgets on sub_top_wgt

        self.left_wgt2 = QWidget()
        self.left_lyt2 = QHBoxLayout(self.left_wgt2)
        self.left_wgt2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.left_wgt2.setObjectName("left1")
        self.left_wgt2.setStyleSheet(" #left1 {background-color: yellow; border-radius: 10px; height: 50px;}")

        self.midle_wgt2 = QWidget()
        self.midle_lyt2 = QHBoxLayout(self.midle_wgt2)
        self.midle_wgt2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.midle_wgt2.setObjectName("midle1")
        self.midle_wgt2.setStyleSheet(" #midle1 {background-color: green; border-radius: 10px; height: 50px;}")

        self.right_wgt2 = QWidget()
        self.right_lyt2 = QHBoxLayout(self.right_wgt2)
        self.right_wgt2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_wgt2.setObjectName("right1")
        self.right_wgt2.setStyleSheet(" #right1 {background-color: red; border-radius: 10px; height: 50px;}")

        # adding the 3 widget on top_lyt

        self.sub_top_lyt.addWidget(self.left_wgt2)
        self.sub_top_lyt.addWidget(self.midle_wgt2)
        self.sub_top_lyt.addWidget(self.right_wgt2)



    # adding body on lyt_add_librarian

        self.body_wgt = QWidget()
        self.body_lyt = QHBoxLayout(self.body_wgt)
        self.body_wgt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.body_wgt.setObjectName("body")
        self.body_wgt.setStyleSheet(" #body {background-color: orange; border-radius: 10px; height: 50px; }")

        # adding widgets on body_wgt

        self.left_wgt2 = QWidget()
        self.left_lyt2 = QHBoxLayout(self.left_wgt2)
        self.left_wgt2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.left_wgt2.setObjectName("left2")
        self.left_wgt2.setStyleSheet(" #left2 {background-color: yellow; border-radius: 10px; height: 50px;}")

        self.midle_wgt2 = QWidget()
        self.midle_lyt2 = QHBoxLayout(self.midle_wgt2)
        self.midle_wgt2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.midle_wgt2.setObjectName("midle2")
        self.midle_wgt2.setStyleSheet(" #midle2 {background-color: green; border-radius: 10px; height: 50px;}")

        self.right_wgt2 = QWidget()
        self.right_lyt2 = QHBoxLayout(self.right_wgt2)
        self.right_wgt2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_wgt2.setObjectName("right2")
        self.right_wgt2.setStyleSheet(" #right2 {background-color: red; border-radius: 10px; height: 50px;}")

        # adding the 3 widget on body_lyt

        self.body_lyt.addWidget(self.left_wgt2)
        self.body_lyt.addWidget(self.midle_wgt2)
        self.body_lyt.addWidget(self.right_wgt2)


    # adding bottom on lyt_add_librarian

        self.bottom_wgt = QWidget()
        self.bottom_lyt = QHBoxLayout(self.bottom_wgt)
        self.bottom_wgt.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.bottom_wgt.setObjectName("bottom")
        self.bottom_wgt.setStyleSheet(" #bottom {background-color: pink; border-radius: 10px; height: 50px; }")

    # adding the 4 main_widget on lyt_readers

        self.lyt_add_librarian.addWidget(self.top_wgt)
        self.lyt_add_librarian.addWidget(self.sub_top_wgt)
        self.lyt_add_librarian.addWidget(self.body_wgt)
        self.lyt_add_librarian.addWidget(self.bottom_wgt)


        return self.wgt_add_librarian


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