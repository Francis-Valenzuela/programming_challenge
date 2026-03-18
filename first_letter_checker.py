value = input("Enter a string: ")
start = input("Enter a start: ")

if value[:len(start)] == start:
    print(True)
else:
    print(False)