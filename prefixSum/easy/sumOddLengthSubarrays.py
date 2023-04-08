def sumOddLengthSubarrays(arr: list[int]) -> int:
    n = len(arr)
    left = 0
    right = 0
    ans = 0
    curr = 0

    while left < n:
        curr += arr[right]

        # if the sliding window length fits the condition (odd length)
        if (right - left + 1) % 2:
            ans += curr

        right += 1

        if right == n:
            curr = 0
            left += 1
            right = left

    return ans


print(sumOddLengthSubarrays([1, 4, 2, 5, 3]))  # 58
print(sumOddLengthSubarrays([1, 2]))  # 3
