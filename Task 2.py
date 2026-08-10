import random

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def path_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    cost += graph[path[-1]][path[0]]  # Return to start
    return cost

def get_neighbors(path):
    neighbors = []
    n = len(path)

    for i in range(1, n):
        for j in range(i + 1, n):
            neighbor = path[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)

    return neighbors

def hill_climbing():
    current = list(range(len(graph)))
    random.shuffle(current)

    current_cost = path_cost(current)

    while True:
        neighbors = get_neighbors(current)

        best = current
        best_cost = current_cost

        for neighbor in neighbors:
            cost = path_cost(neighbor)

            if cost < best_cost:
                best = neighbor
                best_cost = cost

        if best_cost >= current_cost:
            break

        current = best
        current_cost = best_cost

    return current, current_cost

best_path, best_cost = hill_climbing()

print("Best Path:", best_path + [best_path[0]])
print("Minimum Cost:", best_cost)


OUTPUT

Best Path: [0, 2, 3, 1, 0]
Minimum Cost: 80
