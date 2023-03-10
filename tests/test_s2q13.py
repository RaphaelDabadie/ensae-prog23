import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file
from main import Union_Find
from main import kruskal, liste_aretes

import unittest   # The test framework

class Test_Kruskal(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        a=kruskal(g)
        for node in g.nodes:
            self.assertEqual((a.graph[node]).sort(), (g.graph[node]).sort())
        
if __name__ == '__main__':
    unittest.main()