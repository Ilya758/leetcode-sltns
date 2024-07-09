class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1 for _ in range(n)]
        self.count = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            return self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)

        if x != y:
            if self.rank[x] <= self.rank[y]:
                self.rank[x] += self.rank[y]
                self.parent[y] = x
            else:
                self.rank[y] += self.rank[x]
                self.parent[x] = y

            self.count -= 1

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    def getCount(self):
        return self.count


class Solution:
    def minCostConnectPoints(self, A: list[list[int]]) -> int:
        ans = 0
        uf = UF(len(A))

        for w, u, v in sorted(self.constructNeighbors(A)):
            if not uf.isConnected(u, v):
                uf.union(u, v)
                ans += w

            if uf.getCount() == 1:
                break

        return ans


    def constructNeighbors(self, A):
        res = []
        n = len(A)
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    res.append([self.distance(A[i], A[j]), i, j])

        return res

    def distance(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])
      
print(Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])) # 20