numbers = []

while True:
    num = input('Enter a number: ')

    if not num.isdigit():
        break
    
    if num in numbers:
        print('Duplicate number')
    else:
        print('Unique number')
        numbers.append(num)

