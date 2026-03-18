value = input("Enter a statement:")
ending = input("Enter ending:")

if value[-len(ending):] == ending:
    print(True)
else:
    print(False)