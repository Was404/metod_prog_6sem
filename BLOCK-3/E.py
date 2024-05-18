def knapsack(N, M, weights, values):
    # Создаем матрицу для хранения максимальной стоимости для каждого веса и предмета
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Заполняем матрицу пошагово
    for i in range(1, N + 1):
        for j in range(M + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(
                    dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][j] = dp[i - 1][j]

    # Восстанавливаем ответ - определяем, какие предметы были взяты в рюкзак
    result = []
    i, j = N, M
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            result.append(i)
            j -= weights[i - 1]
        i -= 1

    return result


# Чтение входных данных
N, M = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

# Поиск и вывод решения
result = knapsack(N, M, weights, values)
print(" ".join(map(str, result)))
