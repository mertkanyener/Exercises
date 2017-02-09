def palindrome(a):
    if a == a[::-1]:
        print(a + " is palindrome")
    else:
        print(a + " is not palindrome")

a = "madam"
b = "mertkan"

palindrome(a)
palindrome(b)
