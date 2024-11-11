from math import isqrt


class Solution:
    def isprime(self, n):
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False

        return True

    def primeSubOperation(self, nums):
        curMax = max(nums)
        primes = [0] * (curMax + 1)

        for i in range(2, curMax + 1):
            if self.isprime(i):
                primes[i] = i
            else:
                primes[i] = primes[i - 1]

        for i in range(len(nums)):
            if i == 0:
                bound = nums[0]
            else:
                bound = nums[i] - nums[i - 1]
                
            if bound < 1:
                return False

            nums[i] -= primes[bound - 1]

        return True

print(Solution().primeSubOperation([4,9,6,10])) # True