from collections import defaultdict


class Solution:

    def __init__(self, nums: list[int]):
        cache = defaultdict(list)
        scheduler = defaultdict(int)

        for i, num in enumerate(nums):
            cache[num].append(i)

        self.cache = cache
        self.scheduler = scheduler        

    def pick(self, target: int) -> int:
        idx = self.scheduler[target]
        self.scheduler[target] = (self.scheduler[target] + 1) % len(self.cache[target])
        
        return self.cache[target][idx]