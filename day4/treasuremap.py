row1 = ["_","_","_"]
row2 = ["_","_","_"]
row3 = ["_","_","_"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where to put treasure?: ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical-1][horizontal-1] = "X"

print(f"{row1}\n{row2}\n{row3}")