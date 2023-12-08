from collections import Counter

letter_map = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}

rank_patterns = {
    (5,): 6,
    (1, 4): 5,
    (2, 3): 4,
    (1, 1, 3): 3,
    (1, 2, 2): 2,
    (1, 1, 1, 2): 1,
    (1, 1, 1, 1, 1): 0,
}


def score(hand):
    card_counts = Counter(hand)
    sorted_counts = sorted(card_counts.values())
    return rank_patterns.get(tuple(sorted_counts))


def replacements(hand):
    if hand == "":
        return [""]

    return [
        x + y
        for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
        for y in replacements(hand[1:])
    ]


def strength(hand):
    return (
        max(map(score, replacements(hand))),
        [letter_map.get(card, card) for card in hand],
    )


with open("input/input.txt", "r") as file:
    plays = [tuple(line.strip().split(" ")) for line in file]
    plays.sort(key=lambda play: strength(play[0]))
    print(sum(rank * int(bid) for rank, (_, bid) in enumerate(plays, 1)))
