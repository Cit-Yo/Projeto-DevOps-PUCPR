import random

num = random.randint(1,3)

print (num)
if num == 1:
    rand = "Person!"
elif num == 2:
    rand = "Mister!"
else:
    rand = "Madam!"

print("Hello, "+ rand)