from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = set(wordDict)
        queue = deque([0])
        seen = set()

        # this approach is one of possible
        # another solutions required writing DP or PrefixTrie
        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue

                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)

        return False


print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))  # True
print(Solution().wordBreak(s="catsandog", wordDict=[
      "cats", "dog", "sand", "and", "cat"]))  # False
