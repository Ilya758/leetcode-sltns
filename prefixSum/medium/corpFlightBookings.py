class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        prefix = [0] * n

        for a, b, c in bookings:
            prefix[a - 1] += c

            if b < n:  
                prefix[b] -= c

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]

        return prefix

print(Solution().corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
)) # [10, 55, 45, 25, 25]