class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = [] 
        nums = set(to_delete)

        def dfs(node, isRoot):
            if node:
                deleted = node.val in nums
                
                if isRoot and not deleted:
                    ans.append(node)
                
                node.left = dfs(node.left, deleted)
                node.right = dfs(node.right, deleted)
                
                return None if deleted else node

            return None

        dfs(root, root.val not in nums)
        
        return ans
