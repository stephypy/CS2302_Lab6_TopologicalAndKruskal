from collections import deque
from lab6.graph_al import GraphAL


def compute_indegree_vertex(graph):
    all_in_degrees = [0] * len(graph.al)
    for row in graph.al:
        for elem in row:
            all_in_degrees[elem.dest] += 1
    return all_in_degrees


def topological_sort(graph):
    all_in_degrees = compute_indegree_vertex(graph)
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


def main():
    g = GraphAL(6, directed=True)
    g.insert_edge(0, 1)
    g.insert_edge(0, 4)
    g.insert_edge(1, 2)
    g.insert_edge(1, 4)
    g.insert_edge(2, 3)
    g.insert_edge(4, 5)
    g.insert_edge(5, 2)
    g.insert_edge(5, 3)
    g.display()
    print()
    ans = topological_sort(g)
    print(ans)


main()
