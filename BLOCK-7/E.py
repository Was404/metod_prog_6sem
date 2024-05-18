def min_groups_for_billboard(k, n, m, hieroglyphs):
    # создание списка для рисунков
    patterns = [""] * (n * m)
    index = 0
    for row in range(n):
        for col in range(m):
            for hieroglyph in range(k):
                patterns[index] += hieroglyphs[hieroglyph * n + row][col]
            index += 1

    # определение уникальных шаблонов
    unique_patterns = set(patterns)
    return len(unique_patterns)


# Ввод данных пользователя
k, n, m = map(int, input().split())
hieroglyphs = []
for _ in range(k * n):
    hieroglyphs.append(input().strip())

# расчёт и вывод данных
print(min_groups_for_billboard(k, n, m, hieroglyphs))
