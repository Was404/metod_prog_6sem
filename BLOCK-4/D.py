def topological_sort(n, dependencies, indegree):
    graph = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for d in dependencies[i]:
            graph[d].append(i)

    queue = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    order = []
    while queue:
        node = queue.pop(0)
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order


def min_time_to_produce(n, p, dependencies):
    indegree = [0] * (n + 1)
    for i in range(1, n + 1):
        for d in dependencies[i]:
            indegree[d] += 1

    order = topological_sort(n, dependencies, indegree)

    min_time = 0
    required_details = []
    for detail in order:
        min_time += p[detail - 1]
        if detail == 1:
            break
        required_details.append(detail)

    return min_time, len(required_details), required_details


def main():
    n = int(input())
    p = list(map(int, input().split()))

    dependencies = {}
    for i in range(1, n + 1):
        dependencies[i] = list(map(int, input().split()))[1:]

    min_time, k, details = min_time_to_produce(n, p, dependencies)
    print(min_time, k)
    print(*details)


if __name__ == "__main__":
    main()
