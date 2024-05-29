class Solution:
    def reverseWords(self, s: list[str]) -> None:
        n = len(s)
        left, right = 0, n - 1

        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        i = 0

        for j in range(n + 1):
            if j == n or s[j] == ' ':
                left, right = i, j - 1

                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1

                i = j + 1

        print(s)

Solution().reverseWords(s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]) # ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
