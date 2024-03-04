class Solution:
    def bagOfTokensScore(self, A: list[int], power: int) -> int:
        ans = 0
        curMax = 0
        left, right = 0, len(A) - 1
        A.sort()

        while left <= right:
            cur = A[left]

            if power - cur >= 0:
                left += 1
                curMax += 1
                power -= cur
            else:
                if curMax:
                    power += A[right]
                    right -= 1
                    curMax -= 1
                else:
                    left += 1

            ans = max(ans, curMax)

        return ans
    
print(Solution().bagOfTokensScore(A = [100,200,300,400], power = 200)) # 2