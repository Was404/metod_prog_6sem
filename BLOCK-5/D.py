import math
import heapq


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def prim(points, existing_edges):
    n = len(points)
    visited = [False] * n
    min_cost = [float("inf")] * n
    min_cost[0] = 0
    pq = [(0, 0)]
    total_cost = 0

    while pq:
        cost, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost
        for v in range(n):
            if not visited[v]:
                dist = distance(points[u], points[v])
                if (u + 1, v + 1) in existing_edges or (
                    v + 1,
                    u + 1,
                ) in existing_edges:  # Проверка наличия ребра
                    dist = 0
                if dist < min_cost[v]:
                    min_cost[v] = dist
                    heapq.heappush(pq, (dist, v))

    return total_cost


def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    M = int(input())
    existing_edges = set(tuple(sorted(map(int, input().split()))) for _ in range(M))

    mst_cost = prim(points, existing_edges)

    print(f"{mst_cost:.5f}")


if __name__ == "__main__":
    main()
