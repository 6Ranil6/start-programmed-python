# Частота слов. Напишите программу, которая считывает содержимое текстового файла.
# Она должна создать словарь, в котором ключами являются отдельные слова
# в файле, а значениями— количество появлений каждого слова. Например, если слово
# 'это ' появляется 128 раз, то словарь должен содержать элемент с ключом 'это ' и значе­
# нием 128. Программа должна либо показать частотность каждого слова, либо создать
# второй файл, содержащий список слов и их частот.

NAMEFILE = "data.txt"
PATH = f"/home/ranil/Рабочий стол/StudingPython/Unit9/ProgrammedEx/ex5-6/{NAMEFILE}"

def write_text_file(text: str, path):
    with open(path, 'a') as outfile:
        outfile.write(text)

def  unique_word(text: str):
    if text != "":
        string_set = set(text.split())
        unique_word_dict = {el : text.count(el) for el in string_set}
        return unique_word_dict
    else:
        return set()
    
def read_data_file(path):
    try:
        with open(path, 'r') as infile:
            text = infile.read()
    except FileNotFoundError:
        print("Не удалось найти файл!!!\nПоэтому мы создали их автоматически")
        with open(path, 'w') as inf:
            inf.write("")
    else: 
        return text

def buautiful_print(dictinary: dict):
    for key, item in dictinary.items():
        print(f"Слова {key} встречается {item} раз")

def coorectEnter():
    while True:
        try:
            chooes = int(input((f"""Выберите:
1 - ввод строки в текст
2 - вывод количества повторяющихся слов
0 - выйти из программы\n""")
        )) 
        except ValueError:
            print("Вы ввели не целое число")
        else:
            if 0 <= chooes <=2 :
                return chooes
            else:
                print("Можно выбрать 1 или 2 или 0")

def chooes():
    choes = coorectEnter()
    while choes:
        match choes:
            case 1:
                text = input("Введите текст, который хотите записать в файл: ")
                write_text_file(text + '\n' if text != '\n' else "", PATH)
                choes = coorectEnter()
            case 2:
                text = read_data_file(PATH)
                buautiful_print(unique_word(text))
                choes = coorectEnter()

def main():
    chooes()

if __name__ == "__main__":
    main()