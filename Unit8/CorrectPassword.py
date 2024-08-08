# Анализ символов в пароле
# В университете пароли для компьютерной системы кампуса должны удовлетворять приве­
# денным ниже требованиям:
# ♦ пароль должен иметь как минимум семь символов;
# ♦ должен содержать как минимум одну букву в верхнем регистре;
# ♦ должен содержать как минимум одну букву в нижнем регистре;
# ♦ должен содержать как минимум одну цифру.
# Во время создания студентом своего пароля допустимость пароля должна быть проверена,
# чтобы он гарантированно удовлетворял этим требованиям. Вас попросили написать
# программный код, который выполняет эту проверку. Вы решаете написать функцию
# valid password, которая принимает пароль в качестве аргумента и возвращает истину либо
# ложь, чтобы указать, является ли он допустимым. Вот алгоритм функции в псевдокоде:
# функция v a lid _ p a ssw o rd :
# Ранее (в предыдущей рубрике "В центре внимания ") вы создали функцию get login name и
# сохранили ее в модуле login. Поскольку задача функции valid password связана с задачей
# создания учетной записи студента, вы решаете разместить функцию valid password в том
# же модуле login. В программе 8.6 приведен модуль входа в систему login, в который
# добавлена функция valid password. Функция начинается в строке 34.

def get_login():
  
    name = input("Введите имя: ")
    lastname = input("Введите фамилию: ")
    idnumber = input("Введите свой id: ")
    name = name[:3]
    lastname = lastname[:3]
    idnumber = idnumber[-3:]

    return name + lastname + idnumber

def valid_password(password):
    if len(password) > 6:
        keyBigChar = False
        keyLittleChar = False
        keyDigit = False
        for el in password:
            if keyBigChar and keyLittleChar and keyDigit:
                return True
            elif el.isupper():
                keyBigChar = True
            elif el.islower():
                keyLittleChar = True
            elif el.isdigit():
                keyDigit = True
        return False
    else:
        return False

def main():
    login = get_login()
    print(f"Получите свой логин: {login}")
    password = input("Установите пароль: ")
    while not valid_password(password):
        print("Пароль не подходит под условия")
        password = input("Ввелите снова новый пароль: ")
        
if __name__ == "__main__":
    main()