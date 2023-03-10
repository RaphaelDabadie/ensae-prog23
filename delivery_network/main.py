from graph import Graph 

class Union_Find:
    def __init__(self,set):
        self.partition=[[x] for x in set]
    def find(self,x):
        for subset in self.partition:
            if x in subset:
                return subset
    def union(self,x1,x2):
        subset_x1,subset_x2=self.find(x1),self.find(x2)
        self.partition=([subset for subset in self.partition if (subset!=subset_x1 and subset!=subset_x2)]+[subset_x1+subset_x2])


#On teste la classe ainsi définie :

u=Union_Find([0,1,2,3,4,5]) 
print(u.partition)
print(u.find(2))
u.union(1,2)
print(u.partition)
# On trouve bien les valeurs attendues

#Question 12
#Rmq on utilise pour cette question la structure d'Union Find définie plus haut
#On définit préalablement une fonction liste_arêtes qui prend en argument un graphe et renvoie la liste des arêtes

def liste_aretes(G):
    L=[]
    for node in G.nodes:
        for neighbour in G.graph[node]:
            L.append((neighbour[1],node,neighbour[0],neighbour[2]))
    return L



def kruskal(G):
    A=Graph(G.nodes)
    unionfind=Union_Find(G.nodes)
    L=liste_aretes(G)
    L.sort() 
    for edge in L:
        a=edge[1]
        b=edge[2]
        p=edge[0]
        d=edge[3]
        if unionfind.find(a)[0]!=unionfind.find(b)[0]:
            A.add_edge(a,b,p,d)
            unionfind.union(a,b)
    return A



#Question 14
def min_power_bis(G, node1, node2):
    A=kruskal(G)
    return G.get_path_with_power(node1,node2,float('inf'))



