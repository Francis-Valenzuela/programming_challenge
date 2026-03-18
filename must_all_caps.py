value = input("Enter a string: ")
is_upper = True

for char in value:
    if 'a' <= char <= 'z':
        is_upper = False
        break
print(is_upper)