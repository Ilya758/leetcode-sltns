# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

def numberOfSubstrings(s: str) -> int:
    chars = {'a': 0, 'b': 0, 'c': 0}
    left = right = ans = 0
    n = len(s)

    while left <= n - len(chars):
        if chars['a'] and chars['b'] and chars['c']:
            ans += n - right + 1
            chars[s[left]] -= 1
            left += 1
        else:
            if right < n:
                chars[s[right]] += 1
                right += 1
            else:
                break

    return ans


print(numberOfSubstrings(s="abcabc"))  # 10
print(numberOfSubstrings(s="aaacb"))  # 3
