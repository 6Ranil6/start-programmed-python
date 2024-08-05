# К руговая д и аграм м а расходов. Создайте текстовый файл, который содержит ваши
# расходы за прошлый месяц по приведенным ниже статьям:
# •арендная плата;
# •бензин;
# •продукты питания;
# •одежда;
# •платежи по автомашине;
# •прочие.
# Напишите программу Python, которая считывает данные из файла и использует пакет
# matplotlib для построения круговой диаграммы, показывающей, как вы тратите свои
# деньги.

import random
import matplotlib.pyplot as plt

NAMEFILE = "data.txt"
PATH = f"/home/ranil/Рабочий стол/StudingPython/Unit7/ProgramedEx/ex14/{NAMEFILE}"
# самому лень заполнять файл поэтому создам программный код, который это делает вместо меня
SIZE = 6 * 30 # шесть типов платежей на 30 дней
def inputDataInFIle():
    with open(PATH, 'w') as outfile:
        numbers = []
        for i in range(SIZE):
            numbers.append(f"{random.uniform(0, 100):.2f}\n")
        outfile.writelines(numbers)

def readFile():
    data = [0] * 6
    index = 0
    with open(PATH, 'r') as infile:
        for i in range(SIZE):
            data[index] += float(infile.readline().rstrip())
            if index % 5 == 0:
                index = 0
            index += 1
        for i in range(len(data)):
            data[i] = round(data[i], 2)
    return data

def creatPia(data):
    plt.pie(data,  labels = ["арендная плата",
"бензин", 
"продукты питания",
"одежда",
"платежи по автомашине",
"прочие"]) 
    plt.show()
    
def main():
    inputDataInFIle()
    data = readFile()
    creatPia(data)

if __name__ == "__main__":
    main()
