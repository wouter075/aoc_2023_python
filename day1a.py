with open('day1.txt') as f:
    lines = [line.rstrip() for line in f]

cv_total = 0
for line in lines:
    cv = [int(c) for c in line if c.isdigit()]
    if len(cv) > 1:
        cv_total += int(f'{cv[0]}{cv[-1]}')
    if len(cv) == 1:
        cv_total += int(f'{cv[0]}{cv[0]}')

print(cv_total)
