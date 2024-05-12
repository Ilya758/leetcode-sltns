class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left, right = 0, reader.length() - 1

        while left < right:
            mid = (left + right) >> 1
            diff = reader.compareSub(left, mid, mid + 1, right) if (right - left + 1) % 2 == 0 else reader.compareSub(left, mid, mid, right)          

            if diff == 0:
                return mid
            elif diff == 1:
                right = mid
            else:
                left = mid + 1

        return right