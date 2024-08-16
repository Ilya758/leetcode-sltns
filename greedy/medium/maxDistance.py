class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        ans = 0
        curMin, curMax = arrays[0][0], arrays[0][-1]

        for i in range(1, len(arrays)):
            minDiff = abs(arrays[i][-1] - curMin)
            maxDiff = abs(curMax - arrays[i][0])
            ans = max(ans, minDiff, maxDiff)
            curMin = min(curMin, arrays[i][0])
            curMax = max(curMax, arrays[i][-1])
        
        return ans
    
print(Solution().maxDistance(arrays = [[1,2,3],[4,5],[1,2,3]])) # 4