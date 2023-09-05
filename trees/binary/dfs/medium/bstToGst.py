class Solution:
    prefix = 0

    def bstToGst(self, root):
        if root != None:
            self.bstToGst(root.right)
            self.prefix += root.val
            root.val = self.prefix
            self.bstToGst(root.left)

        return root