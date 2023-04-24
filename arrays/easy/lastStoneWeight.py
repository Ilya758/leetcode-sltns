# https://leetcode.com/problems/last-stone-weight/description/

def lastStoneWeight(stones: list[int]) -> int:
    stones = sorted(stones, reverse=True)

    while len(stones) > 1:
        [a, b] = stones[:2]

        if a > b:
            stones = [a-b, *stones[2:]]
        else:
            stones = stones[2:]

        stones = sorted(stones, reverse=True)

    return 0 if not len(stones) else stones[0]


print(lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))  # 1
print(lastStoneWeight(stones=[1]))  # 1
