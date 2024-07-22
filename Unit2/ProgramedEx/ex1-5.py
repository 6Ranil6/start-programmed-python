# #ex 1
# name = input("Введите свое имя: ")
# adres = input("Введите свой адрес проживания, и т.д.: ")
# numberPhone = input("Введите свой номер телефона: ")
# specialisaion = input("Введите свою специализацию: ")
# print(f"{name:>15}\n{adres:>15}\n{numberPhone:>15}\n{specialisaion:>15}")

# #ex 2
# money = float(input("Введите объем продаж: "))
# print(f"Прибыль: {money * 0.23}")

# #ex 3
# metrs = float(input("Введите количество квадратных метров земли: "))
# print(f"Акров: {metrs / 4047:,.2f}")

# #ex 4
# NALOG = 0.07 # налог 7% 
# itog = 0
# for a in range(5):
#     eat  = float(input(f"Введите стоимость {a + 1} продукта: "))
#     itog += eat + eat * NALOG
# # можно было исправить предыдущую строчку и добавить itog += itog * NALOG
# print(f"Итог: {itog}")

# #ex 5
# hour = int(input("Введите количество часов: "))
# speed = 70
# print(f"Вы проехали {hour * speed}км ")