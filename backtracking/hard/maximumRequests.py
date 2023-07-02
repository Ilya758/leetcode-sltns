# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/description/

# We can treat the list of edges as a directed graph.
# By manipulating INDEGREE / OUTDEGREE of a graph nodes, we only care about
# zeros for EACH travel.

class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        def backtrack(i, count, transfers):
            if i == len(requests):
                return count if all(t == 0 for t in transfers) else 0

            [start, end] = requests[i]

            # 1. let the man move from start building to end
            transfers[start] -= 1
            transfers[end] += 1

            included = backtrack(i + 1, count + 1, transfers)

            # 2. and then he returns back
            transfers[start] += 1
            transfers[end] -= 1

            excluded = backtrack(i + 1, count, transfers)

            return max(included, excluded)

        return backtrack(0, 0, [0] * n)


print(Solution().maximumRequests(n=5, requests=[
      [0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]))  # 5
print(Solution().maximumRequests(n=3, requests=[[0, 0], [1, 2], [2, 1]]))  # 3
print(Solution().maximumRequests(
    n=4, requests=[[0, 3], [3, 1], [1, 2], [2, 0]]))  # 4
