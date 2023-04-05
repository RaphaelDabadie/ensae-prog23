from graph import Graph, graph_from_file

def lire_trucks(n):
    data_path = "input/"
    file_name = "trucks."
    numero=str(n)
    g=graph_from_file("input/network."+numero+".in")
    with open(data_path + file_name + numero + '.in', 'r') as file:
        ligne0=file.readline().split()
        taille=int(ligne0[0])
        L=[]
        for i in range(taille):
            lignei=file.readline().split()
            if len(lignei)>1: 
                puissance= int(lignei[0])
                cout= int(lignei[1])
                L.append((puissance,cout))
    return L



def lire_routes(n):
    data_path = "input/"
    file_name = "routes."
    numero=str(n)
    g=graph_from_file("input/network."+numero+".in")
    with open(data_path + file_name + numero + '.in', 'r') as file:
        ligne0=file.readline().split()
        taille=int(ligne0[0])
        L=[]
        for i in range(taille):
            lignei=file.readline().split()
            if len(lignei)>1: 
                ville1= int(lignei[0])
                ville2= int(lignei[1])
                utilite=int(lignei[2])
                L.append((ville1,ville2,utilite))
    return L




#Pour débuter, on va coder une fonction qui renvoie la liste des camions qui ont un intéret (ie tq n'existe pas de camion de puissance supérieure et de cout inférieur)
def useful_tracks(tracks):
    #rq tracks est une liste contenant les couples (puissance, cout) des camions qu'on suppose triés par ordre de puissance croissante (c'est le cas dans les fichiers fournis)
    #la fonction renvoie la liste des camions triée en ordre décroissante
    useful_tracks=[]
    cost=tracks[len(tracks)][1]
    for i in (len(tracks)-1, 0, -1):
        if tracks[i-1]!=tracks[i] and tracks[i][1]<cost:
            useful_tracks.append(tracks[i])
            cost=tracks[i][1]
    return useful_tracks
    


### coder une fonction qui à un trajet associe le coût minimal pour le parcourir en utilisant min_power
def cout_trajet(G,node1,node2,tracks):
    #où tracks est une liste contenant les couples (puissance, cout) des camions triée en ordre décroissant
    power_min_path = min_power_bis(node1,node2,tracks)
    for i in len(tracks):
        if tracks[i][0]<power_min_path:
            if i+1==len(tracks):
                return None
            return tracks[i+1][1]
    

###Implémentation de l'algorithme glouton

def algo_glouton(graphe,tracks):
    useful_tracks= useful_tracks(tracks)
    #on calcule la liste triée par ordre décroisant des rapports entre le gain rapporté par un trajet et le cout minimal nécessaire pour le parcourir 
    liste=[]
    for node1 in graph.nodes:###c'est sans doutes mieux d'énumérer sur la liste des trajets car pas forcément tous les couples de noeuds font partie des trajets à couvrir
        for node2 in graph.nodes:
            c=cout_trajet(graph,node1,node2,tracks)
            if c!=None:
                gain=#à compléter
                x=(gain/c,c,node1,node2)
                liste.append(x)
    sorted(liste, reversed=True) ####à trier par ordre décroissant
    cost=0
    nouvelle_liste=[]
    for i in range(len(liste)):
        if cost+liste[i][1] <= B:
            nouvelle_liste.append(liste[i])
            cost+=liste[i][1]
    return nouvelle_liste

    #pour chacun des éléments de la liste, on choisit le trajet si la somme des trajets est 

def algo_glouton(graphe,tracks,routes):
    #routes est une liste de triplets (noeud1,noeud2,gain), tracks une liste de couples (puissance, cout) supposée triée par ordre décroissant
    useful_tracks= useful_tracks(tracks)
    #on calcule la liste triée par ordre décroisant des rapports entre le gain rapporté par un trajet et le cout minimal nécessaire pour le parcourir 
    liste=[]
    for (noeud1,noeud2,gain) in routes:
        c=cout_trajet(graph,node1,node2,tracks)
        if c!=None:
            x=(gain/c,c,node1,node2)
            liste.append(x)
    sorted(liste,reversed=True) ####à trier par ordre décroissant
    cost=0
    nouvelle_liste=[]
    for i in range(len(liste)):
        if cost+liste[i][1] <= B:
            nouvelle_liste.append(liste[i])
            cost+=liste[i][1]
    return nouvelle_liste   


    