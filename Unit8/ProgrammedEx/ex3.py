# Принтер дат. Напишите программу, которая считывает от пользователя строковое зна­
# чение, содержащее дату в формате дд/мм/гггг. Она должна напечатать дату в формате
# 12 марта 2018 г
import datetime
import locale
locale.setlocale(locale.LC_ALL, "")

def enterAndPrintDate():
    inputdate = datetime.datetime.strptime(input("Введите дату(дд/мм/гггг):"), "%d/%m/%Y").date()
    printdate = inputdate.strftime("%d %B %Y г")
    return printdate

def main():
    print(enterAndPrintDate())

if __name__ == "__main__":
    main()