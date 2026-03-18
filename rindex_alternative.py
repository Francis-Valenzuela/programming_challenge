value = input("Enter a String:")
letter =  input("Enter a Letter:")
position = -1

for i in range(len(value)-1, -1, -1):
    if value[i] == letter:
        position = i
        break
print(position)