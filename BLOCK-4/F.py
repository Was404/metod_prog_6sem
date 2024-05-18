def dfs(graph, city, visited, path, max_weight):
    visited[city] = True
    path.append(city)

    if city == target_city:
        return True, path

    for neighbor, weight in graph[city]:
        if not visited[neighbor]:
            updated_weight = max_weight + weight
            if updated_weight < 0:
                updated_weight = 0
            success, result_path = dfs(
                graph, neighbor, visited[:], path[:], updated_weight
            )
            if success:
                return True, result_path

    return False, []


def main():
    n, m, k = map(int, input().split())
    flights = [list(map(int, input().split())) for _ in range(m)]
    concert_cities = list(map(int, input().split()))

    # Создание графа перелетов
    graph = {i: [] for i in range(1, n + 1)}
    for start, end, weight in flights:
        graph[start].append((end, weight))

    # Поиск пути между концертами
    global target_city
    target_city = concert_cities[0]
    max_weight = 0
    for i in range(k - 1):
        visited = [False] * (n + 1)
        success, path = dfs(graph, concert_cities[i], visited, [], max_weight)
        if not success:
            print("infinitely kind")
            return
        
        target_index = path.index(concert_cities[i]) + 1
        if target_index < len(path):  # Проверяем, есть ли целевой город в пути
            max_weight = max(
                weight
                for _, weight in graph[concert_cities[i]][target_index:]
            )
            max_weight += path[target_index]

    print(len(path) - 1)
    print(*path)


if __name__ == "__main__":
    main()
