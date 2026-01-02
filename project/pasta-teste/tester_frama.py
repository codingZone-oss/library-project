from time import sleep
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtCore import Qt, QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('teste login')
        self.setFixedSize(QSize(450, 500))

        self.button = QPushButton("Press me!")
        self.button.clicked.connect(self.button_clicked)
        self.setCentralWidget(self.button)
        
    def button_clicked(self) -> None:
        print("Button clicked!")
        sleep(2)  # Simulate a long-running task
        print("Disabling button...")
        self.button.setEnabled(False)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

