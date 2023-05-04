# https://leetcode.com/problems/delete-node-in-a-bst/

def deleteNode(self, root, key):
    if not root:
        return None

    if key > root.val:
        root.right = self.deleteNode(root.right, key)
    elif key < root.val:
        root.left = self.deleteNode(root.left, key)
    else:
        if not root.left or not root.right:
            return root.right or root.left

        node = root.right

        while node.left:
            node = node.left

        node.left = root.left

        return root.right

    return root
