def is_star_adjacent(row, col, grid):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for d_row, d_col in dirs:
        adj_row, adj_col = row + d_row, col + d_col
        if (
            0 <= adj_row < len(grid)
            and 0 <= adj_col < len(grid[adj_row])
            and grid[adj_row][adj_col] == "*"
        ):
            return adj_row, adj_col
    return None


adjacent_numbers = {}
with open("input/input.txt", "r") as file:
    grid = [line.strip() for line in file]

    for row, line in enumerate(grid):
        col = 0
        while col < len(line):
            if line[col].isdigit():
                start = col
                while col < len(line) and line[col].isdigit():
                    col += 1
                for k in range(start, col):
                    star_coords = is_star_adjacent(row, k, grid)
                    if star_coords:
                        adjacent_numbers.setdefault(star_coords, []).append(
                            int(line[start:col])
                        )
                        break
            else:
                col += 1

print(sum(nums[0] * nums[1] for nums in adjacent_numbers.values() if len(nums) == 2))
