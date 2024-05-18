import itertools
import math


def calculate_distance(points):
    total_distance = 0
    for i in range(len(points) - 1):
        total_distance += math.sqrt(
            (points[i + 1][0] - points[i][0]) ** 2
            + (points[i + 1][1] - points[i][1]) ** 2
        )
    return total_distance


def solve(n, points):
    min_distance = float("inf")
    min_route = None
    all_distances = [[0] * n for _ in range(n)]


    for i in range(n):
        for j in range(n):
            all_distances[i][j] = math.sqrt(
                (points[j][0] - points[i][0]) ** 2 + (points[j][1] - points[i][1]) ** 2
            )

    for route in itertools.permutations(range(1, n)):
        current_distance = all_distances[0][route[0]]  
        for i in range(len(route) - 1):
            current_distance += all_distances[route[i]][route[i + 1]]
        current_distance += all_distances[route[-1]][
            0
        ]  
        if current_distance < min_distance:
            min_distance = current_distance
            min_route = route

   
    if min_route is not None:
        route_order = [i + 1 for i in min_route]
        return min_distance, route_order
    else:
        return None, None



n = int(input())
points = [list(map(float, input().split())) for _ in range(n)]


min_distance, route_order = solve(n, points)


if min_distance is not None:
    print("{:.12f}".format(min_distance))
    print(" ".join(map(str, route_order)))
else:
    print("No solution found.")
