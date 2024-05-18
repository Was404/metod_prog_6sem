def check(mid, heights, R, C):
    sorted_heights = sorted(heights)
    max_discomfort = 0
    for i in range(N - R * C + 1):
        discomfort = sorted_heights[i + R * C - 1] - sorted_heights[i]
        max_discomfort = max(max_discomfort, discomfort)
    return max_discomfort <= mid


def min_discomfort(N, R, C, heights):
    left, right = 0, max(heights) - min(heights)
    result = right

    while left <= right:
        mid = (left + right) // 2
        if check(mid, heights, R, C):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


# Ввод данных
N, R, C = map(int, input().split())
heights = [int(input()) for _ in range(N)]

# Вывод результата
print(min_discomfort(N, R, C, heights))
