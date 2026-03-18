value = input("Enter string:")
length = int(input("Enter length:"))

spaces = length - len(value)
left_space = spaces // 2
right_space = spaces - left_space

print("_" * left_space + value + "_" * right_space)