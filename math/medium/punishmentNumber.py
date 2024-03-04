class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0

        def check(x, y):
            if x == y:
                return True
            
            d = 10

            while x >= d and y >= x %d:
                if check(x // d, y - x % d):
                    return True
                
                d *= 10

            return False

        for num in range(1, n + 1):
            target = num ** 2

            if check(target, num):
                ans += target

        return ans

print(Solution().punishmentNumber(10))