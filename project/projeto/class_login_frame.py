from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QToolButton
from classs_warning_frame import Alert, Successefull
from class_main_frame import MainFrame
from PySide6.QtCore import Qt, QTimer
from class_conextion import cursor
from PySide6.QtGui import QIcon
from time import sleep
import webbrowser
import sys

class HoverLabel(QLabel):

    def __init__(self, hover_icon, nomal_icon, num, link):
        super().__init__()
        self.hover_pixmap = hover_icon
        self.normal_pixmap = nomal_icon
        self.num_size = num
        self.link = link

        self.setPixmap(QIcon(self.normal_pixmap).pixmap(self.num_size, self.num_size))


    def leaveEvent(self, event):
        self.setPixmap(QIcon(self.normal_pixmap).pixmap(self.num_size, self.num_size))
        super().leaveEvent(event)

    def enterEvent(self, event):
        self.setPixmap(QIcon(self.hover_pixmap).pixmap(self.num_size, self.num_size))
        super().enterEvent(event)

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.LeftButton:
            webbrowser.open(self.link)
        super().mousePressEvent(event)
    

class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Login Frame")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(900, 500)

        # ___________

        # adding central widget to the main window | adicionado widget central à janela principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)    

        # setting the central widget costumizations | definindo as personalizações do widget central
        self.central_widget.setObjectName("central_widget") # id
        self.central_widget.setStyleSheet(""" QWidget#central_widget{background-color: white; border-radius: 18px;}""")
        
        # ___________

        # adding main layout to the central widget (horizontal) | adicionando layout principal ao widget central
        self.main_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)        

        # adding the first layout to the main layout
        self.right_container = QWidget()
        self.right_container.setObjectName("right_container")
        self.right_container.setStyleSheet("""QWidget#right_container{background-color: blue; border-radius: 18px;}""")
        self.layout_right = QVBoxLayout(self.right_container)
        self.layout_right.setAlignment(Qt.AlignCenter)

        # ___________

        # adding title label to the layout on the left side | adicionando rótulo de título ao layout do lado esquerdo
        
        self.label_title2 = QLabel("Libary System")
        self.layout_right.addWidget(self.label_title2, alignment=Qt.AlignCenter)
        self.label_title2.setContentsMargins(80, 0, 0, 0)  # adding bottom margin | adicionando margem inferior
        self.label_title2.setFixedSize(400, 85) # setting a fixed size | definindo um tamanho fixo
        # setting the label_title costumizations | definindo as personalizações do label_title
        self.label_title2.setStyleSheet("""QLabel{ color: white; font-weight: bold; font-size: 38px; padding-top: 30px;}""")

        self.layout_right.addStretch()

        # ____________

        # adding image book label to the left side layout | adicionando imagem de um livors ao layout do lado esquerdo

        self.image_book = QLabel()
        self.image_book.setPixmap(QIcon("imagens/book.png").pixmap(200, 200))
        self.layout_right.addWidget(self.image_book, alignment=Qt.AlignCenter)

        # ____________

        self.layout_right.addStretch()
        self.layout_right.addStretch()
        self.layout_right.addStretch()
        self.layout_right.addStretch()

        # adding the second layout to the central widget on the left side | adicionando o primeiro layout ao widget central no lado esquerdo
        self.left_container = QWidget()
        self.left_container.setStyleSheet("background-color: white;")
        self.layout_left = QVBoxLayout(self.left_container)
        self.layout_left.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.layout_left.setSpacing(20)  # setting spacing between widgets | definindo espaçamento entre widgets

        # ___________
        # adding close button to the layout on the rigth side | adicionando botão de fechar ao layout do lado direito

        self.close_button = QPushButton("X")
        self.close_button.setFixedSize(35, 20)
        self.close_button.setCursor(Qt.PointingHandCursor)
        self.close_button.setStyleSheet("""QPushButton {background-color: lightgray; color: white; font-weight: bold; border: none; border-radius: 10px;} QPushButton:hover { background-color: red; color: white;}""")
        self.close_button.clicked.connect(self.close)
        self.layout_left.addWidget(self.close_button, alignment=Qt.AlignRight)

        # ___________

        self.layout_left.addStretch()

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

        self.layout_left.addStretch()
        self.layout_left.addStretch()

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
        self.button_login.setFixedSize(100, 30)
        self.button_login.setCursor(Qt.PointingHandCursor) # setting the cursor aparences to hand pointing 
        self.button_login.setToolTip("Click to login")  # setting a tooltip | definindo uma dica de ferramenta
        self.button_login.setShortcut("Return")  # setting a shortcut key | definindo uma tecla de atalho
        self.button_login.setContentsMargins(0, 0, 0, 40)  # adding top margin | adicionando margem superior
        self.layout_left.addWidget(self.button_login, alignment=Qt.AlignCenter)

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
        self.layout_left.addStretch()

        # adding icon label of social networking
        
        # icon Facebook
        # self.icon_facebook = QLabel()
        self.icon_facebook = HoverLabel("icons/facebook_cor.png", "icons/facebook_sem_cor.png", 30, "https://www.facebook.com/")
        self.icon_facebook.setCursor(Qt.PointingHandCursor)
        self.icon_facebook.setToolTip("Click to Access Facebook")

        # icon Twitter
        self.icon_twitter = QLabel()
        self.icon_twitter = HoverLabel("icons/twitter_cor.png", "icons/twitter_sem_cor.png", 30, "https://www.x.com/")
        self.icon_twitter.setCursor(Qt.PointingHandCursor)
        self.icon_twitter.setToolTip("Click to Access Twitter")


        # icon Instagram
        self.icon_instagram = QLabel()
        self.icon_instagram = HoverLabel("icons/instagram_cor.png", "icons/instagram_sem_cor.png", 30, "https://www.instagram.com/")
        self.icon_instagram.setCursor(Qt.PointingHandCursor)
        self.icon_instagram.setToolTip("Click to Access Instagram")

        # icon YouTube
        self.icon_youtube = QLabel()
        self.icon_youtube = HoverLabel("icons/youtube_cor.png", "icons/youtube_sem_cor.png", 40, "https://www.youtube.com/")
        self.icon_youtube.setCursor(Qt.PointingHandCursor)
        self.icon_youtube.setToolTip("Click to Access You Tube")
        # self.icon_youtube.

        # icon Linkedin
        self.icon_linkedin = QLabel()
        self.icon_linkedin = HoverLabel("icons/linkedin_cor.png", "icons/linkedin_sem_cor.png", 35, "https://www.linkedin.com/")
        self.icon_linkedin.setCursor(Qt.PointingHandCursor)
        self.icon_linkedin.setToolTip("Click to Access LinkedIn")


        # adding a horizontal layout to put network links | adicionando um layout horizontal para colocar links de rede
        self.links_layout = QHBoxLayout()
        self.layout_left.addLayout(self.links_layout)
        self.links_layout.setContentsMargins(70, 0, 0, 0)  # adding left margin | adicionando margem esquerda
        self.links_layout.setSpacing(5)  # setting spacing between links | definindo espaçamento entre links
        self.links_layout.addWidget(self.icon_facebook)
        self.links_layout.addWidget(self.icon_twitter)
        self.links_layout.addWidget(self.icon_instagram)
        self.links_layout.addWidget(self.icon_youtube)
        self.links_layout.addWidget(self.icon_linkedin)


        # ___________

        # adding both layouts to the main layout | adicionando ambos os layouts ao layout principal
        self.main_layout.addWidget(self.right_container)
        self.main_layout.addWidget(self.left_container)

        # setting equal proportions for both sides | definindo proporções iguais para ambos os lados
        self.main_layout.setStretch(0, 3)  # Right side
        self.main_layout.setStretch(1, 2)  # Left side

        # ___________

    def toggle_button(self) -> None: # this one is used to make changes of the eye icon on input_password label
        if self.input_password.echoMode() == QLineEdit.Password:
            self.input_password.setEchoMode(QLineEdit.Normal)
            self.button_toggle_password.setIcon(QIcon("icons/eye_open20px.png"))
        else:
            self.input_password.setEchoMode(QLineEdit.Password)
            self.button_toggle_password.setIcon(QIcon("icons/fechar-o-olho.png"))

    def handle_DB(self) -> list: # this one is used to make SLQ querys on BD 
        vet = list()
        try: cursor.execute("select user_name, pass_word from user")
        except Exception as e: print(f'Something went worng {e}')
        for line in cursor: vet.append(line)
        return vet

    def open(self) -> None: # this methods close the login frame and also open the main window frame
        self.close()
        self.main = MainFrame()
        self.main.show()


    def handle_login(self) -> None: # this one take care about login handle 
        username = self.input_username.text()
        password = self.input_password.text()
        users = self.handle_DB()
        for user in users:
            if username == user[0] and password == user[1]:
                sleep(1)
                self.success = Successefull("Admin: Fulano de Tal")
                self.success.show()
                self.timer = QTimer()
                self.timer.singleShot(4000, self.open)
                return
        self.alert = Alert(); sleep(0.6); self.alert.show()

app = QApplication(sys.argv)
window = LoginWindow()
window.show()
app.exec()
