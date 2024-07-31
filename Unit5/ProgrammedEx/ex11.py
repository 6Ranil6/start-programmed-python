# Матем атический тест. Напишите программу, которая позволяет проводить простые
# математические тесты. Она должна показать два случайных числа, которые должны
# быть просуммированы вот так:
# 247
# + 129
# Эта программа должна давать обучаемому возможность вводить ответ. Если ответ пра­
# вильный, то должно быть показано поздравительное сообщение. Если ответ неправиль­
# ный, то должно быть показано сообщение с правильным ответом
from random import randrange

ANSWER = None

def EnterAnswer():
    global ANSWER
    ANSWER = int(input("Enter your answer: "))

def cheking(value):
    if value == value1 + value2:
        print("YOUR answer is correct, NICE WORK!!!")
    else:
        print("YOUR ANSWER ISN'T CORRECT!!!")

def repeat():
    ans = None
    while ans != "no":
        print(value1)
        print(f"+ {value2}")
        EnterAnswer()
        cheking(ANSWER)  
        ans = input("Repeat? (Enter: YES or NO) ").lower()
        

value1 = randrange(100,200)
value2 = randrange(100,200)
repeat()