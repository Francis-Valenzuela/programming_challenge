numbers = None
while True:
    num = int(input('Enter a number: '))
    if numbers is None or num < numbers:
        lowest = num
print(lowest)

