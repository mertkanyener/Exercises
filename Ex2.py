def oddEvenCheck():
    number = int(input("Please enter a number"))
    if number%2 == 0:
        print(str(number) +" is an even number.")
        if number%4 == 0:
            print(" and it is divisible by four.")
    else:
        print(str(number) + " is an odd number.")


def divisibleCheck():
    num = int(input("Please enter the number to be divided"))
    check = int(input("Please enter the check number"))
    if num%check == 0:
        result = num/check
        print(str(num) + " is divisible by " + str(check) + ".")
        print("Result: " + str(result))
    else:
        print(str(num) + " is NOT divisible by " + str(check) + ".")

def main():
    choice = input("Please enter '1' for odd-even check, '2' for divisible check")
    if choice == "1":
        oddEvenCheck()
    elif choice == "2":
        divisibleCheck()
    else:
        print("Invalid choice. System exit")

main()