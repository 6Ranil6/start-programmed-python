# Гласные и согласные.
# Напишите программу с функцией, которая в качестве аргумента
# принимает строковое значение и возвращает количество содержащихся в нем гласных.
# Приложение должно иметь еще одну функцию, которая в качестве аргумента принимает
# строковое значение и возвращает количество содержащихся в нем согласных. Приложе­
# ние должно предоставить пользователю возможность ввести строковое значение и пока­
# зать содержащееся в нем количество гласных и согласных.
import re

def is_vowel(symbol: str):
    if re.fullmatch(r"^[aeiouаэиоуы]{1}", symbol, flags= re.IGNORECASE):
        return True
    return False

def counter_Litters(text: str):
    vow = 0
    cons = 0
    for el in text:
        if is_vowel(el):
            vow += 1
        else:
            cons += 1
    return vow, cons

def main():
    text = input("Введите текст: ")
    print(counter_Litters(text))
if __name__ == "__main__":
    main()