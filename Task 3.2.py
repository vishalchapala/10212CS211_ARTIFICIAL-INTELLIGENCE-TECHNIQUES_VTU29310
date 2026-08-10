graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'G': 3},
    'E': {'G': 2},
    'F': {'G': 2},
    'G': {}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

open_list = ['A']
closed_list = []

g = {'A': 0}
parent = {'A': None}

while open_list:

    current = min(open_list, key=lambda node: g[node] + heuristic[node])

    if current == 'G':
        path = []

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()
        print("Optimal Path:", " -> ".join(path))
        break

    open_list.remove(current)
    closed_list.append(current)

    for neighbor, cost in graph[current].items():

        new_cost = g[current] + cost

        if neighbor not in g or new_cost < g[neighbor]:
            g[neighbor] = new_cost
            parent[neighbor] = current

            if neighbor not in open_list and neighbor not in closed_list:
                open_list.append(neighbor)


OUTPUT

Optimal Path: A -> B -> D -> G
