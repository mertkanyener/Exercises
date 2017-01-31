def findDivisors(n):
    divisors = []
    i = 2
    while i < n:
        if n%i == 0:
            divisors.append(i)
        i += 1
    return divisors


n = int(input("Please enter the number:"))
print(findDivisors(n))
