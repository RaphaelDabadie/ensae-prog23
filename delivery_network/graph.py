

class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        
        self.nb_edges+=1
        self.graph[node1].append((node2,power_min, dist))
        self.graph[node2].append((node1,power_min, dist))
        
    

    def get_path_with_power(self, src, dest, power):
        visited = set() #mieux que dictionnaire initialement utilisé

        def dfs2(node, path):
            if node==dest: #on arrête le trajet quand on a atteint la destination souhaitée dest
                return path

            visited.add(node)
            for neighbor, edge_power, edge_dist in self.graph[node]: #on va chercher les couples (voisins, puissance) du point de départ "src"
                if neighbor not in visited and power>=edge_power: # on s'assure que power est bien supérieure ou égale à power_min
                        composante = dfs2(neighbor, path+[neighbor])
                        if composante is not None:
                            return composante
            visited.remove(node)
            return None    #on retourne None au cas où la puissance power n'est pas suffisante
        return dfs2(src, [src])


#question 5 : on utilise Dijkstra


    def get_path_with_power_dijkstra(self, src, dest, power):
        d=dict([(node,(float('inf'),node)) for node in self.nodes])
        d[src]=0
        H, F= [], [(0,src)]
        while F!=[]:
            node=F.pop()
            for neighbor in self.graph[node]:
                if neighbor[1]<=power and (d[neighbor[0]][0], neighbor[0]) not in (F+H):
                    x=d[node[1]][1]+neighbor[2]
                    if x<d[neighbor[0]]:
                        d[neighbor[0]]=(x,node)
                        F=sorted(F.append(d[neighbor[0]][0], neighbor[0]), reverse=True)
                        H.append(node)
        if d[dest][1]==float("inf"):
            return None
        else:
            path,node=[dest],dest
            while node!=src:
                node=d[node][1]
                path.append(node)
            return reversed(path)




        
    
        

    

    def connected_components(self):
        listes_composantes =[]
        noeud_visite = {noeud:False for noeud in self.nodes}
        #On code d'abord un parcours en profondeur
        def dfs(noeud):
            componante =[noeud]
            for neighbor in self.graph[noeud]:
                neighbor= neighbor[0]
                if not noeud_visite[neighbor]:
                    noeud_visite[neighbor]=True
                    componante+= dfs(neighbor)
            return (componante)

        for noeud in self.nodes:
            if not noeud_visite[noeud]:
                listes_composantes.append(dfs(noeud))
        
        return listes_composantes


    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        #on crée une liste regroupant l'ensemble des puissances, on la trie dans l'ordre croissant, puis on recherche la puissance minimum avec une recherche dichotomique
        powers_list=[]
        for node in self.nodes:
            for voisin in self.graph[node]:
                if voisin[1] not in powers_list:
                    powers_list.append(voisin[1]) 
        powers_list.sort()
        maximum=len(powers_list)
        minimum=0
        if self.get_path_with_power(src,dest,powers_list[0])!=None:
            return (self.get_path_with_power(src,dest,powers_list[minimum]),powers_list[minimum])
        while maximum>minimum+1:
            middle=(maximum+minimum)//2
            middle_power=powers_list[middle]
            if self.get_path_with_power(src,dest,middle_power)==None:
                minimum=middle
            else :
                maximum=middle
        return (self.get_path_with_power(src,dest,powers_list[maximum]), powers_list[maximum])
        


    


















        





            


def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """
    with open(filename) as file: #with assure la fermeture du fichier après lecture
        line1 = file.readline().split()
        n=int(line1[0])
        m=int(line1[1])
        nodes= [i for i in range (1,n+1)]
        G=Graph(nodes)
        for i in range(m):
            linei=file.readline().split() #on lit chaque ligne du fichier
            node1= int(linei[0])
            node2= int(linei[1])
            power_min=int(linei[2])
            if len(linei)>3: #cas où on doit prendre en compte la distance
                dist = int(linei[3])
                G.add_edge(node1, node2, power_min, dist)
            else :
                G.add_edge(node1, node2, power_min, dist=1)
    return G




















