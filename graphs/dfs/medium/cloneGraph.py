class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Input: adjacency list

def cloneGraph(node: 'Node') -> 'Node':
    visited = dict()

    def clone(node: 'Node') -> 'Node':
        if not node:
            return None
        if visited.get(node.val):
            return visited.get(node.val)

        copy = Node(node.val)
        visited[node.val] = copy

        for neig in node.neighbors:
            copy.neighbors.append(clone(neig))

        return copy

    return clone(node)
