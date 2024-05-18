import random

class Treap:
    def __init__(self, data):
        self.heap = random.randint(0, 1000000)  
        self.data = data
        self.branch = 1
        self.left = None
        self.right = None

    def split(self, i):
        myi = 0 if not self.left else self.left.branch
        lil = big = None
        if myi < i:
            if self.right:
                self.right, big = self.right.split(i - (myi + 1))
            lil = self
        else:
            if self.left:
                lil, self.left = self.left.split(i)
            big = self
        self.branch = (0 if not self.left else self.left.branch) + \
                      (0 if not self.right else self.right.branch) + 1
        return lil, big

def branchOf(a):
    return 0 if not a else a.branch

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a.heap > b.heap:
        a.right = merge(a.right, b)
        a.branch = branchOf(a.left) + branchOf(a.right) + 1
        return a
    else:
        b.left = merge(a, b.left)
        b.branch = branchOf(b.left) + branchOf(b.right) + 1
        return b

def print_treap(a):
    if a:
        print_treap(a.left)
        print(a.data, end=' ')
        print_treap(a.right)

def main():
    random.seed()  # инициализация случайного генератора
    n, m = map(int, input().split())
    root = None
    for i in range(n):
        root = merge(root, Treap(i + 1))
    for _ in range(m):
        a, b = map(int, input().split())
        B, C = root.split(b)
        A = None
        if B:
            A, B = B.split(a - 1)
        root = merge(B, merge(A, C))
    print_treap(root)

if __name__ == "__main__":
    main()