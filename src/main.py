print("Select you gender (M = Male F = Female):")
x = input()

if x == "M":
    gender = "Mister!"
elif x == "F":
    gender = "Madam!"
else:
    print("Invalid input.")

print("Hello, " + gender)
print("Vamos ver se funciona")