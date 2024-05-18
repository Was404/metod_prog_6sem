def is_valid(x, y, n, board):
    return 0 <= x < n and 0 <= y < n and board[x][y] == 0


def knight_tour(n):
    board = [[0] * n for _ in range(n)]
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def dfs(x, y, step):
        board[x][y] = step
        if step == n * n:
            return True
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, n, board) and dfs(nx, ny, step + 1):
                return True
        board[x][y] = 0
        return False

    if not dfs(0, 0, 1):
        return None
    return board


def main():
    n = int(input())
    result = knight_tour(n)
    if result is None:
        print(0)
    else:
        print(1)
        for row in result:
            print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
