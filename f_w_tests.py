import math
import unittest
from f_w import floyd_warshall, adjacency_list_to_matrix, reconstruct_path


class TestFloydWarshall(unittest.TestCase):

    def setUp(self):
        self.test_graph = [
            [(0, 0), [1, 2]],
            [(1, 1), [0, 2]],
            [(2, 2), [0, 1]],
        ]
        self.adj_list = [node[1] for node in self.test_graph]
        self.num_nodes = len(self.test_graph)

    def test_f_w_basic(self):
        graph_matrix = adjacency_list_to_matrix(self.adj_list, self.num_nodes)
        dist, next_node = floyd_warshall(graph_matrix)

        self.assertEqual(dist[0][1], 1, "Shortest distance from 0 to 1 should be 1.")
        self.assertEqual(dist[0][2], 1, "Shortest distance from 0 to 2 should be 1.")
        self.assertEqual(dist[1][2], 1, "Shortest distance from 1 to 2 should be 1.")

        path_0_to_2 = reconstruct_path(next_node, 0, 2)
        self.assertEqual(path_0_to_2, [0, 2], "Path from 0 to 2 should be [0, 2].")

    def test_f_w_no_path(self):
        disconnected_graph = [
            [(0, 0), [1]],
            [(1, 1), [0]],
            [(2, 2), []],
        ]
        adj_list = [node[1] for node in disconnected_graph]
        num_nodes = len(disconnected_graph)
        graph_matrix = adjacency_list_to_matrix(adj_list, num_nodes)
        dist, next_node = floyd_warshall(graph_matrix)

        self.assertEqual(dist[0][2], math.inf, "There should be no path from 0 to 2.")
        self.assertEqual(
            reconstruct_path(next_node, 0, 2), [], "Path from 0 to 2 should be empty."
        )

    def test_f_w_complex(self):
        complex_graph = [
            [(0, 0), [1, 2]],
            [(1, 1), [0, 2, 3]],
            [(2, 2), [0, 1]],
            [(3, 3), [1]],
        ]
        adj_list = [node[1] for node in complex_graph]
        num_nodes = len(complex_graph)
        graph_matrix = adjacency_list_to_matrix(adj_list, num_nodes)
        dist, next_node = floyd_warshall(graph_matrix)

        self.assertEqual(dist[0][3], 2, "Shortest distance from 0 to 3 should be 2.")
        path_0_to_3 = reconstruct_path(next_node, 0, 3)
        self.assertEqual(
            path_0_to_3, [0, 1, 3], "Path from 0 to 3 should be [0, 1, 3]."
        )


if __name__ == "__main__":
    unittest.main()
