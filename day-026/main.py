# List Comprehension
# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

# Conditional List Comprehension
# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Eleanor", "Dave", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
