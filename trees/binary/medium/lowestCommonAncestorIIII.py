class Solution:
    def lowestCommonAncestorIIII(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)

        def find(node):
            if node in nodes:
                return node

            left = find(node.left)
            right = find(node.right)

            if left and right:
                return node
            else:
                return left or right

        return find(root)
