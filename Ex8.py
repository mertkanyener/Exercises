#rock_paper_scissors
def game():
    while True:
        usr_one = input("Rock, Paper, or Scissors?")
        usr_two = input("Rock, Paper, or Scissors?")
        if usr_one == usr_two:
            print("Draw")
        else:
            helper(usr_one, usr_two)
            usr_one = input("User 1, do you want to play again?")
            usr_two = input("User 2, do you want to play again?")
            if usr_one == "no" or usr_two == "no":
                print("Goodbye!")
                break
            elif usr_one == "yes" and usr_two == "yes":
                game()
            else:
                print("Error!")
                break

def helper(usr_one, usr_two):
    if usr_one == "Rock" and usr_two == "Scissors":
        print("User one wins!")
    elif usr_one == "Scissors" and usr_two == "Rock":
        print("User two wins!")
    elif usr_one == "Paper" and usr_two == "Rock":
        print("User one wins!")
    elif usr_one == "Rock" and usr_two == "Paper":
        print("User two wins")
    elif usr_one == "Scissors" and usr_two == "Paper":
        print("User one wins")
    elif usr_one == "Paper" and usr_two == "Scissors":
        print("User two wins!")
    else:
        print("Something went wrong!")

game()