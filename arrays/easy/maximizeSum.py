# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        return max(nums) * k + k * (k - 1) // 2


print(Solution().maximizeSum(nums=[1, 2, 3, 4, 5], k=3))  # 18
print(Solution().maximizeSum(nums=[5, 5, 5], k=2))  # 11
