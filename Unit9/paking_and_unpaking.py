def summ(*args):
    summ = 0
    for el in args:
        summ += el
    return summ

def person_info(name, age, city, **kwargs):
    info = {"NAME": name, "AGE": age, "CITY": city}
    return {1:info, 2:kwargs}

def creat_dict(**kwargs):
    return kwargs

def task1():
    numbers = (1, 2, 3, 4, 5)
    print(summ(*numbers))

def task2():
    print(person_info("Ranil", "19", "MOSCOW", **{"NAME":"NAIL", "AGE": 14, "CITY": "KAZAN"}))

def task3():
    my_dict = creat_dict(name = "РАНИЛЬ", age = 19, city = "MOSKOW")
    print(my_dict)

if __name__ == "__main__":
    task1()
    task2()
    task3()