def draw(size):
    i = 0
    while i <= size:
        s1_1 = " ---"
        s2_1 = "|   "
        s1 = ""
        s2 = ""
        for j in range(size):
            s1 += s1_1
        print(s1)
        if i < size:
            for k in range(size + 1):
                s2 += s2_1
            print(s2)
        i += 1


draw(3)
