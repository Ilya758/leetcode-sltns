class Solution:
    def minDays(self, A: list[int], m: int, k: int) -> int:
        if len(A) < m * k:
            return -1

        left, right = min(A), max(A)
        ans = float('-inf')

        def check(mid):
            x = cur = 0

            for day in A:
                if day >= mid:
                    cur = 0
                else:
                    cur += 1
                    
                if cur == k:
                    x += 1
                    cur = 0

            return x >= m

        while left <= right:
            mid = (left + right) >> 1
            
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
                ans = max(ans, mid)
           
        return ans

print(Solution().minDays(A = [7,7,7,7,12,7,7], m = 2, k = 3)) # 12