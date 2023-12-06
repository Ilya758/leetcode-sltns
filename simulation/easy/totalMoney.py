class Solution:
    def totalMoney(self, n: int) -> int:
        c = 0
        ans = 0

        while n > 0:
            diff = 7 if max(n - 7, 0) else n
            ans += c * diff + (diff * (diff + 1) // 2) 
            c += 1
            n -= 7

        return ans 

print(Solution().totalMoney(n = 4)) # 10