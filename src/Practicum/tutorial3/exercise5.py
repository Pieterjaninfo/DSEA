from src.Practicum.tutorial3.graph import *
from src.Practicum.tutorial3.exercise2 import *


if __name__ == '__main__':
    g = create_graph_cycle(5)

    print(g)

    # e = Edge(Vertex(g), Vertex(g))
    # g.del_edge(e)

    v = g.vertices[0]
    g.del_vertex(v)

    print(g)