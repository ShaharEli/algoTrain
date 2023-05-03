maze = [["", "W", "", "", ""],
        ["", "W", "", "W", ""],
        ["", "W", "", "W", ""],
        ["", "", "", "", ""],
        ["", "W", "", "W", ""]]

MOVES = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}


def spot_available(maze, spot):
    x, y = spot
    return len(maze) > x and x >= 0 and len(maze[x]) > y and y >= 0 and not maze[x][y]


def maze_solver(start, goal, maze, steps=0):
    if start == goal:
        for row in maze:
            for col in row:
                print(col.center(3), end=" ")
            print()
        print()
        return
    start_x, start_y = start
    for k in MOVES.values():
        move_x, move_y = k
        spot = (start_x+move_x, start_y+move_y)
        if spot_available(maze, spot):
            maze[start_x][start_y] = str(steps+1)
            maze_solver(spot, goal, maze, steps+1)
            maze[start_x][start_y] = ""


maze_solver((0, 0), (4, 4), maze)
