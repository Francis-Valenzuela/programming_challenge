highest = None

while True:
    num = input('Enter a number: ')

    if not num.isdigit():
        break
    num = int(num)

    if highest is None or num > highest:
        highest = num
print(highest)




