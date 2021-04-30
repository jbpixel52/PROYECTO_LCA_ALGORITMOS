import networkx as nx
import json
import matplotlib
import matplotlib.pyplot as plt

print('#### PROYECTO DE ANALISIS DE ALGORITMOS ####\n')

def iterativeChildren(familia, Arbol, Ancestor):
    if("taxon" in familia):
        Arbol.add_node(familia["taxon"])
        Arbol.add_edge(familia["taxon"],Ancestor, weight=4.70)
        ##Es una especie
        pass
    else:
        Arbol.add_node(familia["name"])
        Arbol.add_edge(familia["name"],Ancestor)
        ##Es otro subarbol, reiterar
        for subfamilia in familia["children"]:
            iterativeChildren(subfamilia, Arbol, familia["name"])


with open('./CCNBA_Metazoa_3.json') as animales:
    metazoa = json.load(animales)
    #print(metazoa)
    Arbol = nx.Graph()

    Arbol.add_node("Metazoa_3",size=100, node_color='y')

    for familia in metazoa["children"]:
        iterativeChildren(familia, Arbol, "Metazoa_3")
    

    color_map = []
    for node in Arbol:
        if node == "Metazoa_3":
            color_map.append('blue')
        else:
            color_map.append('green') 
            
    nx.draw(Arbol, font_size=6, node_color=color_map, edge_color='g', with_labels=True)


    #nx.lowest_common_ancestor(G,'Cable','Hope Summers')
    plt.savefig('plotgraph.png', dpi=400, bbox_inches='tight')
    plt.show()
    print (matplotlib.__version__)
