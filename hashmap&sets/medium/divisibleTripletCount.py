from collections import defaultdict


class Solution:
    def divisibleTripletCount(self, nums: list[int], d: int) -> int:
        cache = defaultdict(list)
        ans = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                cache[(nums[i] + nums[j]) % d].append(j)

        for k in range(2, len(nums)):
            target = nums[k] % d
            key = (d - target) % d
            ans += sum(1 for i in cache[key] if i < k)

        return ans
        
print(Solution().divisibleTripletCount(nums = [1,2,3,4,5,6], d = 3)) # 8