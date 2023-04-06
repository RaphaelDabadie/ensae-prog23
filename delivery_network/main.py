from graph import Graph 
from math import log2

class UnionFind:
    def __init__(self, nodes):
        #on initialise chaque noeud comme son propre parent 
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, node): #Trouver la racine d'un noeud 
        if node not in self.parent:
            raise KeyError(f"Noeud {node} introuvable dans UnionFind")
        if self.parent[node] != node: #idée : lorsque le noeud n'est pas la racine, remonter dans l'arbre
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2): #on fusionne deux ensembles différents (ie pas la même racine)
        rac1, rac2 = self.find(node1), self.find(node2)
        if rac1 != rac2:
            if self.rank[rac1] > self.rank[rac2]:
                self.parent[rac2] = rac1
            else:
                self.parent[rac1] = rac2
                if self.rank[rac1] == self.rank[rac2]:
                    self.rank[rac2] += 1
    def print_nodes(self):
        print("Noeuds présents dans UnionFind:")
        for node in self.parent:
            print(node)



#Question 12
#Rmq on utilise pour cette question la structure d'Union Find définie plus haut
#On définit préalablement une fonction liste_arêtes qui prend en argument un graphe et renvoie la liste des arêtes

def liste_aretes(G):
    L=[]
    for node in G.nodes:
        for neighbour in G.graph[node]:
            if node < neighbour[0]: #éviter les doublons du type (node1,node2) (node2,node1)
                L.append((neighbour[0],node,neighbour[1],neighbour[2]))
    return L



def kruskal(G):
    A=Graph(G.nodes)
    unionfind = UnionFind(list(G.graph.keys()))
    L=liste_aretes(G)
    L.sort(key=lambda x: x[0])
    #On trie les arêtes en fonction du premier élément
    for edge in L:
        a, b, p, d = edge
        if unionfind.find(a)!=unionfind.find(b):
            A.add_edge(a,b,p,d)
            unionfind.union(a,b)
    return A



#Question 14


def min_power_bis(G, node1, node2):
    A = kruskal(G) #arbre couvrant de poids minimum
    path = A.get_path_with_power(node1, node2, float('inf')) #float(inf) permet de s'assurer que toutes les arêtes sont parcourues. On trouve ici le chemin entre nodes 1 et 2 dans l'arbre
    #min_power correspond à la puissance minimale nécessaire pour parcourir le chemin : pour cela on trouve l'arête de poids maximal dans ce chemin
    min_power = max(edge[1] for node, list_edge in A.graph.items() for edge in list_edge if ((edge[0] in path) and (node in path))) #on verifie à la fin que l'arête connecte bien deux noeuds présents dans le chemin trouvé. 
    #on choisit un camion qui a au moins une puissance permettant de passer par l'arête de poids max
    return (min_power, path)



