class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n = len(gain)
        prefix = [gain[0]] * n
        ans = gain[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + gain[i]
            ans = max(ans, prefix[i], 0)

        return ans


print(Solution().largestAltitude(gain=[-5, 1, 5, 0, -7]))  # 1
