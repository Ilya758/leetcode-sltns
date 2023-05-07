def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


print(containsDuplicate(nums=[1, 2, 3, 1]))  # True
print(containsDuplicate(nums=[1, 2, 3, 4]))  # False
