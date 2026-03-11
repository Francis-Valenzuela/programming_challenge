total = 0
count = 0
while True:
    num = input("Enter a number: ")

    if not num.isdigit():
        break
    num = int(num)
    total += num
    count += 1

