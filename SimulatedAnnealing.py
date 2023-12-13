import Tree
import random
import math
import utils as u


def get_neighbors(node):
    return [child for child, _ in node.children]


def simulated_annealing(tree, start_node, goal_node, initial_temperature, cooling_rate):
    current_node = start_node
    current_solution = [current_node]

    number_of_iterations = 0

    temperature = initial_temperature

    while current_node.value != goal_node and temperature > 0.1:
        number_of_iterations += 1
        neighbors = get_neighbors(current_node)
        if not neighbors:
            current_node = tree.GetRoot()
            current_solution = [current_node]
            continue

        next_node = random.choice(neighbors)

        delta_e = tree.GetPathLength(next_node) - tree.GetPathLength(current_node)

        if delta_e > 0 or random.uniform(0, 1) < math.exp(delta_e / temperature):
            current_node = next_node
            current_solution.append(current_node)

        temperature *= cooling_rate

    print("Temperature", temperature)

    if goal_node not in [node.value for node in current_solution]:
        print("Solution not found")

    print("Solution:", [node.value for node in current_solution])
    print("Number of iterations:", number_of_iterations)

    return current_solution


# Example usage:
edges_list = u.GetEdges()

tree = Tree.Tree(edges_list)

goal_node = 11

initial_temperature = 50
cooling_rate = 0.9

start_node = tree.GetRoot()

simulated_annealing(tree, start_node, goal_node, initial_temperature, cooling_rate)

# it is possible that this method doesn't find a solution
# if the temperature gets below limit temperature and the solution is not found
