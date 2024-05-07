class Solution:
    def lowestCommonAncestorIII(self, p: 'Node', q: 'Node') -> 'Node':
        path = set()

        while p:
            path.add(p)
            p = p.parent

        while q and q not in path:
            q = q.parent
        
        return q