class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])

        return self.root[x] 

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(len(isConnected))

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i, j)

        return len(set([uf.find(i) for i in range(n)]))
    
        

print(Solution().findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]])) # 2
