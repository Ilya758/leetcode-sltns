from typing import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        chars = [0] * 26
        lap, count, ans = 1, 0, 0
        cache = sorted(Counter(word).items(), key=lambda x: -x[1])

        for k, v in cache:
            chars[ord(k) - 97] = lap
            count = (count + 1) % 8
            ans += lap * v

            if not count:
                lap += 1

        return ans

print(Solution().minimumPushes("abcde")) # 5