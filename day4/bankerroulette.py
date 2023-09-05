import random

names = ["Colin", "Alex", "Ben", "Tyler", "Jeremy", "Alijah", "Nick"]

randint = random.randint(0,len(names)-1)

print(randint)
print(f"Chosen to pay: {names[randint]}")