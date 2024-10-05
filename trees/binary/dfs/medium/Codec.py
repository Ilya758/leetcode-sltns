from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        def dfs(root):
            if not root:
                return ["None,"]

            return [str(root.val) + ","] + \
            dfs(root.left) + dfs(root.right)

        return ''.join(dfs(root))
        

    def deserialize(self, data):
        data = deque([x for x in data.split(',') if x])
        
        def dfs():
            val = data.popleft()
            
            if val == 'None':
                return None
            
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()
            
            return root

        return dfs()
            