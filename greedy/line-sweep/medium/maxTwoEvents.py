class Solution:
    def maxTwoEvents(self, A: list[list[int]]) -> int:
        events = []

        for s, e, v in A:
            events.append([s, 1, v])
            events.append([e + 1, 0, v])

        ans = curMax = 0
        events.sort()

        for _, f, v in events:
            if f:
                ans = max(ans, v + curMax)
            else:
                curMax = max(curMax, v)

        return ans
    
print(Solution().maxTwoEvents([[1,2,4],[3,4,3],[2,3,1]])) # 7