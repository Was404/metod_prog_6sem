INF = 10**9


def bellman_ford(graph, start, n):
    distances = [INF] * n
    distances[start] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, departure, _, arrival in graph[u]:
                if distances[u] != INF and departure <= distances[u] <= arrival:
                    distances[v] = min(distances[v], arrival)

    return distances


def main():
    n = int(input())
    start, end = map(int, input().split())
    k = int(input())

    graph = [[] for _ in range(n)]

    for _ in range(k):
        departure, departure_time, destination, arrival_time = map(int, input().split())
        graph[departure - 1].append(
            (destination - 1, departure_time, destination, arrival_time)
        )

    distances = bellman_ford(graph, start - 1, n)

    print(distances[end - 1])


if __name__ == "__main__":
    main()
