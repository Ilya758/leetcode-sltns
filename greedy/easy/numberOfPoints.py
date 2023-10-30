class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        nums.sort(key=lambda start: start[0])
        left, right = nums[0]
        ans = right - left + 1

        for i in range(1, len(nums)):
            a, b = nums[i]

            if right > a:
                ans += max(b - right, 0)
            else:
                ans += b - a + int(right != a)
            
            left, right = a, max(right, b)
            
        return ans
    
print(Solution().numberOfPoints(nums = [[3,6],[1,5],[4,7]]
)) # 7