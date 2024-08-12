# Имена и адреса электронной почты. Напишите программу, которая сохраняет имена и
# адреса электронной почты в словаре в виде пар "ключ : значение".

# Программа должна
# вывести меню, которое позволяет пользователю 

#  отыскать адрес электронной почты че­ловека,
#  добавить новое имя и адрес электронной почты,
#  изменить существующий адрес электронной почты 
#  удалить существующие имя и адрес электронной почты.

#  Програм­ма должна законсервировать словарь и сохранить его в файле при выходе пользователя
# из программы. При каждом запуске программы она должна извлекать словарь из файла
# и расконсервировать его.
import os
import pickle

NAMEFILE = "data.txt"
PATH = f"{os.path.dirname(__file__)}/{NAMEFILE}"

# Пусть при запуски программы данные из файла вставляются в словарь сразу
try:
    with open(PATH, 'rb') as infile:
        DICTINARY = dict(pickle.load(infile))
except FileNotFoundError:
    DICTINARY = dict()

def corectEnter():
    while True:
        try:
            choise = int(input())
        except ValueError:
            print("Вы ввели не число, попробуйте еще раз: ")
        else:
            if 1 <= choise <= 4:
                return choise
            print("Можно выбрать только 1-4!!!")

def enterAdress():
    adress = input("Введите адрес электронной почты ***@mail.ru: ").strip()
    while not adress.endswith("@mail.ru"):
        adress = input("Введите почту от @mail.ru: ").strip()
    return adress

def addNewData():
    name = input("Введите имя: ").strip()
    while name in DICTINARY:
        name = input("Такой пользователь уже существует!!!\nВведите имя повтроно: ").strip()
    adress = enterAdress()
    DICTINARY[name] = adress
    
def researchName(text: str):
    name = input(text)
    while True:
        if name not in DICTINARY:
            name = input("Такого пользователя нет, введите имя повторно: ").strip()
        else:
            return name

def changeAdress():
    name = researchName("Введите имя пользователя, у которого необходимо изменить адрес электронной почты: ").strip()
    DICTINARY[name] = enterAdress()
    print("Адрес изменился успешно!!!")

def deleteData():
    name = researchName("Введите имя пользователя, у которого хоите удалить все данные: ").strip()
    del DICTINARY[name]
    print("Удаление прошло успешно!!!")

def menu():
    print(f"""Меню:

1 - отыскать адрес электронной почты
2 - добавить новое имя и адрес электронной почты
3 - изменить существующий адрес электронной почты
4 - удалить существующие имя и адрес электронной почты
""")
    choise = corectEnter()
    match choise:
        case 1:
            print("Ваш электронный адрес:",DICTINARY[researchName("Введите имя пользователя, у которого хотели бы найти адрес: ")])
        case 2:
            addNewData()
        case 3:
            changeAdress()
        case 4:
            deleteData()

def main():

    while True:
        menu()
        if input("Введите STOP?, если хотите завершить программу: ").upper() == "STOP":
            break
    
    # записываем данные, которые в DICTINARY заново, приэтом удаляем предыдущие данные в файле
    with open(PATH, 'wb') as oufile:
        pickle.dump(DICTINARY, oufile)
    print("Программа завершилась")

if __name__ == "__main__":
    main()