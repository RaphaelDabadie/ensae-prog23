from time import perf_counter
from graph import Graph, graph_from_file
from main import Union_Find, min_power_bis


#On va faire tourner min_power_bis sur les 'nombre_essais' premiers trajets de routes.n.in
def test_routes_n_bis(n, nombre_essais):
    data_path = "input/"
    file_name = "routes."
    numero=str(n)
    g=graph_from_file("input/network."+numero+".in")
    with open(data_path + file_name + numero + '.in', 'r') as file:
        t1_start = perf_counter()
        s=0
        for i in range(nombre_essais):
            lignei=file.readline().split()
            if len(lignei)>1: #premier élément du fichier routes pose problème donc on l'exclut
                ville1= int(lignei[0])
                ville2= int(lignei[1])
                puissance= min_power_bis(g,ville1, ville2)
            else:
                s+=int(lignei[0])
        t1_stop = perf_counter()

    print("Temps d'exécution pour le fichier routes " + numero + " en secondes:",(t1_stop-t1_start)*s/nombre_essais)


test_routes_n_bis(3, 1)
test_routes_n_bis(4, 1) 
test_routes_n_bis(5, 1) 
test_routes_n_bis(6, 1)
