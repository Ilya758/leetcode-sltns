class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(goal):
            left, cur, count = 0, 0, 0

            for right in range(len(nums)):
                cur += nums[right]

                while left <= right and cur > goal:
                    cur -= nums[left]
                    left += 1

                count += right - left + 1

            return count

        return helper(goal) - helper(goal - 1)
    
print(Solution().numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2)) # 4