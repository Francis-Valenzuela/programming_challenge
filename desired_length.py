value = input("Enter a String: ")
length = int(input("Enter a Number: "))

while len(value) < length:
    value += "_"
print(value)