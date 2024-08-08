# Среднее количество слов. Среди исходного кода главы 8 вы найдете файл text.txt. В нем
# в каждой строке хранится одно предложение. Напишите программу, которая читает со­
# держимое файла и вычисляет среднее количество слов в расчете на предложение.

NAMEFILE = "data.txt"
PATH = f"/home/ranil/Рабочий стол/StudingPython/Unit8/ProgrammedEx/ex6-7/{NAMEFILE}"


def readInFile():
    try:
        with open(PATH, 'r') as outfile:
            lines = outfile.readlines()
    except IOError:
        print("Файл не открылся!!!")
    else:
        lines = [line.split() for line in lines]
        return lines
#task 6
def midWordInLines(lines):
    summWord = 0
    for i in range(len(lines)):
        summWord += len(lines[i])
    return summWord / len(lines)

#task 7
# Анализ символов. Среди исходного кода главы 8 вы найдете файл text.txt. Напишите
# программу, которая читает содержимое файла и определяет:
# •количество букв в файле в верхнем регистре;
# •количество букв в файле в нижнем регистре;
# •количество цифр в файле;
# •количество пробельных символов в файле.

def CounterLetters(lines: str):
    letters = []

    BigLetterCounter = 0
    LittleLetterCounter = 0
    DigitCounter = 0
    SpaceCounter = 0

    for lineIndex in range(len(lines)):
        SpaceCounter += 1
        for WordIndex in range(len(lines[lineIndex])):
            SpaceCounter += 1
            for LetterIndex in  range(len(lines[lineIndex][WordIndex])):
                if lines[lineIndex][WordIndex][LetterIndex].isupper():
                    BigLetterCounter += 1
                elif lines[lineIndex][WordIndex][LetterIndex].islower():
                    LittleLetterCounter += 1
                elif lines[lineIndex][WordIndex][LetterIndex].isdigit():
                    DigitCounter += 1
    return BigLetterCounter, LittleLetterCounter, DigitCounter, SpaceCounter

def main():
    lines = readInFile()
    print("Среднее количество слов: ", midWordInLines(lines))
    
    upper, lower, digit, space = CounterLetters(lines)
    print(f"Количество букв в верхнем регистре: {upper}")
    print(f"Количество букв в нижнем регистре: {lower}")
    print(f"Количество цифр: {digit}")
    print(f"Количество пробелов: {space}")

if __name__ == "__main__":
    main()