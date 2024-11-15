class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        n = len(arr)
        right = n - 1

        while right and arr[right - 1] <= arr[right]:
            right -= 1

        ans = right
        left = 0

        while left < right and (not left or arr[left] >= arr[left - 1]):
            while right < n and arr[left] > arr[right]:
                right += 1

            ans = min(ans, right - left - 1)
            left += 1
        
        return ans

print(Solution().findLengthOfShortestSubarray([1,2,3,10,4,2,3,5])) # 3

