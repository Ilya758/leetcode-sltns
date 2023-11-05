class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        ans = arr[0]
        count = 0

        for i in range(1, len(arr)):
            if arr[i] > ans:
                ans = arr[i]
                count = 1
            else:
                count += 1

            if count == k:
                break

        return ans

print(Solution().getWinner(arr = [2,1,3,5,4,6,7], k = 2))