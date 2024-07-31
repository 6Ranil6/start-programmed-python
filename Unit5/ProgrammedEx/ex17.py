# # Простые числа. Простое число — это число, которое делится без остатка на само себя
# и 1. Например, число 5 является простым, потому что оно делится без остатка только
# на 1 и 5. Однако число 6 не является простым, потому что оно делится без остатка на 1,
# 2, 3 и 6.
# Напишите булеву функцию is prime, которая в качестве аргумента принимает целое
# число и возвращает истину, если аргумент является простым числом, либо ложь в про­
# тивном случае. Примените функцию в программе, которая предлагает пользователю вве­
# сти число и затем выводит сообщение с указанием, является ли это число простым.
import math 
import random

random.seed(5)
MAX_VALUE = 50
SIZE = 5

def main():
    masNum = []
    for counter in range(SIZE):
        masNum.append(random.randrange(MAX_VALUE))
    for counter in range(SIZE):
        answer = "Простое" if is_prime(masNum[counter]) else "НЕ Простое"
        print(f"Число {masNum[counter]:< 5}: {answer}")

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 - единственное четное простое число
    if num % 2 == 0:
        return False  # отсеиваем все четные числа, кроме 2
    sqrt_num = int(math.sqrt(num)) + 1
    for i in range(3, sqrt_num, 2):  # проверяем только нечетные числа
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    main()