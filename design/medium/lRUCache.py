# https://leetcode.com/problems/lru-cache/description/

from collections import deque


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.cache = dict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)

        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)
        elif self.capacity:
            self.capacity -= 1
        else:
            lRUKey = self.queue.popleft()
            del self.cache[lRUKey]

        self.queue.append(key)
        self.cache[key] = value


lRUCache = LRUCache(2)

lRUCache.put(1, 0)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))
