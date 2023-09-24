from random import *
import json


def save():
    with open("books.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(books, ensure_ascii=False))
    print("Библиотека обновлена!")


def load():
    with open("books.json", "r", encoding="utf-8") as fh:
        return json.load(fh)


def print_books(book_list):
    for item in book_list:
        print(f"{item[0]} - {item[1]}")


try:
    books = load()
except FileNotFoundError:
    books = []


while True:
    command = input("Введите команду: ")
    if command == "/start":
        print("Бот-библиотека запущен")
    elif command == "/stop":
        save()
        print("Бот-библиотека остановлен. Увидимся позже!")
        break
    elif command == "/add":
        author = input("Введите автора книги, которую хотите добавить: ")
        book = input("Введите название книги, которую хотите добавить: ")
        if not [author, book] in books:
            books.append([author, book])
            print("Книга добавлена в библиотеку")
        else:
            print("Книга уже есть в библиотеке!")
    elif command == "/remove":
        author = input("Введите автора книги, которую хотите удалить: ")
        book = input("Введите название книги, которую хотите удалить: ")
        if [author, book] in books:
            books.remove([author, book])
            print("Книга удалена!")
        else:
            print("Такой книги нет в библиотеке")
    elif command == "/all":
        if len(books) == 0:
            print("Библиотека пуста! Добавьте книги командой /add")
        else:
            print(f"Вот список всех книг с авторами: ")
            print_books(books)
    elif command == "/author":
        author = input("Введите автора: ")
        author_books = [i for i in books if i[0] == author]
        if len(author_books) != 0:
            print_books(author_books)
        else:
            print("Книг этого автора нет в библиотеке! Добавьте книги командой /add")
    elif command == "/random":
        book = choice(books)
        print(f"{book[0]} - {book[1]}")
    elif command == "/help":
        help_text = ("/start - начать работу бота\n"
                     "/all - вывести список всех книг в библиотеке\n"
                     "/author - вывести список книг по автору\n"
                     "/random - вывести случайную книгу\n"
                     "/add - добавить книгу в библиотеку\n"
                     "/remove - удалить книгу из библиотеки\n"
                     "/help - вывести список команд\n"
                     "/stop - остановить работу бота\n")
        print("Список команд: ")
        print(help_text)
    else:
        print("Команда не найдена. Пожалуйста, введите /help, чтобы получить список команд")
