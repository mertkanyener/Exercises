#List comprehension exercise
def evenFilter(a):
    result = [i for i in a if i%2 == 0]
    return result

a = [i for i in range(0,51,3)]
print(a)
result = evenFilter(a)
print(result)