import networkx as nx
import json
import matplotlib
import matplotlib.pyplot as plt

class Node():
    def __init__(self, name, isFamily, left, right, properties):
        self.isFamily = isFamily
        self.left = left
        self.right = right
        self.properties = properties
        self.name = name
        pass    

class Tree():
    def __init__(self, root, size):
        self.root = root
        self.size = size
        pass

print('#### PROYECTO DE ANALISIS DE ALGORITMOS ####\n')

def iterativeChildren(familia, Arbol, Ancestor, NodoReino):
    if("taxon" in familia):
        Arbol.add_node(familia["taxon"])
        Arbol.add_edge(familia["taxon"],Ancestor, weight=4.70)
        ##Es una especie
        ##Anadir al arbol artesanal Derecho y animal
        if(NodoReino.right!= None):
            NodoReino.left = Node(familia["taxon"],False,None,None,familia)
        else:
            NodoReino.right = Node(familia["taxon"],False,None,None,familia)
    else:
        Arbol.add_node(familia["name"])
        Arbol.add_edge(familia["name"],Ancestor, weight=4.70)
        ##Es otro subarbol, reiterar
        ##Pero antes meter al arbol artesanal
        if(familia["name"]=="Coelomata_6"):
            print("a")
        if(NodoReino.left != None):
            ##Nota, puede haber dos familias
            NodoReino.right = Node(familia["name"],True,None,None,None)
            for subfamilia in familia["children"]:
                iterativeChildren(subfamilia, Arbol, familia["name"], NodoReino.right)
        else:
            NodoReino.left = Node(familia["name"],True,None,None,None)
            for subfamilia in familia["children"]:
                iterativeChildren(subfamilia, Arbol, familia["name"], NodoReino.left)   


with open('./CCNBA_Metazoa_3.json') as animales:
    metazoa = json.load(animales)
    #print(metazoa)
    Arbol = nx.Graph()
    Arbol.add_node("Metazoa_3",size=100, node_color='y')

    Reino = Tree(None,0)
    Reino.root = Node("Metazoa_3",True,None,None,None)
    
    for familia in metazoa["children"]:
        iterativeChildren(familia, Arbol, "Metazoa_3", Reino.root)
    

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
    print(Reino)
