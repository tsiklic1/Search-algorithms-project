import Tree as t
import utils as u

edgesList = u.GetEdges()

tree = t.Tree(edgesList)
targetValue = 11


def DFS(root, targetValue, tree=tree):
    print("DFS:")
    number_of_iterations = 0
    stack = [tree.GetRoot()]
    visited = [root]

    while len(stack) > 0:
        number_of_iterations += 1
        node = stack.pop()

        if node.value == targetValue:
            print("Found it! =>", node.value)
            print("Path: ", tree.GetPath(node))
            print("Path length: ", tree.GetPathLength(node))
            print("Number of iterations:", number_of_iterations)
            return True

        for child, distance in node.children:
            if child not in visited:
                stack.append(child)
                visited.append(child)

    return False


DFS(tree.GetRoot(), targetValue)
