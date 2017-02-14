from src.PythonExercises.tutorial3.graph import *
from src.PythonExercises.tutorial3.graph_io import load_graph, write_dot # graphIO import graphs.py, so we do not need to import it here.
import os
from math import inf
from termcolor import colored

# Use these options to change the tests:

TEST_BELLMAN_FORD_DIRECTED = True
TEST_BELLMAN_FORD_UNDIRECTED = True
TEST_DIJKSTRA_DIRECTED = True
TEST_DIJKSTRA_UNDIRECTED = True

WRITE_DOT_FILES = True

# Use this to select the graphs to test your algorithms on:
TestInstances = ["weightedexample.gr"]
# TestInstances=["randomplanar.gr"]
# TestInstances = ["randomplanar10.gr"]
# TestInstances=["bd.gr","bbf.gr"]; WriteDOTFiles=False
# TestInstances=["bbf2000.gr"]; WriteDOTFiles=False
# TestInstances=["bbf200.gr"]
# TestInstances=["negativeweightexample.gr"]
# TestInstances=["negativeweightcycleexample.gr"]
# TestInstances=["WDE100.gr","WDE200.gr","WDE400.gr","WDE800.gr","WDE2000.gr"]; WriteDOTFiles=False
# TestInstances=["WDE2000.gr"]
# TestInstances=["weightedex500.gr"];	WriteDOTFiles=False


USE_UNSAFE_GRAPH = False

"""
TEST RESULTS
Bellman-ford directed
- W2000: 36.41883420944214 seconds, improved: 0.2511610984802246 seconds
- bbf2000: 6.311946868896484 seconds, improved:6.749789714813232 seconds
"""


def bellman_ford_undirected(graph, start):
    """
    Arguments: <graph> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <graph>.
    Action: Uses the Bellman-Ford algorithm to compute all vertex distances
        from <start> in <graph>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <graph> is viewed as an undirected graph.
    """
    n = len(graph)

    # Initialize the vertex attributes
    for v in graph.vertices:
        v.dist = inf
        v.in_edge = None
    start.dist = 0

    # Update vertex attributes each iteration
    changed_made = False
    for i in range(0, n - 1):
        for edge in graph.edges:
            if relax(edge, False):
                changed_made = True

        if not changed_made:
            print(colored('Bellman-Ford algorithm ended early on iteration ' + str(i + 1), 'green'))
            break
        changed_made = False

    # Negative cycle detection
    for edge in graph.edges:
        u = edge.tail
        v = edge.head
        w = edge.weight
        if v.dist > u.dist + w or u.dist > v.dist + w:
            print(colored('Negative cycle in bellman-ford undirected', 'red'))


def bellman_ford_directed(graph, start):
    """
    Arguments: <graph> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <graph>.
    Action: Uses the Bellman-Ford algorithm to compute all vertex distances
        from <start> in <graph>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <graph> is viewed as a directed graph.
    """
    n = len(graph)

    # Initialize the vertex attributes
    for v in graph.vertices:
        v.dist = inf
        v.in_edge = None
    start.dist = 0

    # Update vertex attributes each iteration
    changes_made = False
    for i in range(0, n - 1):
        for edge in graph.edges:
            if relax(edge, True):
                changes_made = True

        if not changes_made:
            print(colored('Bellman-Ford algorithm ended early on iteration ' + str(i + 1), 'green'))
            break
        changes_made = False

    # Negative cycle detection
    for edge in graph.edges:
        u = edge.tail
        v = edge.head
        w = edge.weight
        if v.dist > u.dist + w:
            print(colored('Negative cycle in bellman-ford directed', 'red'))
            return False
    return True


def dijkstra_undirected(graph, start):
    """
    Arguments: <graph> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <graph>.
    Action: Uses Dijkstra's algorithm to compute all vertex distances
        from <start> in <graph>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <graph> is viewed as an undirected graph.
    """
    # Initialize the vertex attributes
    for v in graph.vertices:
        v.dist = inf
        v.in_edge = None
    start.dist = 0

    # Update vertex attributes each iteration
    S = []
    while len(S) != len(graph.vertices):
        v = pick_smallest_vertex(graph.vertices, S)
        S.append(v)
        for edge in graph.edges:
            relax(edge, False)


