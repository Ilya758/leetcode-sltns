class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        n = len(nums)

        def bt(i, path):
            if len(path) > 1:
                ans.add(tuple(path))
            if i == n:
                return

            for j in range(i, n):
                if path[-1] <= nums[j]:
                    path.append(nums[j])
                    bt(j + 1, path)
                    path.pop()

        for i in range(n):
            bt(i + 1, [nums[i]])

        return ans
    
print(Solution().findSubsequences([4,6,7,7])) # [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]