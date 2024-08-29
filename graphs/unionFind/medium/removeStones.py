from collections import defaultdict

class UF:
    def __init__(self, n):
        self.rank = [1] * n
        self.root = list(range(n))
        self.n = n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.root[self.root[x]]

            return self.find(self.root[x])

        return self.root[x]
    
    def union(self, x, y):
        a, b = self.find(x), self.find(y)

        if a != b:
            self.n -= 1

            if self.rank[a] >= self.rank[b]:
                self.rank[a] += self.rank[b]
                self.root[b] = a
            else:
                self.rank[b] += self.rank[a]
                self.root[a] = b

    def count(self):
        return self.n

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        n = len(stones)
        uf = UF(n)
        rows = defaultdict(list)
        cols = defaultdict(list)

        for i, (x, y) in enumerate(stones):
            rows[x].append(i)
            cols[y].append(i)

        for indices in rows.values():
            for i in range(len(indices) - 1):
                uf.union(indices[i], indices[i + 1])

        for indices in cols.values():
            for i in range(len(indices) - 1):
                uf.union(indices[i], indices[i + 1])

        return n - uf.count()
