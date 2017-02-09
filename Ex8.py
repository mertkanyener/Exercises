#rock_paper_scissors
def game():
    usr_one =""
    usr_two =""
    while usr_one != "no" or usr_two != "no":
        usr_one = input("Rock, Paper, or Scissors?")
        usr_two = input("Rock, Paper, or Scissors?")
        if usr_one == usr_two:
            print("Draw")


def helper(usr_one, usr_two):
    if usr_one == "Rock" and usr_two == "Scissors":
        print("User one wins!")
    elif usr_one == "Scissors" and usr_two == "Rock":
        print("User two wins!")
    elif usr_one == "Paper" and usr_two == "Scissors":
