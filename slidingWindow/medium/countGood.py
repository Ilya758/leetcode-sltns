from collections import defaultdict


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        cache = defaultdict(int)
        ans = c = left = 0

        for num in nums:
            c += cache[num]
            cache[num] += 1

            while c >= k:
                cache[nums[left]] -= 1
                c -= cache[nums[left]]
                left += 1

            ans += left
            
        return ans
    
print(Solution().countGood(nums = [3,1,4,3,2,2,4], k = 2
)) # 4 