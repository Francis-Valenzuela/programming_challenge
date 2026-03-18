value = input("Enter a word: ")
i = len(value) - 1

while i >= 0 and value[i] == " ":
    i -= 1
print(value[:i+1])