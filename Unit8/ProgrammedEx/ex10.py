# С ам ы й частотны й символ. Напишите программу, которая предоставляет пользователю
# возможность ввести строковое значение и выводит на экран символ, который появляется
# в нем наиболее часто.

def frequancy_Litters(text: str):
    Litters_list = [[], []] # обращение по индексу 0 - сама буква по индексу 1 - его количество в строке
    for sym in text:
        if sym not in Litters_list[0] and not sym.isspace():
            Litters_list[0].append(sym)
            Litters_list[1].append(text.count(sym))

    return "Чаще всего встречается: " + Litters_list[0][Litters_list[1].index(max(Litters_list[1]))]

text = input("Введите текст: ")

print(frequancy_Litters(text))