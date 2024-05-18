def find_N(X):
    current_number = int(X)

    for i in range(1, len(X) + 1):
        current_number = int(X[:-i])
        next_number = int(X[:-i]) + 1

        if str(next_number) not in X:
            return i


# Ввод данных
X = input()

# Получение и вывод результата
result = find_N(X)
print(result)
