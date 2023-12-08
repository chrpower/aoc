from collections import Counter

letter_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

rank_patterns = {
    (5,): 6,
    (1, 4): 5,
    (2, 3): 4,
    (1, 1, 3): 3,
    (1, 2, 2): 2,
    (1, 1, 1, 2): 1,
    (1, 1, 1, 1, 1): 0,
}


def strength(hand):
    card_counts = Counter(hand)
    sorted_counts = sorted(card_counts.values())

    return (
        rank_patterns.get(tuple(sorted_counts), 0),
        [letter_map.get(char, char) for char in hand],
    )


with open("input/input.txt", "r") as file:
    plays = [tuple(line.strip().split(" ")) for line in file]
    plays.sort(key=lambda play: strength(play[0]))
    print(sum(rank * int(bid) for rank, (_, bid) in enumerate(plays, 1)))
