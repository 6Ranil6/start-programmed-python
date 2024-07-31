# Счетчик четны х/нечетны х чисел. В этой главе вы увидели пример написания алго­
# ритма, который определяет четность или нечетность числа. Напишите программу, кото­
# рая генерирует 100 случайных чисел и подсчитывает количество четных и нечетных
# случайных чисел.

import random

random.seed(5)

SIZE = 5
MAX_VALUE = 20

def main():
    numData = GenerateData()
    PrintData(numData)
    _2n, _2n1 = is_2n(numData)
    print(f"Четных чисел: {_2n}\nНечетных чисел: {_2n1}")

def GenerateData():
    numData = []
    for counter in range(SIZE):
        numData.append(random.randrange(MAX_VALUE))
    return numData

def PrintData(mas):
    print("Your input Data:")
    for counter in range(SIZE):
        print(f"{mas[counter]:<5}", end= "")
    print()

def is_2n(mas):
    """Подсчитывает количество четных и нечетных чисел в списке."""
    even_count = 0
    odd_count = 0
    for number in mas:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count     

if __name__ == '__main__':
    main()