def findMiddleIndex(nums: list[int]) -> int:
    left = 0
    right = sum(nums)

    for i, value in enumerate(nums):
        left += value

        if right == left:
            return i

        right -= value

    return -1


print(findMiddleIndex([2, 3, -1, 8, 4]))  # 3
print(findMiddleIndex([1, -1, 4]))  # 2
