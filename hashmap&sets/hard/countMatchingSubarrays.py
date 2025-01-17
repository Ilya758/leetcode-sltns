class Solution:
    def get(self, nums):
        res = []

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                res.append(0)
            else:
                res.append(1 if nums[i] > nums[i - 1] else -1)

        return res

    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        n, m = len(nums), len(pattern)
        prev, i = 0, 1
        lps = [0] * m

        while i < m:
            if pattern[i] == pattern[prev]:
                prev += 1
                lps[i] = prev
                i += 1
            elif prev:
                prev = lps[prev - 1]
            else:
                i += 1

        ans = 0
        i = j = 0
        nums = self.get(nums)

        while i < n - 1:
            if nums[i] == pattern[j]:
                i += 1
                j += 1

                if j == m:
                    ans += 1
                    j = lps[j - 1]
            elif j:
                j = lps[j - 1]
            else:
                i += 1

        return ans

print(Solution().countMatchingSubarrays(nums = [1,2,3,4,5,6], pattern = [1,1])) # 4