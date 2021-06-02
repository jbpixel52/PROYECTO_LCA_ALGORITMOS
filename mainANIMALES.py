#%%
import networkx as nx
import json
import matplotlib
import matplotlib.pyplot as plt

animalesDisponibles = [
    "Turkey",
    "Green anole",
    "Gray short-tailed opossum",
    "Tasmanian devil",
    "Ferret",
    "Dog",
    "Giant panda",
    "Pig",
    "European shrew",
    "Thirteen-lined ground squirrel",
    "Domestic guinea pig",
    "Northern tree shrew",
    "Bottlenosed dolphin",
    "Alpaca",
    "Large flying fox",
    "Little brown bat",
    "Horse",
    "Philippine tarsier",
    "Small-eared galago",
    "Ord's kangaroo rat",
    "Nine-banded armadillo",
    "Cattle",
    "Western European hedgehog",
    "Human",
    "Western gorilla",
    "Sumatran orangutan",
    "Northern white-cheeked gibbon",
    "Rhesus monkey",
    "Gray mouse lemur",
    "Norway rat",
    "House mouse",
    "Cape rock hyrax",
    "Platypus",
    "Western clawed frog",
    "Coelacanth",
    "Japanese medaka",
    "Southern platyfish",
    "Nile tilapia",
    "Torafugu",
    "Spotted green pufferfish",
    "Zebrafish",
    "Coelacanth",
    "D.persimilis",
    "D.pseudoobscura",
    "D.grimshawi",
    "D.yakuba",
    "D.erecta",
    "D.simulans",
    "D.sechellia",
    "Fruit fly",
    "D.anannassae",
    "D.pseudoobscura",
    "D.persimilis",
    "D.willistoni",
    "D.virilis",
    "D.mojavensis",
    "D.grimshawi",
    "African malaria mosquito",
    "Mosquito",
    "Southern house mosquito",
    "Yellow fever mosquito",
    "Leafcutter ant",
    "Honey bee",
    "Wasp",
    "Red flour beetle",
    "Monarch butterfly",
    "The red postman",
    "Domestic silkworm",
    "Human louse",
    "Common water flea",
    "Pea aphid",
    "Pine wood nematode",
    "Northern root-knot nematode",
    "Netamode",
    "Rat parasite",
    "C.remanei",
    "C.briggsae",
    "C.brenneri",
    "C.elegans",
    "C.japonica",
    "C.japonica",
    "Pine wood nematode",
    "Whipworm",
    "Black-legged tick",
    "Owl limpet",
    "Sea vase",
    "Sea squirt",
    "Purple urchin",
    "Starlet sea anemone",
    "Placozoa",
    "Sponge",
    "Blood fluke"
]


## ---------------- Ingreso de datos ------------------------------------------------------------ ##
print('#### PROYECTO DE ANALISIS DE ALGORITMOS ####\n')
input("Presione cualquier tecla para mostrar un listado de animales disponibles para uso de LCA: ")

for animal in animalesDisponibles:
    print(animal)

print()
test = input("Ingrese el primer animal: ")
test2 = input("Ingrese el segundo animal: ")

## ---------------------------------------------------------------------------------------------- ## 

class Node():
    def __init__(self, name, isFamily, left, right, properties, commonName):
        self.isFamily = isFamily
        self.left = left
        self.right = right
        self.properties = properties
        self.name = name
        self.commonName = commonName
        pass    

class Tree():
    def __init__(self, root, size):
        self.root = root
        self.size = size
        self.superNodoA  = None ##Gren anole
        self.superNodoB = None ##sumatran oran
        pass

def lowestCommonAncestor(root, node1, node2): 
    if(not root):
         return None
    if (vars(root) == vars(node1) or vars(root) == vars(node2)): 
        return root
    left = lowestCommonAncestor(root.left, node1, node2)
    right = lowestCommonAncestor(root.right, node1, node2)
    if left!=None and right!=None:
        return root
    if left:
        return left
    else:
        return right

def iterativeChildren(familia, Arbol, Ancestor, NodoReino, ReinoU):    
    if("taxon" in familia):
        if(familia["common_name"]==test):
            ReinoU.superNodoA = Node(familia["taxon"],False,None,None,familia, None)
        if(familia["common_name"]==test2):
            ReinoU.superNodoB = Node(familia["taxon"],False,None,None,familia, None)       
        Arbol.add_node(familia["taxon"])
        Arbol.add_edge(familia["taxon"],Ancestor, weight=4.70)
        ##Es una especie
        ##Anadir al arbol artesanal Derecho y animal
        if(NodoReino.right!= None):
            NodoReino.left = Node(familia["taxon"],False,None,None,familia, None)
        else:
            NodoReino.right = Node(familia["taxon"],False,None,None,familia, None)
    else:

        Arbol.add_node(familia["name"])
        Arbol.add_edge(familia["name"],Ancestor, weight=4.70)
        ##Es otro subarbol, reiterar
        ##Pero antes meter al arbol artesanal
        if(NodoReino.left != None):
            ##Nota, puede haber dos familias
            NodoReino.right = Node(familia["name"],True,None,None,None, None)
            for subfamilia in familia["children"]:
                iterativeChildren(subfamilia, Arbol, familia["name"], NodoReino.right, ReinoU)
        else:
            NodoReino.left = Node(familia["name"],True,None,None,None, None)
            for subfamilia in familia["children"]:
                iterativeChildren(subfamilia, Arbol, familia["name"], NodoReino.left, ReinoU)   


with open('./CCNBA_Metazoa_3.json') as animales:

    metazoa = json.load(animales)
    Arbol = nx.Graph()
    Arbol.add_node("Metazoa_3",size=100, node_color='y')

    Reino = Tree(None,0)
    Reino.root = Node("Metazoa_3",True,None,None,None, None)
    
    for familia in metazoa["children"]:
        iterativeChildren(familia, Arbol, "Metazoa_3", Reino.root, Reino)
    

    color_map = []
    for node in Arbol:
        if node == "Metazoa_3":
            color_map.append('blue')
        else:
            color_map.append('green') 
            
    nx.draw(Arbol, font_size=6, node_color=color_map, edge_color='g', with_labels=True)

    LCAtest = lowestCommonAncestor(Reino.root, Reino.superNodoA,Reino.superNodoB)
    print('LCA is:', LCAtest.name)


# %%
