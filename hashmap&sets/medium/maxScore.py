from collections import defaultdict


class Solution:
    def maxScore(self, prices: list[int]) -> int:
        cache = defaultdict(int)

        for i in range(prices):
            cache[prices[i] - i] += prices[i] 

        return max(cache.values())
        
print(Solution().maxScore(prices = [5,6,7,8,9])) # 35