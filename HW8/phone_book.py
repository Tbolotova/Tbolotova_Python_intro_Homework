import sqlite3 as sq
from re import *


def add_contact():
    contact_first_name = input("Введите имя контакта: ")
    contact_last_name = input("Введите фамилию контакта: ")
    contact_city = input("Введите город контакта: ")
    phones = dict()
    # get any number of phone numbers
    number_of_phones = int(input("Введите количество номеров телефона, которое хотите добавить для контакта: "))
    count = 0
    while count < number_of_phones:
        phone_type = input("Введите тип номера телефона: ")
        contact_phone = input("Введите номер телефона: ")
        phone_valid = match(phone_pattern, contact_phone)
        while not phone_valid:
            print("Номер введен в некорректном формате. ")
            contact_phone = input("Введите номер в формате +71234567890 или 81234567890: ")
            phone_valid = match(phone_pattern, contact_phone)
        phones[phone_type] = contact_phone
        count += 1
    # add info to the db
    cur.execute(f"""INSERT INTO contacts(first_name, last_name, city)
        VALUES('{contact_first_name}', '{contact_last_name}', '{contact_city}')
    """)
    cur.execute(f"""SELECT id FROM contacts 
        WHERE first_name = '{contact_first_name}' AND last_name = '{contact_last_name}'""")
    current_id = cur.fetchone()
    for key in phones.keys():
        cur.execute(f"""INSERT INTO phones(type, phone, contact_id) 
            VALUES('{key}', '{phones[key]}', '{current_id[0]}')""")


def get_contact(first, last):
    cur.execute(f"""SELECT id, city FROM contacts 
        WHERE first_name = '{first}' AND last_name = '{last}'""")
    contacts_data = cur.fetchone()
    cur.execute(f"""SELECT type, phone, contact_id FROM phones WHERE contact_id = '{contacts_data[0]}'""")
    phones_data = cur.fetchall()
    print(f"Контакт: {first} {last}")
    print(f"Город: {contacts_data[1]}")
    print("Номера телефонов:")
    for row in phones_data:
        print(f"{row[0]}: {row[1]}")


def get_all():
    cur.execute("""SELECT contacts.first_name, contacts.last_name, contacts.city, phones.type, phones.phone 
        FROM contacts JOIN phones ON contacts.id = phones.contact_id""")
    contacts_table = cur.fetchall()
    header = ["Имя", "Фамилия", "Город", "Тип телефона", "Номер телефона"]
    for item in header:
        print(f"{f'{item}':<15}", end='')
    print('')
    for row in contacts_table:
        for column in row:
            print(f"{f'{column}':<15}", end='')
        print('')


def edit_contact(first, last):
    print("Текущие данные по данному контакту:")
    cur.execute(f"""SELECT id FROM contacts 
            WHERE first_name = '{first}' AND last_name = '{last}'""")
    current_id = cur.fetchone()[0]
    get_contact(first, last)
    field_to_edit = input("Введите название поля, которое хотите изменить - Имя, Фамилия, Город или Телефон: ").lower()
    if field_to_edit == "имя":
        new_name = input("Введите новое имя контакта: ")
        cur.execute(f"""UPDATE contacts SET first_name = '{new_name}' WHERE id = '{current_id}'""")
    elif field_to_edit == "фамилия":
        new_last_name = input("Введите новую фамилию: ")
        cur.execute(f"""UPDATE contacts SET last_name = '{new_last_name}' WHERE id = '{current_id}'""")
    elif field_to_edit == "город":
        new_city = input("Введите новый город: ")
        cur.execute(f"""UPDATE contacts SET city = '{new_city}' WHERE id = '{current_id}'""")
    elif field_to_edit == "телефон":
        cur.execute(f"""SELECT type FROM phones WHERE contact_id = '{current_id}'""")
        phone_types = cur.fetchall()
        phone_types_str = ", ".join(''.join(item) for item in phone_types)
        phone_type_to_edit = input(f"Введите тип телефона, который хотите изменить - {phone_types_str}: ").lower()
        new_phone = input(f"Введите новый номер телефона: ")
        cur.execute(f"""UPDATE phones SET phone = '{new_phone}' 
            WHERE contact_id = '{current_id}' AND type = '{phone_type_to_edit}'""")
    print("Контакт успешно обновлен.")


def delete_contact(first, last):
    cur.execute(f"""SELECT id FROM contacts 
                WHERE first_name = '{first}' AND last_name = '{last}'""")
    current_id = cur.fetchone()[0]
    cur.execute(f"""DELETE FROM phones WHERE contact_id = '{current_id}'""")
    cur.execute(f"""DELETE FROM contacts WHERE id = '{current_id}'""")
    print("Контакт успешно удален.")


def delete_number(first, last):
    cur.execute(f"""SELECT id FROM contacts 
                    WHERE first_name = '{first}' AND last_name = '{last}'""")
    current_id = cur.fetchone()[0]
    get_contact(first, last)
    cur.execute(f"""SELECT type FROM phones WHERE contact_id = '{current_id}'""")
    phone_types = cur.fetchall()
    phone_types_str = ", ".join(''.join(item) for item in phone_types)
    phone_type_to_delete = input(f"Введите тип телефона, который хотите изменить - {phone_types_str}: ").lower()
    cur.execute(f"""DELETE FROM phones WHERE contact_id = '{current_id}' AND type = '{phone_type_to_delete}'""")
    print("Номер успешно удален.")


con = sq.connect("phone_book.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city TEXT NOT NULL 
)""")

cur.execute("""CREATE TABLE IF NOT EXISTS phones(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    phone TEXT NOT NULL,
    contact_id INTEGER,
    FOREIGN KEY(contact_id) REFERENCES contacts(id)
)""")

con.commit()
phone_pattern = "(^\d|^\+\d)\d{10}$"

print("Работа телефонного справочника начата. Введите /help, чтобы получить список команд.")

while True:
    command = input("Введите команду: ")
    if command == "/add":
        add_contact()
    elif command == "/stop":
        con.commit()
        print("Работа телефонного справочника завершена. Данные сохранены.")
        break
    elif command == "/get":
        first_name = input("Введите имя контакта: ")
        last_name = input("Введите фамилию контакта: ")
        get_contact(first_name, last_name)
    elif command == "/save":
        con.commit()
        print("Данные успешно сохранены.")
    elif command == "/get_all":
        get_all()
    elif command == "/edit":
        first_name = input("Введите имя контакта: ")
        last_name = input("Введите фамилию контакта: ")
        edit_contact(first_name, last_name)
    elif command == "/delete_contact":
        first_name = input("Введите имя контакта: ")
        last_name = input("Введите фамилию контакта: ")
        delete_contact(first_name, last_name)
    elif command == "/delete_number":
        first_name = input("Введите имя контакта: ")
        last_name = input("Введите фамилию контакта: ")
        delete_number(first_name, last_name)
    elif command == "/help":
        help_text = ("/get - вывести информацию о контакте\n"
                     "/get_all - вывести список всех контактов в виде таблицы\n"
                     "/add - добавить контакт\n"
                     "/edit - отредактировать контакт"
                     "/save - сохранить данные"
                     "/delete_contact - удалить контакт\n"
                     "/delete_number - удалить один из телефонов контакта"
                     "/help - вывести список команд\n"
                     "/stop - остановить работу бота и сохранить данные\n")
        print("")
    else:
        print("Команда не опознана. Введите /help для получения списка команд.")
