with open('day3.txt') as f:
    lines = [line.rstrip() for line in f]

# find all the numbers
numbers = []
sum_numbers = []
symbols = []

for line in lines:
    number = ""
    for x in range(len(line)):
        if line[x].isnumeric():
            number += line[x]
        if line[x] == "." and number:
            numbers.append(int(number))
            number = ""
        if line[x] != "." and not line[x].isnumeric():
            symbols.append(line[x])
    if number:
        numbers.append(int(number))

# print(symbols)
sum_numbers = numbers
# check for symbol
# print(numbers)
for number in numbers:
    for row in range(len(lines)):
        pos = lines[row].find(str(number))

        if pos >= 0:
            # found, now check in the prev row and next row if a symbol is there:
            # print(number)
            # [pos - 1:pos + len(str(number)) + 1]
            # if row + 1 < len(lines):
            # print(lines[row + 1])
            if pos == 0:
                start = 0
            else:
                start = pos - 1

            print(number)
            # next row
            pop = True
            if row + 1 < len(lines):
                print(lines[row + 1][start: pos + len(str(number)) + 1].replace(".", ""))
                if lines[row + 1][start: pos + len(str(number)) + 1].replace(".", "") in symbols:
                    pop = False

            # prev row
            if row - 1 > 0:
                print(lines[row - 1][start: pos + len(str(number)) + 1].replace(".", ""))
                if lines[row - 1][start: pos + len(str(number)) + 1].replace(".", "") in symbols:
                    pop = False

            # now the current row
            current_row = lines[row][start: pos + len(str(number)) + 1].replace(".", "")
            current_row = ''.join((x for x in current_row if not x.isdigit()))
            print(current_row)
            if current_row in symbols:
                pop = False

            print("-"*10)
            print(pop)
            if pop:
                sum_numbers.remove(number)
                continue

print(sum(sum_numbers))
