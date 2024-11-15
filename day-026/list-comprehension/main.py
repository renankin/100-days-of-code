import random

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

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

student_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in
                   student_scores.items() if score > 50}
print(student_scores)
print(passed_students)
