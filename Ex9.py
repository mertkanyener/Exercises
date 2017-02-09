#Guessing game
import random

guess = ""
while True:
    print('Type "exit" if you do not want to play')
    guess = input("What's your guess?")
    number = random.randrange(1,10)
    if guess == "exit":
        print("Goodbye!")
        break
    guess = int(guess)
    if guess == number:
        print("Correct!")
    elif guess < number:
        print("Your guess is lower")
    elif guess > number:
        print("Your guess is higher")
    else:
        print("Wrong type of input")

