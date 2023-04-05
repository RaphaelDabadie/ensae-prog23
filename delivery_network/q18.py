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

