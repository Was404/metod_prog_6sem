import random

class TNode:
    gen = random.Random()

    def __init__(self, k):
        self.key = k
        self.prior = self.gen.random()
        self.left = None
        self.right = None

class TTreap:
    def __init__(self):
        self.Head = None

    def _free(self, ptr):
        if ptr is None:
            return
        self._free(ptr.left)
        self._free(ptr.right)
        del ptr

    def _split(self, ptr, val):
        if ptr is None:
            return None, None
        elif val > ptr.key:
            l, r = self._split(ptr.right, val)
            ptr.right = l
            return ptr, r
        else:
            l, r = self._split(ptr.left, val)
            ptr.left = r
            return l, ptr

    def _merge(self, t1, t2):
        if t1 is None or t2 is None:
            return t2 if t1 is None else t1
        elif t1.prior > t2.prior:
            t1.right = self._merge(t1.right, t2)
            return t1
        t2.left = self._merge(t1, t2.left)
        return t2

    def _find_min(self, ptr):
        if ptr is None:
            return -1
        elif ptr.left is None:
            return ptr.key
        return self._find_min(ptr.left)

    def find(self, value):
        l, r = self._split(self.Head, value)
        ans = self._find_min(r)
        self.Head = self._merge(l, r)
        return ans

    def insert(self, value):
        l, r = self._split(self.Head, value)
        self.Head = self._merge(self._merge(l, TNode(value)), r)

if __name__ == "__main__":
    n = int(input())
    tree = TTreap()
    prev = 0
    for _ in range(n):
        operation, val = input().split()
        val = int(val)
        if operation == '+':
            tree.insert((val + prev) % 1_000_000_000)
            prev = 0
        elif operation == '?':
            prev = tree.find(val)
            print(prev)