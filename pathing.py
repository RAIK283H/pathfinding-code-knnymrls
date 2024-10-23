from re import A
from webbrowser import get
import graph_data 
import global_game_data
import random 

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
    assert target_node != starting_node, "Error: The target node must not be the start node."
    assert target_node != ending_node, "Error: The target node must not be the exit node."
    
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
    assert target_node in dfs(starting_node, target_node), "Error: The path must include the target node."
    assert dfs(starting_node, target_node)[-1] == target_node, "Error: The path must end at the target node." # type: ignore
    assert dfs(starting_node, target_node)[0] == starting_node, "Error: The path must start at the start node." # type: ignore
    
    return dfs(starting_node, target_node) + dfs(target_node, ending_node)[1:] # type: ignore


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
    path_to_exit = bfs(target_node, exit_node)[1:] # type: ignore
    full_path = path_to_target + path_to_exit # type: ignore

# Post conditions
    assert full_path[0] == 0, "Error: Path should start at node 0."
    assert full_path[-1] == exit_node, "Error: Path should end at the exit node."
    assert target_node in full_path, "Error: Path should include the target node."

    return full_path

def get_dijkstra_path():
    return [1,2]
