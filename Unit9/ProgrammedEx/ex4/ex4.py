# У н и к а л ь н ы е слова. Напишите программу, которая открывает заданный текстовый файл
# и затем показывает список всех уникальных слов в файле. (Подсказка: храните слова
# в качестве элементов множества.)
NAMEFILE = "data.txt"
PATH = f"/home/ranil/Рабочий стол/StudingPython/Unit9/ProgrammedEx/ex4/{NAMEFILE}"

import pickle

def open_file():
    with open(PATH, 'rb') as infile:
        sets = set(pickle.load(infile))
    return sets

def write_file(_object_):
    with open(PATH, 'ab') as oufile:
        pickle.dump(_object_, oufile)

def main():
    myList = input("Введите текст, который хотите сохранить: ").split()
    write_file(myList)
    print("уникальнные данные в файле:", open_file())

if __name__ == "__main__":
    main()