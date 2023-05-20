# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        chars = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz',
        }

        ans = []

        def backtrack(i=0, path=[]):
            if i == len(digits):
                if len(path):
                    ans.append("".join(path[:]))

                return

            for char in chars[int(digits[i])]:
                path.append(char)
                backtrack(i + 1, path)
                path.pop()

        backtrack()

        return ans


print(Solution().letterCombinations(digits="23"))
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]
