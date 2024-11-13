from collections import defaultdict


class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        self.cache = defaultdict(int)
        self.times = times
        self.winner = []
        prev = persons[0]

        for i in range(len(persons)):
            self.cache[persons[i]] += 1
            prev = persons[i] if self.cache[persons[i]] >= self.cache[prev] else prev
            self.winner.append(prev)

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1

        while left <= right:
            mid = (left + right) >> 1

            if self.times[mid] > t:
                right = mid - 1
            else:
                left = mid + 1

        return self.winner[left - 1]