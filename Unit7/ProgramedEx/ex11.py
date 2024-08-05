# М агический к в ад р ат  Ш у.
#  Магический квадрат До Шу представляет собой таблицу
# с 3 строками и 3 столбцами (рис. 7.21). Магический квадрат Jlo Ш у имеет свойства:
# •таблица содержит числа строго от 1 до 9;
# •сумма каждой строки, каждого столбца и каждой диагонали в итоге составляет одно
# и то же число (рис. 7.22).
# Магический квадрат можно сымитировать в программе при помощи двумерного списка.
# Напишите функцию, которая принимает двумерный список в качестве аргумента и
# определяет, является ли список магическим квадратом Ло Шу. Протестируйте функцию
# в программе

def IsMagicSquare(data):
    long = len(data)

    SummCol = 0
    summDiag = 0
    summUnDiag = 0

    for i in range(long):
        if sum(data[i]) == sum(data[-1]):
            for j in range(long):
                SummCol += data[i][j]
                if i == j:
                    summDiag += data[i][j]
                if i + j == long - 1:
                    summUnDiag += data[i][j]
        else: 
            return False
    if SummCol / 3 == sum(data[0]) == summDiag == summUnDiag:
        return True
    else:
        return False
    
def main():
    mas = [[4, 9, 2],
           [3, 5, 7],
           [8, 1, 6]]
    mas2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    print(IsMagicSquare(mas), IsMagicSquare(mas2))
if __name__ == "__main__":
    main()