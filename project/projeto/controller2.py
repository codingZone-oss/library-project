from class_book_page import Book
from class_home_page import Home


class AppController2:
    def __init__(self):
        self.book = Book(self)
        self.home = Home(self)

    def __setstate__(self):
        