class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        return len(set([x for x in nums if x > 0]))

