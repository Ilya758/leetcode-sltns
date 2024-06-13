class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q: return 0

        def find(node):
            if not node:
                return None

            left = find(node.left)
            right = find(node.right)

            if node.val in [p, q] or (left and right):
                return node

            return left or right

        lca = find(root)
        
        def findDepth(node, val, depth = 0):
            if not node:
                return -1
            if node.val == val:
                return depth

            left = findDepth(node.left, val, depth + 1)

            if left != -1:
                return left
                
            return findDepth(node.right, val, depth + 1) 

        return findDepth(lca, p) + findDepth(lca, q)
