import random

class Coin:
    def __init__(self):
        self.__sideup = "Орел"
    
    def tose(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Орел"
        else:
            self.__sideup = "Решка"

    def get_sideup(self):
        return self.__sideup
    
def main():
    coin1 = Coin()
    print(coin1.get_sideup())
    coin1.tose()
    print(coin1.get_sideup())

if __name__ == "__main__":
    main()