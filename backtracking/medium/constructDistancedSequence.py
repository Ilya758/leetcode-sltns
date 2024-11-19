class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        seq = [0] * (2 * n - 1)
        self.ans = []   
        seen = set()

        def bt(i):
            if i == len(seq):
                self.ans = seq[:]
                return True

            if seq[i]:
                return bt(i + 1)

            for j in range(n, 0, -1):
                if j in seen:
                    continue

                if j == 1:
                    seen.add(1)
                    seq[i] = 1

                    if bt(i + 1):
                        return True

                    seq[i] = 0
                    seen.remove(1)
                elif i + j < len(seq) and not seq[i + j]:
                    seq[i] = seq[i + j] = j
                    seen.add(j)

                    if bt(i + 1):
                        return True

                    seen.remove(j)
                    seq[i] = seq[i + j] = 0

            return False

        bt(0)

        return self.ans

print(Solution().constructDistancedSequence(3)) # [3, 1, 2, 3, 2]