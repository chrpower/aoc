with open("input/input.txt", "r") as file:
    card_wins = {}
    for line in file:
        card_id_str, nums = line.split(":", 1)
        card_id = int(card_id_str.strip().split()[-1])
        card_wins[card_id] = card_wins.get(card_id, 0) + 1

        win_str, player_str = nums.split("|")
        win_nums = {int(num) for num in win_str.strip().split()}
        player_nums = {int(num) for num in player_str.strip().split()}
        match_count = len(win_nums & player_nums)

        for next_id in range(card_id + 1, card_id + match_count + 1):
            card_wins[next_id] = card_wins.get(next_id, 0) + card_wins[card_id]

    print(sum(card_wins.values()))
