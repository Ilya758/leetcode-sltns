from collections import deque


def minMutation(startGene: str, endGene: str, bank: list[str]) -> int:
    seen = {startGene}
    q = deque([(startGene, 0)])

    def getNodes(gene: str) -> list[str]:
        genes = []
        choices = {'A', 'C', 'G', 'T'}

        for i in range(len(gene)):
            for choice in choices:
                if gene[i] != choice:
                    newGene = "".join([
                        gene[:i],
                        choice,
                        gene[i + 1:]
                    ])
                    genes.append(newGene)

        return genes

    while q:
        gene, steps = q.popleft()

        if gene == endGene:
            return steps

        for node in getNodes(gene):
            if node not in seen and node in bank:
                seen.add(node)
                q.append((node, steps + 1))

    return -1


print(minMutation(startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGGTA"]
                  ))  # 1
print(minMutation(startGene="AACCGGTT", endGene="AAACGGTA", bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"]
                  ))  # 2
