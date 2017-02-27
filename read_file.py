def read(file):
    names = {}
    with open(file, 'r') as open_file:
        lines = open_file.read().splitlines() #add every line of the file to a list
        for line in lines:
            if line in names:
                names[line] += 1
            else:
                names[line] = 1
    return names


def print_dict(d):
    all_keys = d.keys()
    for key in all_keys:
        print(key + ": " + str(d[key]))

print_dict(read('nameslist.txt'))

