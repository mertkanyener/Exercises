def no_duplicate_one(l):
    temp_l = set(l)
    result = list(temp_l)
    return result

a = ['aa', 'bb', 'aa']
print(no_duplicate_one(a))


def no_duplicate_two(l):
    result = []
    for i in l:
        if i not in result:
            result.append(i)
    return result

print(no_duplicate_two(a))


