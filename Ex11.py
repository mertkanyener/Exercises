def isPrime(n):
    prime = True
    if n < 2:
        prime = False
    elif n == 2:
        prime = True
    else:
        i = 2
        while i < n/2 + 1:
            if n%i == 0:
                prime = False
                break
            else:
                i += 1
    return prime

print(isPrime(5))
print(isPrime(11))
print(isPrime(119))
