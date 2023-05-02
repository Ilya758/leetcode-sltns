# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

def arraySign(nums: list[int]) -> int:
    sign = 1

    for num in nums:
        if num == 0:
            return 0
        elif num < 0:
            sign *= -1

    return sign


print(arraySign(nums=[-1, -2, -3, -4, 3, 2, 1]))  # 1
print(arraySign(nums=[1, 5, 0, 2, -3]))  # 0
