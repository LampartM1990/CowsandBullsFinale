# projekt_2.py: druhý projekt do Engeto Online Python Akademie
#
# Autor: Martin Lampart
# email: westn.m01@gmail.com

# Popis: Hra Bulls & Cows
import random
separator = "-" * 50

def welcome():
    """Pomocí této funkce program přivítá uživatele
    a vypíše mu pravidla hry."""
    print("Hello, welcome to the game Bulls and Cows!")
    print(separator)
    print("I ve generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    print(separator)

def generate_secret_number():
    """Tato funkce generuje náhodné 4 místné
    číslo které je v rozsahu 1 - 9 a nezačíná nulou."""
    numbers = []

    number = random.randint(1, 9)
    numbers.append(number)

    while len(numbers) < 4:
        number = random.randint(0, 9)
        if number not in numbers:
            numbers.append(number)

    return numbers

def get_bulls_and_cows(number, keys):
    """Tady v této funkci si porovnáváme pomocí
    cyklu for nahodně generované číslo z číslem zadaným
    od uživatele."""
    bulls = 0
    cows = 0

    for i in range(0, len(number)):
        if int(keys[i]) == (number[i]):
            bulls += 1

    for i in range(len(keys)):
        if int(keys[i]) in (number):
            cows += 1
    return bulls, cows


def main():
    """Pomocí funkce main se spouští celý program.
    V těle programu je cyklus while ve kterém program běží
    a pomocí podmínek pomůže uživateli uhodnout vygenerovane číslo"""
    welcome()
    number = generate_secret_number()
    print(number)

    while True:
        keys = input(">>> ")

        if len(keys) < 4 or len(keys) > 4:
            print("Wrong number. Try again.")
            break
        elif keys.isnumeric() == False:
            print("You did not enter the number. Try again.")
            continue
        elif len(number) != len(set(keys)):
            print("Number is duplicited. Try again.")
            continue
        elif keys[0] == "0":
            print("Number not start with 0. Try again.")
            continue
        else:
            bulls, cows = get_bulls_and_cows(number, keys)
            bull_word = "bull" if bulls == 1 else "bulls"
            cow_word = "cow" if cows == 1 else "cows"
            line = "-" * 50
            print(f"{bulls} {bull_word}, {cows} {cow_word}\n{line}")

        if bulls == 4:
            print("You won!")
            break


if __name__ == "__main__":
    main()
