class Solution:
    def validateBinaryTreeNodes(self, n: int, left: list[int], right: list[int]) -> bool:
        def findRoot():
            children = set(left) | set(right)

            for i in range(n):
                if i not in children: return i

            return -1
        
        root = findRoot()

        if root == -1: return False

        seen = {root}
        stack = [root]

        while stack:
            node = stack.pop()

            for i in [left[node], right[node]]:
                if i != -1:
                    if i in seen: 
                        return False

                    seen.add(i)
                    stack.append(i)

        return len(seen) == n
    
print(Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1])) # True