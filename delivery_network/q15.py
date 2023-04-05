from time import perf_counter
from graph import Graph, graph_from_file
from main import min_power_bis

data_path = "input/"
file_name = "network.04.in"




def creer_route_out(n,puissances):
    file_name = "routes."+str(n)+".out"
    with open(file_name, 'w') as file:
        for el in puissances:
            file.write(str(el[0])+"\n")

#On va faire tourner min_power_bis sur les 'nombre_essais' premiers trajets de routes.n.in
def test_routes_n_bis(n, nombre_essais):
    data_path = "input/"
    file_name = "routes."
    numero=str(n)
    g=graph_from_file("input/network."+numero+".in")
    puissances = []
    with open(data_path + file_name + numero + '.in', 'r') as file:
        t1_start = perf_counter()
        s=0
        for i in range(nombre_essais):
            lignei=file.readline().split()
            if len(lignei)>1: #premier élément du fichier routes pose problème donc on l'exclut
                ville1= int(lignei[0])
                ville2= int(lignei[1])
                print(ville1,ville2)
                print(lignei)
                if lignei[0] in g.nodes:
                    puissance= min_power_bis(g,ville1, ville2)
                    if puissance==None:
                        print("a")
                    puissances.append(puissance)
                    print(puissances)
                else:
                    continue
            else:
                s+=int(lignei[0])
        t1_stop = perf_counter()

    print("Puissances :", puissances)
    print("Temps d'exécution pour le fichier routes " + numero + " en secondes:",(t1_stop-t1_start)*(s/nombre_essais)),
    creer_route_out(n, puissances)

test_routes_n_bis(3, 15)
test_routes_n_bis(4, 15) 
test_routes_n_bis(5, 15) 
test_routes_n_bis(6, 15)
test_routes_n_bis(7, 15)



