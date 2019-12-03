from lab6.graph_am import GraphAM
from lab6.dsf import DisjointSetForest


class Kruskal:
    # Assumption: Graph for Kruskal's is UNDIRECTED
    def kruskal(self, graph):
        edge_weights = []
        # Append source, destination, and edge weight to the created list
        for src in range(len(graph.am)):
            for dest in range(len(graph.am[src])):
                # Disregard edges with no weight
                if graph.am[src][dest] != 0:
                    edge_weights.append((src, dest, graph.am[src][dest]))
        # Sort the list by weight in increasing order
        edge_weights.sort(key=lambda weight: weight[2])
        min_span_tree = GraphAM(len(graph.am), weighted=True)
        connections = DisjointSetForest(len(graph.am))
        for edge in edge_weights:
            src = connections.find(edge[0])
            dest = connections.find(edge[1])

            if src != dest:
                min_span_tree.insert_edge(edge[0], edge[1], edge[2])
                connections.union(src, dest)
        return min_span_tree
