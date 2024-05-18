def min_route(N, distances, exclude_mask):
    INF = float("inf")
    dp = [[INF] * (1 << N) for _ in range(N)]
    dp[0][
        1
    ] = 0  # Начинаем из первой точки, маска 1 означает, что мы посетили эту точку

    for mask in range(1 << N):
        for u in range(N):
            if mask & (1 << u):
                for v in range(N):
                    if (mask & (1 << v)) == 0:
                        dp[v][mask | (1 << v)] = min(
                            dp[v][mask | (1 << v)], dp[u][mask] + distances[u][v]
                        )

    min_length = INF
    for v in range(1, N):
        if exclude_mask & (1 << v) == 0:  # Исключаем вычеркнутые точки
            min_length = min(min_length, dp[v][(1 << N) - 1])

    return min_length


# Чтение входных данных
N = int(input())
distances = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())

# Обработка запросов
for _ in range(Q):
    exclude_data = list(map(int, input().split()))
    C = exclude_data[0]
    exclude_mask = 0
    for i in range(1, C + 1):
        exclude_mask |= 1 << exclude_data[i]

    result = min_route(N, distances, exclude_mask)
    print(result)
