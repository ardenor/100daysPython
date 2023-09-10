numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Colin"
new_list = [letter for letter in name]
print(new_list)

rng = range(1,5)
new_rng = [num * 2 for num in rng]
print(new_rng)

names = ["Colin", "Ben", "Alex", "Leah"]
short_names = [name.upper() for name in names if len(name) <= 4]
print(short_names)