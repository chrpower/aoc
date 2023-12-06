with open("input/input.txt", "r") as file:
    time, dist = (int("".join(line.split(":")[1].split())) for line in file)
    print(sum(1 for i in range(time) if (time - i) * i > dist))
