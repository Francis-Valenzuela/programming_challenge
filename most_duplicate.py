nums =[]

while True:
    value = input("Enter a number: ")
    if not value.isdigit():
        break
    nums.append(int(value))

    