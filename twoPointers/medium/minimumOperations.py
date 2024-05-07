class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        i, j = 0, len(nums) - 1
        ans = 0

        while i < j:
            a, b = nums[i], nums[j]

            if a == b:
                i += 1
                j -= 1
            elif a > b:
                ans += 1
                j -= 1
                nums[j] += b
            else: 
                ans += 1
                i += 1
                nums[i] += a

        return ans
    
print(Solution().minimumOperations([4,3,2,1,2,3,1])) # 2