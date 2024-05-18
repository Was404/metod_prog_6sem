def count_cows(stalls, distance):
    count = 1
    current_position = stalls[0]

    for stall in stalls:
        if stall - current_position >= distance:
            count += 1
            current_position = stall

    return count


def max_distance(N, K, stalls):
    stalls.sort()
    low, high = 1, stalls[-1] - stalls[0]

    while low < high:
        mid = (low + high + 1) // 2

        if count_cows(stalls, mid) >= K:
            low = mid
        else:
            high = mid - 1

    return low


# Ввод данных
N, K = map(int, input().split())
stalls = list(map(int, input().split()))

# Получение и вывод результата
result = max_distance(N, K, stalls)
print(result)
