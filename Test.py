import random, string


chars = string.digits
a = "".join(random.choice(chars) for _ in range(4))
print(a)


