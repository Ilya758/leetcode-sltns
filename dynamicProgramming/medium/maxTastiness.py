from functools import cache


class Solution:
    def maxTastiness(self, price: list[int], tastiness: list[int], maxAmount: int, maxCoupons: int) -> int:
        @cache
        def dp(i, mxA, mxC):
            if mxA < 0 or mxC < 0:
                return float('-inf')
            if i == len(price):
                return 0

            tasty = tastiness[i] 
            res = dp(i + 1, mxA, mxC)

            if mxA - price[i] >= 0:
                res = max(res, tasty + dp(i + 1, mxA - price[i], mxC))
            if mxC:
                res = max(res, tasty + dp(i + 1, mxA - price[i] // 2, mxC - 1))
            
            return res

        return dp(0, maxAmount, maxCoupons)
    
print(Solution().maxTastiness(price = [10,20,20], tastiness = [5,8,8], maxAmount = 20, maxCoupons = 1)) # 13