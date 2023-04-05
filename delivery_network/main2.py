
"""
from graph import Graph

class DisJointSets():
    def __init__(self,N):
        # Initially, all elements are single element subsets
        self._parents = [node for node in range(N)]
        self._ranks = [1 for _ in range(N)]

    def find(self, u):
        while u != self._parents[u]:
            # path compression technique
            u = self._parents[u]
            self._parents[u] = self._parents[self._parents[u]]
        return u

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def union(self, u, v):
        # Union by rank optimization
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return True
        if self._ranks[root_u] > self._ranks[root_v]:
            self._parents[root_v] = root_u
        elif self._ranks[root_v] > self._ranks[root_u]:
            self._parents[root_u] = root_v
        else:
            self._parents[root_u] = root_v
            self._ranks[root_v] += 1
        return False



def liste_aretes(G):
    L=[]
    for node in G.nodes:
        for neighbour in G.graph[node]:
            L.append((neighbour[1],node,neighbour[0],neighbour[2]))
    return L



def kruskal(G):
    A=Graph(G.nodes)
    unionfind=DisJointSets(len(G.nodes))
    L=liste_aretes(G)
    L.sort() 
    for edge in L:
        a=edge[1]
        b=edge[2]
        p=edge[0]
        d=edge[3]
        if unionfind.find(a)!=unionfind.find(b):
            A.add_edge(a,b,p,d)
            unionfind.union(a,b)
    return A

"""


