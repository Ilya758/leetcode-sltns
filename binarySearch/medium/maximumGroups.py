class Solution:
    def maximumGroups(self, grades: list[int]) -> int:
        def check(k):
            return ((k * (k + 1)) // 2) > len(grades) 

        left, right = 0, 10e5

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return int(left) - 1

print(Solution().maximumGroups([10,6,12,7,3,5])) # 3