from bisect import bisect_right


class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        starts = []
        ends = []
        
        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)
            
        starts.sort()
        ends.sort()
        ans = []

        for person in people:
            i = bisect_right(starts, person)
            j = bisect_right(ends, person)
            ans.append(i - j)
        
        return ans
    
print(Solution().fullBloomFlowers(flowers = [[1,6],[3,7],[9,12],[4,13]], people= [2,3,7,11])) # [1,2,2,2]