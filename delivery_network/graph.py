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
        noeud_visite = {noeud:False for noeud in self.nodes}

        def dfs2(node, path):
            if node==dest: #on arrête le trajet quand on a atteint la destination souhaitée dest
                return path
            for voisin in self.graph[node]: #on va chercher les voisins du point de départ "src"
                if not noeud_visite[voisin[0]] and power>=voisin[1]: # on s'assure que power est bien supérieure ou égale à power_min
                        noeud_visite[voisin[0]]=True
                        composante = dfs2(voisin[0], path+[voisin[0]])
                        if composante is not None:
                            return composante
            return None    #on retourne None au cas où la puissance power n'est pas suffisante
        return dfs2(src, [src])


#question 5 


    def get_path_with_power2(self, src, dest, power):
            noeud_visite = {noeud:False for noeud in self.nodes}

            def dfs3(node, path):
                distance=0
                if node==dest: #on arrête le trajet quand on a atteint la destination souhaitée dest
                    return path
                for voisin in self.graph[node]: #on va chercher les voisins du point de départ "src"
                    if not noeud_visite[voisin[0]] and power>=voisin[1]: # on s'assure que power est bien supérieure ou égale à power_min
                            noeud_visite[voisin[0]]=True
                            composante= dfs3(voisin[0], path+[voisin[0]])
                            distance+=voisin[2]
                            if composante is not None:
                                return distance
                return None    #on retourne None au cas où la puissance power n'est pas suffisante
            return dfs3(src, [src])


        
    
        

    

    def connected_components(self):
        listes_composantes =[]
        noeud_visite = {noeud:False for noeud in self.nodes}

        def dfs(noeud):
            componante =[noeud]
            for neighbour in self.graph[noeud]:
                neighbour= neighbour[0]
                if not noeud_visite[neighbour]:
                    noeud_visite[neighbour]=True
                    componante+= dfs(neighbour)
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
        def get_path_with_power(self, src, dest, power):
            noeud_visite = {noeud:False for noeud in self.nodes}

            def dfs2(node, path):
                if node==dest: #on arrête le trajet quand on a atteint la destination souhaitée dest
                    return path
                for voisin in self.graph[node]: #on va chercher les voisins du point de départ "src"
                    if not noeud_visite[voisin[0]] and power>=voisin[1]: # on s'assure que power est bien supérieure ou égale à power_min
                            noeud_visite[voisin[0]]=True
                            composante = dfs2(voisin[0], path+[voisin[0]])
                            if composante is not None:
                                return composante
                return None    #on retourne None au cas où la puissance power n'est pas suffisante
            return dfs2(src, [src])

        #liste triée de toutes les power, partir de la puissance du milieu et utiliser gpwp. Si on en a, on va chercher voiture avec puissance plus basse et inversement sinon
        powers_list=[]
        for node in self.nodes:
            if self.graph[node][1] not in powers_list:
                powers_list.append(self.graph[node][1]) 
        powers_list.sort()
        middle=(len(powers_list)//2)
        puissance=powers_list[middle] #on part de la puissance du milieu
        if get_path_with_power(src,dest,puissance)==None: #dans ce cas on doit augmenter la puissance du camion
            while get_path_with_power(src,dest,puissance)==None:
                puissance=powers_list[middle+1]
            return (get_path_with_power(src,dest,puissance), puissance)
        else:
                puissance=powers_list[middle-1]
                if get_path_with_power(src,dest,puissance)==None:
                    return((get_path_with_power(src,dest,powers_list[middle]), powers_list[middle]))
                else:
                    while not get_path_with_power(src,dest,puissance)==None:
                        puissance=powers_list[middle-1]
                    return (get_path_with_power(src,dest,puissance+1), puissance+1)


        

            















        





            


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
    with open(filename) as file:
        ligne1 = file.readline().split()
        n=int(ligne1[0])
        m=int(ligne1[1])
        nodes= [i for i in range (1,n+1)]
        G=Graph(nodes)
        for i in range(m):
            lignei=file.readline().split()
            node1= int(lignei[0])
            node2= int(lignei[1])
            power_min=int(lignei[2])
            if len(lignei)>3:
                dist = int(lignei[3])
                G.add_edge(node1, node2, power_min, dist)
            else :
                G.add_edge(node1, node2, power_min, dist=1)
    return G



