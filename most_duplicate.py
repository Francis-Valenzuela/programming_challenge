nums =[]

while True:
    value = input("Enter a number: ")
    if not value.isdigit():
        break
    nums.append(int(value))

if nums:
    print(max(set(nums), key=nums.count))
else:
    print("No numbers")