size = input("What size pizza?: ")
add_pepp = input("Do you want pepperoni?: ")
extra_cheese = input("Do you want extra cheese?: ")

total = 0

if size == "S":
    total += 15
    if add_pepp == "Y":
        total += 2
        if extra_cheese == "Y":
            total += 1
elif size == "M":
    total += 20
    if add_pepp == "Y":
        total += 3
        if extra_cheese == "Y":
            total += 1
elif size == "L":
    total += 25
    if add_pepp == "Y":
        total += 3
        if extra_cheese == "Y":
            total += 1
print(total)

# if size == "S":
#     total += 15
# elif size == "M":
#     total += 20
# else:
#     total += 25
#
# if add_pepp == "Y":
#     if size == "S":
#         total += 2
#     else:
#         total += 3
# if extra_cheese == "Y":
#     total += 1
# print(total)