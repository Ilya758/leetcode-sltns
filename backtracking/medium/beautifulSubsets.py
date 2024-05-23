class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        count = [0] * (max(max(nums), k) + 1)

        def bt(i, path):
            if i <= n:
                if path:
                    nonlocal ans
                    ans += 1

            for j in range(i, n):
                diff = nums[j] - k

                if count[diff] <= 0:
                    count[nums[j]] += 1
                    bt(j + 1, path + [nums[j]])
                    count[nums[j]] -= 1

        bt(0, [])

        return ans
    
print(Solution().beautifulSubsets(nums = [10,4,5,7,2,1], k = 3)) # 23