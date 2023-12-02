def is_valid_game(game_str, cubes):
    for pair in game.split(","):
        qty, color = pair.strip().split()
        cubes[color] -= int(qty)
        if cubes[color] < 0:
            return False

    return True


total_ids = 0
with open("input/input.txt", "r") as file:
    for line in file:
        game_id_str, details = line.split(":", 1)
        game_id = int(game_id_str.split()[-1])
        games = details.split(";")

        valid = True
        for game in games:
            valid &= is_valid_game(game, {"red": 12, "green": 13, "blue": 14})

        if valid:
            total_ids += game_id

print(total_ids)
