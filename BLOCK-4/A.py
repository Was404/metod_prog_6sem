def is_valid(x, y):
    return 0 < x <= 8 and 0 < y <= 8


def bfs(start, end):
    queue = [start]
    visited = set([start])
    moves = 0

    while queue:
        size = len(queue)
        for _ in range(size):
            x, y = queue.pop(0)
            if (x, y) == end:
                return moves
            for dx, dy in [
                (2, 1),
                (1, 2),
                (-1, 2),
                (-2, 1),
                (-2, -1),
                (-1, -2),
                (1, -2),
                (2, -1),
            ]:
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
        moves += 1

    return -1


def main():
    start_input, end_input = input().strip().split()

    start = (ord(start_input[0]) - ord("a"), int(start_input[1]) - 1)
    end = (ord(end_input[0]) - ord("a"), int(end_input[1]) - 1)

    result = bfs(start, end)

    if result == -1:
        print(1)
    else:
        print(result)


if __name__ == "__main__":
    main()
