from collections import Counter


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        prefix = Counter(nums)

        for i in range(prefix[0]): nums[i] = 0

        prefix[1] += prefix[0]

        for i in range(prefix[0], prefix[1]): nums[i] = 1

        prefix[2] += prefix[1]

        for i in range(prefix[1], prefix[2]): nums[i] = 2
        
print(Solution().sortColors(nums = [2,0,2,1,1,0]))