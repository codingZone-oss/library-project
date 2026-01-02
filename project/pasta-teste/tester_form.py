from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
import sys


window_titles = [

    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on the earth',
    'What on the earth',
    'This is Surprise',
    'This is Surprise',
    'Something Went Wrong'

]

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.n_times_cliked = 0
        self.setWindowTitle('My App')

        self.button = QPushButton('Press Me!')
        self.button.clicked.connect(self.button_clicked)
        self.setCentralWidget(self.button)

    def button_clicked(self):
        self.n_times_cliked += 1
        index = (self.n_times_cliked - 1) // 2
        if index < len(window_titles):
            new_title = window_titles[index]
            self.setWindowTitle(new_title)
            self.button.setEnabled(index % 2 == 0)

app = QApplication(sys.argv)
window = MainWindow()

window.show()
app.exec()