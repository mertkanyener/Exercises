import random

def intersect(A,B):
    result = []
    for x in A:
        if x in B and x not in result:
            result.append(x)
    return result

#Creates a random list of integers
def randList(lower, upper, length):
    result = [random.randrange(lower,upper+1) for i in range(length)]
    return result

def test():
    a = randList(0, 50, 20)
    b = randList(0, 50, 20)
    print("a = " + str(a))
    print("b = " + str(b))
    print(intersect(a, b))

test()



