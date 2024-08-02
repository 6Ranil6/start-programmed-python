# нужно реализовать файловую систему таким образом, чтобы я мог вносить данные в файл и покзывать эти данные изменять и удалять
# пусть объектом будем машина со свойствами: макс. скорость, и цвет машины
import os
class Car:
    speed = None
    color = None

def main():
    PathFile = "Data_about_Cars"
    AddDataInFile(PathFile)
    PrintInfornation(PathFile)
    ChangedData(PathFile)
    DeleateData(PathFile)
def AddDataInFile(nameFile):
    outfile = open(nameFile, 'a')
    countCar = int(input("Введите количество машин: "))
    for counter in range(countCar):    
        objectCar = Car()
        objectCar.speed = float(input("Введите максимальную скорость этой машины: "))
        objectCar.color = input("Введите цвет этой машины: ")
        outfile.write(f"{objectCar.speed}\n")
        outfile.write(f"{objectCar.color}\n")
        outfile.write('-' * 20 + '\n')
    outfile.close()    

def PrintInfornation(nameFile):
    infile = open(nameFile, 'r')
    print("\nВаши данные:\n")
    speed = infile.readline()
    while speed != "":
        color = infile.readline()
        space = infile.readline()
        print(f"Максимальная скорость: {speed:<}")
        print(f"Цвет: {color:<}")
        speed = infile.readline()

    infile.close()

def ChangedData(nameFile):
    print("Введите показатели той машины, которую Вы хотели бы изменить:")
    searchSpeed = input("Введите максимальную скорость: ")
    searchColor = input("Введите цвет: ")
    key = False
    #создаю два файловых переменных: 1 - где данные 2 - куда эти данные записываются
    #потом переписываю данные пока не найдут совпавшиеся данные
    infile = open(nameFile, 'r')
    outfile = open("temp", 'w')

    inSpeed = infile.readline()
    while inSpeed != "":
        inColor = infile.readline()
        space = infile.readline()
        if float(inSpeed) == float(searchSpeed) and inColor.rstrip() == searchColor:
            print("Введите новые данные: ")
            objectCar = Car()
            objectCar.speed = input("Введите скорость: ")
            objectCar.color = input("Введите цвет: ")
            key = True
            outfile.write(str(float(objectCar.speed)) + "\n")
            outfile.write((objectCar.color) + "\n")
            outfile.write(space)
        else:
            outfile.write(inSpeed)
            outfile.write(inColor)
            outfile.write(space)
        inSpeed = infile.readline()
    if not key:
        print("Не нашли данные, которые надо было изменить")
    else:
        print("Все прошло успешно!!!")
       
    outfile.close()
    infile.close()
    os.remove(nameFile)
    os.rename("temp", nameFile)

def DeleateData(nameFile):
    print("Введите показатели той машины, которую Вы хотели бы удалить:")
    searchSpeed = input("Введите максимальную скорость: ")
    searchColor = input("Введите цвет: ")
    key = False
    #создаю два файловых переменных: 1 - где данные 2 - куда эти данные записываются
    #потом переписываю данные пока не найдут совпавшиеся данные
    infile = open(nameFile, 'r')
    outfile = open("temp", 'w')

    inSpeed = infile.readline()
    while inSpeed != "":
        inColor = infile.readline()
        space = infile.readline()
        if float(inSpeed) == float(searchSpeed) and inColor.rstrip() == searchColor:
            key = True
        else:
            outfile.write(inSpeed)
            outfile.write(inColor)
            outfile.write(space)
        inSpeed = infile.readline()
    if not key:
        print("Не нашли данные, которые надо было изменить")
    else:
        print("Все прошло успешно!!!")
       
    outfile.close()
    infile.close()
    os.remove(nameFile)
    os.rename("temp", nameFile)
if __name__ == "__main__":
    main()