# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i - k - 1])

            if nums[i] in window:
                return True

            window.add(nums[i])

        return False


print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))  # True
print(Solution().containsNearbyDuplicate(
    nums=[1, 2, 3, 1, 2, 3], k=2))  # False
