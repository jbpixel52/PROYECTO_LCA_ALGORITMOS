#%%
import networkx as nx
import json
import matplotlib.pyplot as plt

print('#### PROYECTO DE ANALISIS DE ALGORITMOS ####\n')

with open('./characters.json') as got:
    GOT = json.load(got)
    

G = nx.DiGraph()
characterlist = []



def family(name):
    # for character in GOT:
    #     if character['name']==name:
    #         G.add_node((character['name']),node_size=len(character['_children']))
    #         for children in character['_children']:
    #             G.add_edge(character['name'],children['name'])

    for character in GOT['characters']:
        if character['characterName']==name:
            G.add_node(character['characterName'])
            if 'parentOf' in character:
                for children in character['parentOf']:
                    G.add_edge(character['characterName'],children)

def search(name):
    #Creo que esta ya funciona
    for node in G:
        if node ==name:
            #print(name, 'exists in G')
            return True
    #print(name,'no existe en G')
    return False


def index_character():

    count=0
    for character in GOT['characters']:
        if count>500:
            return
        characterlist.append(character)
        count+=1
        
def adder():
    for character in characterlist:
        if search(character['characterName'])==False:
            family(character['characterName'])


def child_to_root():
     for node in G:
         if(len(list(G.predecessors(node))) < 1):
            # Para personas que no tienen ancestros
            G.add_edge('ROOT',node)


def revisarAncestros(nodo, tempList):
    
    for element in list(G.predecessors(nodo)):
        tempList.append(element)
        if(len(list(G.predecessors(element))) > 1):
            revisarAncestros(element, tempList)
        else:
            
            tempList.append(list(G.predecessors(element))[0])

    return tempList


def LCA(nodo1, nodo2):
    todosLosAncestrosNodo1 = []
    todosLosAncestrosNodo2 = []
    
    print(revisarAncestros(nodo1, todosLosAncestrosNodo1))
    print(revisarAncestros(nodo2, todosLosAncestrosNodo2))
    
    


def main():
    index_character()
    G.add_node('ROOT', node_size=200,node_color='y')
    print('IS G TREE?',nx.is_tree(G))
    adder()
    child_to_root()
    plt.gcf().set_size_inches(2 * plt.gcf().get_size_inches()) 
    nx.draw_networkx(G, pos = nx.random_layout(G),node_size=50,node_color='r',edge_color='b',font_size=5,with_labels=True, alpha=0.5)

    LCA("Robb Stark", "Jon Snow")

    plt.savefig('gotplotgraph.png', dpi=400, bbox_inches='tight')
    plt.show()


main()
# %%
