from collections import deque


def canReach(arr: list[int], start: int) -> bool:
    seen = {start}
    q = deque([start])

    def getNodes(index: int) -> list[int]:
        indices = []

        for v in [index - arr[index], index + arr[index]]:
            if 0 <= v < len(arr):
                indices.append(v)

        return indices

    while q:
        index = q.popleft()

        if arr[index] == 0:
            return True

        for node in getNodes(index):
            if node not in seen:
                seen.add(node)
                q.append(node)

    return False
