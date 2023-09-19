class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]

        slow = 0

        while slow != fast:
            slow, fast = nums[slow], nums[fast]

        return slow

print(Solution().findDuplicate(nums = [1,3,4,2,2]
)) # 2 