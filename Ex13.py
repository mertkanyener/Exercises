def fibonacci(n):
    result = [1, 1]
    if n < 1:
        print("Wrong input!")
    elif n == 1:
        result = [1]
    elif n == 2:
        result = [1, 1]
    else:
        i = 1
        while i < n-1:
            new = result[i-1] + result[i]
            result.append(new)
            i += 1
    return result

print(fibonacci(8))


