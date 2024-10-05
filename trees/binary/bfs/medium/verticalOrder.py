from collections import defaultdict, deque


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([[root, 0]])
        cache = defaultdict(list)

        while q:
            for _ in range(len(q)):
                node, i = q.popleft()

                if node:
                    cache[i].append(node.val)
                    q.append([node.left, i - 1])
                    q.append([node.right, i + 1])

        return [cache[k] for k in sorted(cache)]      