from queue import PriorityQueue

def a_star(graph, heuristic, start, goal):

    open_list = PriorityQueue()
    open_list.put((0, start))

    g = {node: float('inf') for node in graph}
    g[start] = 0

    parent = {start: None}

    while not open_list.empty():

        current = open_list.get()[1]

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, cost in graph[current]:

            new_cost = g[current] + cost

            if new_cost < g[neighbor]:
                g[neighbor] = new_cost
                f = new_cost + heuristic[neighbor]
                open_list.put((f, neighbor))
                parent[neighbor] = current

    return None


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
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

start = 'A'
goal = 'G'

path = a_star(graph, heuristic, start, goal)

print("Optimal Path:", " -> ".join(path))


OUTPUT

Optimal Path: A -> B -> D -> G
