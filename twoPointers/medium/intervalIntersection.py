class Solution:
    def intervalIntersection(self, f: list[list[int]], s: list[list[int]]) -> list[list[int]]:
        left = 0
        right = 0
        ans = []

        while left < len(f) and right < len(s):
            fl, fr = f[left]
            rl, rr = s[right]
            range = [max(fl, rl), min(fr, rr)]

            if range[0] <= range[1]: ans.append(range)

            if fr < rr: left += 1
            else: right += 1

        return ans
    
print(Solution().intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
)) # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]