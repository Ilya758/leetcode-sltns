from collections import deque


def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    wl = set(wordList)
    seen = {beginWord}
    q = deque([(beginWord, 0)])

    def getWords(word: str) -> list[str]:
        words = []

        for i in range(len(word)):
            for j in range(26):
                if word[i] != chr(97 + j):
                    newWord = "".join(
                        [word[:i],
                         chr(97 + j),
                         word[i + 1:]]
                    )

                    words.append(newWord)

        return words

    while q:
        word, steps = q.popleft()

        if word == endWord:
            return steps + 1

        for w in getWords(word):
            if w in wl and w not in seen:
                seen.add(w)
                q.append((w, steps + 1))

    return 0


print(ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]
                   ))  # 5
print(ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]
                   ))  # 0
