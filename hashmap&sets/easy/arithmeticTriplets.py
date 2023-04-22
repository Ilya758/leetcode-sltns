# https://leetcode.com/problems/number-of-arithmetic-triplets/description/

def arithmeticTriplets(nums: list[int], diff: int) -> int:
    s = set(nums)
    c = 0

    for num in nums:
        if (num + diff in s and num + diff * 2 in s):
            c += 1

    return c


print(arithmeticTriplets(nums=[0, 1, 4, 6, 7, 10], diff=3))  # 2
