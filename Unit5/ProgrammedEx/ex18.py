# С писок просты х чисел. Это упражнение предполагает, что вы уже написали функцию
# is prime в упражнении 17. Напишите еще одну программу, которая показывает все про­
# стые числа от 1 до 100. В программе должен быть цикл, который вызывает функцию
# is_prime.
import ex17

SIZE = 100

def main():
    for counter in range(1, SIZE):
        if ex17.is_prime(counter):
            print(counter, end=" ")

if  __name__ == "__main__":
    main()