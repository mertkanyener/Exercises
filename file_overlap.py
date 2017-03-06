def read(file):
    result = []
    with open(file, 'r') as open_file:
        lines = open_file.read().splitlines()
        for line in lines:
            result.append(int(line))
    return result


def overlapping(list_one, list_two):
    result = []
    for i in list_one:
        if i in list_two:
            result.append(i)
    return result


l = overlapping(read('primenumbers.txt'), read('happynumbers.txt'))
print(l)

