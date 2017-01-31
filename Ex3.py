def filterList(L):
    result = []
    number = int(input("Please enter the number: "))
    for x in L:
        if x < number:
            result.append(x)
    return result

def main():
    a = [1,1,2,3,5,8,13,21,34,55,89]
    print(filterList(a))

main()