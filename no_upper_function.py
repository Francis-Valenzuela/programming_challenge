value = input("Enter a string: ")
result = ''

for char in value:
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)