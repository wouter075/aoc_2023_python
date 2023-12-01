with open('day1.txt') as f:
    lines = [line.rstrip() for line in f]

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
nu = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


def to_number(line):
    new_line = ""
    for x in range(len(line)):
        for number in numbers:
            # print(line[x:x+1].isnumeric())
            if line[x:].startswith(number):
                new_line += nu[number]
                x += len(nu[number])
                continue

            if line[x:x+1].isnumeric():
                new_line += line[x:x+1]
                x += 1
                continue

    return new_line


cv_total = 0
for line in lines:
    line = to_number(line)
    cv = [int(c) for c in line if c.isdigit()]
    if len(cv) > 1:
        print(int(f'{cv[0]}{cv[-1]}'))
        cv_total += int(f'{cv[0]}{cv[-1]}')
    if len(cv) == 1:
        print(int(f'{cv[0]}{cv[0]}'))
        cv_total += int(f'{cv[0]}{cv[0]}')

# # 55470 to low
# # 55920 to high
print(cv_total)
