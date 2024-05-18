def find_occurrences(list1, list2):
    occurrences = {}

    for i, num in enumerate(list1, start=1):
        if num not in occurrences:
            occurrences[num] = [i, i]
        else:
            occurrences[num][1] = i

    result = []
    for num in list2:
        if num in occurrences:
            result.append(occurrences[num])
        else:
            result.append([0, 0])

    return result


# Ввод данных
N, M = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# Поиск и вывод результатов
results = find_occurrences(list1, list2)
for res in results:
    print(*res)
