from collections import deque


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        n, m = len(target), len(stamp)
        A = []
        q = deque([])
        ans = []
        done = [False] * n

        for i in range(n - m + 1):
            made, todo = set(), set()

            for j, c in enumerate(stamp):
                t = target[i + j]

                if t == c:
                    made.add(i + j)
                else:
                    todo.add(i + j)

            A.append((made, todo))

            if not todo:
                ans.append(i)

                for j in range(i, i + m):
                    if not done[j]:
                        done[j] = True
                        q.append(j)

        while q:
            i = q.popleft()
            
            for j in range(max(0, i - m + 1), min(n - m, i) + 1):
                if i in A[j][1]:
                    A[j][1].discard(i)

                    if not A[j][1]:
                        ans.append(j)

                        for x in A[j][0]:
                            if not done[x]:
                                done[x] = True
                                q.append(x)

        return ans[::-1] if all(done) else []   

print(Solution().movesToStamp(stamp = "abca", target = "aabcaca")) # [3,0,1]
