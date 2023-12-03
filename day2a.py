with open('day2.txt') as f:
    lines = [line.rstrip() for line in f]


game_sum = 0
for line in lines:
    game, temp = line.replace("Game ", "").split(": ")
    sets = temp.split("; ")

    game_check = True
    for game_set in sets:
        cubes = game_set.split(", ")
        tmp = []

        for cube in cubes:
            amount, color = cube.split(" ")
            amount = int(amount)

            if color == "red" and amount > 12:
                game_check = False
            if color == "green" and amount > 13:
                game_check = False
            if color == "blue" and amount > 14:
                game_check = False
    if game_check:
        game_sum += int(game)

print(game_sum)




