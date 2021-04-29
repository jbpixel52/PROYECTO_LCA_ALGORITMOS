# %%
import networkx as nx
import json
import matplotlib.pyplot as plt

print('#### PROYECTO DE ANALISIS DE ALGORITMOS ####\n')

with open('./marvel.json') as marvel:
    MARVEL = json.load(marvel)


G = nx.DiGraph()
characterlist = []


def king():
    hijos = 0
    name = ''
    for character in MARVEL:
        temp = 0
        temp = len(character['_children'])
        if temp > hijos:
            hijos = temp
            temp = 0
            name = character['name']
    print(name, 'es quien tiene mas hijos')

    return name


def family(name):
    for character in MARVEL:
        if character['name'] == name:
            G.add_node((character['name']),
                       node_size=len(character['_children']))
            for children in character['_children']:
                G.add_edge(character['name'], children['name'])


def search(name):
    for node in G:
        if node == name:
            print(name, 'exists in G')
            return True
    print(name, 'no existe en G')
    return False


def index_character():
    count = 0
    for character in MARVEL:
        if count > 50:
            return
        characterlist.append(character)
        count += 1


def adder():
    for character in characterlist:
        if search(character['name']) == False:
            family(character['name'])


def child_to_root():
    for node in G:
        G.add_edge('ROOT', node)


def main():

    index_character()
    G.add_node('ROOT', node_size=1000)
    print('IS G TREE?', nx.is_tree(G))
    adder()
    child_to_root()

    nx.draw(G, node_color='r', edge_color='g', with_labels=True)
    #nx.lowest_common_ancestor(G,'Cable','Hope Summers')
    plt.savefig('plotgraph.png', dpi=300, bbox_inches='tight')
    plt.show()


main()


# %%
