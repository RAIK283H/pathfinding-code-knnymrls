import math
import unittest
from pathing import get_random_adjacent_node, get_random_path
import global_game_data

class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    def setUp(self):
        global_game_data.current_graph_index = 0 
        global_game_data.target_node = [1]
        self.test_graph = [
            [(0, 0), [1, 2]], 
            [(1, 1), [0, 2]],  
            [(2, 2), [0, 1]]   
        ]

    def test_get_random_adjacent_node(self):
        current_node = 0
        adjacent_node = get_random_adjacent_node(self.test_graph, current_node)
        self.assertIn(adjacent_node, [1, 2], "Random adjacent node should be one of the valid neighbors [1, 2].")

    def test_random_path_basic(self):
        random_path = get_random_path()
        self.assertEqual(random_path[0], 0, "Path should start at node 0.")
        self.assertEqual(random_path[-1], 2, "Path should end at node 2 (the exit node).")

if __name__ == '__main__':
    unittest.main()
