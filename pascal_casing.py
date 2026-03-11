full_name = input('Enter a full name: ')
full_name = full_name.split()
pascal_full_name = ''

for words in full_name:
    pascal_full_name += words.capitalize()

print(pascal_full_name)