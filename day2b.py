with open('day2.txt') as f:
    lines = [line.rstrip() for line in f]


game_sum = 0

for line in lines:
    game, temp = line.replace("Game ", "").split(": ")
    sets = temp.split("; ")
    red = 0
    green = 0
    blue = 0

    game_check = True
    for game_set in sets:
        cubes = game_set.split(", ")
        tmp = []

        for cube in cubes:
            amount, color = cube.split(" ")
            amount = int(amount)

            if color == "red" and amount > red:
                red = amount
            if color == "green" and amount > green:
                green = amount
            if color == "blue" and amount > blue:
                blue = amount
    if game_check:
        game_sum += (red*green*blue)

print(game_sum)
