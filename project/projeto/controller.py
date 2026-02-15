from PySide6.QtWidgets import QApplication
import sys
from class_login_frame import LoginWindow
from class_main_frame import MainFrame
from class_home_page import Home

class AppController:
    def __init__(self):
        self.login = LoginWindow(self)
        self.main = MainFrame(self)
        self.home = Home(self)

    def show_login(self):
        self.main.hide()
        self.login.show()

    def show_main(self):
        self.login.hide()
        self.main.show()

app = QApplication(sys.argv)
window = AppController()
window.show_login()
app.exec()
