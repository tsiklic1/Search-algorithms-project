import Tree as t
from collections import deque
import utils as u

edgesList = u.GetEdges()

tree = t.Tree(edgesList)
targetValue = 11


def BFS(root, targetValue, tree=tree):
    print("BFS:")

    number_of_iterations = 0

    queue = deque([tree.GetRoot()])
    visited = [root]

    while len(queue) > 0:
        number_of_iterations += 1
        node = queue.popleft()

        if node.value == targetValue:
            print("Found it! => ", node.value)
            print("Path: ", tree.GetPath(node))
            print("Path length: ", tree.GetPathLength(node))
            print("Number of iterations:", number_of_iterations)
            return True

        for child, distance in node.children:
            if child not in visited:
                queue.append(child)
                visited.append(child)

    return False


BFS(tree.GetRoot(), targetValue)
