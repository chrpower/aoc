with open("input/input.txt", "r") as file:
    sections = file.read().split("\n\n")

    inputs = list(map(int, sections[0].split(":")[1].split()))
    seeds = []
    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

    for section in sections[1:]:
        ranges = [list(map(int, line.split())) for line in section.splitlines()[1:]]

        new = []
        while seeds:
            seed_start, seed_end = seeds.pop()
            for dest_start, source_start, range_length in ranges:
                os = max(seed_start, source_start)
                oe = min(seed_end, source_start + range_length)
                if os < oe:
                    new.append(
                        (os - source_start + dest_start, oe - source_start + dest_start)
                    )
                    if os > seed_start:
                        seeds.append((seed_start, os))
                    if seed_end > oe:
                        seeds.append((oe, seed_end))
                    break
            else:
                new.append((seed_start, seed_end))
        seeds = new

    print(min(seeds)[0])
