from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = defaultdict(TrieNode)

class Trie:

    def __init__(self):
        self.cache = defaultdict(int)
        self.root = TrieNode()  
        self.prefix = defaultdict(int)

    def insert(self, word: str) -> None:
        node = self.root

        for w in word:
            node.children[w].count += 1
            node = node.children[w]

        self.cache[word] += 1

    def search(self, word):
        node = self.root

        for w in word:
            if w not in node.children:
                return 0

            node = node.children[w]

        return node.count

    def countWordsEqualTo(self, word: str) -> int:
        return self.cache[word]

    def countWordsStartingWith(self, prefix: str) -> int:
        return self.search(prefix)

    def erase(self, word: str) -> None:
        node = self.root

        for w in word:
            node.children[w].count -= 1
            node = node.children[w]

        self.cache[word] -= 1