# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

def isCovered(ranges: list[list[int]], left: int, right: int) -> bool:
    count = 0
    num = left
    ptr = 0

    while num <= right:
        if ranges[ptr][0] <= num <= ranges[ptr][1]:
            count += 1
            ptr = 0
            num += 1
        else:
            ptr += 1

            if ptr >= len(ranges):
                ptr = 0
                num += 1

    return count == right - left + 1


print(isCovered(ranges=[[1, 2], [3, 4], [5, 6]], left=2, right=5))  # True
print(isCovered(ranges=[[1, 10], [10, 20]], left=21, right=21))  # False
