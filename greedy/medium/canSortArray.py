class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        def get(x):
            res = 0  

            while x:
                x &= x - 1
                res += 1

            return res
    
        count = 0
        segments = []
        i = -1

        for num in nums:
            x = get(num)

            if count == x:
                segments[i][0] = min(segments[i][0], num)
                segments[i][1] = max(segments[i][1], num)
            else:
                i += 1
                segments.append([num, num])
                count = x
    
        for i in range(len(segments) - 1):
            if segments[i][1] > segments[i + 1][0]:
                return False

        return True

print(Solution().canSortArray([3,16,8,4,2])) # False