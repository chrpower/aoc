with open("input/input.txt", "r") as file:
    time, dist = (list(map(int, line.split(":")[1].split())) for line in file)

    combs = 1
    for t, d in zip(time, dist):
        combs *= sum(1 for i in range(t) if (t - i) * i > d)
    print(combs)
