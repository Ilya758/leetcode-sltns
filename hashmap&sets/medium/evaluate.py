# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        map = dict()

        for k, v in knowledge:
            map[k] = v

        key = ''
        ans = ''
        isOpened = False

        for char in s:
            if char == '(':
                isOpened = True
            elif char == ')':
                isOpened = False
                ans += map.get(key, '?')
                key = ''
            elif isOpened:
                key += char
            else:
                ans += char

        return ans


print(Solution().evaluate(s="(name)is(age)yearsold", knowledge=[
      ["name", "bob"], ["age", "two"]
      ]))  # bobistwoyearsold
