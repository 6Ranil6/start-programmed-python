# Задание 1:
# Напишите программу, которая принимает от пользователя строку и выводит:

# Количество уникальных символов в строке
# Все слова, которые начинаются с гласной буквы
# Все слова, которые содержат только цифры
# Строку, где все цифры заменены на их словесное представление (например, "123" -> "one two three")
import re
reVowels = re.compile("[a,e,i,o,u]\w*", flags=re.IGNORECASE)

digitDict = {
    "zero": 0,
    'one': 1,
    'two': 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def counter_uniq_symb(string: str):
    uniqueSym = [string[0]]
    for Sym in string[1:]:
        if Sym not in uniqueSym:
            uniqueSym.append(Sym)
    print("Количество уникальных символов: {0}".format(len(uniqueSym)))

def WordsStartWithVowels(text: str):
    return [el for el in text.split() if re.match(reVowels, el)]

def IsWordsDigits(text: str):
    return [el for el in text.split() if re.match("\d+", el)]

def WordsInDigitDict(text: str):
    return [el for el in text.split() if el in tuple(digitDict.keys())]

def main():
    text = input("Введите текст: ")
    counter_uniq_symb(text)

    print("Вывод: ")
    print("Слова начинающие с гласных букв: {0}".format(" | ".join(WordsStartWithVowels(text))))
    print(f"Слова состоящие только из цифр: {' | '.join(IsWordsDigits(text))}")
    print("Слова,где цифры заменены на их словесное представление: {0}".format(" ".join(WordsInDigitDict(text))))

if __name__ == "__main__":
    main()