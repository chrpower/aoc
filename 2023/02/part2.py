def tally_cubes(game_str, cubes):
    for pair in game_str.split(","):
        qty, color = pair.strip().split()
        cubes[color] += int(qty)
    return cubes


total_pwr = 0
with open("input/input.txt", "r") as file:
    for line in file:
        _, details = line.split(":", 1)
        games = details.split(";")

        max_cubes = {"red": 0, "green": 0, "blue": 0}
        for game in games:
            curr_cubes = tally_cubes(game, {"red": 0, "green": 0, "blue": 0})
            max_cubes = {
                color: max(max_cubes.get(color, 0), curr_cubes.get(color, 0))
                for color in set(max_cubes).union(curr_cubes)
            }

        pwr = 1
        for val in max_cubes.values():
            pwr *= val

        total_pwr += pwr

print(total_pwr)
