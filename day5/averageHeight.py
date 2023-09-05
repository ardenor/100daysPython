student_heights = [180, 124, 165, 173, 189, 169, 146]
total = 0

for height in student_heights:
    total += height

print(round(total / len(student_heights)))