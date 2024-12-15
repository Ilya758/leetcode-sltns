class Solution:
    def widestPairOfIndices(self, nums1: list[int], nums2: list[int]) -> int:
        cache = {0: -1}
        ans = total = 0
        n = len(nums1)

        for i in range(n):
            total += nums1[i] - nums2[i]

            if total in cache:
                ans = max(ans, i - cache[total])
            else:
                cache[total] = i

        return ans
    
print(Solution().widestPairOfIndices(nums1 = [1,1,0,1], nums2 = [0,1,1,0])) # 3