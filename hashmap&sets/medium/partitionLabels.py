# https://leetcode.com/problems/partition-labels/description/

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # 1. store the last index of every char in string
        chars = {char: i for i, char in enumerate(s)}

        # 2. track the maximum possible index of a window
        curMax, left = 0, 0
        ans = []

        for right in range(len(s)):
            curMax = max(curMax, chars[s[right]])

            # 3. every time the indexes of the end of a window met
            # shrink the window and add this partition to ans
            if right == curMax:
                ans.append(right - left + 1)
                left = right + 1

        return ans


print(Solution(s="ababcbacadefegdehijhklij").partitionLabels())  # [9, 7, 8]
