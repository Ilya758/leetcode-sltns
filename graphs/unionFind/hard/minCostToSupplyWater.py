from heapq import *


class UF:
    def __init__(self, n):
        self.root = list(range(n + 1))
        self.rank = [1] * (n + 1)
        self.n = n + 1

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.root[self.root[x]]
            return self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)

        if a != b:
            if self.rank[a] >= self.rank[b]:
                self.rank[a] += self.rank[b]
                self.root[b] = a
            else:
                self.rank[b] += self.rank[a]
                self.root[a] = b

            self.n -= 1

    def count(self):
        return self.n

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
        heap = []
        ans = 0
        uf = UF(n)

        for u, v, w in pipes:
            heappush(heap, (w, u, v))

        for idx, weight in enumerate(wells):
            heappush(heap, (weight, 0, idx + 1))

        while heap:
            w, u, v = heappop(heap)

            if not uf.isConnected(u, v):
                uf.union(u, v)
                ans += w

                if uf.count() == 0:
                    return ans

        return ans
    
print(Solution().minCostToSupplyWater(n =
5,
wells =
[46012,72474,64965,751,33304],
pipes =
[[2,1,6719],[3,2,75312],[5,3,44918]]))