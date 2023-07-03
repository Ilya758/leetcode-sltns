class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) < len(s):
            return True
        pairs = []
        for a, b in zip(s, goal):
            if a != b:
                pairs.append((a, b))
                if len(pairs) >= 3:
                    return False
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


print(Solution().buddyStrings(s="ab", goal="ba"))  # True
print(Solution().buddyStrings(s="ab", goal="ab"))  # False
print(Solution().buddyStrings(s="aa", goal="aa"))  # True
