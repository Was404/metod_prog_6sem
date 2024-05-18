def longest_palindrome(s):
    n = len(s)
    start = 0
    max_len = 1

    # Создаем таблицу для хранения результатов проверок палиндромов
    dp = [[False] * n for _ in range(n)]

    # Все подстроки длины 1 являются палиндромами
    for i in range(n):
        dp[i][i] = True

    # Проверяем подстроки длины 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Проверяем подстроки длины больше 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                start = i
                max_len = length

    return max_len, s[start : start + max_len]


# Чтение входных данных
input_str = input().strip()

# Поиск и вывод ответа
length, result = longest_palindrome(input_str)
print(length)
print(result)
