from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QToolButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
import webbrowser

import sys

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Frame")
        self.setFixedSize(900, 500)

        # ___________

        # adding central widget to the main window | adicionado widget central à janela principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # setting the central widget costumizations | definindo as personalizações do widget central
        self.central_widget.setStyleSheet("background-color: white;")

        # ___________

        # adding main layout to the central widget (horizontal) | adicionando layout principal ao widget central
        self.main_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        # self.layout.setAlignment(Qt.AlignCenter)
        

        # adding the first layout to the main layout
        self.rigth_container = QWidget()
        self.rigth_container.setStyleSheet("background-color: blue;")
        self.layout_rigth = QVBoxLayout(self.rigth_container)
        self.layout_rigth.setAlignment(Qt.AlignCenter)

        # adding the second layout to the central widget on the left side | adicionando o primeiro layout ao widget central no lado esquerdo
        self.left_container = QWidget()
        self.left_container.setStyleSheet("background-color: white;")
        self.layout_left = QVBoxLayout(self.left_container)
        self.layout_left.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.layout_left.setSpacing(20)  # setting spacing between widgets | definindo espaçamento entre widgets

        # ___________

        # adding title label to the layout on the rigth side | adicionando rótulo de título ao layout do lado direito
        self.label_title = QLabel("Login to Your Account")
        self.layout_left.addWidget(self.label_title, alignment=Qt.AlignCenter)
        self.label_title.setContentsMargins(80, 0, 0, 0)  # adding bottom margin | adicionando margem inferior
        self.label_title.setFixedSize(400, 40) # setting a fixed size | definindo um tamanho fixo
        # setting the label_title costumizations | definindo as personalizações do label_title
        self.label_title.setStyleSheet("""
                QLabel{
                    color: black;
                    font-weight: bold;
                    font-size: 25px;
                    }
                """)

        # ___________

        # adding user name lable widgets to the layout on the rigth side | adicionando o rótulo de nome de usuário aos widgets do layout no lado direito
        self.label_username = QLabel("User Name:")
        self.layout_left.addWidget(self.label_username)
        self.label_username.setContentsMargins(70, 0, 0, 0)  # adding right margin | adicionando margem lateral direita
        self.label_username.setFixedSize(400, 20)


        # setting the label_usernames costumizations | definindo as personalizações do label_username
        self.label_username.setStyleSheet("""
                QLabel{
                    color: black;
                    font-weight: normal;
                    font-size: 16px;
                    }        
                """)
        
        # ___________

        # adding user name input widgets to the layout on rigth side too | adicionando widgets de entrada de nome de usuário ao layout do lado direito também
        self.input_username = QLineEdit()
        self.input_username.setFixedSize(260, 25)
        self.input_username.setPlaceholderText("Enter your username")
        # self.layout_left.addWidget(self.input_username, alignment=Qt.AlignCenter)

        
        # setting the input_usernames field costumizations | definindo as personalizações do campo input_username
        self.input_username.setStyleSheet("color: black;")

        
        # ___________

        # adding user icon label to the rigth side layout | adicionando rótulo de ícone de usuário ao layout do lado direito
        self.user_icon = QLabel()
        self.user_icon.setPixmap(QIcon("icons/avatar-do-usuario.png").pixmap(30, 30))
        self.user_icon.setStyleSheet("margin-left: 5px;")  # adding left margin | adicionando margem esquerda

        # building a horizontal layout to hold both user icon and username input field | construindo um layout horizontal para conter tanto o ícone do usuário quanto o campo de entrada do nome de usuário

        
        self.username_layout = QHBoxLayout()
        self.username_layout.addWidget(self.user_icon, alignment=Qt.AlignCenter)
        self.username_layout.addWidget(self.input_username, alignment=Qt.AlignCenter)
        self.layout_left.addLayout(self.username_layout)
        self.username_layout.setContentsMargins(0, 0, 50, 0)  # removing margins | removendo margens

        # ___________

        # adding password lable widgets to the layout on the rigth side | adicionando o rótulo de senha aos widgets do layout no lado direito
        self.label_password = QLabel("Pass Word:")
        self.layout_left.addWidget(self.label_password)
        self.label_password.setContentsMargins(70, 0, 0, 0)  # adding top margin | adicionando margem superior
        self.label_username.setFixedSize(400, 20)


        # setting label_password costumizations | definindo as personalizações do label_password
        self.label_password.setStyleSheet("""
                QLabel{
                    color: black;
                    font-weight: normal;
                    font-size: 16px;
                    }        
                """)

        # ___________

        # adding password input widgets to the layout on rigth side too | adicionando widgets de entrada de senha ao layout do lado direito também
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setPlaceholderText("Enter your password")
        self.input_password.setFixedSize(260, 25) 
        # self.layout_left.addWidget(self.input_password, alignment=Qt.AlignCenter)       


        # setting the input_password field costumizations | definindo as personalizações do campo input_password
        self.input_password.setStyleSheet("""
            QLineEdit {
                color: black;
                }
            """)
        
        # ___________

        # adding passwor icon label to the rigth side layout | adicionando rótulo de ícone de password ao layout do lado direito
        self.password_icon = QLabel()
        self.password_icon.setPixmap(QIcon("icons/cadeado.png").pixmap(35, 35))
        self.password_icon.setStyleSheet("margin-left: 5px;")  # adding left margin | adicionando margem esquerda

        # building a horizontal layout to hold both password icon and password input field | construindo um layout horizontal para conter tanto o ícone da password quanto o campo de entrada da password

        
        self.password_layout = QHBoxLayout()
        self.password_layout.addWidget(self.password_icon, alignment=Qt.AlignCenter)
        self.password_layout.addWidget(self.input_password, alignment=Qt.AlignCenter)
        self.layout_left.addLayout(self.password_layout)
        self.password_layout.setContentsMargins(0, 0, 50, 0)  # removing margins | removendo margens

        # ___________

        # building the password view toggle button | construindo o botão de alternância de exibição de senha
        self.button_toggle_password = QToolButton(self.input_password)
        self.button_toggle_password.setIcon(QIcon("icons/fechar-o-olho.png"))
        self.button_toggle_password.setCursor(Qt.PointingHandCursor)
        self.button_toggle_password.setStyleSheet("border: none;")
        # self.button_toggle_password.setFixedSize(20, 20) # this isent necessary

        # setting the button_toggle_password Direction

        self.input_password.setLayoutDirection(Qt.LeftToRight)
        self.input_password.setTextMargins(0, 0, 20, 0)    
        self.button_toggle_password.move(self.input_password.width() - 25, (self.input_password.height() - 20) // 2)

        # conecting the button_toggle_password to change the visibility
        self.button_toggle_password.clicked.connect(self.toggle_button)

        # ___________

        # adding login button to the layout on the rigth side | adicionando botão de login ao layout do lado direito
        self.button_login = QPushButton("Login")
        self.button_login.clicked.connect(self.handle_login)
        self.layout_left.addWidget(self.button_login, alignment=Qt.AlignCenter)
        self.button_login.setFixedSize(100, 30)
        self.button_login.setCursor(Qt.PointingHandCursor) # setting the cursor aparences to hand pointing 
        self.button_login.setToolTip("Click to login")  # setting a tooltip | definindo uma dica de ferramenta
        self.button_login.setShortcut("Return")  # setting a shortcut key | definindo uma tecla de atalho
        self.button_login.setContentsMargins(0, 0, 0, 40)  # adding top margin | adicionando margem superior

        # setting the login button costumizations | definindo as personalizações do botão de login

        self.button_login.setStyleSheet("""
                QPushButton {
                    background-color: Blue;
                    color: white;
                    font-weight: bold;
                    font-size: 14px;
                    border: none;
                    border-radius: 5px;
                    }
                QPushButton:hover {
                    background-color: darkblue;
                    text-decoration: underline;
                    }
            """)    

        # ___________

        # adding a spacer at the bottom to push the widgets upwards | adicionando um espaçador na parte inferior para empurrar os widgets para cima
        # self.layout_left.addStretch(1.5)

        # adding icon label of social networking
        
        # icon Facebook
        self.icon_facebook = QLabel()
        self.icon_facebook.mousePressEvent = lambda event: self.link_networking("https://www.facebook.com/")
        self.icon_facebook.setPixmap(QIcon("icons/facebook_sem_cor.png").pixmap(30, 30))
        self.icon_facebook.setCursor(Qt.PointingHandCursor)
        self.icon_facebook.setToolTip("Click to Access Facebook")

        # icon Twitter
        self.icon_twitter = QLabel()
        self.icon_twitter.mousePressEvent = lambda event: self.link_networking("https://www.x.com/")
        self.icon_twitter.setPixmap(QIcon("icons/twitter_sem_cor.png").pixmap(30, 30))
        self.icon_twitter.setCursor(Qt.PointingHandCursor)
        self.icon_twitter.setToolTip("Click to Access Twitter")


        # icon Instagram
        self.icon_instagram = QLabel()
        self.icon_instagram.mousePressEvent = lambda event: self.link_networking("https://www.instagram.com/")
        self.icon_instagram.setPixmap(QIcon("icons/instagram_sem_cor.png").pixmap(30, 30))
        self.icon_instagram.setCursor(Qt.PointingHandCursor)
        self.icon_instagram.setToolTip("Click to Access Instagram")

        # icon YouTube
        self.icon_youtube = QLabel()
        self.icon_youtube.mousePressEvent = lambda event: self.link_networking("https://www.youtube.com/")
        self.icon_youtube.setPixmap(QIcon("icons/youtube_sem_cor.png").pixmap(30, 30))
        self.icon_youtube.setCursor(Qt.PointingHandCursor)
        self.icon_youtube.setToolTip("Click to Access You Tube")
        # self.icon_youtube.



        # adding a horizontal layout to put network links | adicionando um layout horizontal para colocar links de rede
        self.links_layout = QHBoxLayout()
        self.layout_left.addLayout(self.links_layout)
        self.links_layout.setContentsMargins(70, 0, 0, 0)  # adding left margin | adicionando margem esquerda
        self.links_layout.setSpacing(5)  # setting spacing between links | definindo espaçamento entre links
        self.links_layout.addWidget(self.icon_facebook)
        self.links_layout.addWidget(self.icon_twitter)
        self.links_layout.addWidget(self.icon_instagram)
        self.links_layout.addWidget(self.icon_youtube)


        # ___________

        # adding both layouts to the main layout | adicionando ambos os layouts ao layout principal
        self.main_layout.addWidget(self.rigth_container)
        self.main_layout.addWidget(self.left_container)

        # setting equal proportions for both sides | definindo proporções iguais para ambos os lados
        self.main_layout.setStretch(0, 3)  # Right side
        self.main_layout.setStretch(1, 2)  # Left side

        # ___________

    def link_networking(self, text) -> None:
        webbrowser.open(text)

    def toggle_button(self) -> None:
        if self.input_password.echoMode() == QLineEdit.Password:
            self.input_password.setEchoMode(QLineEdit.Normal)
            self.button_toggle_password.setIcon(QIcon("icons/eye_open20px.png"))
        else:
            self.input_password.setEchoMode(QLineEdit.Password)
            self.button_toggle_password.setIcon(QIcon("icons/fechar-o-olho.png"))

    def handle_login(self) -> None:
        username = self.input_username.text()
        password = self.input_password.text()

        if username == "admin" and password == "password":
            QMessageBox.information(self, "Login Successful", "Welcome, admin!")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

app = QApplication(sys.argv)
window = LoginWindow()
window.show()
app.exec()
