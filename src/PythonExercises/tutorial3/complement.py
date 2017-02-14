from src.PythonExercises.tutorial3.graph import *
from src.PythonExercises.tutorial3.exercise2 import *


# Saved the complement of an undirected graph from the given location to the given location
def complement(file_in, file_out):
    g = open_graph(file_in)
    g_vertices_size = len(g.vertices)
    graph = Graph(False, g_vertices_size)

    for i in range(0, g_vertices_size):
        for j in range(i + 1, g_vertices_size):
            if not g.is_adjacent(g.vertices[i], g.vertices[j]):
                graph += Edge(graph.vertices[i], graph.vertices[j])
    write_graph(graph, file_out)


if __name__ == '__main__':
    complement('resources/graphs/short_graph.gr', 'resources/made_graphs/complement_graph.gr')
