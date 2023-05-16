# https://leetcode.com/problems/guess-number-higher-or-lower/

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n

        while left <= right:
            mid = (left + right) // 2
            # use the helper API to find an answer
            ans = guess(mid)

            match ans:
                case 1:
                    left = mid + 1
                case -1:
                    right = mid - 1
                case _:
                    return mid
