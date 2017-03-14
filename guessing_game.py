def game(lower, upper):
    l = [i for i in range(lower, upper + 1)]
    run = True
    count = 1
    while run:
        i = int(len(l)/2)
        guess = l[i]
        answer = input("is it " + str(guess) + "?")
        if answer == "too high":
            count += 1
            l = l[:i]
        elif answer == "too low":
            count += 1
            l = l[i:]
        elif answer == "yes":
            run = False
            print("Guesses: " + str(count))
        else:
            print("I can't understand")


game(0, 100)





