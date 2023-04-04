from graph import Graph, graph_from_file
from main import kruskal


data_path = "input/"
file_name = "network.3.in"

g = graph_from_file(data_path + file_name)
r=kruskal(g)
print(r)


 