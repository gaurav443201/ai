
# BFS for Blocks World Problem

start = (('A', 'C'), ('B',))
goal = (('C', 'B', 'A'),)

queue = [[start, []]]
visited = [start]

while len(queue) > 0:

    state, path = queue.pop(0)

    # Check goal state
    if state == goal:
        print("Goal State Reached!")
        print("Steps:")

        for move in path:
            print(move)

        print("Total Moves:", len(path))
        break

    # Generate new states
    for i in range(len(state)):

        # Take the top block
        block = state[i][-1]

        # Remove the top block
        new_state = list(state)
        new_state[i] = state[i][:-1]

        if new_state[i] == ():
            new_state.pop(i)

        # Move block to the table
        table_state = tuple(sorted(new_state + [(block,)]))

        if table_state not in visited:
            visited.append(table_state)

            new_path = path + ["Move " + block + " to table"]
            queue.append([table_state, new_path])

        # Move block onto another stack
        for j in range(len(new_state)):

            temp = new_state[:]
            temp[j] = temp[j] + (block,)

            next_state = tuple(sorted(temp))

            if next_state not in visited:
                visited.append(next_state)

                new_path = path + [
                    "Move " + block + " onto " + temp[j][-2]
                ]

                queue.append([next_state, new_path])

else:
    print("No solution found!")
