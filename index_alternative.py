value = input("Enter a string: ")
letter = input("Enter a letter: ")
position = -1

for i in range(len(value)):
    if value[i] == letter:
        position = i
        break