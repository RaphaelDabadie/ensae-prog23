from graph import Graph 

class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1




#Question 12
#Rmq on utilise pour cette question la structure d'Union Find définie plus haut
#On définit préalablement une fonction liste_arêtes qui prend en argument un graphe et renvoie la liste des arêtes

def liste_aretes(G):
    L=[]
    for node in G.nodes:
        for neighbour in G.graph[node]:
            if node < neighbour[0]: #éviter les doublons du type (node1,node2) (node2,node1)
                L.append((neighbour[1],node,neighbour[0],neighbour[2]))
    return L



def kruskal(G):
    A=Graph(G.nodes)
    unionfind = UnionFind(list(G.graph.keys()))
    L=liste_aretes(G)
    L.sort(key=lambda x: x[0])  #On trie les arêtes en fonction du premier élément
    for edge in L:
        a, b, p, d = edge
        if unionfind.find(a)!=unionfind.find(b):
            A.add_edge(a,b,p,d)
            unionfind.union(a,b)
    return A



#Question 14


def min_power_bis(G, node1, node2):
    A = kruskal(G)
    path = A.get_path_with_power(node1, node2, float('inf'))
    min_power = 0
    for node, next_node in zip(path[:-1], path[1:]):
        edge_index = next((i for i, edge in enumerate(A.graph[node]) if edge[0] == next_node), None)
        edge_power = A.graph[node][edge_index][1]
        min_power = max(min_power, edge_power)

    return (min_power, path)

