numbers = []

while True:
    num = int(input('Enter a number: '))

    if num in numbers:
        print('Duplicate number')
    else:
        print('Unique number')
        numbers.append(num)

