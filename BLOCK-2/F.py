from collections import defaultdict


def count_partitions(numbers):
    partitions_count = defaultdict(int)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            partitions_count[numbers[i] + numbers[j]] += 1

    return [partitions_count[num] for num in numbers]


# Ввод данных
N = int(input())
numbers = [int(input()) for _ in range(N)]

# Получение и вывод результатов
result = count_partitions(numbers)
for res in result:
    print(res)
