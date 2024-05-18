def main():
    # Сокращаем время ввода данных.
    s, n = map(int, input().split())

    # Первый индекс - количество рассмотренных предметов, второй - вес.
    # Предметов меньше (максимум 300), а весов больше (до 10000),
    # поэтому предметы на первом месте (цикл на меньше итераций).
    dp = [[False] * (s + 1) for _ in range(n + 1)]

    dp[0][0] = True

    weights = list(map(int, input().split()))
    for i in range(1, n + 1):
        w = weights[i - 1]
        for j in range(s + 1):
            if dp[i - 1][j]:
                # Если не брать предмет с номером i.
                dp[i][j] = True
            # Если взять предмет с номером i (не превышая вместимость рюкзака).
            if j + w <= s:
                dp[i][j + w] = True

        # Найти максимальный полученный вес.
    for i in range(s, -1, -1):
        if dp[n][i]:
            print(i)
        break


if __name__ == "__main__":
    main()
