num = int(input("Enter a number (0-1000): "))
while 0 > num or num > 1000:
    num = int(input("Enter a number (0-1000): "))
formatted_num = f"{num:06d}"
print(formatted_num)