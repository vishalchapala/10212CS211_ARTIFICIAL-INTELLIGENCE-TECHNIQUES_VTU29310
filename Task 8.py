def solve_n_queens(n):
    board = [-1] * n

    def is_safe(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(row, col):
                board[row] = col

                if backtrack(row + 1):
                    return True

                board[row] = -1

        return False

    if backtrack(0):
        for row in range(n):
            print(" ".join("Q" if board[row] == col else "."
                          for col in range(n)))
    else:
        print("No solution")


# 4 Queens
solve_n_queens(4)



OUTPUT

. Q . .
. . . Q
Q . . .
. . Q .
