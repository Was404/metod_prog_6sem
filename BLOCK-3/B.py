def levenshtein_distance(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    # Создаем матрицу для хранения расстояний Левенштейна
    dp = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

    # Инициализация первой строке и столбца матрицы
    for i in range(len_str1 + 1):
        dp[i][0] = i
    for j in range(len_str2 + 1):
        dp[0][j] = j

    # Заполнение матрицы
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # Удаление
                dp[i][j - 1] + 1,  # Вставка
                dp[i - 1][j - 1] + cost,  # Замена
            )

    return dp[len_str1][len_str2]


# Чтение входных данных
str1 = input().strip()
str2 = input().strip()

# Вычисление и вывод расстояния Левенштейна
result = levenshtein_distance(str1, str2)
print(result)
