import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My Application")
        self.minimumSize()
        # self.setMaximumSize(QSize(1000, 500))
        # self.setFixedSize(QSize(1000, 500))
        # self.setWindowState(Qt.WindowMaximized)
        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)

        # chamada de um método
        self.button.clicked.connect(self.button_clicked)
        self.button.toggled.connect(self.butto_toggle)

        self.setCentralWidget(self.button)

    def button_clicked(self) -> None:
        print("Button clicked!")
        # self.button.setStatus(False)

    def butto_toggle(self, checado) -> None:
        print(type(checado))
        print("Checked ?", checado)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()


