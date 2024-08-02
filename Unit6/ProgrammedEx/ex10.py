# Очки в игре в гольф. Любительский гольф-клуб проводит турниры каждые выходные.
# Президент клуба попросил вас написать две программы:
# •программу, которая читает имя каждого игрока и его счет в игре, вводимые с клавиа­
# туры, и затем сохраняет их в виде записей в файле golf.txt (каждая запись будет иметь
# поле для имени игрока и поле для счета игрока);
# •программу, которая читает записи из файла golf.txt и выводит их на экран.
from func_for_file import *

NAMEFILE = "golf"
PATH = f"/home/ranil/Рабочий стол/{NAMEFILE}"

def corectEnterIntNum():
    num = None
    while True:
        try:
            num = int(input("Введите свой счет: "))
        except ValueError:
           print("Вы ввели не целое число!!!")
        else:
            break
    return num

def addData(path):
    data = ""
    line = input("Введите свое имя: ") + '\n'
    while line != '\n':
        data += line
        line = str(corectEnterIntNum()) + '\n'
        data += line
        line = input("Введите свое имя: ") + '\n'
    try:  
        with open(path, 'a') as outfile:
            outfile.write(data)
    except IOError:
        print("Файл не открылся!!!")

def PrintData(path):

    print("\nВаши данные\n")
    try:
        with open(path, 'r') as outfile:
            name = outfile.readline().rstrip()
            while name != '':
                count = outfile.readline().rstrip()
                print(f"Ваше имя: {name}")
                print(f"Ваш счет: {count}")
                name = outfile.readline().rstrip() 
    except:
        print("Такого файла не существует!")

def main():
    creat_file(PATH)
    addData(PATH)
    PrintData(PATH)

if __name__ == "__main__":
    main()