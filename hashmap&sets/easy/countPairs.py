from collections import defaultdict


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        d = defaultdict(list)
        count = 0

        for i, n in enumerate(nums):
            if n in d:
                for index in d[n]:
                    if index * i % k == 0:
                        count += 1
            d[n].append(i)
    
        return count
    
print(Solution().countPairs([3,1,2,2,2,1,3], k = 2)) # 4