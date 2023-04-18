def mergeAlternately(word1: str, word2: str) -> str:
    left = 0
    right = 0
    isLeft = True
    ans = ''

    while (left < len(word1) and right < len(word2)):
        if isLeft:
            ans += word1[left]
            left += 1
        else:
            ans += word2[right]
            right += 1

        isLeft = not isLeft

    if left < len(word1):
        ans += word1[left:]
    if right < len(word2):
        ans += word2[right:]

    return ans


print(mergeAlternately(word1="abc", word2="pqr"))  # apbqcr
print(mergeAlternately(word1="ab", word2="pqrs"))  # apbqrs
