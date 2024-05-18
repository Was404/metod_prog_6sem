def find_lis(n, a1, k, b, m):
    # Генерация последовательности
    sequence = [a1]
    for i in range(2, n + 1):
        ai = (k * sequence[-1] + b) % m
        sequence.append(ai)

    # Вычисление наибольшей возрастающей подпоследовательности
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Находим индекс максимального значения в dp
    max_len_index = dp.index(max(dp))

    # Восстанавливаем подпоследовательность
    lis = []
    while max_len_index != -1:
        lis.insert(0, sequence[max_len_index])
        max_len_index = prev[max_len_index]

    return lis


# Чтение входных данных
n = int(input())
a1, k, b, m = map(int, input().split())

# Поиск и вывод наибольшей возрастающей подпоследовательности
result = find_lis(n, a1, k, b, m)
print(" ".join(map(str, result)))
