with open("input/input.txt", "r") as file:
    sections = file.read().split("\n\n")

    seeds = list(map(int, sections[0].split(":")[1].split()))

    for section in sections[1:]:
        ranges = [list(map(int, line.split())) for line in section.splitlines()[1:]]
        new = []
        for s in seeds:
            for dest_start, source_start, range_length in ranges:
                if s in range(source_start, source_start + range_length):
                    new.append(s - source_start + dest_start)
                    break
            else:
                new.append(s)
        seeds = new

    print(min(seeds))
