import matplotlib.pyplot as plt

x_cords = [1, 2, 3, 4, 5]
y_cords = [3, 5, 4, 3, 1]

plt.plot(x_cords, y_cords, '<')
plt.grid(True)
# plt.xlim(xmax = 50, xmin = -10)
# plt.ylim(ymax = 34, ymin = -10)
plt.xlabel("Количество покупателей")
plt.ylabel("Цена товара")
x_ticks = [el for el in x_cords]
y_ticks = [el for el in y_cords]
plt.xticks(x_ticks, ["milk", "orange", "juce", "apple", "coffe"])
plt.yticks(y_ticks, [el * 10 for el in y_ticks])
plt.show()
