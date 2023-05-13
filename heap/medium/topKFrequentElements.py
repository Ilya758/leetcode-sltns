# https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import Counter


def topKFrequentElements(nums, k):
    map = sorted(Counter(nums).items(), key=lambda a: a[1], reverse=True)

    return [map[i][0] for i in range(0, k)]


print(topKFrequentElements(nums=[1, 1, 1, 2, 2, 3], k=2))
