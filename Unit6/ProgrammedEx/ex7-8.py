# Программа записи файла со случайными числами. Напишите программу, которая
# пишет в файл ряд случайных чисел. Каждое случайное число должно быть в диапазоне
# от 1 до 500. Приложение должно предоставлять пользователю возможность назначать
# количество случайных чисел, которые будут содержаться в файле.

import random

NAMEFILE = "randomNum"
PATH = f"/home/ranil/Рабочий стол/{NAMEFILE}"

def corectEnterIntNum():
    num = None
    while True:
        try:
            num = int(input("Введите колиство рандомных чисел: "))
        except ValueError:
           print("Вы ввели не целое число!!!")
        else:
            break
    return num

def readDataWithFileLine(path):
    try:
        with open(path, 'r') as infile:
            for line in infile:
                print(line.rstrip())
    except IOError as err:
        print(err)

def summNumbers(path):
    
    summ = 0
    try:
        with open(path, 'r') as infile:
            for line in infile:
                summ += int(line.rstrip())
    except IOError as err:
        print(f"{err.filename} файла не существует")
    else:
        return summ
    
def count_number(path):
    counter = 0
    try:    
        outfile = open(path, 'r')
    except IOError:
        print("Ошибка!!!\nТакого файла не существует!")
    else:
        for line in outfile:
            counter += 1
    finally:
        outfile.close()
        return counter

def main():
    count = corectEnterIntNum()
    # Creat file with random numbers
    with open(PATH, 'a') as outfile:
        for i in range(count):
            outfile.write(f"{random.randint(1,500)}\n")
    readDataWithFileLine(PATH)
    print(f"Сумма цифр в файле: {summNumbers(PATH)}") if summNumbers(PATH) != None else print("Там нет данных")
    print(f"Количество цифр в файле: {count_number(PATH)}") if count_number(PATH) != None else print("Там нет данных")
if __name__ == "__main__":
    main()

# Программа чтения файлов со случайными числами. Выполнив предыдущее задание
# (программу записи файла со случайными числами), напишите еще одну программу, ко­
# торая читает случайные числа из файла, выводит их на экран и затем показывает приве­
# денные ниже данные:
# •сумму чисел;
# •количество случайных чисел, прочитанных из файла.