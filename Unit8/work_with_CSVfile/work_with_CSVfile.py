data = []
with open("/home/ranil/Рабочий стол/StudingPython/Unit8/work_with_CSVfile/Цены.csv") as infile:
    data = infile.readlines()
data = [el.rstrip().split(',') for el in data]
print(data)