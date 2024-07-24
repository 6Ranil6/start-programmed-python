# # остальные слишком легкие задачи эта хотя бы поинтреснее 

# # +/- - это ответ на вопрос есть ли в этом ресторне определенная еда

# burger = "Изысканные гамбургеры от Джо" #--- 
# pizza = "Центральная пицерия"#+-+
# coffe = "Кафе за углом" #+++
# italion = "Блюда от итальянской мамы" #+--
# homeCook =  "Кухня шеф-повара" #+++

# restorans = []
# restorans.append(burger)
# restorans.append(pizza)
# restorans.append(coffe)
# restorans.append(italion)
# restorans.append(homeCook)

# answer_1 = input("Будет ли на ужине вегетерианец: ")
# answer_2 = input("Будет ли на ужине веган: ")
# answer_3 = input("Будет ли на ужине приверженец безглютеновой диеты: ")

# answer_1.lower()
# answer_2.lower()
# answer_3.lower()

# if answer_1 == "да":
#     restorans[0] = False
# if answer_2 == "да":
#     restorans[0] = False
#     restorans[1] = False
#     restorans[3] = False
# if answer_3 == "да":
#     restorans[0] = False
#     restorans[3] = False

# print("Вам пойдут рестораны: ")
# for counter in range(5):
#     if restorans[counter] != False:
#         print(restorans[counter])