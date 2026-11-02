from collections import deque

start = {"A": "T", "B": "T", "C": "A"}
goal = {"A": "B", "B": "C", "C": "T"}

queue = deque([(start, [])])
visited = [start]

while queue:
    state, path = queue.popleft()

    if state == goal:
        print("Goal State Reached!")
        for move in path:
            print(move)
        print("Total Moves:", len(path))
        break

    for block in state:
        # Check if block is clear
        if block in state.values():
            continue

        for dest in ["T", "A", "B", "C"]:
            if dest == block:
                continue

            # Destination must be clear
            if dest != "T" and dest in state.values():
                continue

            new = state.copy()
            new[block] = dest

            if new not in visited:
                visited.append(new)

                if dest == "T":
                    move = "Move " + block + " to Table"
                else:
                    move = "Move " + block + " onto " + dest

                queue.append((new, path + [move]))

else:
    print("No solution found!")
