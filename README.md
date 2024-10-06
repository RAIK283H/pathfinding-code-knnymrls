## Pathfinding Starter Code

#### Understanding the requirements
The first thing I noticed in the user story is no specification for efficientcy of the algorith. It simply says it wants a random path from start to finish. This means that the path can be inefficient and not the shortest path. This is important to note because it will affect the way I implement the pathfinding algorithm.

The next thing I noticed is the second requirement which is seeing another statistic which I deem to be the number of steps taken to reach the end. This is important because it will help me determine the efficiency of the algorithm I implement.

#### Designing the algorithm

```python
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    starting_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    ending_node = len(graph) - 1
    current_node = starting_node
    path = [current_node]
```
First thing I did was get the graph data from the graph_data file. I then set the starting node to 0 and the target node to the last node in the graph. I then set the current node to the starting node and created a list to store the path.

```python
    while current_node != target_node:
        next_node = get_random_adjacent_node(graph, current_node)
        path.append(next_node)
        current_node = next_node
```
I then created a while loop that runs until the current node is the target node. In the loop, I randomly choose the next node from the current node's neighbors and append it to the path. I then set the current node to the next node.

```python
    while current_node != ending_node:
        next_node = get_random_adjacent_node(graph, current_node)
        path.append(next_node)
        current_node = next_node
```
I then created another while loop that runs until the current node is the ending node. In the loop, I randomly choose the next node from the current node's neighbors and append it to the path. I then set the current node to the next node.

```python
    def get_random_adjacent_node(graph, current_node):
    adjacent_nodes = graph[current_node][1] 
    random_index = random.randint(0, len(adjacent_nodes) - 1)
    
    return adjacent_nodes[random_index]
```
I use this as a helper function that returns a random adjacent node from the current node.

#### Statistic tracking

```python
    path_label = pyglet.text.Label("Path: ", x=0, y=0, font_name='Arial', font_size=self.font_size, batch=batch, group=group, color=player[2][colors.TEXT_INDEX])
            self.player_path_display.append((path_label, player))
            
            nodes_visited_label = pyglet.text.Label("Nodes Visited: 0", x=0, y=0, font_name='Arial', font_size=self.font_size, batch=batch, group=group, color=player[2][colors.TEXT_INDEX])
            self.player_nodes_visited_display.append((nodes_visited_label, player))
```
I created a label to display the path and another label to display the number of nodes visited similar to the prior labels in the code.

```python
    def update_nodes_visited(self):
        for index, (label, player) in enumerate(self.player_nodes_visited_display):
            num_nodes_visited = len(global_game_data.graph_paths[index])  # Count the nodes in the player's path
            label.text = f"Nodes Visited: {num_nodes_visited}"
```
I then created a function that updates the number of nodes visited by the player. I do this by counting the number of nodes in the player's path and updating the label with the new number.

```python
    def update_scoreboard(self):
        self.update_elements_locations()
        self.update_paths()
        self.update_distance_to_exit()
        self.update_distance_traveled()
        self.update_nodes_visited()
```
I finally added the update_nodes_visited function to the update_scoreboard function so that it updates the number of nodes visited when the scoreboard is updated.