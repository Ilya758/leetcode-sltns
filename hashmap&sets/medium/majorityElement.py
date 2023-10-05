from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        return [k for k, v in Counter(nums).items() if v > len(nums) / 3]

print(Solution().majorityElement(nums = [3,2,3]
)) # 3