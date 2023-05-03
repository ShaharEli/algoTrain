
# https://leetcode.com/problems/unique-paths-iii
grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]


valid_directions = [
    (1, 0), (-1, 0),
    (0, 1), (0, -1)
]


def check_dir(coord, direction, grid):
    new_cord = coord[0]+direction[0], coord[1]+direction[1]
    if new_cord[0] < 0 or new_cord[1] < 0 or new_cord[0] >= len(grid) or new_cord[1] >= len(grid[0]):
        return False
    return new_cord


def check_is_full(grid):
    for row in grid:
        for col in row:
            if not col:
                return False
    return True


def unique_paths_helper(grid, coord):
    valid_paths_count = 0
    for direction in valid_directions:
        valid_dir = check_dir(coord, direction, grid)
        if valid_dir:
            x, y = valid_dir
            content = grid[x][y]
            if content == -1:
                continue
            if content == 2:
                if check_is_full(grid):
                    valid_paths_count += 1
            if content == 0:
                grid[x][y] = 1
                valid_paths_count += unique_paths_helper(grid, valid_dir)
                grid[x][y] = 0

    return valid_paths_count


def unique_paths(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                coord = i, j
    return unique_paths_helper(grid, coord)


print(unique_paths(grid))
