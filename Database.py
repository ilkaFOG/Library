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

    @property
    def author(self):
        return self.__author
        
    @title.setter
    def title(self, title:str):
        assert isinstance(title, str), 'Заголовок должен быть строкой!'
        self.__title = title

    @author.setter
    def author(self, author:str):
        assert isinstance(author, str), 'Автор должен быть строкой!'
        self.__author = author    

    def __str__(self):
        return f'Год издания: {self.year}, Название: {self.title}, Автор: {self.author};'


class Library:
    def __init__(self, books):
        self.books = books
    

book = Book(2001, 'Бу-га-га', 'Килька Фрог')
print(book)


input()