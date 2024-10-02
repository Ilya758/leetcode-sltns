class Solution:
    def maxSumRangeQuery(self, nums: list[int], requests: list[list[int]]) -> int:
        ans = 0
        n = len(nums)
        events = [0] * (n + 1)

        for a, b in requests:
            events[a] += 1
            events[b + 1] -= 1

        for i in range(1, n + 1):
            events[i] += events[i - 1]

        for k, v in zip(sorted(events[:-1]), sorted(nums)):
            ans += k * v

        return ans % (10 ** 9 + 7)
    
print(Solution().maxSumRangeQuery(nums = [1,2,3,4,5], requests = [[1,3],[0,1]])) # 19