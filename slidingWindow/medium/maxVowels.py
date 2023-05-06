# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

def maxVowels(s: str, k: int) -> int:
    match = {'a', 'e', 'i', 'o', 'u'}
    curr, ans = 0, 0

    for i in range(len(s)):
        if ans == k:
            return ans
        if s[i - k] in match and i >= k:
            curr -= 1
        if s[i] in match:
            curr += 1

        ans = max(ans, curr)

    return ans


print(maxVowels(s="abciiidef", k=3))  # 3
print(maxVowels(s="leetcode", k=3))  # 2
