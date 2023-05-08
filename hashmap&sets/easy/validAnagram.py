from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map = defaultdict(int)

    for i in range(len(s)):
        map[s[i]] += 1
        map[t[i]] -= 1

    for key in map:
        if map[key] != 0:
            return False

    return True


print(isAnagram(s="anagram", t="nagaram"))  # True

print(isAnagram(s="anagram", t="nagaram"))  # True
print(isAnagram(s="rat", t="car"))  # False
