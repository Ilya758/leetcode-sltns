def minimumDifference(nums: list[int], k: int) -> int:
    if (len(nums) == 1):
        return 0

    nums = sorted(nums)
    ans = nums[k - 1] - nums[0]

    for i in range(k, len(nums)):
        ans = min(ans, nums[i] - nums[i - k + 1])

    return ans


print(minimumDifference(nums=[90], k=1))  # 0
print(minimumDifference(nums=[9, 4, 1, 7], k=2))  # 2
