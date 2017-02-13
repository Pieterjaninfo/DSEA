from src.Practicum.tutorial3.graph import *
from src.Practicum.tutorial3.exercise2 import *


if __name__ == '__main__':
    g = create_path_graph(5)

    print(g)
    # e = Edge(Vertex(g), Vertex(g))
    e = g.edges[0]
    print(e.tail.is_adjacent(e.head))
    g.del_edge(e)

    print(g)
    print(e.tail.is_adjacent(e.head))


    # h = create_graph_cycle(5)
    # print(h)
    # v = h.vertices[0]
    # h.del_vertex(v)
    # print(h)
