class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.ans = ''

        def backtrack(path):
            nonlocal k

            if k == 0: return

            if len(path) == n:
                k -= 1
                self.ans = "".join(path)
                return

            for i in range(3):
                char = chr(97 + i)

                if not path or path[-1] != char:
                    path.append(char)
                    backtrack(path)
                    path.pop()
    
        backtrack([])

        return self.ans if not k else ''
    
print(Solution().getHappyString(n = 3, k = 9)) # 'cab