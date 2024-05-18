import random

class Vertex:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.label = 0
        self.parent = None
        self.left = None
        self.right = None

    def set(self, xi, yi, labeli):
        self.x = xi
        self.y = -yi
        self.label = labeli

def swap(a, b):
    return b, a

class DecTree:
    def __init__(self, size=None):
        self.vertexCount = 0

        if size is None:
            self.treeSize = int(input())
            self.vertexs = [Vertex() for _ in range(self.treeSize)]
            self.ordered = [None] * self.treeSize
            for i in range(self.treeSize):
                a, b = map(int, input().split())
                self.vertexs[i].set(a, b, i + 1)
                self.ordered[i] = self.vertexs[i]
        else:
            self.treeSize = size
            self.vertexs = [Vertex() for _ in range(self.treeSize)]
            self.ordered = [None] * self.treeSize

        self._sortQuick(0, self.treeSize)
        self._makeTree()

    def _sortIns(self, left, right):
        for i in range(left + 1, right):
            j = i - 1
            shift = self.ordered[i]

            while j >= left and self.ordered[j].x > shift.x:
                self.ordered[j + 1] = self.ordered[j]
                j -= 1

            self.ordered[j + 1] = shift

    def _sortQuick(self, left, right):
        if right - left <= 1:
            return

        random.seed()
        l, r = left, right - 1
        p = self.ordered[l + random.randint(0, right - left - 1)]

        while l <= r:
            while self.ordered[l].x < p.x:
                l += 1
            while self.ordered[r].x > p.x:
                r -= 1

            if l <= r:
                self.ordered[l], self.ordered[r] = swap(self.ordered[l], self.ordered[r])
                l += 1
                r -= 1

        if r - left > 16:
            self._sortQuick(left, r + 1)
        else:
            self._sortIns(left, r + 1)

        if right - l > 16:
            self._sortQuick(l, right)
        else:
            self._sortIns(l, right)

    def _makeTree(self):
        self.root = self.ordered[0]
        last = self.root

        for i in range(1, self.treeSize):
            while last.parent and self.ordered[i].y > last.y:
                last = last.parent

            if self.ordered[i].y <= last.y:
                self.ordered[i].left = last.right
                self.ordered[i].parent = last
                if last.right:
                    last.right.parent = self.ordered[i]
                last.right = self.ordered[i]
            else:
                self.ordered[i].left = last
                last.parent = self.ordered[i]
                self.root = self.ordered[i]

            last = self.ordered[i]

    def resultsDisplay(self):
        print("YES")
        for i in range(self.treeSize):
            parent = self.vertexs[i].parent.label if self.vertexs[i].parent else 0
            left = self.vertexs[i].left.label if self.vertexs[i].left else 0
            right = self.vertexs[i].right.label if self.vertexs[i].right else 0
            print(parent, left, right)

def main():
    mytree = DecTree()
    mytree.resultsDisplay()

if __name__ == "__main__":
    main()