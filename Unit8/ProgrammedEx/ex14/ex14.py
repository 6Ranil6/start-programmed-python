# Цены на бензин. Среди исходного кода главы 8 вы найдете файл GasPrices.txt. Этот
# файл содержит еженедельные средние цены за галлон бензина в США, начиная 5 апреля
# 1993 года и заканчивая 26 августа 2013 года. На рис. 8.8 показан пример первых не­
# скольких строк данного файла

# Каждая строка в файле содержит среднюю цену за галлон бензина в указанный день
# и отформатирована следующим образом:
# ММ-ДЦ-ГСТГ:Цена
# где мм— двухзначный месяц; д ц — двухзначный день; г г г г — четырехзначный год;
# Цена — это средняя цена галлона бензина в указанный день.
# В рамках этого задания необходимо написать одну или несколько программ, которые
# считывают содержимое данного файла и выполняют приведенные ниже вычисления.
# •Средняя цена за год: вычисляет среднюю цену бензина за год для каждого года
# в файле. (Данные файла начинаются апрелем 1993 года и заканчиваются августом
# 2013 года. Используйте данные, предоставленные за период с 1993 по 2013 год.)

# •Средняя цена за месяц: вычисляет среднюю цену в каждом месяце в файле.

# •Наибольшая и наименьшая цены в году: в течение каждого года в файле опреде­
# ляет дату и величину самой низкой и самой высокой цены.

# •Список цен, упорядоченный по возрастанию: генерирует текстовый файл, в кото­
# ром даты и цены отсортированы в возрастающем порядке.

# •Список цеи, упорядоченный по увеличению: генерирует текстовый файл, в кото­
# ром даты и цены отсортированы в убывающем порядке.
# Для выполнения всех этих вычислений можно написать одну программу или несколько
# разных программ, по одной для каждого вычисления.

import datetime

PATH = "/home/ranil/Рабочий стол/StudingPython/Unit8/ProgrammedEx/ex14/data.txt"

def ReadFile():
    
    file_list = []
    while True:
        try:
            global PATH
            with open(PATH, 'r') as outfile:
                file_list = outfile.readlines()
            file_list = [el.rstrip() for el in file_list]
        except IOError:
            print("Такого файла нет")
            PATH = input("Введите путь к файлу: ")
        else:
            return file_list


def getListData(file_list):
    data = []
    data.append([ datetime.datetime.strptime(el[:el.find(':')], "%m-%d-%Y") for el in file_list]) # здесь будет находиться данные даты
    data.append([float(el[el.find(':') + 1:]) for el in file_list]) # здесь будет находиться данные цены за эту дату
    return data

# суть в том, что я должен отделить месяц и год в одну сторону это скорее всего достигну благодаря двойному срезу
# я буду смотреть количество дней между двумя датами начало firstMonth и начало secondMonth каждый месяц первое число...
# в итоге нашел количество дней в месяце / 7 и запелил в функцию round()
# параллельно пока я исал количество дней я пытаюсь найти и сумму за этот период
def getmidPriceMonth(data):
    date = [[data[0][0].month], [data[0][0].year], [data[0][0].day]] # храняться данные о дате в которой изменяется месяц
    summ = [0]
    index = 0
    for i in range(len(data[0])):
        if data[0][i].month  == data[0][i - 1].month or i == 0:
            summ[index] += data[1][i]
        else:
            index += 1
            summ.append(0)
            date[0].append(data[0][i].month)
            date[1].append(data[0][i].year)
            date[2].append(data[0][i].day)
    delta = []
    for  i in range(1, len(date[0])):
        firstMonth  = datetime.date(day = date[2][i - 1], month = date[0][i - 1], year = date[1][i - 1])
        secondMonth = datetime.date(day = date[2][i], month = date[0][i], year = date[1][i])
        delta.append((secondMonth - firstMonth).days / 7)
    # снизу в переменных храняться числа, в которых заключается последняя запись даты, когда изменился месяц
    oldYear = date[1][-1]
    oldMonth = date[0][-1]
    oldDay = date[2][-1]
    # возьмем последнюю запись в файле
    secondMonth = data[0][-1]
    firstMonth  = datetime.datetime(day = oldDay, month = oldMonth, year = oldYear)
    delta.append((secondMonth - firstMonth).days / 7)
    midPrice = [summ[i] /delta[i] for i in range(len(summ))]
    return [round(el, 3) for el in midPrice], date

def getmidPriceYear(data):
    summ = [0]
    index = 0 # длина и индекс, -1 потому что когда счет начинается он попадает в else  и ему прибавляется +1 = 0
    weeks = [0]
    years = [data[0][0].year]
    for i in range(len(data[0])):
        if data[0][i].year == data[0][i - 1].year or index == 0:
            summ[index] += data[1][i]
            weeks[index] += 1
        else:
            summ.append(0)
            weeks.append(0)
            index += 1
            years.append(data[0][i].year)
    return [round(summ[i]/weeks[i], 2) for i in range(index + 1)], years

def PrintMidPriceYears(midPr, years):
    print("Средняя цена за год: ")
    for i in range(len(years)):
        print(f"{years[i]} : {midPr[i]}")

def PrintMidPriceMonths(midPr, date):
    print("Средняя цена за месяц: ")
    for i in range(len(midPr)):
        print(f"{date[0][i]}-{date[1][i]} : {midPr[i]}")


def main():
    data = getListData(ReadFile())
    mid_price, years = getmidPriceYear(data)
    PrintMidPriceYears(mid_price, years)
    mid_price, months = getmidPriceMonth(data)
    PrintMidPriceMonths(mid_price, months)

if __name__ == "__main__":
    main()