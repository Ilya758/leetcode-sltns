class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        n = len(s)

        def parse(index):
            if index >= n:
                return None, index

            start = index

            if s[index] == '-':
                index += 1

            while index < n and s[index].isdigit():
                index += 1

            root = TreeNode(int(s[start:index]))

            if index < n and s[index] == '(':
                root.left, i = parse(index + 1)
                index = i + 1        
            if index < n and s[index] == '(':
                root.right, i = parse(index + 1)
                index = i + 1        

            return root, index

        return parse(0)[0]