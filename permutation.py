import math


def generate_permutations(size):
    # Create a perm list of integers from 0 to size - 1
    perm = list(range(size))
    directions = [-1] * size
    perms = []

    while True:
        perms.append(perm[:])

        # Finds the largest mobile integer in the permutation
        largest_mobile = -1
        for i in range(size):
            neighbor_index = i + directions[i]
            if 0 <= neighbor_index < size and perm[i] > perm[neighbor_index]:
                if largest_mobile == -1 or perm[i] > perm[largest_mobile]:
                    largest_mobile = i
        # Stops if no mobile integer is found
        if largest_mobile == -1:
            break

        # Swaps the mobile integer in its direction
        swap_pos = largest_mobile + directions[largest_mobile]
        perm[largest_mobile], perm[swap_pos] = perm[swap_pos], perm[largest_mobile]
        directions[largest_mobile], directions[swap_pos] = (
            directions[swap_pos],
            directions[largest_mobile],
        )

        # Reverses the direction of all elements larger than the mobile integer
        for i in range(size):
            if perm[i] > perm[swap_pos]:
                directions[i] = -directions[i]

    return perms


def find_cycles(graph):
    num_nodes = len(graph)
    all_perms = generate_permutations(num_nodes)
    cycles = []

    # Check if each permutation forms a valid cycle
    for perm in all_perms:
        if is_cycle(perm, graph):
            cycles.append(perm)

    return cycles or -1


def is_cycle(path, graph):
    for i in range(len(path) - 1):
        if path[i + 1] not in graph[path[i]][1]:
            return False
    return True


def cycle_distance(path, graph):
    """Calculates the total Euclidean distance of a cycle."""
    distance = 0
    for i in range(len(path) - 1):
        distance += edge_distance(path[i], path[i + 1], graph)
    distance += edge_distance(path[-1], path[0], graph)
    return distance


def edge_distance(start, end, graph):
    """Calculate the Euclidean distance between two nodes in the graph."""
    coord_start = graph[start][0]
    coord_end = graph[end][0]
    distance = math.sqrt(
        (coord_end[0] - coord_start[0]) ** 2 + (coord_end[1] - coord_start[1]) ** 2
    )
    return distance


def find_best_cycle(graph):
    all_cycles = find_cycles(graph)

    min_distance = float("inf")
    best_cycle = None

    # Finds the cycle with the shortest distance
    for cycle in all_cycles:  # type: ignore
        dist = cycle_distance(cycle, graph)
        if dist < min_distance:
            min_distance = dist
            best_cycle = cycle

    return best_cycle
