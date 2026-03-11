#2. Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
num_1,num_2 = map(float, input("Enter two Numbers:"),split())
print('Equal' if num_1 == num_2 else 'Not Equal')
