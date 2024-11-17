from re import A
from webbrowser import get
import graph_data
import global_game_data
import random
import heapq
import math


def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    # Important Variables for Path Generation
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    starting_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    ending_node = len(graph) - 1
    current_node = starting_node
    path = [current_node]

    # Precondition
    assert path[0] == starting_node, "Error: The path must start at the start node."

    # Generate a path from start to target
    while current_node != target_node:
        next_node = get_random_adjacent_node(graph, current_node)
        path.append(next_node)
        current_node = next_node

    # Post condition
    assert target_node in path, "Error: The path must include the target node."

    # Generate a path from target to end
    while current_node != ending_node:
        next_node = get_random_adjacent_node(graph, current_node)
        path.append(next_node)
        current_node = next_node

    # Post condition 2
    assert path[-1] == ending_node, "Error: The path must end at the exit node."

    return path


# Selects random adjacent node using the adjacency list of the current node
def get_random_adjacent_node(graph, current_node):
    adjacent_nodes = graph[current_node][1]
    random_index = random.randint(0, len(adjacent_nodes) - 1)

    return adjacent_nodes[random_index]


def get_dfs_path():
    # Important Variables for Path Generation
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    starting_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    ending_node = len(graph) - 1

    # Preconditions
    assert starting_node == 0, "Error: The path must start at the start node."
    assert (
        target_node != starting_node
    ), "Error: The target node must not be the start node."
    assert (
        target_node != ending_node
    ), "Error: The target node must not be the exit node."

    # Helper function that performs my depth-first search
    def dfs(start, goal):
        nodes_vistited = set()
        stack = [[start]]
        while stack:
            path = stack.pop()
            node = path[-1]
            if node == goal:
                return path
            if node in nodes_vistited:
                continue
            for adjacent_node in graph[node][1]:
                new_path = list(path)
                new_path.append(adjacent_node)
                stack.append(new_path)
            nodes_vistited.add(node)
        return None

    # Post conditions
    assert target_node in dfs(
        starting_node, target_node
    ), "Error: The path must include the target node."
    assert dfs(starting_node, target_node)[-1] == target_node, "Error: The path must end at the target node."  # type: ignore
    assert dfs(starting_node, target_node)[0] == starting_node, "Error: The path must start at the start node."  # type: ignore

    return dfs(starting_node, target_node) + dfs(target_node, ending_node)[1:]  # type: ignore


def get_bfs_path():
    # Important Variables for Path Generation
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = len(graph) - 1

    # Preconditions
    assert target_node != 0, "Error: The target node must not be the start node."
    assert target_node != exit_node, "Error: The target node must not be the exit node."

    # Helper function that performs my breadth-first search
    def bfs(start_node, end_node):
        queue = [[start_node]]
        visited = set()
        visited.add(start_node)

        while queue:
            current_path = queue.pop(0)
            current_node = current_path[-1]

            if current_node == end_node:
                return current_path

            for neighbor in graph[current_node][1]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = current_path + [neighbor]
                    queue.append(new_path)

    path_to_target = bfs(0, target_node)
    path_to_exit = bfs(target_node, exit_node)[1:]  # type: ignore
    full_path = path_to_target + path_to_exit  # type: ignore

    # Post conditions
    assert full_path[0] == 0, "Error: Path should start at node 0."
    assert full_path[-1] == exit_node, "Error: Path should end at the exit node."
    assert target_node in full_path, "Error: Path should include the target node."

    return full_path


def calculate_distance(coord1, coord2):
    """Calculate Euclidean distance between two coordinates."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def dijkstra(graph, start, end):
    """Dijkstra's algorithm to find the shortest path."""
    distances = {i: float("inf") for i in range(len(graph))}
    distances[start] = 0
    parents = {start: None}
    queue = [(0, start)]  # (distance, node)

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        current_coord, neighbors = graph[current_node]
        for neighbor in neighbors:
            neighbor_coord = graph[neighbor][0]
            weight = calculate_distance(current_coord, neighbor_coord)
            new_dist = current_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parents[neighbor] = current_node
                heapq.heappush(queue, (new_dist, neighbor))  # type: ignore

    # Reconstruct the path
    path = []
    while end is not None:
        path.append(end)
        end = parents[end]
    return path[::-1]


def get_dijkstra_path():
    """Find the complete path using Dijkstra's algorithm."""
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    start = 0
    target = global_game_data.target_node[global_game_data.current_graph_index]
    end = len(graph) - 1

    start_to_target = dijkstra(graph, start, target)
    target_to_end = dijkstra(graph, target, end)
    full_path = start_to_target[:-1] + target_to_end

    assert full_path[0] == start, "Path must start at the start node."
    assert full_path[-1] == end, "Path must end at the exit node."
    assert validate_path(graph, full_path), "Path is not fully connected."
    return full_path


def validate_path(graph, path):
    """Ensure all nodes in the path are connected."""
    return all(path[i + 1] in graph[path[i]][1] for i in range(len(path) - 1))
