import random

def intersect(a, b):
    result = []
    init_result = [i for i in a if i in b]
    for i in init_result:
        if i not in result:
            result.append(i)
    return result

a = [random.randrange(1, 10) for i in range(20)]
b = [random.randrange(1, 10) for i in range(20)]
print(a)
print(b)
print(intersect(a, b))
