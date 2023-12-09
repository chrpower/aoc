import itertools

with open("input/input.txt", "r") as file:
    steps, _, *rest = file.read().splitlines()

    moves = {}
    for line in rest:
        key, value = line.split(" = ")
        moves[key] = value[1:-1].split(", ")

    path_length = 0
    current = "AAA"
    for step in itertools.cycle(steps):
        if current == ("ZZZ"):
            break

        current = moves[current][0 if step[0] == "L" else 1]
        path_length += 1

    print(path_length)
