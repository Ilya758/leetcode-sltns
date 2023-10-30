class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        bin = []

        for i, value in enumerate(arr):
            num = arr[i]
            count = 0

            while num:
                count += num & 1
                num >>= 1

            bin.append({ "value": value, "count": count })

        bin = sorted(bin, key=lambda a: (a['count'], a['value']))

        return [x['value'] for x in bin]


print(Solution().sortByBits(arr = [0,1,2,3,4,5,6,7,8])) # [0,1,2,4,8,3,5,6,7]