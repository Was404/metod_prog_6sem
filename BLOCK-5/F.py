def assign_tasks(matrix):
    K = len(matrix)
    total_time = 0

    while True:
        # Находим минимальное время выполнения задачи
        min_time = float("inf")
        for i in range(K):
            for j in range(K):
                if matrix[i][j] < min_time:
                    min_time = matrix[i][j]

        # Если минимальное время равно бесконечности, значит все задачи уже выполнены
        if min_time == float("inf"):
            break

        # Добавляем минимальное время к общему времени
        total_time += min_time

        # Обнуляем строки и столбцы, содержащие минимальное время выполнения задачи
        for i in range(K):
            for j in range(K):
                if matrix[i][j] == min_time:
                    for k in range(K):
                        matrix[i][k] = float("inf")
                        matrix[k][j] = float("inf")
                    break  # Переходим к следующей строке после обнуления столбца
            else:
                continue  # Эта строка выполнится, если break не был вызван, т.е. если строка не содержала минимального времени выполнения задачи
            break  # Переходим к следующей итерации после обнуления строки

    return total_time


def main():
    with open("input.txt", "r") as file:
        K = int(file.readline().strip())
        matrix = [list(map(int, file.readline().strip().split())) for _ in range(K)]

    min_total_time = assign_tasks(matrix)

    with open("output.txt", "w") as file:
        file.write(str(min_total_time))


if __name__ == "__main__":
    main()
