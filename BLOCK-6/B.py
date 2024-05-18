class SegmentTree:
    def __init__(self, array):
        self.tree = [None] * (4 * len(array))
        self.build(array, 1, 0, len(array) - 1)

    def build(self, array, v, tl, tr):
        if tl == tr:
            self.tree[v] = tl
        else:
            tm = (tl + tr) // 2
            self.build(array, v * 2, tl, tm)
            self.build(array, v * 2 + 1, tm + 1, tr)
            if array[self.tree[v * 2]] >= array[self.tree[v * 2 + 1]]:
                self.tree[v] = self.tree[v * 2]
            else:
                self.tree[v] = self.tree[v * 2 + 1]

    def query(self, v, tl, tr, l, r, array):
        if l > r:
            return -1
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        max_left = self.query(v * 2, tl, tm, l, min(r, tm), array)
        max_right = self.query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, array)
        if max_left == -1:
            return max_right
        elif max_right == -1:
            return max_left
        elif array[max_left] >= array[max_right]:
            return max_left
        else:
            return max_right


# Чтение входных данных
N = int(input())
array = list(map(int, input().split()))
K = int(input())
queries = [tuple(map(int, input().split())) for _ in range(K)]

# Создание и инициализация дерева отрезков
segment_tree = SegmentTree(array)

# Обработка запросов
for query in queries:
    left, right = query
    max_index = segment_tree.query(1, 0, N - 1, left - 1, right - 1, array)
    print(max_index + 1, end=" ")
