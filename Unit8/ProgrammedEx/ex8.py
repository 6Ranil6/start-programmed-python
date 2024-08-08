# Корректор предложений. Напишите программу с функцией, принимающей в качестве
# аргумента строковое значение и возвращающей его копию, в котором первый символ ка­
# ждого предложения написан в верхнем регистре. Например, если аргументом является
# "привет! меня зовут джо. а как твое имя?", то эта функция должна вернуть строковое зна­
# чение 'Привет! Меня зовут Джо. А как твое имя?'. Программа должна предоставить
# пользователю возможность ввести строковое значение и затем передать его в функцию.
# Модифицированное строковое значение должно быть выведено на экран.
import re

def correcting(text):
    delimiters = re.findall(r"[.!?]+", text)
    centencses = re.split(r"[.!?]+", text)
    result = ""
    for i in range(len(delimiters)):
        result += centencses[i].lstrip().capitalize() + delimiters[i] + ' '
    return result

def main():
    text = input("Введите текст: ")
    centecses = correcting(text)
    print(centecses)

if __name__ == "__main__":
    main()