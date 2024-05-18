def topological_sort(graph, in_degree):
    result = []
    queue = []

    for node in range(1, len(in_degree)):
        if in_degree[node] == 0:
            queue.append(node)

    while queue:
        current_node = queue.pop(0)
        result.append(current_node)

        for neighbor in graph[current_node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result


def solve(K, N, bets):
    graph = {}
    in_degree = [0] * (K + 1)

    for i in range(1, K + 1):
        graph[i] = []

    for bet in bets:
        graph[bet[0]].append(bet[1])
        in_degree[bet[1]] += 1

    order = topological_sort(graph, in_degree)

    if len(order) != K:
        return 0

    return order


# Ввод данных
K, N = map(int, input().split())
bets = [list(map(int, input().split())) for _ in range(N)]

# Получение результата
result = solve(K, N, bets)

# Вывод результата
if result:
    print(*result)
else:
    print(0)
