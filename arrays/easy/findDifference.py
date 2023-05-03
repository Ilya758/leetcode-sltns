# https://leetcode.com/problems/find-the-difference-of-two-arrays/

def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set1 = set(nums1)
    set2 = set(nums2)

    return [set1.difference(set2), set2.difference(set1)]


print(findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))  # [[1,3],[4,6]]
print(findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]))  # [[3],[]]
