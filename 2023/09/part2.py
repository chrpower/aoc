def predict(seq):
    if sum(seq) == 0:
        return 0
    return seq[-1] + predict([y - x for x, y in zip(seq, seq[1:])])


with open("input/input.txt", "r") as file:
    print(sum(predict(list(map(int, line.split()))[::-1]) for line in file))
