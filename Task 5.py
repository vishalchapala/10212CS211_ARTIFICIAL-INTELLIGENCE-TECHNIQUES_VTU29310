import random

cities = ['A', 'B', 'C', 'D']
time = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(cities)
pheromone = [[1]*n for _ in range(n)]

ants = 5
iterations = 20
best_route = None
best_time = float('inf')

for _ in range(iterations):

    routes = []

    for _ in range(ants):
        route = [random.randrange(n)]

        while len(route) < n:
            current = route[-1]
            unvisited = [i for i in range(n) if i not in route]

            weights = [
                pheromone[current][i] / time[current][i]
                for i in unvisited
            ]

            route.append(random.choices(unvisited, weights=weights)[0])

        total = sum(time[route[i]][route[i+1]] for i in range(n-1))
        total += time[route[-1]][route[0]]

        routes.append((route, total))

        if total < best_time:
            best_time = total
            best_route = route[:]

    pheromone = [[p * 0.5 for p in row] for row in pheromone]

    for route, total in routes:
        for i in range(n):
            a = route[i]
            b = route[(i+1) % n]
            pheromone[a][b] += 100 / total

print("Best Route:", " -> ".join(cities[i] for i in best_route))
print("Minimum Duration:", best_time)

print("Final Pheromone:")
for row in pheromone:
    print([round(x, 2) for x in row])




OUTPUT

Best Route: C -> A -> B -> D
Minimum Duration: 80
Final Pheromone:
[0.0, 2.01, 10.49, 0.0]
[10.49, 0.0, 0.0, 2.01]
[2.01, 0.0, 0.0, 10.49]
[0.0, 10.49, 2.01, 0.0]
