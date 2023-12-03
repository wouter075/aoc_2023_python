with open('day3.txt') as f:
    lines = [line.rstrip() for line in f]

symbols = "*!@#$%&*/=-"

symbol_loc = []

for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] in symbols:
            symbol_loc.append([row, col])

for row, col in symbol_loc:
    if lines[row - 1][col].isnumeric():
        print(row - 1, col)
    if lines[row + 1][col].isnumeric():
        print(row + 1, col)
    if lines[row][col - 1].isnumeric():
        print(row, col - 1)
    if lines[row][col + 1].isnumeric():
        print(row, col + 1)
    if lines[row - 1][col - 1].isnumeric():
        print(row - 1, col - 1)
    if lines[row - 1][col + 1].isnumeric():
        print(row - 1, col + 1)
    if lines[row + 1][col - 1].isnumeric():
        print(row + 1, col - 1)
    if lines[row + 1][col + 1].isnumeric():
        print(row + 1, col + 1)
