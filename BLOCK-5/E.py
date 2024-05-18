from collections import deque


def bfs(graph, residual_graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.popleft()
        for ind, val in enumerate(residual_graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return visited[sink]


def edmonds_karp(graph, source, sink):
    residual_graph = [list(row) for row in graph]
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, residual_graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

    return max_flow


def main():
    n, m = map(int, input().split())
    graph = [[0] * n for _ in range(n)]

    for _ in range(m):
        u, v, capacity = map(int, input().split())
        graph[u - 1][v - 1] = capacity

    source, sink = 0, n - 1
    max_flow = edmonds_karp(graph, source, sink)
    print(max_flow)


if __name__ == "__main__":
    main()
