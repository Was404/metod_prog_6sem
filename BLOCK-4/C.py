from collections import deque


def shortest_path(N, M, start_x, start_y, end_x, end_y, grid):
    directions = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
    visited = [[False] * M for _ in range(N)]
    queue = deque([(start_x - 1, start_y - 1, 0, "")])  # (x, y, time, path)

    while queue:
        x, y, time, path = queue.popleft()
        if x == end_x - 1 and y == end_y - 1:
            return time, path

        for direction, (dx, dy) in directions.items():
            new_x, new_y = x + dx, y + dy
            if (
                0 <= new_x < N
                and 0 <= new_y < M
                and not visited[new_x][new_y]
                and grid[new_x][new_y] != "#"
            ):
                visited[new_x][new_y] = True
                new_time = (
                    time + 1 if grid[new_x][new_y] == "." else time + 2
                ) 
                queue.append((new_x, new_y, new_time, path + direction))

    return -1


# Чтение входных данных
N, M = map(int, input().split())  # Размеры карты
start_x, start_y = map(int, input().split())  # Начальная позиция
end_x, end_y = map(int, input().split())  # Конечная позиция
grid = [input() for _ in range(N)]  # Карта мира

# Поиск кратчайшего пути
result = shortest_path(N, M, start_x, start_y, end_x, end_y, grid)

# Вывод результата
if result == -1:
    print(-1)
else:
    print(result[0])
    print(result[1])
