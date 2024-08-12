# Информация об учебных курсах. Напишите программу, которая создает словарь,
# содержащий номера курсов и номера аудиторий, где проводятся курсы. Словарь должен
# иметь приведенные в табл. 9.2 пары "ключ : значение".
# Таблица 9.2
# Номер курса (ключ)Номер аудитории (значение)
# CS101 3004
# CS102 4501
# CS103 6755
# CS104 1244
# CS105 1411
# Программа должна также создать словарь, содержащий номера курсов и имена препо­
# давателей, которые ведут каждый курс. Словарь должен иметь приведенные в табл. 9.3
# пары "кл ю ч : значение".
# Таблица 9.3
# Номер курса (ключ)Преподаватель (значение)
# CS101 Хайнс
# CS102 Альварадо
# CS103 Рич
# CS104 Берк
# CS105 Ли
# Программа также должна создать словарь, содержащий номера курсов и время проведе­
# ния каждого курса. Словарь должен иметь приведенные в табл. 9.4 пары "кл ю ч : значе­
# ние".
# Таблица 9.4
# Номер курса (ключ)Время (значение)
# CS101 8:00
# CS102 9:00
# CS103 10:00
# CS104 11:00
# CS105 13:00
# Программа должна позволить пользователю ввести номер курса, а затем показать номер
# аудитории, имя преподавателя и время проведения курса.
import datetime

dictinary_curse = {
    "CS101":
    {
        "Number_aditurium": 3004,
        "Names_professor": "Хайнс",
        "Times_start_classes": datetime.time(8, 0, 0)
    },

    "CS102":
    {
        "Number_aditurium": 4501,
        "Names_professor": "Альварадо",
        "Times_start_classes": datetime.time(9, 0, 0)
    },

    "CS103":
    {
        "Number_aditurium": 6755,
        "Names_professor": "Рич",
        "Times_start_classes": datetime.time(10, 0, 0)
    },

    "CS104":
    {
        "Number_aditurium": 1244,
        "Names_professor": "Берк",
        "Times_start_classes": datetime.time(11, 0, 0)
    },

    "CS105":
    {
        "Number_aditurium": 1411,
        "Names_professor": "Ли",
        "Times_start_classes": datetime.time(12, 0, 0)
    }
}

number_cours = input("Введите номер курса: ")
while number_cours not in dictinary_curse:
    print("Такого курса нет!!!")
    number_cours = input("Введите номер курса заново: ")
number_auditoruim = dictinary_curse[number_cours]["Number_aditurium"]
names_professor = dictinary_curse[number_cours]["Names_professor"]
time_start_classes = dictinary_curse[number_cours]["Times_start_classes"]
print(f"""Номер адитории: {number_auditoruim}
Имя преподователя: {names_professor}
Время проведения занятий: {time_start_classes}
""")