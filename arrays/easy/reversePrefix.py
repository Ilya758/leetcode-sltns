# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = -1

        for j in range(len(word)):
            if word[j] == ch:
                i = j
                break

        if i == -1:
            return word

        return word[:i + 1][::-1] + word[i + 1:]


print(Solution().reversePrefix(word="abcdefd", ch="d"))  # dcbaefd
