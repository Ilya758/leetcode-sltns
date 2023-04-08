# the first approach - slow, but clear
def leftRightDifference(nums: list[int]) -> list[int]:
    n = len(nums)
    left = [0] * n
    right = [0] * n

    for i in range(1, n):
        left[i] = nums[i - 1] + left[i - 1]
        right[n - 1 - i] = nums[n - i] + right[n - i]

    return [abs(left[i] - right[i]) for i in range(n)]


print(leftRightDifference([10, 4, 8, 3]))  # [15,1,11,22]
print(leftRightDifference([1]))  # [0]

# the second one, more faster


def leftRightDifference(nums: list[int]) -> list[int]:
    left = 0
    right = sum(nums)

    for i, value in enumerate(nums):
        left += value
        nums[i] = abs(left - right)
        right -= value

    return nums
