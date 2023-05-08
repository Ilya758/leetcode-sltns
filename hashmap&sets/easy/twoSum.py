
def twoSum(nums: list[int], target: int) -> list[int]:
    map = {}

    for i, val in enumerate(nums):
        diff = target - val

        if diff in map:
            return [map[diff], i]

        map[val] = i

    return []


print(twoSum(nums=[2, 7, 11, 15], target=9))  # [0, 1]
