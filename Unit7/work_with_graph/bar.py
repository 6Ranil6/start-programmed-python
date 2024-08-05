import matplotlib.pyplot as plt

bar_width = 10
x_bar = [10, 15, 20, 25] 
y_bar = [10, 15, 20, 25]
plt.bar(x_bar, y_bar, bar_width, color = ('b', 'k', 'm', 'c'))
plt.xlim(xmax = 25)
plt.title("Продажи с разбивкой по годам")
plt.xlabel("Год")
plt.ylabel("Объем продаж")
plt.xticks(x_bar, ["2016", "2017", "2018", "2019"])
plt.yticks([0] + y_bar, ["$0m", "$1m", "$2m", "$3m", "$4m"])
plt.show()
