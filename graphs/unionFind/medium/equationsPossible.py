class UF:
    def __init__(self, n):
        self.rank = [1] * n
        self.root = list(range(n))

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            return self.find(self.root[x])

        return x

    def union(self, x, y):
        a, b = self.find(x), self.find(y)

        if a != b:
            if self.rank[a] >= self.rank[b]:
                self.rank[a] += self.rank[b]
                self.root[b] = a
            else:
                self.rank[b] += self.rank[a]
                self.root[a] = b

        return True

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        uf = UF(26)

        def convert(a, b):
            return (ord(a) - 97, ord(b) - 97)

        for eq in equations:
            if eq[1] == '=':
                uf.union(*convert(eq[0], eq[3]))

        for eq in equations:
            if eq[1] == '!' and uf.isConnected(*convert(eq[0], eq[3])):
                return False
            
        return True
    
print(Solution().equationsPossible(equations = ["a==b","b!=a"])) # False