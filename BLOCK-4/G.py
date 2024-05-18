def bellman_ford(graph, n):
    distances = [float("inf")] * n
    parents = [-1] * n

    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if (
                    graph[u][v] != 100000
                    and distances[u] != float("inf")
                    and distances[u] + graph[u][v] < distances[v]
                ):
                    distances[v] = distances[u] + graph[u][v]
                    parents[v] = u

    # Проверяем наличие цикла отрицательного веса
    for u in range(n):
        for v in range(n):
            if (
                graph[u][v] != 100000
                and distances[u] != float("inf")
                and distances[u] + graph[u][v] < distances[v]
            ):
                return True, u

    return False, None


def find_negative_cycle(graph, n, start):
    cycle = []
    visited = [False] * n
    current = start

    while not visited[current]:
        cycle.append(current)
        visited[current] = True
        
        # Поиск ребра с отрицательным весом
        min_weight = float('inf')
        next_vertex = None
        for v, weight in enumerate(graph[current]):
            if weight < min_weight:
                min_weight = weight
                next_vertex = v
        
        current = next_vertex

    # Определение начальной вершины отрицательного цикла
    cycle_start = cycle.index(current)
    cycle = cycle[cycle_start:]  # Срез для получения цикла
    
    return cycle


def main():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    has_negative_cycle, start = bellman_ford(graph, n)

    if has_negative_cycle:
        cycle = find_negative_cycle(graph, n, start)
        print("YES")
        print(len(cycle))
        print(*cycle)
    else:
        print("NO")


if __name__ == "__main__":
    main()
