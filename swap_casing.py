value = input("Enter a string: ")
result =  ''

for char in value:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)