value = input("Enter a String:")
prefix  = input("Enter a Prefix:")

if value[:len(prefix)] == prefix:
    print(value[len(prefix):])
else:
    print(value)