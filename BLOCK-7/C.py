def count_palindromic_substrings(s):
    n = len(s)
    count = 0

    def expand_around_center(left, right):
        nonlocal count
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(n):
        expand_around_center(i, i)  # палиндром нечётной длины
        expand_around_center(i, i + 1)  # палиндром чётной длины

    return count


# Ввод данных пользователем
user_input = input()
print(count_palindromic_substrings(user_input))
