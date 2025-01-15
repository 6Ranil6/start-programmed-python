expression = input().split()

value1 = int(expression[0])
operator = expression[1]
value2 = float(expression[2])

if operator == "/" and value2 == 0:
    print("Деление на ноль невозможно.")
else:
    if operator == "+":
        result = value1 + value2
    elif operator == "-":
        result = value1 - value2
    elif operator == "*":
        result = value1 * value2
    elif operator == "/":
        result = value1 / value2
    elif operator == "%":
        result = value1 % value2
    else:
        print("Неверная операция.")
        exit()
    result = round(result, 2)
    print(f"Результат: {result:}")