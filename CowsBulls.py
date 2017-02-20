import random, string


def cows_bulls(chars=string.digits):
    state = True
    while state:
        number = "".join(random.choice(chars) for _ in range(4))
        guess = input("Please enter your guess")
        if len(guess) < 4:
            print("Error! You must enter a 4-digit number")
        else:
            print("Number: " + number)
            cows = cow_func(guess, number)
            bulls = bull_func(guess, number) - cows
            print(str(cows) + " cows, " + str(bulls) + " bulls")
            if cows == 4:
                print("Congratulations!")
                state = False


def cow_func(guess, number):
    result = 0
    guess = str(guess)
    number = str(number)
    i = 0
    while i < len(number):
        if guess[i] == number[i]:
            result += 1
        i += 1
    return result


def bull_func(guess, number):
    result = 0
    guess = str(guess)
    number = str(number)
    for i in guess:
        if i in number:
            result += 1
    return result



cows_bulls()