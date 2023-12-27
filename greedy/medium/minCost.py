class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total = curMax = neededTime[0]
        ans = 0

        for i in range(1, len(colors)):
            if colors[i] != colors[i - 1]:
                ans += total - curMax
                total = curMax = neededTime[i]
            elif curMax < neededTime[i]:
                curMax = neededTime[i]
                total += curMax
            else:
                total += neededTime[i]

        return ans + total - curMax

print(Solution().minCost(colors = "aaabbbabbbb",neededTime = [3,5,10,7,5,3,5,5,4,8,1])) # 26
