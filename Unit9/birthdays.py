# Хранение имен и дней рождения в словаре
# В этой рубрике мы рассмотрим программу, которая хранит в словаре имена ваших друзей
# и их дни рождения. Каждая запись в словаре использует имя друга в качестве ключа, а его
# день рождения в качестве значения. Эту программу можно использовать для поиска дней
# рождения друзей по вводимому имени.Гпава 9. Словари и множества

# Программа показывает меню, которое позволяет пользователю выбрать один из приведен­
# ных ниже вариантов действий:
# 1. Отыскать день рождения.
# 2. Добавить новый день рождения.
# 3. Изменить день рождения.
# 4. Удалить день рождения.
# 5. Выйти из программы.
# Программа первоначально начинает работу с пустого словаря, поэтому вам нужно выбрать
# из меню пункт 2, чтобы добавить новую запись. Когда вы добавите несколько записей, мож­
# но выбрать пункт 1, чтобы отыскать день рождения определенного человека, пункт 3, чтобы
# изменить существующий день рождения в словаре, пункт 4, чтобы удалить день рождения
# из словаря, или пункт 5, чтобы выйти из программы.
# В программе 9.2 приведен соответствующий код. Программа разделена на шесть функций:
# main (главная), get_menu_choice (получить пункт меню), look up (отыскать), add (добавить),
# change (изменить) и delete (удалить). Вместо того чтобы приводить всю программу цели­
# ком, давайте сначала исследуем глобальные константы и главную функцию main.
import datetime
import pickle

NAMEFILE = "data.txt"
PATH = f"/home/ranil/Рабочий стол/StudingPython/Unit9/{NAMEFILE}"
STOPWORD = "!!!ВСЁ!!!"
BIRTHDAYS = {}

def inter_fullname():
    first_name = input("Введите имя пользователя: ")
    last_name = input("Введите фамилию пользователя: ")
    return (first_name.strip() + " " + last_name.strip()).title()

def correct_digit(text: str):
    while True:
        try:
            day = int(input(text))
        except ValueError:
            print("Вы ввели не целое число!!!")
        else:
            return day

def enter_date():
    while True:
        try:
            month = correct_digit("Введите номер месяца: ")
            day = correct_digit("Введите число: ")
            date = datetime.date(datetime.date.today().year, month, day) #year - находится год ввода данных
        except:
            print("Вы ввели некоректное число или номер месяца\nПопробуйте еще раз")
        else:
            return date

def researchBirthday():
    fullname = inter_fullname()
    day = BIRTHDAYS.get(fullname, 0)
    while day == 0:
        print("Такого пользователя нет, попробуйте еще раз")
        fullname = inter_fullname()
        day = BIRTHDAYS.get(fullname)
    print(f"День рождение у {fullname}: {day} (год - это год, когда были введены данные)")
    return fullname

def addNewBirthday():

    while True:
        fullname = inter_fullname()
        if fullname not in BIRTHDAYS:
            break
        else:
            print("Такой пользователь существует\nВведите данные заново!!!")

    print("Ввод его дня рождения")
    date = enter_date()

    BIRTHDAYS[fullname] = date

def changedBirthday():
    fullname = researchBirthday()
    date =  enter_date() 
    print("Введите дату, которую хотите установить")
    BIRTHDAYS[fullname] = date

def removeBirthday():
    fullname = researchBirthday()
    del BIRTHDAYS[fullname]

def exit():
    return STOPWORD

def chooise():
    print(f"""1. Отыскать день рождения.
2. Добавить новый день рождения.
3. Изменить день рождения.
4. Удалить день рождения.
5. Выйти из программы.
6. Очистить данные в файле {NAMEFILE}""")
    try:
        value = int(input())
        while 1 > value or value > 6:
            value = int(input("Число додлжно быть 1-6\nПопробуйте еще раз выбрать действие: "))
    except ValueError:
        print("Вы введи не число")
    else:
        match value:
            case 1:
                print("Поиск пользователя")
                researchBirthday()
                return ""
            case 2:
                print("Добаление данных")
                addNewBirthday()
                return ""
            case 3:
                print("Изиенение данных")
                changedBirthday()
                return ""
            case 4:
                print("Удаление данных")
                removeBirthday()
                return ""
            case 5:
                print("Программа завершилась")
                return exit()
            case 6:
                BIRTHDAYS.clear()
                return ""

def main():
    key = ""
    while key != STOPWORD:
        key = chooise()
if __name__ == "__main__":
    try:
        with open(PATH, 'rb') as infile:
            BIRTHDAYS = pickle.load(infile)
    except FileNotFoundError: # если файл не нашелся создать его
        open(PATH, "w").close()
    main()
    with open(PATH, 'wb') as outfile:
        pickle.dump(BIRTHDAYS, outfile)
    print(BIRTHDAYS)
