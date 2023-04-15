# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/

def garbageCollection(garbage: list[str], travel: list[int]) -> int:
    prefix = [0]
    ans = 0

    for time in travel:
        prefix.append(prefix[-1] + time)

    p = g = m = 0

    for i in range(len(garbage)):
        ans += len(garbage[i])

        if "M" in garbage[i]:
            m = i
        if "G" in garbage[i]:
            g = i
        if "P" in garbage[i]:
            p = i

    return ans + prefix[p] + prefix[g] + prefix[m]


print(garbageCollection(
    garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3]))  # 12
