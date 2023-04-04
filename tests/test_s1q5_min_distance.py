import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_Reachability(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.get_path_with_power_dijkstra(2, 3, 5), [2,3])
        self.assertEqual(g.get_path_with_power_dijkstra(1, 3, 0), None)

if __name__ == '__main__':
    unittest.main()
