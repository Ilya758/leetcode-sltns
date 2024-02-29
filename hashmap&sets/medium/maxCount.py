class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        ans = 0
        nums = [i for i in range(1, n + 1) if i not in banned]

        for num in nums:
            maxSum -= num

            if maxSum < 0:
                break

            ans += 1

        return ans

print(Solution().maxCount([1,6], 10, 9)) # 3