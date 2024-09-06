class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        ans = [0] * (length + 1)

        for start, end, inc in updates:
            ans[start] += inc
            ans[end + 1] -= inc

        for i in range(1, length):
            ans[i] += ans[i - 1]

        return ans[:-1]
    
print(Solution().getModifiedArray(length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]])) # [-2,0,3,5,3]