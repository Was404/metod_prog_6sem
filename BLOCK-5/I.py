import heapq

def read_graph(n, m):
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        b, e, w = map(int, input().split())
        graph[b].append((e, w))
        graph[e].append((b, w))
    return graph

def prim(graph, start):
    visited = [False] * (len(graph) + 1)
    min_heap = [(0, start)]
    total_weight = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if not visited[node]:
            visited[node] = True
            total_weight += weight
            for neighbor, edge_weight in graph[node]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor))

    return total_weight

def main():
    n, m = map(int, input().split())
    graph = read_graph(n, m)
    start_node = 1  
    mst_weight = prim(graph, start_node)
    print(mst_weight)

if __name__ == "__main__":
    main()