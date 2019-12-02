from scipy.interpolate import interp1d
from lab6.dsf import DisjointSetForest
import matplotlib.pyplot as plt
import numpy as np


class GraphAM:

    def __init__(self, vertices, weighted=False, directed=False):
        self.am = []

        for i in range(vertices):  # Assumption / Design Decision: 0 represents non-existing edge
            self.am.append([0] * vertices)

        self.directed = directed
        self.weighted = weighted
        self.representation = 'AM'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.am)

    def insert_vertex(self):
        for lst in self.am:
            lst.append(0)

        new_row = [0] * (len(self.am) + 1)  # Assumption / Design Decision: 0 represents non-existing edge
        self.am.append(new_row)

        return len(self.am) - 1  # Return new vertex id

    def insert_edge(self, src, dest, weight=1):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.am[src][dest] = weight

        if not self.directed:
            self.am[dest][src] = weight

    def delete_edge(self, src, dest):
        self.insert_edge(src, dest, 0)

    def num_vertices(self):
        return len(self.am)

    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        for i in range(len(self.am)):
            if self.am[src][i] != 0:
                reachable_vertices.add(i)

        return reachable_vertices

    def get_highest_cost_edge(self):

        max_key = -float("inf")

        for lst in self.am:
            for edge_weight in lst:
                max_key = max(edge_weight, max_key)

        return max_key

    def num_edges(self):
        count = 0

        for lst in self.am:
            for edge_weight in lst:
                if edge_weight != 0:
                    count += 1

        return count

    def edge_weight(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return 0  # Design decision

        return self.am[src][dest]

    def reverse_edges(self):

        graph = GraphAM(vertices=len(self.am), weighted=self.weighted, directed=self.directed)

        for i in range(len(self.am)):
            for j in range(len(self.am)):
                if self.am[i][j] != 0:
                    graph.insert_edge(j, i, self.am[i][j])

        self.am = graph.am

    def is_identical(self, graph):
        if len(self.am) != len(graph.am):
            return False

        for i in range(len(self.am)):
            for j in range(len(self.am)):
                if self.am[i][j] != graph.am[i][j]:
                    return False

        return True

    def num_of_self_edges(self):
        count = 0

        for i in range(len(self.am)):
            if self.am[i][i] != 0:
                count += 1

        return count

    def contains_cycle(self):  # Assumption: Directed Graph
        dsf = DisjointSetForest(self.num_vertices())

        for i in range(len(self.am)):
            for j in range(len(self.am)):
                if self.am[i][j] != 0:
                    if dsf.find(i) == dsf.find(j):
                        return True

                    dsf.union(i, j)

        return False

    def is_isolated(self, v):
        if not self.is_valid_vertex(v):
            return False

        for i in range(len(self.am)):
            if self.am[i][v] != 0 or self.am[v][i] != 0:
                return False

        return True

    def display(self):
        for i in range(len(self.am)):
            print(i, ': [', end='')
            for j in range(len(self.am[i])):
                edge = self.am[i][j]
                if edge != 0:
                    print('(' + str(j) + ',' + str(edge) + ')', end='')
            print(']', end='\n')

    def draw(self):
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(self.am)):
            for j in range(len(self.am[i])):
                edge = self.am[i][j]

                if edge != 0:
                    d, w = j, edge
                    if self.directed or d > i:
                        x = np.linspace(i * scale, d * scale)
                        x0 = np.linspace(i * scale, d * scale, num=5)
                        diff = np.abs(d - i)
                        if diff == 1:
                            y0 = [0, 0, 0, 0, 0]
                        else:
                            y0 = [0, -6 * diff, -8 * diff, -6 * diff, 0]
                        f = interp1d(x0, y0, kind='cubic')
                        y = f(x)
                        s = np.sign(i - d)
                        ax.plot(x, s * y, linewidth=1, color='k')
                        if self.directed:
                            xd = [x0[2] + 2 * s, x0[2], x0[2] + 2 * s]
                            yd = [y0[2] - 1, y0[2], y0[2] + 1]
                            yd = [y * s for y in yd]
                            ax.plot(xd, yd, linewidth=1, color='k')
                        if self.weighted:
                            xd = [x0[2] + 2 * s, x0[2], x0[2] + 2 * s]
                            yd = [y0[2] - 1, y0[2], y0[2] + 1]
                            yd = [y * s for y in yd]
                            ax.text(xd[2] - s * 2, yd[2] + 3 * s, str(w), size=12, ha="center", va="center")
            ax.plot([i * scale, i * scale], [0, 0], linewidth=1, color='k')
            ax.text(i * scale, 0, str(i), size=20, ha="center", va="center",
                    bbox=dict(facecolor='w', boxstyle="circle"))
        ax.axis('off')
        ax.set_aspect(1.0)
        plt.show()
