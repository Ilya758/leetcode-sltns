from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target: return 0

        stops = defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                stops[stop].add(bus)

        visitedStops = { source }
        visitedBuses = set()
        queue = deque([(source, 0)])

        while queue:
            stop, count = queue.popleft()
            
            if stop == target: return count

            for bus in stops[stop]:
                if bus not in visitedBuses:
                    visitedBuses.add(bus)

                    for nextStop in routes[bus]:
                        if nextStop not in visitedStops:
                            visitedStops.add(nextStop)
                            queue.append((nextStop, count + 1))

        return -1
          

print(Solution().numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6)) # 2 