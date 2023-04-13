# https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/

def divisorSubstrings(num: int, k: int) -> int:
    s = str(num)
    ans = 0

    for i in range(k, len(s) + 1):
        n = int(s[i - k:i])

        if n and num % n == 0:
            ans += 1

    return ans


print(divisorSubstrings(num=240, k=2))  # 2
print(divisorSubstrings(num=430043, k=2))  # 2
