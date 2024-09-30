class Solution:
    def removeCoveredIntervals(self, A: list[list[int]]) -> int:
        A.sort(key=lambda x: [x[0], -x[1]])
        ans = 0
        end = 0

        for i in A:
            if i[1] > end:
                end = i[1]
                ans += 1

        return ans
    
print(Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]])) # 2