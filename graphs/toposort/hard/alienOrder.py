from collections import Counter, defaultdict, deque


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        graph = defaultdict(set)
        indegree = Counter({c : 0 for word in words for c in word})

        for first, second in zip(words, words[1:]):
            for c, d in zip(first, second):
                if c != d:
                    if d not in graph[c]:
                        graph[c].add(d)
                        indegree[d] += 1
                    break
                    
            if len(second) < len(first) and first.startswith(second): return ""

        ans = []
        q = deque([c for c in indegree if indegree[c] == 0])

        while q:
            node = q.popleft()
            ans.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        if len(ans) < len(indegree):
            return ""
            
        return "".join(ans)

print(Solution().alienOrder(['abc', 'ab'])) # ""