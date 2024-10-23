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
    ## Important Variables for Path Generation
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    starting_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    ending_node = len(graph) - 1
    
    def dfs(start, goal):
        visited = set()
        stack = [[start]]
        while stack:
            path = stack.pop()
            node = path[-1]
            if node == goal:
                return path
            if node in visited:
                continue
            for neighbor in graph[node][1]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
            visited.add(node)
        return None
    
    return dfs(starting_node, target_node) + dfs(target_node, ending_node)[1:] # type: ignore


def get_bfs_path():
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
    queue = [[current_node]]
    visited = set()
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == target_node:
            break
        if node in visited:
            continue
        for neighbor in graph[node][1]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
        visited.add(node)
        
    # Post condition
    assert target_node in path, "Error: The path must include the target node."
    
    # Generate a path from target to end
    current_node = target_node
    while current_node != ending_node:
        next_node = get_random_adjacent_node(graph, current_node)
        path.append(next_node)
        current_node = next_node
        
    # Post condition 2
    assert path[-1] == ending_node, "Error: The path must end at the exit node."
    
    return path


def get_dijkstra_path():
    return [1,2]
