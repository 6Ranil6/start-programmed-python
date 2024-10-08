# Применение словаря для имитации карточной колоды
# В некоторых играх, связанных с игральными картами, картам присваиваются числовые зна­
# чения. Например, в игре блек-джек картам даются числовые значения:
# ♦ числовым картам присваивается значение, которое на них напечатано. Например, двойка
# пик равняется 2, а пятерка бубей равняется 5;
# ♦ валетам, дамам и королям назначается значение 10;
# ♦ тузам назначается 1 либо 11 в зависимости от выбора игрока.
# В этой рубрике мы рассмотрим программу, которая применяет словарь для имитирования
# стандартной колоды игральных карт, где картам присваиваются числовые значения, подоб­
# ные тем, которые используются в игре блек-джек. (В этой программе мы присваиваем всем
# тузам значение 1.) В парах "кл ю ч : значение" достоинство карты используется в качестве
# ключа, а числовое значение карты — в качестве значения. Например, пара "ключ : значение"
# для дамы червей будет такой:
# 'Дама червей':10486
# А пара "ключ : значение" для восьмерки бубей будет такой:
# '8 бубей':8
# Программа предлагает пользователю ввести количество карт, которые нужно раздать,
# и произвольным образом раздает на руки это количество карт из колоды. Затем выводятся
# достоинства розданных карт, а также сумма их достоинств. В программе 9.1 приведен соот­
# ветствующий код. Программа разделена на три функции: main (главная), create deck (соз­
# дать колоду) и deal cards (раздать карты).
import random

def creat_cards():
    cards = {
        "2 буби" : 2, "3 буби" : 3,
        "4 буби" : 4, "5 буби" : 5,
        "6 буби" : 6, "7 буби" : 7,
        "8 буби" : 8, "9 буби" : 9,
        "10 буби" : 10, "Валет буби" : 10,
        "Дама буби" : 10, "Король буби" : 10,
        "Туз буби" : 1,

        "2 черви" : 2, "3 черви" : 3,
        "4 черви" : 4, "5 черви" : 5,
        "6 черви" : 6, "7 черви" : 7,
        "8 черви" : 8, "9 черви" : 9,
        "10 черви" : 10, "Валет черви" : 10,
        "Дама черви" : 10, "Король черви" : 10,
        "Туз черви" : 1,

        "2 пик" : 2, "3 пик" : 3,
        "4 пик" : 4, "5 пик" : 5,
        "6 пик" : 6, "7 пик" : 7,
        "8 пик" : 8, "9 пик" : 9,
        "10 пик" : 10, "Валет пик" : 10,
        "Дама пик" : 10, "Король пик" : 10,
        "Туз пик" : 1,
        
        "2 крести" : 2, "3 крести" : 3,
        "4 крести" : 4, "5 крести" : 5,
        "6 крести" : 6, "7 крести" : 7,
        "8 крести" : 8, "9 крести" : 9,
        "10 крести" : 10, "Валет крести" : 10,
        "Дама крести" : 10, "Король крести" : 10,
        "Туз крести" : 1,
    }
    return cards

def deal_card(cards: dict):
    counter = 0
    while True:
        try:
            counter = int(input("Введи количество карт, которое вы хоте ли бы взять: "))
        except ValueError:
            print("Вы можете ввести только целое число!!!")
        else:
            break
    pull_card = random.sample(list(cards.keys()), counter)
    for i in range(len(pull_card)):
        if pull_card[i].startswith("Туз"):
            value = 0
            while True:
                value = input(f"Введите значение, которое вы бы зотели получить за {pull_card[i]}: (1 или 11): ")
                if value == "11" or value == "1":
                    break
                print("Вы ввели не правильное значение, еще раз!!!")
            cards[pull_card[i]] = int(value)
    summ = 0
    print("Вам выпало: ")
    for card in pull_card:
        print(f"'{card.upper()}' за него вы получили {cards[card]}")
        summ += cards[card]
    
    return summ

def main():
    while True:
        cards = creat_cards()
        summ = deal_card(cards)
        print("Суммарное количество баллов:", summ)
        if input("Если не хотите продолжить введите 'y': ").upper() == 'Y':
            break
    print("Игра закончилась!!!")

if __name__ == "__main__":
    main()