value = input("Enter a string: ")
result = ''
new_word = True

for char in value:
    if char == ' ':
        result  += char
        new_word =  True
    elif new_word and 'a' <= char <= 'z':
        result += chr(ord(char) - 32)
        new_word = False