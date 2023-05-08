def diagonalSum(mat: list[list[int]]) -> int:
    ans = 0
    left = 0
    n = len(mat)
    right = n - 1

    while left < n:
        if left == (n - 1) / 2 and (n - 1) % 2 == 0:
            ans += mat[left][left]
        else:
            ans += mat[left][left] + mat[left][right]

        left += 1
        right -= 1

    return ans


print(diagonalSum(mat=[[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]]))  # 25
