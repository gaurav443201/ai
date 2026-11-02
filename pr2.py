
# Model-Based Agent for Grid Navigation

grid = [
    ['S', '0', 'X', '0'],
    ['0', '0', 'X', '0'],
    ['X', '0', '0', '0'],
    ['0', '0', '0', 'G']
]

visited = []

x = 0
y = 0

while grid[x][y] != 'G':

    print("Current Position:", x, y)
    visited.append((x, y))

    # Move Right
    if y + 1 < 4 and grid[x][y+1] != 'X' and (x, y+1) not in visited:
        y = y + 1
        print("Moved Right")

    # Move Down
    elif x + 1 < 4 and grid[x+1][y] != 'X' and (x+1, y) not in visited:
        x = x + 1
        print("Moved Dowm")

    # Move Left
    elif y - 1 >= 0 and grid[x][y-1] != 'X' and (x, y-1) not in visited:
        y = y - 1
        print("Moved Left")

    # Move Up
    elif x - 1 >= 0 and grid[x-1][y] != 'X' and (x-1, y) not in visited:
        x = x - 1
        print("Moved Up")

    else:
        print("No path found!")
        break

if grid[x][y] == 'G':
    print("Goal Reached!")
    print("Final Position:", x, y)
