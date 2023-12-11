class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List of tuples (node, distance)
        self.parent = None
        self.path_length = 0


class Tree:
    def __init__(self, edgesList, root=0):
        self.root = root

        highest_order_node = max([max(edge[:2]) for edge in edgesList])

        self.nodes = [TreeNode(i) for i in range(highest_order_node + 1)]

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
        current_node = targetNode
        while current_node is not None:
            path.insert(0, current_node.value)
            current_node = current_node.parent

        return path

    def GetPathLength(self, targetNode):
        path_length = 0
        current_node = targetNode
        while current_node is not None:
            parent_node = current_node.parent
            if parent_node is not None:
                for child, distance in parent_node.children:
                    if child == current_node:
                        path_length += distance
                        break

            current_node = parent_node

        return path_length
