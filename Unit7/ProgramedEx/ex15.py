# График еженедельных цен на беизин за 1994 год. Среди исходного кода главы 7 вы
# найдете файл 1994_Weekly_ Gas_Averages.txt. 
# Он содержит среднюю цену бензина в те­чение каждой недели 1994 года. (В файле 52 строки.) Используя пакет matplotlib,
# напишите программу Python, которая считывает содержимое файла и затем строит либо
# линейный график, либо гистограмму. Не забудьте показать содержательные метки вдоль
# осей х и у, я также метки делений.

import matplotlib.pyplot as plt

PATH = "/home/ranil/Загрузки/9785977568036/source-code/Упражнения по программированию/Глава 07/data/1994_Weekly_Gas_Averages.txt"
SIZE = 1000

def read_data_in_file():
    data = []
    with open(PATH, 'r') as outfile:
        data = outfile.readlines()
        data = [el.rstrip() for el in data]
    return data

def creat_bar(data):

    plt.bar([el * SIZE for el in range(1,53)], [el * SIZE for el in data], SIZE/2)
    plt.ylim(ymin = 0)
    plt.xlabel("Номер недели")
    plt.ylabel("Средняя цена бензина")
    plt.xticks([el * SIZE for el in range(1,53)], [el for el in range(1,53)])
    plt.yticks([el * SIZE for el in data], data)
    plt.show()

def main():
    dataWithFile = read_data_in_file()
    creat_bar(dataWithFile)

if __name__ == "__main__":
    main()
