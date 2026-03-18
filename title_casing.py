value = input("Enter a string: ")
result = ''
new_word = True

for char in value:
    if char == ' ':
        result  += char
        new_word =  True