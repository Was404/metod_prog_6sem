from collections import defaultdict
import heapq


def min_cost_to_reach_destination(N, fuel_prices, M, roads):
    graph = defaultdict(list)

    # Построение графа
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    # Инициализация значений
    INF = float("inf")
    min_cost = [[INF, INF] for _ in range(N + 1)]
    min_cost[1][0] = fuel_prices[1]  # Стоимость в первом городе без канистры
    min_cost[1][1] = 0  # Стоимость в первом городе с канистрой

    # Очередь с приоритетом
    pq = [(fuel_prices[1], 1, 0)]  # (стоимость, город, канистра пуста)

    while pq:
        cost, city, canister = heapq.heappop(pq)

        if city == N:
            return min_cost[city][canister]

        if (
            cost > min_cost[city][canister]
        ):  # Пропускаем, если мы нашли более дешевый путь ранее
            continue

        for neighbor in graph[city]:
            new_cost = cost + fuel_prices[neighbor] if canister == 0 else cost

            # Попытка заправить канистру
            if canister == 0:
                new_cost_with_canister = cost + fuel_prices[neighbor] * 2
                if new_cost_with_canister < min_cost[neighbor][1]:
                    min_cost[neighbor][1] = new_cost_with_canister
                    heapq.heappush(pq, (new_cost_with_canister, neighbor, 1))

            # Обновление стоимости пути без канистры
            if new_cost < min_cost[neighbor][canister]:
                min_cost[neighbor][canister] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, canister))

    return -1  # Если добраться невозможно


# Считывание входных данных
N = int(input())
fuel_prices = [0] + list(map(int, input().split()))
M = int(input())
roads = [tuple(map(int, input().split())) for _ in range(M)]

# Вывод результата
print(min_cost_to_reach_destination(N, fuel_prices, M, roads))
