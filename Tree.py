class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List of tuples (node, distance)
        self.parent = None
        self.pathLength = 0


class Tree:
    def __init__(self, edgesList, root=0):
        self.root = root

        highestOrderNode = max([max(edge[:2]) for edge in edgesList])

        self.nodes = [TreeNode(i) for i in range(highestOrderNode + 1)]

        edges = edgesList

        for edge in edges:
            parent_value, child_value, distance = edge
            parent_node = self.nodes[parent_value]
            child_node = self.nodes[child_value]
            child_node.parent = parent_node
            parent_node.children.append((child_node, distance))

    def GetRoot(self):
        return self.nodes[0]

    def GetPath(self, targetNode):
        path = []
        currentNode = targetNode
        while currentNode is not None:
            path.insert(0, currentNode.value)
            currentNode = currentNode.parent

        return path

    def GetPathLength(self, targetNode):
        pathLength = 0
        currentNode = targetNode
        while currentNode is not None:
            parentNode = currentNode.parent
            if parentNode is not None:
                for child, distance in parentNode.children:
                    if child == currentNode:
                        pathLength += distance
                        break

            currentNode = parentNode

        return pathLength
