# Номера строк. Напишите программу, которая запрашивает у пользователя имя файла.
# Программа должна вывести на экран содержимое файла, при этом каждая строка должна
# предваряться ее номером и двоеточием. Нумерация строк должна начинаться с 1

def wondeful_read_file(path):
    outfile = open(path, 'r')
    counter = 1
    line = outfile.readline().rstrip()
    while line != '':
        print(f"{counter}: {line}")
        line = outfile.readline().rstrip()
        counter += 1
    outfile.close()

def main():
    namefile = input("Введите название файла: ")
    path = f"/home/ranil/Рабочий стол/{namefile}"
    wondeful_read_file(path)

if __name__ == "__main__":
    main()