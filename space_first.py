value = input("Enter a string: ")
length = int(input("Enter a number: "))

while len(value) < length:
    value += " " + value

print(value)