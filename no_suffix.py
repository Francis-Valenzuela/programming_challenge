value = input("Enter a String: ")
suffix = input("Enter a Suffix: ")

if value[-len(suffix):] == suffix:
    print(value[:-len(suffix)])
else:
    print(value)