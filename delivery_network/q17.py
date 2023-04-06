from time import perf_counter
from graph import Graph, graph_from_file
from main import min_power_bfs

def test_routes_n_bis(n, nombre_essais):
    data_path = "input/"
    file_name = "routes."
    numero = str(n)
    g = graph_from_file("input/network." + numero + ".in")
    
    with open(data_path + file_name + numero + '.in', 'r') as file:
        t1_start = perf_counter()
        s= 0
        output= []
        
        for i in range(nombre_essais):
            lignei = file.readline().split()
            if len(lignei) > 1:  # premier élément du fichier routes pose problème donc on l'exclut
                ville1 = int(lignei[0])
                ville2 = int(lignei[1])
                min_power= min_power_bfs(g, ville1, ville2)
                output.append(min_power)
            else:
                s += int(lignei[0])
        
        t1_stop = perf_counter()
    
    with open(data_path + file_name + "bis" + numero + '.out', 'w') as outfile:
        for power in output:
            outfile.write(str(power) + '\n')


    print("Temps d'exécution pour le fichier routes " + numero + " en secondes:",(t1_stop-t1_start)*(s/nombre_essais)),


test_routes_n_bis(1, 15)
test_routes_n_bis(4, 15) 
test_routes_n_bis(5, 15) 
test_routes_n_bis(6, 15)
test_routes_n_bis(7, 15)

