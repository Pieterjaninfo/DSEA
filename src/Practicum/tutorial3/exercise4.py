from src.Practicum.tutorial3.graph import *
from src.Practicum.tutorial3.exercise2 import *
from collections import OrderedDict


def breath_first_search(graph):
    L = [graph.vertices[0]]
    label = OrderedDict()
    label[L[0]] = 1
    pred = {L[0]: []}
    k = 1

    while L:
        v = L[0]
        if exists_unlabeled_neighbour(label, v.neighbours):
            w = exists_unlabeled_neighbour(label, v.neighbours)
            k += 1
            label[w] = k
            pred[w] = v
            L.append(w)
        else:
            L.remove(v)
    return label, pred


def depth_first_search(graph):
    L = [graph.vertices[0]]
    label = OrderedDict()
    label[L[0]] = 1
    pred = {L[0]: []}
    k = 1

    while L:
        v = L[-1]
        if exists_unlabeled_neighbour(label, v.neighbours):
            w = exists_unlabeled_neighbour(label, v.neighbours)
            k += 1
            label[w] = k
            pred[w] = v
            L.append(w)
        else:
            L.remove(v)
    return label, pred


def exists_unlabeled_neighbour(label, neighbours):
    for neighbour in neighbours:
        if neighbour not in label:
            return neighbour


if __name__ == '__main__':
    # g = create_path_graph(5)
    g = open_graph('resources/graphs/examplegraph.gr')
    result = breath_first_search(g)

    # print(g)
    for key in result[0]:
        print((result[0][key], key))
