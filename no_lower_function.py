value = input("Enter anything:")
result = ''

for character in value:
    if "A" <= character <= "Z":
        result += chr(ord(character) + 32)