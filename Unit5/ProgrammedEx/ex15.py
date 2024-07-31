# Средний балл и его уровень. Напишите программу, которая просит пользователя вве­
# сти пять экзаменационных оценок (баллов). Программа должна показать буквенный
# уровень для каждой оценки и средний балл. Предусмотрите в программе функции:
# • calc average — функция должна принимать в качестве аргументов пять балльных
# оценок и возвращать средний балл;
# • determine grade — функция должна принимать в качестве аргумента балльную
# оценку и возвращать буквенный уровень оценки, опираясь на приведенную в табл. 5.3
# классификацию.

def main():
    my_list = []
    for a in range(5):
        my_list.append(int(input("Enter your mark: ")))
    mid_ball = calc_average(my_list[0], my_list[1], my_list[2], my_list[3], my_list[4])
    
    print(f"Ваш средний балл: {mid_ball}")
    print("Ваши баллы: ", end= "")
    for counter in range(5):
        print(f"{(determine_grade(my_list[counter])):<3}", end= ' ')
    print()
    
def calc_average(m1, m2, m3, m4, m5):
    return (m1 + m2 + m3 + m4 + m5) / 5

def determine_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 80 and mark <= 89:
        return 'B'
    elif mark >= 70 and mark <= 79:
        return 'C'
    elif mark >= 60 and mark <= 69:
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    main()