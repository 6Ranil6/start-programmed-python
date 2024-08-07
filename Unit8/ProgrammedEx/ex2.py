# 2 Сумма цифр в строке. Напишите программу, которая просит пользователя ввести ряд
# однозначных чисел без разделителей. Программа должна вывести на экран сумму всех
# однозначных чисел в строковом значении. Например, если пользователь вводит 2514, то
# этот метод должен вернуть значение 12, которое является суммой 2, 5, 1 и 4.

def enterCorrectNumber():
    while True:
        try:
            numbers = int(input("Введите ряд однозначных чисел: "))
        except ValueError:
            print("Вы ввели не целое число!!!")
        else:
            return numbers

def summNumbers(numbers):
    return sum([int(digit) for digit in str(numbers)])

def main():
    numbers = enterCorrectNumber()    
    print(summNumbers(numbers))

if __name__ == "__main__":
    main()