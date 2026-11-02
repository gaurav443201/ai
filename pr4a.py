
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = 4

def total_distance(route):
    total = 0

    for i in range(n - 1):
        total += distance[route[i]][route[i + 1]]

    total += distance[route[n - 1]][route[0]]
    return total


beam = [[0, 1, 2, 3]]
best_route = beam[0]
best_distance = total_distance(best_route)

for step in range(20):

    new_routes = []

    for route in beam:
        for i in range(1, n):
            for j in range(i + 1, n):

                new = route[:]
                new[i], new[j] = new[j], new[i]

                if new not in new_routes:
                    new_routes.append(new)

    if len(new_routes) == 0:
        break

    new_routes.sort(key=total_distance)

    beam = new_routes[:3]

    if total_distance(beam[0]) < best_distance:
        best_route = beam[0]
        best_distance = total_distance(best_route)

best_route = best_route + [best_route[0]]

print("Best Tour:", best_route)
print("Minimum Distance:", best_distance)
