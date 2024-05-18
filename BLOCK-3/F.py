def find_longest_valid_parentheses(s):
    stack = []
    result = []
    open_to_close = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if stack and stack[-1] == open_to_close[char]:
                stack.pop()
                result.append(char)

    return "".join(result)


# Чтение входных данных
input_str = input().strip()

# Поиск и вывод ответа
result = find_longest_valid_parentheses(input_str)
print(result)
