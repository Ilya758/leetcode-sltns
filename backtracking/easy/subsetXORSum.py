from functools import reduce


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        subsets = []
        n = len(nums)

        def bt(node, path):
            if node <= n:
                subsets.append([*path])

                for i in range(node, n):
                    path.append(nums[i])
                    bt(i + 1, path)
                    path.pop()

        bt(0, [])

        return sum([reduce(lambda a, c: a ^ c, x, 0) for x in subsets])

print(Solution().subsetXORSum([1, 3])) # 6

