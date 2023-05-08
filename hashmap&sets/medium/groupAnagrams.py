from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    map = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        map[key].append(s)

    return [val for val in map.values()]


print(groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
# [["bat"],["nat","tan"],["ate","eat","tea"]]
