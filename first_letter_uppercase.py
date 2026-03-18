value = input("enter a string: ")
result = ""

for i in range(len(value)):
    if i == 0 and 'a' <= value[i] <= 'z':
        result += chr(ord(value[i]) -32 )
    elif 'A' <= value[i] <= 'Z':
        result += chr(ord(value[i]) + 32)
    else:
        result += value[i]
print(result)