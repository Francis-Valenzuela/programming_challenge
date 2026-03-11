sorted_numbers = []
while True:
    num = input("Enter a number: ")

    if not num.isdigit():
        break
    num = int(num)
    sorted_numbers.append(num)
sorted_numbers.sort(reverse=True)
print(sorted_numbers)