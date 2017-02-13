from src.Practicum.tutorial3.graph import *
from src.Practicum.tutorial3.graph_io import load_graph, write_dot # graphIO import graphs.py, so we do not need to import it here.
from math import inf

# Use these options to change the tests:

TEST_BELLMAN_FORD_DIRECTED = False
TEST_BELLMAN_FORD_UNDIRECTED = False
TEST_DIJKSTRA_DIRECTED = False      # True
TEST_DIJKSTRA_UNDIRECTED = True
TEST_KRUSKAL = False
USE_UNSAFE_GRAPH = False

WRITE_DOT_FILES = True

# Use these options to select the graphs to test your algorithms on:
TestInstances = ["weightedexample.gr"]
# TestInstances=["graph1.gr","graph2.gr","graph3.gr","graph4.gr","graph5.gr","graph6.gr"]
# TestInstances=["negativeweightexample.gr"]
# TestInstances=["negativeweightcycleexample.gr"]
# TestInstances=["WDE100.gr","WDE200.gr","WDE400.gr","WDE800.gr","WDE2000.gr"]; WriteDOTFiles=False
# TestInstances=["bbf2000.gr"]


def relax(edge, directed):
    u = edge.tail
    v = edge.head
    w = edge.weight

    if v.dist > u.dist + w:
        v.dist = u.dist + w
        v.in_edge = u

    if not directed and u.dist > v.dist + w:
        u.dist = v.dist + w
        u.in_edge = v


def bellman_ford_undirected(graph, start):
    """
    Arguments: <G> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <G>.
    Action: Uses the Bellman-Ford algorithm to compute all vertex distances
        from <start> in <G>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <G> is viewed as an undirected graph.
    """
    n = len(graph)

    for v in graph.vertices:
        v.dist = inf
        v.in_edge = None
    start.dist = 0

    # Insert your code here.
    for i in range(0, n - 1):
        for edge in graph.edges:
            relax(edge, False)

    for edge in graph.edges:
        u = edge.tail
        v = edge.head
        w = edge.weight
        if v.dist > u.dist + w or u.dist > v.dist + w:
            return 'neg. cycle'
    return 0


def bellman_ford_directed(graph, start):
    """
    Arguments: <G> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <G>.
    Action: Uses the Bellman-Ford algorithm to compute all vertex distances
        from <start> in <G>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <G> is viewed as a directed graph.
    """
    n = len(graph)

    for v in graph.vertices:
        v.dist = inf
        v.in_edge = None
    start.dist = 0

    # Insert your code here.
    for i in range(0, n - 1):
        for edge in graph.edges:
            relax(edge, True)

    for edge in graph.edges:
        u = edge.tail
        v = edge.head
        w = edge.weight
        if v.dist > u.dist + w:
            return 'neg. cycle'
    return 0


def dijkstra_undirected(graph, start):
    """
    Arguments: <G> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <G>.
    Action: Uses Dijkstra's algorithm to compute all vertex distances
        from <start> in <G>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <G> is viewed as an undirected graph.
    """
    for v in graph.vertices:
        v.dist = inf
        v.in_edge = None
    start.dist = 0

    S = []
    while len(S) != len(graph.vertices):
        v = pick_smallest_vertex(graph.vertices, S)
        S.append(v)
        for edge in graph.edges:
            relax(edge, False)


def dijkstra_directed(graph, start):
    """
    Arguments: <G> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <G>.
    Action: Uses Dijkstra's algorithm to compute all vertex distances
        from <start> in <G>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <indedge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <G> is viewed as a directed graph.
    """
    for v in graph.vertices:
        v.dist = inf
        v.in_edge = None
    start.dist = 0

    S = []
    while len(S) != len(graph.vertices):
        v = pick_smallest_vertex(graph.vertices, S)
        S.append(v)
        for edge in graph.edges:
            relax(edge, True)


