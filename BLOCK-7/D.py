def minimum_cyclic_shift(s1, s2):
    if len(s1) != len(s2):
        return -1
    double_s1 = s1 + s1
    pos = double_s1.find(s2)
    if pos == -1:
        return -1
    return (len(s1) - pos) % len(s1)


# Ввод данных пользователем
user_input1 = input()
user_input2 = input()

print(minimum_cyclic_shift(user_input1, user_input2))
