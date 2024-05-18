def count_segments(lengths, target_length):
    count = 0

    for length in lengths:
        count += length // target_length

    return count

def max_segments_length(N, K, lengths):
    low, high = 1, max(lengths)

    while low < high:
        mid = (low + high + 1) // 2

        if count_segments(lengths, mid) >= K:
            low = mid
        else:
            high = mid - 1

    return low

# Ввод данных
N, K = map(int, input().split())
lengths = [int(input()) for _ in range(N)]

# Получение и вывод результата
result = max_segments_length(N, K, lengths)
print(result)
