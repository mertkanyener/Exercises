def reverse_string():
    input_str = input("Please enter a string containing multiple words: ")
    input_str = input_str.split()
    result = []
    i = len(input_str) - 1
    while i >= 0:
        result.append(input_str[i])
        i -= 1
    result = " ".join(result)
    return result

print(reverse_string())


