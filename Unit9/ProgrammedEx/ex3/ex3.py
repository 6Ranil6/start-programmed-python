# Шифрование и дешиф рование файлов. Напишите программу, которая применяет сло­
# варь для присвоения "кодов" каждой букве алфавита. Например:
# codes = \
# 'а':'9\ 'Б':'0', 'б':'#' ...}
# Здесь букве А присвоен символ %, букве а — число 9, букве Б — символ 0 и т. д. Про­
# грамма должна открыть заданный текстовый файл, прочитать его содержимое и приме­
# нить словарь для записи зашифрованной версии содержимого файла во второй файл.
# Каждый символ во втором файле должен содержать код для соответствующего символа
# из первого файла.
# Напишите вторую программу, которая открывает зашифрованный файл и показывает его
# дешифрованное содержимое на экране.
import os
NAMEFILE = "data.txt"
PATH = f"/home/ranil/Рабочий стол/StudingPython/Unit9/ProgrammedEx/ex3/{NAMEFILE}"

codes ={'а': 'z', 'б': '3', 'в': 'Q',
        'г': 'k', 'д': 'M', 'е': 'w',
        'ё': '8', 'ж': 'F', 'з': 'n',
        'и': 'D', 'й': 'p', 'к': '5',
        'л': 'B', 'м': 'r', 'н': 'S', 
        'о': 'x', 'п': '2', 'р': 'G', 
        'с': 'a', 'т': 'T', 'у': '9', 
        'ф': 'L', 'х': 'J', 'ц': 'Y', 
        'ч': '4', 'ш': 'V', 'щ': '7', 
        'ъ': 'q', 'ы': 'H', 'ь': 'Z', 
        'э': 'i', 'ю': 'c', 'я': '6',
        ' ': ' ', '\n' : '\n'}


def write_in_file():
    text = input("Введите текст, который хотите зашифровать: ",)
    while True:
        try:
            encrapted_text = "".join([codes[Litter] for Litter in text])
        except:
            print("Вы ввели букву не из русского алфавита")
            text = input("Введите текст, который хотите зашифровать заново: ",)
        else:
            break
    with open(PATH, 'a') as outfile:
        outfile.write(encrapted_text + "\n")
    
def unencrapting(text: str):
    uncodes = dict(zip(codes.values(), codes.keys()))
    unencrapted_text = "".join([uncodes[Litters] for Litters in text])
    print(unencrapted_text)

def read_in_file():
    try:
        with open(PATH, 'r') as infile:
            unencrapting(infile.readline().rstrip())
    except FileNotFoundError:
        print("Такого файла нет!!!")

def main():
    while input("Введите stop, если хотите закончить рабоу с программой: ").upper() != "STOP":
        try:
            match int(input("Введите:\n1 - если хотетите зашифровать данные и записать в файл\n2 - если хотите прочитать данные из файла\n3 - если хотите удалить данные из файла\n")):
                case 1:
                    write_in_file()
                case 2:
                    read_in_file()
                case 3:
                    os.remove(PATH)
                case _:
                    print("Нет такой команды!!!\nАварийное завершение")
                    break
        except ValueError:
            print("Вы ввели не число!!!")

if __name__ == "__main__":
    main()