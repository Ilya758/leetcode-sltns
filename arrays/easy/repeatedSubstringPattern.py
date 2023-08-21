class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # if we concatenate string with itself,
        # it's possible that the chunk exists
        # inside of that concatenation excluding
        # the leftmost and the rightmost characters,
        # otherwise cases like 'aba' | 'abcba'
        # will return True instead of False
        return s in (s + s)[1:-1]


print(Solution().repeatedSubstringPattern('abcabc'))  # True
