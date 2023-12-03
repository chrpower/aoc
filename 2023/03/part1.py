def is_adjacent(row, col, grid):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for d_row, d_col in dirs:
        adj_row, adj_col = row + d_row, col + d_col
        if (
            0 <= adj_row < len(grid)
            and 0 <= adj_col < len(grid[adj_row])
            and grid[adj_row][adj_col] not in {".", *map(str, range(10))}
        ):
            return True
    return False


total = 0
with open("input/input.txt", "r") as file:
    grid = [line.strip() for line in file]

    for row, line in enumerate(grid):
        col = 0
        while col < len(line):
            if line[col].isdigit():
                start = col
                while col < len(line) and line[col].isdigit():
                    col += 1
                if any(is_adjacent(row, k, grid) for k in range(start, col)):
                    total += int(line[start:col])
            else:
                col += 1

print(total)
