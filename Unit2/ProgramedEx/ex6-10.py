# # ex 6
# regionalTax = 0.025
# federalTax = 0.05

# paySumm = float(input("Введите сумму покупки: "))

# print(f"Ваш региональный налог составляет: {paySumm * regionalTax}")
# print(f"Ваш федеральный налог составляет: {paySumm * federalTax}")
# print(f"В итоге сумма покупки: {paySumm + paySumm * regionalTax + paySumm * federalTax}")

# #ex 7
# distance = float(input("Введите пройденное растояние: "))
# consuption_oil = float(input("Введите расзод бензина: "))
# print(f"Расход: {distance / consuption_oil}")

# #ex 8 
# count = 1
# summ = 0
# tax = 0.07
# tips = 0.18
# while True:
#     summ += float(input(f"Введите стоимость {count} продукта: "))
#     answer = input("Хотите продолжить?")
#     bAnswer = answer.upper()
#     if(bAnswer == "NO"):
#         break
#     count += 1
# summTips = summ * tips
# summTax = summ * tax
# summ += summTips + summTax
# print(f"ИТОГ: {summ:,.2f}")
# print(f"Вы оставили {summTips} чаевых")
# print(f"Налог: {summTax}")

# #ex 9
# C = float(input("Введите температуры по шкалле цельсия: "))
# F = (9/5) * C + 32
# print(f"По фаренгейту: {F}")

# #ex 10
# buns = int(input("Введите количество булочек: "))
# # Количество ингредиентов на одну булочку
# sugar = 1.5 / 48
# butter = 1 / 48 
# flour = 2.75 / 48

# print(f"САХАР: {buns * sugar:.2F}\nМАСЛО: {buns * butter:.2F}\nМУКИ: {buns * flour:.2F}")
