with open('day4.txt') as f:
    lines = [line.rstrip() for line in f]

total_points = 0
cards = []
for line in lines:
    winning_numbers, my_numbers = line.split(" | ")
    card = winning_numbers.split(": ")[0].replace("Card ", "").strip()
    card = int(card)
    # cards.append(card)
    winning_numbers = winning_numbers.split(": ")[1].strip().replace("  ", " ")
    winning_numbers = [eval(i) for i in winning_numbers.split(" ")]

    my_numbers = my_numbers.replace("  ", " ").strip().split(" ")
    my_numbers = [eval(i) for i in my_numbers]

    points = []
    for wn in winning_numbers:
        if wn in my_numbers:
            points.append(wn)

    if len(points) > 0:
        for x in range(card + 1, card + len(points) + 1):
            print(x)
            cards.append(x)
    print("-"*10)
print(cards)

print(total_points)
