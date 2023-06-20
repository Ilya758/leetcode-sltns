from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        left = 0
        count = 0
        chars = defaultdict(int)

        for right in range(len(s2)):
            chars[s2[right]] += 1
            count += 1

            while (s2[right] not in freq and left < right) or count > len(s1):
                if chars[s2[left]]:
                    chars[s2[left]] -= 1

                left += 1

                if count:
                    count -= 1

            if count >= len(s1):
                allIncluded = True

                for k in freq:
                    if k not in chars or (k in chars and chars[k] < freq[k]):
                        allIncluded = False

                if allIncluded:
                    return True

        return False


print(Solution().checkInclusion(s1="ab", s2="eidbaooo"))  # True
print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))  # False
