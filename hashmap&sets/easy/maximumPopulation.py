# https://leetcode.com/problems/maximum-population-year/

from collections import defaultdict


class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        cache = defaultdict(int)

        for b, d in logs:
            for year in range(b, d):
                cache[year] += 1

        ans = [float('inf'), float('-inf')]

        for year, pop in cache.items():
            if ans[1] < pop or (ans[1] == pop and year < ans[0]):
                ans = [year, pop]

        return ans[0]


print(Solution().maximumPopulation(logs=[[1993, 1999], [2000, 2010]]))  # 1993
print(Solution().maximumPopulation(
    logs=[[1950, 1961], [1960, 1971], [1970, 1981]]))  # 1960
