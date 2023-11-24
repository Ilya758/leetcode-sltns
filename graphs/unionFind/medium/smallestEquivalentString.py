class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])

        return self.root[x] 

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootX] = rootY
    
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)

        for i in range(len(s1)):
            uf.union(ord(s1[i]) - 97, ord(s2[i]) - 97)

        return ''.join([chr(uf.find(ord(x) - 97) + 97) for x in baseStr])
        
        

print(Solution().smallestEquivalentString("parker", "morris", "parser")) # 'makkek'