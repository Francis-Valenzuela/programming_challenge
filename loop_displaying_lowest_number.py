numbers = None
while True:
    num = input('Enter a number: ')

    if not num.isdigit():
        break

    num = int(num)
    if numbers is None or num < numbers:
        lowest = num
print(lowest)


