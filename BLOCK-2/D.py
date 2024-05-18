def restore_tournament_table(K, points):
    table = [[0] * K for _ in range(K)]

    # Заполнение верхнего треугольника таблицы
    for i in range(K - 1):
        for j in range(i + 1, K):
            if points[i] < points[j]:
                table[i][j] = 2
            elif points[i] == points[j]:
                table[i][j] = 1

    # Заполнение нижнего треугольника таблицы
    for i in range(1, K):
        for j in range(i):
            table[i][j] = 2 - table[j][i]

    return table


# Ввод данных
K = int(input())
points = list(map(int, input().split()))

# Получение результата
result_table = restore_tournament_table(K, points)

# Вывод результата
for row in result_table:
    print(*row)
