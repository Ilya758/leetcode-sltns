# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/

def minimumSum(num: int) -> int:
    nums: list[int] = list(map(int, str(num)))
    nums = sorted(nums)

    return nums[0] * 10 + nums[2] + nums[1] * 10 + nums[3]


print(minimumSum(2932))  # 52
print(minimumSum(4009))  # 13
