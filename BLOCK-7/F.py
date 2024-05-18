# ввод данных
N, M = map(int, input().split())
# создание двумерного массива
painting = [input() for _ in range(N)]


# определения симметричности прямоугольной области
def is_symmetric(rectangle):
    n = len(rectangle)
    m = len(rectangle[0])
    for i in range(n):
        for j in range(m):
            if (
                rectangle[i][j] != rectangle[n - i - 1][m - j - 1]
            ):  # проверка симметричности относительно центра
                return False
    return True


count = 0
for i in range(N):
    for j in range(M):
        for k in range(i, N):
            for l in range(j, M):
                # проверка симметричности прямоугольной области
                if is_symmetric([row[j : l + 1] for row in painting[i : k + 1]]):
                    count += 1


print(count)
