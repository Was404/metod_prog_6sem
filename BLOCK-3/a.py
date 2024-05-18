def find_lcs(seq1, seq2):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)

    # Создаем матрицу для хранения длин наибольших общих подпоследовательностей
    lcs_matrix = [[0] * (len_seq2 + 1) for _ in range(len_seq1 + 1)]

    # Заполняем матрицу пошагово
    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i - 1][j], lcs_matrix[i][j - 1])

    # Находим наибольшую общую подпоследовательность
    lcs = []
    i, j = len_seq1, len_seq2
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs.insert(0, seq1[i - 1])
            i -= 1
            j -= 1
        elif lcs_matrix[i - 1][j] > lcs_matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs


# Чтение входных данных
N = int(input())
seq1 = list(map(int, input().split()))
M = int(input())
seq2 = list(map(int, input().split()))

# Поиск и вывод наибольшей общей подпоследовательности
result = find_lcs(seq1, seq2)
print(" ".join(map(str, result)))
