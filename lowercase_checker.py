value = input("Enter a string: ")
is_lower = True

for char in value:
    if 'A' <= char <= 'Z':
        is_lowercase = False
        break
print(is_lower)