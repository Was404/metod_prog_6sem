def flip_subarray(array, L, R):
    # Переворачиваем подмассив на месте
    array[L-1:R] = array[L-1:R][::-1]

def min_in_subarray(array, L, R):
    # Находим минимум в подмассиве
    return min(array[L-1:R])

def process_queries(n, m, array, queries):
    results = []
    for query in queries:
        q_type, L, R = query
        if q_type == 1:
            flip_subarray(array, L, R)
        elif q_type == 2:
            results.append(min_in_subarray(array, L, R))
    return results

# Считывание входных данных
n, m = map(int, input().split())
array = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Обработка запросов и вывод результатов
output = process_queries(n, m, array, queries)
for result in output:
    print(result)