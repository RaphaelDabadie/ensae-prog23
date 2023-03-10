import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file, get_path_with_power
from main import Union_Find
from main import kruskal, liste_aretes, min_power_bis

import unittest   # The test framework

class Test_minpowerbis(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        a=g.min_power(2,10)
        b=min_power_bis(g,2,10)
        for node in g.nodes:
            self.assertEqual((a.graph[node]).sort(), (g.graph[node]).sort())

if __name__ == '__main__':
    unittest.main()