from src.PythonExercises.tutorial3.graph_io import load_graph, save_graph
from src.PythonExercises.tutorial3.exercise1 import *


def open_graph(filename):
    with open('../../../' + filename) as f:
        graph = load_graph(f)
    return graph


def write_graph(graph, filename):
    with open('../../../' + filename, 'w') as f:
        save_graph(graph, f)


if __name__ == '__main__':
    g = open_graph('resources/graphs/examplegraph.gr')

    v = Vertex(g)
    g += v
    g += Edge(g.vertices[0], v)
    write_graph(g, 'resources/made_graphs/new_examplegraph.gr')
    print(g)

    h = open_graph('resources/made_graphs/new_examplegraph.gr')
    print(h)
