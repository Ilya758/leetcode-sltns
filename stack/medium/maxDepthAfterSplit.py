class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = [0] * len(seq)
        depth = 0

        for i in range(len(seq)):
            if seq[i] == '(':
                depth += 1

                if depth % 2 == 0:
                    ans[i] = 1
            else:
                if depth % 2 == 0:
                    ans[i] = 1

                depth -= 1
                
        return ans

print(Solution().maxDepthAfterSplit(seq = "()(())()"))