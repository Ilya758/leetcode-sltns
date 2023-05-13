# https://leetcode.com/problems/maximum-units-on-a-truck/description/

class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda a: a[1], reverse=True)
        i = 0
        ans = 0

        while truckSize and i < len(boxTypes):
            a, b = boxTypes[i]

            if truckSize < a:
                ans += truckSize * b
                break

            truckSize -= a
            ans += a * b
            i += 1

        return ans


print(Solution().maximumUnits(
    boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4))  # 8
