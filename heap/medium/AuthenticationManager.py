from collections import defaultdict
from heapq import *

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.heap = []
        self.cache = defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        expiryTime = self.ttl + currentTime
        heappush(self.heap, (expiryTime, tokenId))
        self.cache[tokenId] = expiryTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.cache and self.cache[tokenId] > currentTime:
            newExpiryTime = self.ttl + currentTime
            heappush(self.heap, (newExpiryTime, tokenId))
            self.cache[tokenId] = newExpiryTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.heap and self.heap[0][0] <= currentTime:
            expiryTime, tokenId = heappop(self.heap)

            if self.cache.get(tokenId) == expiryTime:
                del self.cache[tokenId]

        return len(self.cache)
