# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

from heapq import *


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        ans = []
        m = len(nums1)
        n = len(nums2)
        visited = set()
        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        heapify(minHeap)
        visited.add((0, 0))

        while k and minHeap:
            _, (i, j) = heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))

            if j + 1 < n and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))

            k -= 1

        return ans


print(Solution().kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
# [[1,2],[1,4],[1,6]]
