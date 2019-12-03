from collections import deque


class Topological:
    def compute_indegree_vertex(self, graph):
        all_in_degrees = [0] * len(graph.al)
        i = 0
        for row in graph.al:
            if graph.is_isolated(i):
                all_in_degrees[i] = -1
            i += 1
            for elem in row:
                all_in_degrees[elem.dest] += 1
        return all_in_degrees

    def topological_sort(self, graph):
        all_in_degrees = self.compute_indegree_vertex(graph)
        sort_result = []
        queue = deque([])

        for i in range(len(all_in_degrees)):
            if all_in_degrees[i] == 0:
                queue.append(i)

        while len(queue) != 0:
            u = queue.popleft()

            sort_result.append(u)

            for adj_vertex in graph.vertices_reachable_from(u):
                all_in_degrees[adj_vertex] -= 1

                if all_in_degrees[adj_vertex] == 0:
                    queue.append(adj_vertex)

        if len(sort_result) != graph.num_vertices():
            return None
        return sort_result
