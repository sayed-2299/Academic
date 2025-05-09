def is_safe(board, n, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve(board, n, col, m, queens_placed):
    if queens_placed == m:
        return True

    if col >= n:
        return False

    for row in range(n):
        if is_safe(board, n, row, col):
            board[row][col] = 1
            if solve(board, n, col + 1, m, queens_placed + 1):
                return True
            board[row][col] = 0

    return solve(board, n, col + 1, m, queens_placed)

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    if solve(board, N, 0, M, 0):
        print_board(board, N)
    else:
        print("Not Possible")