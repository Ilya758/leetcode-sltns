class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: list[int]) -> List[int]:
        heights = [0] * 100001
        self.curMax = 0

        def ltr(node, h):
            if node:
                heights[node.val] = self.curMax
                self.curMax = max(self.curMax, h)
                ltr(node.left, h + 1)
                ltr(node.right, h + 1)
        
        def rtl(node, h):
            if node:
                heights[node.val] = max(heights[node.val], self.curMax)
                self.curMax = max(self.curMax, h)
                rtl(node.right, h + 1)
                rtl(node.left, h + 1)

        ltr(root, 0)
        self.curMax = 0
        rtl(root, 0)

        return [heights[q] for q in queries]