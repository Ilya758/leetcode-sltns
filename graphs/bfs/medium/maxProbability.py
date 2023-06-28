
from collections import defaultdict, deque


class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        queue = deque([start])
        while queue:
            cur_node = queue.popleft()
            for nxt_node, path_prob in graph[cur_node]:
                print(max_prob[cur_node] * path_prob, max_prob[nxt_node])
                if max_prob[cur_node] * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = max_prob[cur_node] * path_prob
                    queue.append(nxt_node)

        return max_prob[end]


print(Solution().maxProbability(n=3, edges=[[0, 1], [1, 2], [
      0, 2]], succProb=[0.5, 0.5, 0.2], start=0, end=2))  # 0.25
print(Solution().maxProbability(n=3, edges=[[0, 1], [1, 2], [
      0, 2]], succProb=[0.5, 0.5, 0.3], start=0, end=2))  # 0.3
print(Solution().maxProbability(n=3, edges=[
      [0, 1]], succProb=[0.5], start=0, end=2))  # 0
