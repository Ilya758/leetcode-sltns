class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def fibo(k):
            dp = [0, 1]

            while dp[-1] < k:
                dp.append(dp[-1] + dp[-2])

            return dp
        
        seq = fibo(k)
        ans = 0

        for num in seq[::-1]:
            if k == 0:
                break
            if num > k:
                continue
                
            c = k // num
            ans += c
            k -= c * num

        return ans
        

print(Solution().findMinFibonacciNumbers(7)) # 2
