from collections import defaultdict, deque


class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        graph = defaultdict(set)
        indegree = defaultdict(int)
        s = set(supplies)

        for recipe, ingredient in zip(recipes, ingredients):
            for node in ingredient:
                if node not in s:
                    graph[node].add(recipe)
                    indegree[recipe] += 1 
        
        q = deque([recipe for recipe in recipes if not indegree[recipe]])
        ans = set()

        while q:
            node = q.popleft()
            ans.add(node)

            for recipe in graph[node]:
                indegree[recipe] -= 1

                if not indegree[recipe]:
                    q.append(recipe)
                
        return ans


print(Solution().findAllRecipes(recipes =
["bread","sandwich","burger"],
ingredients =
[["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]],
supplies =
["yeast","flour","meat"])) # ["bread","sandwich","burger"]