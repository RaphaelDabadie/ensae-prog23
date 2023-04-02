from graph import Graph, graph_from_file
import graphviz

data_path = "input/"
file_name = "network.1.in"

g = graph_from_file(data_path + file_name)

from graphviz import Graph

#on crée un nouveau graphe
Graphe_a_afficher = graphviz.Graph()
for node in g.nodes:
    noeud=str(node)
    Graphe_a_afficher.node(noeud)

print(Graphe_a_afficher)


L=[]
for node in g.graph:
    edges=g.graph[node]
    for i in range (len(edges)):
        #Edge prend en arguments des chaines de caractères donc on veille à ce que les paramètres soient des str
        neighbor=str(g.graph[node][i][0])
        power=str(g.graph[node][i][1])
        distance=str(g.graph[node][i][2])
        noeud=str(node)
        Graphe_a_afficher.edge(noeud, neighbor,label=f"{power}, {distance}")
    else:
        continue


Graphe_a_afficher.render('graphefinal', view=True, format='png')

