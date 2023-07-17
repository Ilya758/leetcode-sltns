# https://leetcode.com/problems/course-schedule/

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)

        cache = dict()

        def dfs(node, seen):
            if node not in graph:
                return True

            for neig in graph[node]:
                if neig not in seen:
                    seen.add(neig)

                    # since that some or more paths lead
                    # to the same destination,
                    # we'll provide a cache
                    if neig not in cache:
                        cache[neig] = dfs(neig, seen)

                    # every time we found a cycle in graph
                    # we can complete all of the courses
                    if not cache[neig]:
                        return False

                    # since we don't want to affect future result
                    # we using a little trick here by removing
                    # previously added node
                    # (backtracking influence)
                    seen.remove(neig)
                else:
                    return False

            return True

        for i in graph:
            if not dfs(i, set({i})):
                return False

        return True


print(Solution().canFinish(
    numCourses=5,
    prerequisites=[[1, 4], [2, 4], [3, 1], [3, 2]]
))  # True
print(Solution().canFinish(numCourses=20, prerequisites=[
      [0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]))  # False
