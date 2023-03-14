import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   

class Test_Reachability(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.get_path_with_power(1, 3, 4), [1, 2, 3])
        self.assertEqual(g.get_path_with_power(1, 2, 3), None)


if __name__ == '__main__':
    unittest.main()
