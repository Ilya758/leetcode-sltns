from collections import deque


class Codec:
    def encode(self, root):
        if not root:
            return None

        rootNode = TreeNode(root.val)
        queue = deque([(rootNode, root)])

        while queue:
            parent, curr = queue.popleft()
            prevBNode = None
            headBNode = None
            
            for child in curr.children:
                newBNode = TreeNode(child.val)
                if prevBNode:
                    prevBNode.right = newBNode
                else:
                    headBNode = newBNode
                prevBNode = newBNode
                queue.append((newBNode, child))

            parent.left = headBNode

        return rootNode


    def decode(self, node):
        if not node:
            return None

        rootNode = Node(node.val, [])
        queue = deque([(rootNode, node)])

        while queue:
            parent, curr = queue.popleft()
            firstChild = curr.left
            sibling = firstChild

            while sibling:
                newNode = Node(sibling.val, [])
                parent.children.append(newNode)
                queue.append((newNode, sibling))
                sibling = sibling.right

        return rootNode