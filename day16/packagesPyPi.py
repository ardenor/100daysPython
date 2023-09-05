#import prettytable
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ["Pikachu"])
table.add_column("Type", ["Electric"])
table.align = "l"
print(table)