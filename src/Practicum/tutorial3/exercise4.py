from src.Practicum.tutorial3.graph import *
from src.Practicum.tutorial3.exercise2 import *


def breath_first_search(graph):
    L = [graph.vertices[0]]
    label = [L[0]]
    pred = {L[0] : []}
    k = 1

    while L:
        v = L[0]
        for neighbour in v.neighbours:
            if neighbour not in label:
                k += 1



    # S = []
    # Q = []




if __name__ == '__main__':
    g = create_path_graph(5)
    breath_first_search(g)
