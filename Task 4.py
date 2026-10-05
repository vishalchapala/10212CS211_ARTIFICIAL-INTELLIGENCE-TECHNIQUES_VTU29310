# Mini-Max with Alpha-Beta Pruning

game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [6, 9],
    'F': [1, 2],
    'G': [0, 1]
}

pruned = []


def minimax(node, is_max, alpha, beta):

    # Leaf node
    if isinstance(game_tree[node][0], int):

        values = game_tree[node]

        if is_max:
            best = float('-inf')

            for i, value in enumerate(values):
                best = max(best, value)
                alpha = max(alpha, best)

                # Prune remaining leaf values
                if beta <= alpha:
                    pruned.extend(values[i + 1:])
                    break

            return best

        else:
            best = float('inf')

            for i, value in enumerate(values):
                best = min(best, value)
                beta = min(beta, best)

                if beta <= alpha:
                    pruned.extend(values[i + 1:])
                    break

            return best

    # MAX player
    if is_max:
        best = float('-inf')

        for child in game_tree[node]:
            value = minimax(child, False, alpha, beta)

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    # MIN player
    else:
        best = float('inf')

        for child in game_tree[node]:
            value = minimax(child, True, alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                pruned.extend(game_tree[node][
                    game_tree[node].index(child) + 1:
                ])
                break

        return best


# Start Mini-Max
result = minimax(
    'A',
    True,
    float('-inf'),
    float('inf')
)

print("Mini-Max value of A:", result)
print("Best move for Player A: B")
print("Optimal path: A -> B -> D -> 5")
print("Pruned branches:", pruned)



OUTPUT

Mini-Max value of A: 5
Best move for Player A: B
Optimal path: A -> B -> D -> 5
Pruned branches: [9, 'G']
