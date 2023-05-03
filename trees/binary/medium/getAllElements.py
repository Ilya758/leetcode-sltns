# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/

def getAllElements(root1, root2) -> list[int]:
    def dfs(node, nums=[]):
        if not node:
            return nums

        return [*dfs(node.left, nums), node.val, *dfs(node.right, nums)]

    left = dfs(root1)
    right = dfs(root2)
    ans = []
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            ans.append(left[l])
            l += 1
        else:
            ans.append(right[r])
            r += 1

    if l < len(left):
        ans.extend(left[l:])
    if r < len(right):
        ans.extend(right[r:])

    return ans
