def choose_stylish_outfit(N, colors):
    colors.sort()  # Сортируем цвета по возрастанию
    return colors[0]


# Ввод данных
outfits = []
for _ in range(4):
    N = int(input())
    colors = list(map(int, input().split()))
    outfits.append((N, colors))

# Получение и вывод результата
result = [choose_stylish_outfit(N, colors) for N, colors in outfits]
print(*result)
