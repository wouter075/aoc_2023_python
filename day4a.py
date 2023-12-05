with open('day4.txt') as f:
    lines = [line.rstrip() for line in f]

total_points = 0
for line in lines:
    winning_numbers, my_numbers = line.split(" | ")
    winning_numbers = winning_numbers.split(": ")[1].strip().replace("  ", " ")
    winning_numbers = [eval(i) for i in winning_numbers.split(" ")]

    my_numbers = my_numbers.replace("  ", " ").strip().split(" ")
    my_numbers = [eval(i) for i in my_numbers]

    points = []
    for wn in winning_numbers:
        if wn in my_numbers:
            points.append(wn)

    p = 0
    if len(points) > 0:
        p = 1
        for _ in range(len(points) - 1):
            p += p
        total_points += p

print(total_points)
