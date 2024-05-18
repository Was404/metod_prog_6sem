def find_maximum_k(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    # Находим наименьшую длину подстроки, которая может быть повторена
    smallest_repeat_length = n - pi[-1]
    if n % smallest_repeat_length == 0:
        return n // smallest_repeat_length
    else:
        return 1


# Ввод данных пользователем
user_input = input()
print(find_maximum_k(user_input))
