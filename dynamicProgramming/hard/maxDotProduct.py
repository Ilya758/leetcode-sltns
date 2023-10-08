from functools import cache


class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        @cache
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            
            use = nums1[i] * nums2[j] + dp(i + 1, j + 1)
            return max(use, dp(i + 1, j), dp(i, j + 1))
        
        return dp(0, 0)
    
print(Solution().maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6])) # 18