from graph_data import graph_data
import math


def floyd_warshall(graph_matrix):
    n = len(graph_matrix)
    dist = [[math.inf] * n for _ in range(n)]
    next_node = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph_matrix[i][j] != math.inf:
                dist[i][j] = graph_matrix[i][j]
                next_node[i][j] = j  # type: ignore

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node


def adjacency_list_to_matrix(adj_list, num_nodes):
    matrix = [[math.inf] * num_nodes for _ in range(num_nodes)]
    for u, neighbors in enumerate(adj_list):
        for v in neighbors:
            matrix[u][v] = 1
    for i in range(num_nodes):
        matrix[i][i] = 0
    return matrix


def reconstruct_path(next_node, start, end):
    if next_node[start][end] is None:
        return []
    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)
    return path


if __name__ == "__main__":
    graph = graph_data[0]
    num_nodes = len(graph)
    adj_list = [node[1] for node in graph]
    graph_matrix = adjacency_list_to_matrix(adj_list, num_nodes)

    dist, next_node = floyd_warshall(graph_matrix)

    print("Distance Matrix:")
    for row in dist:
        print(row)

    print("\nNext Node Matrix:")
    for row in next_node:
        print(row)

    start, end = 0, num_nodes - 1
    path = reconstruct_path(next_node, start, end)
    print(f"\nPath from {start} to {end}: {path}")
    print(f"Path length: {dist[start][end]}")
