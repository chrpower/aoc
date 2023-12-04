with open("input/input.txt", "r") as file:
    total_pts = 0
    for line in file:
        _, card_data = line.split(":", 1)
        win_str, player_str = card_data.split("|")

        win_nums = set(map(int, win_str.strip().split()))
        player_nums = set(map(int, player_str.strip().split()))

        matches = win_nums & player_nums
        if matches:
            card_pts = 1
            for _ in range(1, len(matches)):
                card_pts *= 2
            total_pts += card_pts

    print(total_pts)
