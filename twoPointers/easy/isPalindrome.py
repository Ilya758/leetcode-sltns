import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clearStr = re.sub('[\W_]*', '', s).lower()

        left = 0
        right = len(clearStr) - 1

        while left <= right:
            if clearStr[left] != clearStr[right]:
                return False

            left += 1
            right -= 1

        return True


print(Solution().isPalindrome(s="A man, a plan, a canal: Panama"))  # True
