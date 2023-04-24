def countConsistentStrings(allowed: str, words: list[str]) -> int:
    ans = 0
    chars = dict()

    for c in allowed:
        chars[c] = True

    for word in words:
        ans += 1

        for char in word:
            if char not in chars:
                ans -= 1
                break

    return ans


print(countConsistentStrings(allowed="ab", words=[
      "ad", "bd", "aaab", "baa", "badab"]))  # 2
print(countConsistentStrings(allowed="abc", words=[
      "a", "b", "c", "ab", "ac", "bc", "abc"]))  # 7
