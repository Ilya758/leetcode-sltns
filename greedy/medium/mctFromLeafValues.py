class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        ans = 0

        while len(arr) > 1:
            i = arr.index(min(arr))

            curLeft, curRight = float('inf'), float('inf')

            if i - 1 >= 0:
                curLeft = arr[i - 1]

            if i + 1 < len(arr):
                curRight = arr[i + 1]

            ans += min(curLeft, curRight) * arr[i]
            arr.pop(i)

        return ans
    
print(Solution().mctFromLeafValues(arr = [6,2,4])) # 32