import os

class Console_utilite:
    def ClearConsole():
        clear = lambda: os.system('cls' if os.name=='nt' else 'clear')  # Назначили ссылку на метод в поле clear
        clear() # Вызываем при необходимости очистки консоли


class Book:
    def __init__(self, year:int, title:str, author:str):
        self.year = year
        self.title = title
        self.author = author
    
    @property
    def title(self):   
        return self.__title

    @title.setter
    def title(self, title:str):
        assert type(title) is type(str()), 'Заголовок должен быть строкой!'
        self.title = title

    def __str__(self):
        return 'Год издания: {}, Название: {}, Автор: {}'.format(self.year, self.title, self.author)


class Library:
    def __init__(self, books):
        self.books = books
    

book = Book(2001, 'Бу-га-га', 'Бетховен')
print(book)


input()