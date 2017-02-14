import itertools
from src.PythonExercises.tutorial3.graph import *
# with open('mygraph.dot', 'w') as f: write_dot(G,f)


# Creates an undirected path graph
def create_path_graph(n):
    graph = Graph(False, n)

    v = graph.vertices
    for i in range(0, n - 1):
        graph += Edge(v[i], v[i + 1])
    return graph


# Creates an undirected full cycle graph
def create_graph_cycle(n):
    graph = Graph(False, n)

    v = graph.vertices
    for i in range(0, n):
        graph += Edge(v[i], v[(i + 1) % n])
    return graph


# Creates an undirected complete graph
def create_complete_graph(n):
    graph = Graph(False, n)

    v = graph.vertices
    for i in range(0, n):
        for j in range(i + 1, n):
            graph += Edge(v[i], v[j])
    return graph


if __name__ == '__main__':
    g = create_path_graph(5)
    h = create_graph_cycle(5)
    l = create_complete_graph(5)

    # print('G:\n' + str(g))
    # print('H:\n' + str(h))
    print('L:\n' + str(l))

    k1 = create_path_graph(3)
    k2 = create_path_graph(2)
    k = k1 + k2

    print('k1\n' + str(k1))
    print('k2\n' + str(k2))
    print('k1+k2\n' + str(k))




