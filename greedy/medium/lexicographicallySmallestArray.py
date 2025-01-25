from collections import defaultdict, deque


class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        groups = defaultdict(deque)
        numToGroup = defaultdict(int)
        idx = 0
        sortedNums = sorted(nums)
        numToGroup[sortedNums[0]] = 0
        groups[0].append(sortedNums[0])

        for i in range(1, n):
            if abs(sortedNums[i] - sortedNums[i - 1]) > limit:
                idx += 1

            numToGroup[sortedNums[i]] = idx
            groups[idx].append(sortedNums[i]) 

        
        for i in range(n):
            num = nums[i]
            group = numToGroup[num]
            nums[i] = groups[group].popleft()

        return nums

print(Solution().lexicographicallySmallestArray(nums = [1,7,6,18,2,1], limit = 3))