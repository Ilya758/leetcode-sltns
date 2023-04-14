from cmath import inf

# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/


def minimumRecolors(blocks: str, k: int) -> int:
    n = len(blocks)
    ans = inf

    # the size of an array is the formulae
    for i in range(n - k + 1):
        c = blocks.count('W', i, i + k)

        if c < ans:
            ans = c

    return ans


print(minimumRecolors(blocks="WBBWWBBWBW", k=7))  # 3
print(minimumRecolors(blocks="WBWBBBW", k=2))  # 0
