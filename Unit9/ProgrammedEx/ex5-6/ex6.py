# Анализ файла. Напишите программу, которая читает содержимое двух текстовых фай­
# лов и сравнивает их следующим образом:
# •показывает список всех уникальных слов, содержащихся в обоих файлах;
# •показывает список слов, входящих в оба файла;
# •показывает список слов из первого файла, не входящих во второй;
# •показывает список слов из второго файла, не входящих в первый;
# •показывает список слов, входящих либо в первый, либо во второй файл, но не входя­щих в оба файла одновременно.

from os.path import dirname
import ex5 as my
NAMEFILE1 = "data1.txt"
NAMEFILE2 = "data2.txt"
current_dir = dirname(__file__)
file1 = f"{current_dir}/{NAMEFILE1}"
file2 = f"{current_dir}/{NAMEFILE2}"

def coorectEnter():
    while input("Если хотите выйти из программы, введите STOP: ").upper() != "STOP":
        try:
            chooes = int(input((f"""Выберите:
1 - ввод строки в {NAMEFILE1}
2 - ввод строки в {NAMEFILE2}
3 - показать список всех уникальных слов, содержащихся в обоих файлах
4 - показать список слов, входящих в оба файла;
5 - показать список слов из первого файла, не входящих во второй;
6 - показать список слов из второго файла, не входящих в первый;
7 - показать список слов, входящих либо в первый, либо во второй файл, но не входя­щих в оба файла одновременно.\n""")
        )) 
        except ValueError:
            print("Вы ввели не целое число")
        else:
            if 1 <= chooes <= 7 :
                return chooes
            else:
                print("Можно выбрать 1-7")


def change_print(result, text):
    print(text)
    for index, el in enumerate(result, 1):
        print(f"{index}) {el}")


def choose():
    file1_set = set(my.unique_word(my.read_data_file(path= file1)).keys())
    file2_set = set(my.unique_word(my.read_data_file(path= file2)).keys())
    choes = coorectEnter()
    while choes:
        match choes:
            case 1:
                text = input(f"Введите текст, который хотите записать в {NAMEFILE1}: ")
                my.write_text_file(text + '\n' if text != '\n' else "", file1)
            case 2:
                text = input(f"Введите текст, который хотите записать в {NAMEFILE2}: ")
                my.write_text_file(text + '\n' if text != '\n' else "", file2)
            case 3:
                print(file1_set, file2_set)
                change_print(file1_set | file2_set, "Слова, содержащиеся в обоих файлах:")
            case 4:
                print(file1_set, file2_set)
                change_print(file1_set & file2_set, "Cлова, входящих в оба файла:")
            case 5:
                print(file1_set, file2_set)
                change_print(file1_set - file2_set, "Cлова из первого файла, не входящие во второй:")
            case 6:
                print(file1_set, file2_set)
                change_print(file2_set - file1_set, "Слова из второго файла, не входящие в первый: ")
            case 7:
                print(file1_set, file2_set)
                change_print(file1_set ^ file2_set, "Слова, входящие либо в первый, либо во второй файл, но не входя­щие в оба файла одновременно")
        choes = coorectEnter()
    print("Программа завершилась")


def main():
    choose()


if __name__ == "__main__":
    main()