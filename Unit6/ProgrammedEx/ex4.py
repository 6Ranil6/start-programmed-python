# Счетчи кзначений. Допустим, что файл с серией имен (в виде строковых значений)
# называется names.txt и существует на диске компьютера. Напишите программу, которая
# показывает количество хранящихся в файле имен. (Подсказка: откройте файл и прочи­
# тайте каждую хранящуюся в нем строку. Используйте переменную для подсчета количе­
# ства прочитанных из файла значений.)

NAMEFILE = "names"

def count_names():
    path = f"/home/ranil/Рабочий стол/{NAMEFILE}"
    counter = 0
    try:    
        outfile = open(path, 'r')
    except IOError:
        print("Ошибка!!!\nТакого файла не существует!")
    else:
        for line in outfile:
            counter += 1
    finally:
        outfile.close()
        return counter

def main():
    print(f"Количество имен: {count_names():<,}")

if __name__ == "__main__":
    main()