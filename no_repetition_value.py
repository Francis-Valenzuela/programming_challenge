numbers = []

for num in range(10):
    num = int(input('Enter a number: '))
    numbers.append(num)

for num in set(numbers):
    print(num, end=' ')
