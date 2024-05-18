def find_lis(arr):
    n = len(arr)
    dp = [1] * n  # Массив для хранения длин возрастающих подпоследовательностей
    prev = [
        -1
    ] * n  # Массив для хранения предыдущих индексов для восстановления подпоследовательности

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Находим индекс максимального значения в dp
    max_len_index = dp.index(max(dp))

    # Восстанавливаем подпоследовательность
    lis = []
    while max_len_index != -1:
        lis.insert(0, arr[max_len_index])
        max_len_index = prev[max_len_index]

    return lis


# Чтение входных данных
N = int(input())
sequence = list(map(int, input().split()))

# Поиск и вывод наибольшей возрастающей подпоследовательности
result = find_lis(sequence)
print(" ".join(map(str, result)))
