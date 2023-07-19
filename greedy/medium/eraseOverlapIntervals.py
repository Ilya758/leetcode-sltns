# https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # since we're only care about non-overlaping intervals
        # assume the 'champion' segment => such that it's
        # ending point is the first across all other
        intervals.sort(key=lambda x: x[1])
        last = 0
        excluded = 0

        for i in range(1, len(intervals)):
            if intervals[last][1] > intervals[i][0]:
                excluded += 1
            else:
                last = i

        return excluded


print(Solution().eraseOverlapIntervals(
    intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))  # 1
print(Solution().eraseOverlapIntervals(
    intervals=[[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2], [30, 47], [-40, -26]]))  # 7
