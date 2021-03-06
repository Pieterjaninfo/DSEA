from src.PythonExercises.tutorial3.graph_io import *
from src.PythonExercises.tutorial3.exercise1 import *
from src.PythonExercises.tutorial3.complement import *


def writeDOT(graph, filepath):
    with open('../../../' + filepath, 'w') as f:
        write_dot(graph, f)


if __name__ == '__main__':
    # g = create_graph_cycle(6)
    g = open_graph('resources/graphs/examplegraph.gr')
    writeDOT(g, 'resources/made_graphs/examplegraph.dot')
