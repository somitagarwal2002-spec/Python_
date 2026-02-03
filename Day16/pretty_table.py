from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon",["pikachu", "squirtle", "charmander"])
table.add_column("type", ["electric", "water", "fire"])

print(table)

table.align = "l"
print(table)
