class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            w, h = 0, 0

            for j in range(i - 1, -1, -1):
                w += books[j][0]

                if w > shelfWidth:
                    break

                h = max(h, books[j][1])
                dp[i] = min(dp[i], dp[j] + h)

        return dp[n]
    
print(Solution().minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4)) # 6