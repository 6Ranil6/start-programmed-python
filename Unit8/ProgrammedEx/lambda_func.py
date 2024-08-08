# Задача: Генерация списка квадратов нечетных чисел Описание: Дано целое число n. Необходимо создать список квадратов всех нечетных чисел от 1 до n. Пример входных данных:
# n = 10
# Ожидаемый результат:

# [1 ,9 ,25 .49 .81]
# Задача: Фильтрация списка чисел Описание: Дан список чисел. Необходимо создать новый список только из положительных чисел или только из отрицательных чисел. Пример входных данных:
# numbers = [1, -2, -3 ,4 , -5 ,6 ,-7 ]
# Ожидаемый результат при фильтрации положительных чисел:

# [1 ,4 ,6 ]
def task1():
    number = 0
    while True:
        try:
            number = int(input("Enter Number: "))
        except ValueError:
            print("Вы ввели не число!!!")
        else:
            break
    x = lambda  mylist: [el ** 2 for el in mylist if el % 2 != 0]
    print(x([el for el in range(number) + 1]))

def task2():
    numbers = [1, -2, -3 ,4 , -5 ,6 ,-7 ]
    print((lambda mylist: [el for el in mylist if el > 0])(numbers))

def main():
    # task1()
    task2()
if __name__ == "__main__":
    main()