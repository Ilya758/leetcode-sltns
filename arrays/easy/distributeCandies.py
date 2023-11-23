class Solution:
    def distributeCandies(self, n, limit):
        ways = 0

        for i in range(min(n, limit) + 1):
            for j in range(min(n - i, limit) + 1):
                if n - i - j <= limit:
                    ways += 1
                    
        return ways
    
print(Solution().distributeCandies(5, 2)) # 3