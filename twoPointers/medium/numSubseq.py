
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/


def numSubseq(nums: list[int], target: int) -> int:
    nums.sort()
    ans = 0
    n, mod = len(nums), 10**9 + 7
    left, right = 0, n - 1

    while (left <= right):
        if nums[left] + nums[right] <= target:
            ans = (ans + pow(2, right - left, mod)) % mod
            left += 1
        else:
            right -= 1

    return ans


print(numSubseq(nums=[2, 3, 3, 4, 6, 7], target=12))  # 61
