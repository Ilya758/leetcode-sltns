class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        left = -1
        n = len(nums)
        ans = [-1] * n
        prefix = [nums[0]] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        for right in range(k, n - k):
            before = 0 if left == -1 else prefix[left]
            ans[right] = (prefix[k + right] - before) // (2 * k + 1)
            left += 1

        return ans


print(Solution().getAverages(nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3))
# [-1,-1,-1,5,4,4,-1,-1,-1]
print(Solution().getAverages(nums=[100000], k=0))  # [100000]
print(Solution().getAverages(nums=[8], k=100000))  # [-1]
