# https://leetcode.com/problems/open-the-lock/description/

from collections import deque


def openLock(deadends: list[str], target: str) -> int:
    def getNeighbors(node: str) -> list[int]:
        ans = []

        for i in range(4):
            num = int(node[i])

            for ch in [-1, 1]:
                x = (num + ch) % 10
                ans.append(node[:i] + str(x) + node[i + 1:])

        return ans

    seen = set(deadends)

    if "0000" in deadends:
        return -1

    q = deque([("0000", 0)])

    while q:
        node, steps = q.popleft()

        if (node == target):
            return steps

        for neig in getNeighbors(node):
            if neig not in seen:
                seen.add(neig)
                q.append((neig, steps + 1))

    return -1


print(openLock(deadends=["0201", "0101", "0102",
      "1212", "2002"], target="0202"))  # 6