def pick_smallest_vertex(vertices, S):
    min_v = None
    val = inf
    for vertex in vertices:
        if vertex not in S and vertex.dist < val:
            min_v = vertex
            val = vertex.dist
    return min_v


def kruskal(G):
    """
    Arguments: <G> is a graph object, where edges have integer <weight> attributes.
    Action: Uses Kruskal's algorithm to compute all a minimum weight spanning tree
        of <G> (or a minimum weight maximal spanning forest if <G> is not connected).
        Returns a list <ST> of all edges that are in the minimum weight spanning
        tree (forest).
    """
    spanning_tree = []  # will be the spanning tree. Append edge objects to this list.

    # Insert your code here.

    return spanning_tree

##############################################################################
#
# Below is test code that does not need to be changed.
#
##############################################################################


def print_max_dist(graph):
    unreachable = False
    numreachable = 0
    remote = next(iter(graph.vertices))
    for v in graph:
        if v.dist is None:
            unreachable = True
        # print("Vertex",v,"is unreachable")
        else:
            numreachable += 1
            if remote.dist is None or v.dist > remote.dist:
                remote = v
    print("Number of reachable vertices:", numreachable, "out of", len(graph))
    print("Largest distance:", remote.dist, "For vertex", remote)


def prepare_drawing(graph):
    for e in graph.edges:
        e.colornum = 0
    for v in graph.vertices:
        if hasattr(v, "in_edge") and v.in_edge is not None:
            v.in_edge.colornum = 1
    for v in graph:
        if v.dist is not None:
            v.label = v.dist
        else:
            v.label = "inf"


if __name__ == "__main__":
    from time import time

    for FileName in TestInstances:
        if USE_UNSAFE_GRAPH:
            print("\n\nLoading graph", FileName, "(Fast graph)")
            with open("../../resources/graphs/" + FileName) as f:
                G = load_graph(f, Graph)
        else:
            print("\n\nLoading graph", FileName)
            with open("../../../resources/graphs/" + FileName) as f:
                G = load_graph(f)

        for i, vertex in enumerate(list(G.vertices)):
            vertex.colornum = i

        # Tuple arguments below:
        # First: printable string
        # Second: Boolean value
        # Third: Function
        # Fourth: Filename
        # Fifth: Whether output should be directed
        for testalg in [("Bellman-Ford, undirected", TEST_BELLMAN_FORD_UNDIRECTED, bellman_ford_undirected,
                         "BellmanFordUndirected", False),
                        ("Bellman-Ford, directed", TEST_BELLMAN_FORD_DIRECTED, bellman_ford_directed, "BellmanFordDirected",
                         True),
                        ("Dijkstra, undirected", TEST_DIJKSTRA_UNDIRECTED, dijkstra_undirected, "DijkstraUndirected",
                         False),
                        ("Dijkstra, directed", TEST_DIJKSTRA_DIRECTED, dijkstra_directed, "DijkstraDirected", True),
                        ("Kruskal", TEST_KRUSKAL, kruskal, "Kruskal", False)]:
            if testalg[1]:
                print("\n\nTesting", testalg[0])
                startt = time()
                if testalg[0] == "Kruskal":
                    ST = testalg[2](G)
                    totalweight = 0
                    for e in ST:
                        totalweight += e.weight
                else:
                    testalg[2](G, next(iter(G.vertices)))
                endt = time()
                print("Elapsed time in seconds:", endt - startt)

                if testalg[0] != "Kruskal":
                    print_max_dist(G)
                    prepare_drawing(G)
                else:
                    if len(ST) < len(G.vertices) - 1:
                        print("Total weight of maximal spanning forest:", totalweight)
                    else:
                        print("Total weight of spanning tree:", totalweight)
                    for e in G.E():
                        e.colornum = 0
                    for e in ST:
                        e.colornum = 1
                    for v in G.vertices:
                        v.label = v._label

                if WRITE_DOT_FILES:
                    with open("../../../resources/made_graphs/" + testalg[3] + '.dot', 'w') as f:
                        write_dot(G, f, directed=testalg[4])
