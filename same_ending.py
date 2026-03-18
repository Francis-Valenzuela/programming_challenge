value = input("Enter a statement:").lower
ending = input("Enter ending:").lower

if value[-len(ending):] == ending:
    print(True)
else:
    print(False)