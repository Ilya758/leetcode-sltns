# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        cache = {}
        ans = 1

        for num in arr:
            prev = cache.get(num - difference, 0)
            cache[num] = prev + 1
            ans = max(ans, cache[num])

        return ans
