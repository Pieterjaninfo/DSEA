from src.Practicum.tutorial3.graph_io import *
from src.Practicum.tutorial3.exercise1 import *
from src.Practicum.tutorial3.complement import *


def writeDOT(graph, filepath):
    with open('../../../' + filepath, 'w') as f:
        write_dot(graph, f)


if __name__ == '__main__':
    g = create_graph_cycle(6)
    writeDOT(g, 'resources/made_graphs/new_graph.dot')
