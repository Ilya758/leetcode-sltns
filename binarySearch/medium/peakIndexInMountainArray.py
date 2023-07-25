# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if 0 < mid < len(arr) - 1:
                if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                    return mid
                elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif mid == 0:
                if arr[mid] > arr[mid + 1]:
                    return mid
                else:
                    left = mid + 1
            else:
                if arr[mid] > arr[mid - 1]:
                    return mid
                else:
                    right = mid - 1

        return -1


print(Solution().peakIndexInMountainArray(arr=[0, 1, 0]))  # 1
print(Solution().peakIndexInMountainArray(arr=[3, 2, 1, 0]))  # 0
print(Solution().peakIndexInMountainArray(arr=[0, 1, 2, 3]))  # 3
