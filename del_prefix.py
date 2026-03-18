value = input("Enter a String:")
prefix  = input("Enter a Prefix:")

if value[:len(prefix)] == prefix:
    print("Prefix Match")