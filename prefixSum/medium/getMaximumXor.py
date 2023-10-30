class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        k = 2 ** maximumBit - 1
        prefix = [nums[0]]
        n = len(nums)

        for i in range(1, n): prefix.append(prefix[i - 1] ^ nums[i])

        ans = []
        
        for i in range(n - 1, -1, -1):
            ans.append(prefix[i] ^ k)

        return ans

print(Solution().getMaximumXor(nums = [0,1,1,3], maximumBit = 2
)) # [0,3,2,3]