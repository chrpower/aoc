from math import gcd
import itertools

with open("input/input.txt", "r") as file:
    steps, _, *rest = file.read().splitlines()

    moves = {}
    for line in rest:
        key, value = line.split(" = ")
        moves[key] = value[1:-1].split(", ")

    cycle_lengths = []
    for current in [k for k in moves if k.endswith("A")]:
        step_count = 0
        first_z = 0

        for step in itertools.cycle(steps):
            if current.endswith("Z"):
                if first_z == 0:
                    first_z = step_count
                else:
                    cycle_lengths.append(step_count - first_z)
                    break

            current = moves[current][0 if step[0] == "L" else 1]
            step_count += 1

    lcm = 1
    for cl in cycle_lengths:
        lcm = lcm * cl // gcd(lcm, cl)

    print(lcm)
