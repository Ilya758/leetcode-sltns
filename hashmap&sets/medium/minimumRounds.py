from math import ceil
from typing import Counter


class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        tasks = Counter(tasks)
        
        return -1 if 1 in tasks.values() else sum([ceil(x/3) for x in tasks.values()])

print(Solution().minimumRounds(tasks = [2,2,3,3,2,4,4,4,4,4])) # 4