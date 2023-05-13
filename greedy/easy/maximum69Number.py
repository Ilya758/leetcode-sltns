# https://leetcode.com/problems/maximum-69-number/description/

class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)

        for i in range(len(s)):
            if s[i] == '6':
                return int(s[:i] + '9' + s[i + 1:])

        return int(s)


print(Solution().maximum69Number(num=9669))  # 9969
