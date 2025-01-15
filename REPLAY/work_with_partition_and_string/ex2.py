# Задание 2:
# Создайте программу, которая принимает от пользователя строку и использует регулярные выражения для:

# Проверки, содержит ли строка только латинские буквы и цифры
# Замены всех email-адресов в строке на "[EMAIL]"
# Поиска и вывода всех телефонных номеров в формате +X(XXX)XXX-XX-XX

import re
alphaAndDigit = re.compile('\w+', flags= re.IGNORECASE)

Replayser = re.compile("\w+@mail.ru")

PhoneNumbers = re.compile("[+]{1}\d{1}[(]{1}\d{3}[)]{1}\d{3}-\d{2}-\d{2}")

def chekingDigitAndAlpha(text: str):
    return [el for el in text.split() if not re.fullmatch(alphaAndDigit, el)]

def replay(text: str):
    newList = []
    for el in text.split():
        if re.search(Replayser, el):
            newList.append("[EMAIL]")
        else:
            newList.append(el)
    return " ".join(newList)

def printTelephoneNumbers(text: str):
    print("Номера телефонов: ")
    for el in text.split():
        if re.fullmatch(PhoneNumbers, el):
            print(el) 

def main():
    text = input("Введите текст: ")
    print("Строка содержит только латинские буквы и цифры") if not chekingDigitAndAlpha(text) else print("Строка не содержит только латинские буквы и цифры") 
    print("Новая строка:", replay(text))
    printTelephoneNumbers(text)

if __name__ == "__main__":
    main()