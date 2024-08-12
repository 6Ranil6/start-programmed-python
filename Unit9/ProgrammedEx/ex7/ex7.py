# Победители М и р о в о й серии. Среди исходного кода главы 9 вы найдете файл
# WorldSeriesWinners.txt. Он содержит хронологический список команд-победителей Ми­
# ровой серии по бейсболу с 1903 по 2009 год. (Первая строка в файле является названием
# команды, которая победила в 1903 году, последняя строка— названием команды, кото­
# рая победила в 2009 году. Обратите внимание, что Мировая серия не проводилась в 1904
# и 1994 годах. В файле имеются указывающие на это пометки.)

#1) Напишите программу, которая читает этот файл и создает словарь, в котором ключи —
# это названия команд, а связанные с ними значения — количество побед команды в Ми­
# ровой серии.

# 2)Программа также должна создать словарь, в котором ключи — это годы,
# а связанные с ними значения — названия команд, которые побеждали в том году.
# Программа должна предложить пользователю ввести год в диапазоне между 1903 и
# 2009 годами и вывести название команды, которая выиграла Мировую серию в том году
# и количество побед команды в Мировой серии.

import os
FILENAME = "WorldSeriesWinners.txt"
PATH = f"{os.path.dirname(__file__)}/{FILENAME}"

def read_file():
    with open(PATH, 'r') as outfile:
        winersList = outfile.readlines()
    return [winer.rstrip() for winer in winersList]

def BeautifulPrint1(winersDict: dict):
    for winer, counter in winersDict.items():
        print(f"{winer} победил {counter} раз")

def BeautifulPrint2(yearsDict: dict):
    for year, winer in yearsDict.items():
        print(f"В {year} году победил {winer}") if not winer.startswith("World Series Not Played") else print("World Series Not Played")

def CreateDict1():
    winersList = read_file()
    winersSet = set(winersList)
    BeautifulPrint1({el : winersList.count(el) for el in winersSet if not el.startswith("World Series Not Played")})

def creatDict2():
    winersList = read_file()
    dict2 = {year: winer for year, winer in enumerate(winersList, 1903)}
    BeautifulPrint2(dict2)

def main():
    CreateDict1()
    print("-" * 20)
    creatDict2()

if __name__ == "__main__":
    main()