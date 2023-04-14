# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

def numOfSubarrays(arr: list[int], k: int, threshold: int) -> int:
    left = 0
    right = 0
    ans = 0
    n = len(arr)
    cur = 0

    while left < n - k + 1:
        cur += arr[right]

        if right - left + 1 == k:
            if cur / k >= threshold:
                ans += 1

            cur -= arr[left]
            left += 1

        right += 1

    return ans


print(numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))  # 3
print(numOfSubarrays(arr=[11, 13, 17, 23, 29,
      31, 7, 5, 2, 3], k=3, threshold=5))  # 6
