from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        map = Counter(arr)
        ordered = sorted(map.values(), reverse=True)

        while k:
            num = ordered[-1]

            if k >= num:
                k -= num
                ordered.pop()
            else:
                break

        return len(ordered)


print(Solution().findLeastNumOfUniqueInts(arr=[5, 5, 4], k=1))  # 1
print(Solution().findLeastNumOfUniqueInts(arr=[4, 3, 1, 1, 3, 3, 2], k=3))  # 2
