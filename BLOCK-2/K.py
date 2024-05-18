def cubic_equation_root(a, b, c, d, x0=0, epsilon=1e-9, max_iterations=1000):
    for _ in range(max_iterations):
        f_x = a * x0**3 + b * x0**2 + c * x0 + d
        f_prime_x = 3 * a * x0**2 + 2 * b * x0 + c

        x0 = x0 - f_x / f_prime_x

        if abs(f_x) < epsilon:
            return x0

    return None  # В случае, если не удалось найти корень


# Ввод данных
a, b, c, d = map(int, input().split())

# Получение и вывод результата
result = cubic_equation_root(a, b, c, d)
print("{:.9f}".format(result))
