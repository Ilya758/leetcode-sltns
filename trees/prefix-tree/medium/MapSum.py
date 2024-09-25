from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.score = 0
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, val):
        cur = self.root

        for k in key:
            cur = cur.children[k]

        cur.score = val

    def search(self, key):
        cur = self.root
        
        for k in key:
            if k not in cur.children:
                return None

            cur = cur.children[k]

        return cur

class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def dfs(self, root):
        return root.score + sum([self.dfs(node) for node in root.children.values()])

    def sum(self, prefix: str) -> int:
        root = self.trie.search(prefix)

        return self.dfs(root) if root else 0
    
m = MapSum()
m.insert("apple", 3)
print(m.sum("apple")) # 3
m.insert("app", 2) 
print(m.sum("ap")) # 5
