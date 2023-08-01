class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def numberToBase(n, b):
            if n == 0:
                return [0]
            digits = []

            while n:
                digits.append(int(n % b))
                n //= b
            return "".join(map(str, digits[::-1]))

        for i in range(n - 2, 1, -1):
            num = numberToBase(n, i)

            left = 0
            right = len(num) - 1

            while left <= right:
                if num[left] == num[right]:
                    left += 1
                    right -= 1

                return False

        return True


print(Solution().isStrictlyPalindromic(n=9))  # False
print(Solution().isStrictlyPalindromic(n=4))  # False
