from collections import defaultdict


class Solution:
    def maximumBeauty(self, flowers):
        prefix = [0]
        cache = defaultdict(int)
        ans = 0

        for idx, flower in enumerate(flowers):
            a = flower if flower >= 0 else 0
            b = flower if flower < 0 else 0
            prefix.append(prefix[-1] + a)
        
            if not flower in cache:
                cache[flower] = idx
            else:
                curSum = 2 * b + prefix[idx + 1] - prefix[cache[flower]]
                ans = max(ans, curSum)

        return ans

print(Solution().maximumBeauty([1,2,3,1,2])) # 8