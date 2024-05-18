from collections import defaultdict

def find_eulerian_path(graph, start):
    path = []
    stack = [start]
    while stack:
        node = stack[-1]
        if graph[node]:
            next_node = graph[node].pop()
            stack.append(next_node)
        else:
            path.append(stack.pop())
    return path[::-1]

def main():
    N = int(input())
    graph = defaultdict(list)
    degree = defaultdict(int)
    for _ in range(2 * N):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1

    odd_degree_nodes = [node for node, deg in degree.items() if deg % 2 == 1]
    if odd_degree_nodes:
        print("No")
        return

    start = 1
    path = find_eulerian_path(graph, start)
    if len(path) != 4 * N:
        print("No")
        return

    print("Yes")
    print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()