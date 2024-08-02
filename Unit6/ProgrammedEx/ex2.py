# Вывод на экран верхней части файла. Напишите программу, которая запрашивает
# у пользователя имя файла. Программа должна вывести на экран только первые пять строк
# содержимого файла. Если в файле меньше пяти строк, то она должна вывести на экран
# все содержимое файла.


def creat_file(namefile) :
    outfile = open(f"{namefile}", 'w') 
    for counter in range(2):
        outfile.write(f"{counter}" + "\n")
    outfile.close()

def read_forward_line(namefile):
    try:
        infile = open(namefile, 'r')
    except IOError:
        print("Файла не существует!!!")
    else:
        counter = 0
        while counter < 5:
            line = infile.readline().rstrip()
            if line != '':
                print(line)
                counter += 1
            else:
                break
        infile.close()

def main():
    namefile = input("Введите название файла: ")
    path = f"/home/ranil/Рабочий стол/{namefile}"
    creat_file(path)    
    read_forward_line(path)
if __name__ == "__main__":
    main()