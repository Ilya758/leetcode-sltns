class Solution:
    def threeSumSmaller(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans = 0
        n = len(nums)

        for i in range(n - 2):
            a = nums[i]
            left, right = i + 1, n - 1

            while left < right:
                if a + nums[left] + nums[right] < target:
                    ans += right - left
                    left += 1
                else:
                    right -= 1          

        return ans
    
print(Solution().threeSumSmaller(nums = [-2,0,1,3], target = 2)) # 2