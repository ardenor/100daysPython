import random

names = ["Colin", "Ben", "Alex", "Leah"]



students_scores = {name:random.randint(0,100) for name in names}
print(students_scores)

passed_students = {key:value for (key, value) in students_scores.items() if value > 50}
print(passed_students)

