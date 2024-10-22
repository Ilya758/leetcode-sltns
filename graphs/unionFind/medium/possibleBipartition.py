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

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        adj = [[] for _ in range(n + 1)]
        
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])
        
        dsu = UF(n + 1)

        for node in range(1, n + 1):
            for neighbor in adj[node]:
                if dsu.find(node) == dsu.find(neighbor): return False
                
                if adj[node][0] != neighbor:
                    dsu.union(adj[node][0], neighbor)
        
        return True
        

        
    
print(Solution().possibleBipartition(n = 3, dislikes = [[1,2],[1,3],[2,3]])) # False