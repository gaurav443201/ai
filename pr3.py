
# A* Search using Manhattan Distance

start = [[1, 2, 3],
         [4, 0, 6],
         [7, 5, 8]]

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

def h(a):
    d = 0
    for i in range(3):
        for j in range(3):
            n = a[i][j]
            if n != 0:
                x = (n - 1) // 3
                y = (n - 1) % 3
                d += abs(i-x) + abs(j-y)
    return d

open_list = [(start, 0)]
visited = []

while open_list:
    best = 0

    for i in range(len(open_list)):
        if open_list[i][1] + h(open_list[i][0]) < open_list[best][1] + h(open_list[best][0]):
            best = i

    board, g = open_list.pop(best)

    if board == goal:
        print("Goal Reached!")
        print("Total Moves:", g)
        break

    if board in visited:
        continue

    visited.append(board)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                r, c = i, j

    for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r+x, c+y

        if 0 <= nr < 3 and 0 <= nc < 3:
            new = [row[:] for row in board]
            new[r][c], new[nr][nc] = new[nr][nc], new[r][c]

            if new not in visited:
                open_list.append((new, g+1))

else:
    print("No Solution")
