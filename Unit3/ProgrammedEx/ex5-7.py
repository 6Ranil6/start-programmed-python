# # ex 5

# m = int(input("Введите массу в килограммах"))
# p = 9.8 * m

# if p > 500:
#     print("Слишком большой вес")
# elif p < 100:
#     print("Слишком легкий вес")
# else:
#     print(f"Ващ вес: {p:,}")

# ex 6

# date = input("Введите дату(учитывая, что год духзначный): ")

# num = date.split(".")

# day = num[0]
# month = num[1]
# years = num[2]

# if int(day) * int(month) == int(years):
#     print("Это воолшебное число")
# else:
#     print("Это обычное число")

# ex 7 

# red = "красный"
# blue = "синий"
# yellow = "желтый"

# color_1 = input("Введите цвет: ")
# if color_1 != red or color_1 != blue or color_1 != yellow:
#     color_1.lower()
#     print("ОШИБКА ВЫ ВВЕЛИ НЕ ТОТ ЦВЕТ")
# else:
#     color_2 = input("Введите цвет: ")
#     color_2.lower()
#     if color_1 != red or color_1 != blue or color_1 != yellow:
#         print("ОШИБКА ВЫ ВВЕЛИ НЕ ТОТ ЦВЕТ")
#     else:
#         if color_1 == color_2:
#             print(f"{color_1}")
#         elif (color_1 == red or color_1 == blue) and (color_2 == red or color_2 == blue):
#             print("фиолетовый")
#         elif (color_1 == red or color_1 == yellow) and (color_2 == red or color_2 == yellow):
#             print("оранжевый")
#         else:
#             print("зеленый")