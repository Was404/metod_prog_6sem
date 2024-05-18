import itertools
import math


# евклидово расстояние между двумя точками на плоскости
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# расстояние от начала до конца
def calculate_total_distance(points, order):
    total_distance = calculate_distance(points[0], points[order[0]])
    for i in range(len(order) - 1):
        total_distance += calculate_distance(points[order[i]], points[order[i + 1]])
    total_distance += calculate_distance(points[order[-1]], points[0])
    return total_distance


def main():
    n = int(input())
    points = [tuple(map(float, input().split())) for _ in range(n)]

    min_distance = float("inf")
    min_order = None

    # Перебираем все возможные перестановки вершин, кроме первой (так как она всегда должна быть в начале и конце)
    for order in itertools.permutations(range(1, n)):
        distance = calculate_total_distance(points, order)
        if distance < min_distance:
            min_distance = distance
            min_order = order

    # Выводим минимальную длину маршрута и порядок посещения вершин
    print(f"{min_distance:.10e}")
    print(" ".join(map(lambda x: str(x + 1), sorted(min_order))))


if __name__ == "__main__":
    main()
