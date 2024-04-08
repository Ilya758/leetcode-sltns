class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(lst, node):
            if not lst:
                return True
            if not node:
                return False
            return node.val == lst.val and (dfs(lst.next, node.left) or dfs(lst.next, node.right))

        def traverse(node):
            if not node:
                return False
            return dfs(head, node) or traverse(node.left) or traverse(node.right)

        return traverse(root)