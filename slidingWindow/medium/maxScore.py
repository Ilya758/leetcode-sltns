class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        
        if n == k:
            return total

        cur = sum(cardPoints[:n-k])
        minSum = cur
        
        for i in range(n - k, n):
            cur += cardPoints[i] - cardPoints[i - n + k]
            minSum = min(minSum, cur)

        return total - minSum

print(Solution().maxScore(A = [1,2,3,4,5,6,1], k = 3)) # 12