def dijkstra_directed(graph, start):
    """
    Arguments: <graph> is a graph object, where edges have integer <weight>
        attributes,	and <start> is a vertex of <graph>.
    Action: Uses Dijkstra's algorithm to compute all vertex distances
        from <start> in <graph>, and assigns these values to the vertex attribute <dist>.
        Optional: assigns the vertex attribute <in_edge> to be the incoming
        shortest path edge, for every reachable vertex except <start>.
        <graph> is viewed as a directed graph.
    """
    # Initialize the vertex attributes
    for v in graph.vertices:
        v.dist = inf
        v.in_edge = None
    start.dist = 0

    # Update vertex attributes each iteration
    S = []
    while len(S) != len(graph.vertices):
        v = pick_smallest_vertex(graph.vertices, S)
        S.append(v)
        for edge in graph.edges:
            relax(edge, True)


def relax(edge, directed):
    """
    Corrects a violating triangle inequality
    :param edge: Potentially violating edge
    :param directed: true if the graph is directed, else false
    """
    change_made = False
    u = edge.tail
    v = edge.head
    w = edge.weight

    if v.dist > u.dist + w:
        v.dist = u.dist + w
        v.in_edge = u
        change_made = True

    if not directed and u.dist > v.dist + w:
        u.dist = v.dist + w
        u.in_edge = v
        change_made = True
    return change_made


def pick_smallest_vertex(vertices, S):
    """
    Returns the vertex with the lowest distance (stored in its label) to be explored next
    :param vertices: All the vertices of the given graph
    :param S: List containing all the previously explored vertices
    :return: Vertex with the lowest distance in the frontier list
    """
    min_v = None
    val = inf
    for vertex in vertices:
        if vertex not in S and vertex.dist < val:
            min_v = vertex
            val = vertex.dist
    return min_v

##############################################################################
#
# Below is test code that does not need to be changed.
#
##############################################################################

def print_max_dist(graph):
    unreachable = False
    numreachable = 0
    sorted_vertices = sorted(graph.vertices, key=lambda v: v.label)
    remote = sorted_vertices[0]
    for v in graph.vertices:
        if v.dist == inf:
            unreachable = True
            # print("Vertex", v,"is unreachable")
        else:
            numreachable += 1
            if v.dist > remote.dist:
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
        v.label = str(v.dist)


def do_testalg(testalg, G):
    if testalg[1]:
        print("\n\nTesting", testalg[0])
        startt = time()
        if testalg[0] == "Kruskal":
            ST = testalg[2](G)
            totalweight = 0
            for e in ST:
                totalweight += e.weight
        else:
            sorted_vertices = sorted(G.vertices, key=lambda v: v.label)
            testalg[2](G, sorted_vertices[0])
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
            for e in G.edges:
                e.colornum = 0
            for e in ST:
                e.colornum = 1
            for v in G.vertices:
                v.label = v._label

        if WRITE_DOT_FILES:
            with open(os.path.join(os.getcwd() + '/../../../resources/made_graphs/', testalg[3] + '.dot'), 'w') as f:
                write_dot(G, f, directed=testalg[4])


if __name__ == "__main__":
    from time import time

    for FileName in TestInstances:
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
                        ("Dijkstra, directed", TEST_DIJKSTRA_DIRECTED, dijkstra_directed, "DijkstraDirected", True)]:
            if USE_UNSAFE_GRAPH:
                print("\n\nLoading graph", FileName, "(Fast graph)")
                with open(os.path.join(os.getcwd() + '/../../../resources/graphs/', FileName)) as f:
                    G = load_graph(f, Graph)
            else:
                print("\n\nLoading graph", FileName)
                with open(os.path.join(os.getcwd() + '/../../../resources/graphs/', FileName)) as f:
                    G = load_graph(f)

            for i, vertex in enumerate(list(G.vertices)):
                vertex.colornum = i
            do_testalg(testalg, G)
